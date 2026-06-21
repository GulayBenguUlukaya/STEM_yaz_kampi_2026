"""
Eurovision Song Contest GERÇEK tarihsel verisi (2000-2023) +
ev sahibi uzaklık özelliği + ülke-ülke oy verisi.

Kaynak:
- Spijkervet/eurovision-dataset GitHub release (CC-BY orijinal repo)
- Ülke koordinatları (başkent lat/lon): manuel, halka açık coğrafi veri

Türkiye 2012'den sonra katılmadı — gerçek hayattaki durum.

Çıktılar:
- input_data/eurovision.csv (916 katılım, ev_sahibi_uzaklik_km dahil)
- input_data/eurovision_oylar.csv (oylama matrisi, komşuluk analizi için)
"""
import io
import math
import requests
import pandas as pd
import numpy as np

URL_KATILIMCI = 'https://github.com/Spijkervet/eurovision-dataset/releases/download/2023/contestants.csv'
URL_OY = 'https://github.com/Spijkervet/eurovision-dataset/releases/download/2023/votes.csv'
CIKTI_KATILIMCI = '/sc/arion/scratch/ulukag01/STEM_yaz_kampi_2026/input_data/eurovision.csv'
CIKTI_OY = '/sc/arion/scratch/ulukag01/STEM_yaz_kampi_2026/input_data/eurovision_oylar.csv'

# İngilizce → Türkçe ülke adı eşleştirmesi
ULKE_TR = {
    'Turkey': 'Türkiye', 'Turkiye': 'Türkiye',
    'Sweden': 'İsveç', 'Italy': 'İtalya', 'Ukraine': 'Ukrayna',
    'Norway': 'Norveç', 'Greece': 'Yunanistan', 'Germany': 'Almanya',
    'United Kingdom': 'Birleşik Krallık', 'France': 'Fransa', 'Spain': 'İspanya',
    'Israel': 'İsrail', 'Azerbaijan': 'Azerbaycan', 'Romania': 'Romanya',
    'Serbia': 'Sırbistan', 'Poland': 'Polonya', 'Russia': 'Rusya',
    'Austria': 'Avusturya', 'Belgium': 'Belçika', 'Netherlands': 'Hollanda',
    'Portugal': 'Portekiz', 'Finland': 'Finlandiya', 'Estonia': 'Estonya',
    'Latvia': 'Letonya', 'Lithuania': 'Litvanya', 'Czech Republic': 'Çek Cumhuriyeti',
    'Czechia': 'Çek Cumhuriyeti', 'Croatia': 'Hırvatistan',
    'Switzerland': 'İsviçre', 'Denmark': 'Danimarka', 'Ireland': 'İrlanda',
    'Bulgaria': 'Bulgaristan', 'Hungary': 'Macaristan', 'Slovenia': 'Slovenya',
    'Slovakia': 'Slovakya', 'Iceland': 'İzlanda', 'Albania': 'Arnavutluk',
    'Armenia': 'Ermenistan', 'Belarus': 'Belarus', 'Bosnia & Herzegovina': 'Bosna-Hersek',
    'Cyprus': 'Kıbrıs', 'Georgia': 'Gürcistan', 'Macedonia': 'Makedonya',
    'North Macedonia': 'Kuzey Makedonya', 'Malta': 'Malta', 'Moldova': 'Moldova',
    'Montenegro': 'Karadağ', 'Australia': 'Avustralya',
    'San Marino': 'San Marino', 'Andorra': 'Andorra', 'Monaco': 'Monako',
    'Luxembourg': 'Lüksemburg', 'Morocco': 'Fas',
    'Serbia & Montenegro': 'Sırbistan-Karadağ', 'Yugoslavia': 'Yugoslavya',
}

# ISO 3166-1 alpha-2 kod → Türkçe ülke adı (Eurovision ülkeleri)
ISO_TR = {
    'tr': 'Türkiye', 'se': 'İsveç', 'it': 'İtalya', 'ua': 'Ukrayna',
    'no': 'Norveç', 'gr': 'Yunanistan', 'de': 'Almanya', 'gb': 'Birleşik Krallık',
    'fr': 'Fransa', 'es': 'İspanya', 'il': 'İsrail', 'az': 'Azerbaycan',
    'ro': 'Romanya', 'rs': 'Sırbistan', 'pl': 'Polonya', 'ru': 'Rusya',
    'at': 'Avusturya', 'be': 'Belçika', 'nl': 'Hollanda', 'pt': 'Portekiz',
    'fi': 'Finlandiya', 'ee': 'Estonya', 'lv': 'Letonya', 'lt': 'Litvanya',
    'cz': 'Çek Cumhuriyeti', 'hr': 'Hırvatistan', 'ch': 'İsviçre',
    'dk': 'Danimarka', 'ie': 'İrlanda', 'bg': 'Bulgaristan', 'hu': 'Macaristan',
    'si': 'Slovenya', 'sk': 'Slovakya', 'is': 'İzlanda', 'al': 'Arnavutluk',
    'am': 'Ermenistan', 'by': 'Belarus', 'ba': 'Bosna-Hersek', 'cy': 'Kıbrıs',
    'ge': 'Gürcistan', 'mk': 'Kuzey Makedonya', 'mt': 'Malta', 'md': 'Moldova',
    'me': 'Karadağ', 'au': 'Avustralya', 'sm': 'San Marino', 'ad': 'Andorra',
    'mc': 'Monako', 'lu': 'Lüksemburg', 'ma': 'Fas',
    'cs': 'Sırbistan-Karadağ', 'yu': 'Yugoslavya',
}

# Ülke başkenti koordinatları (lat, lon)
# Halka açık coğrafi veri — uzaklık hesabı için kullanılıyor
ULKE_KOORDINAT = {
    'Türkiye': (39.93, 32.86),       # Ankara
    'İsveç': (59.33, 18.07),          # Stockholm
    'İtalya': (41.90, 12.50),         # Roma
    'Ukrayna': (50.45, 30.52),        # Kiev
    'Norveç': (59.91, 10.75),         # Oslo
    'Yunanistan': (37.98, 23.73),     # Atina
    'Almanya': (52.52, 13.40),        # Berlin
    'Birleşik Krallık': (51.51, -0.13),  # Londra
    'Fransa': (48.86, 2.35),          # Paris
    'İspanya': (40.42, -3.70),        # Madrid
    'İsrail': (31.78, 35.22),         # Kudüs
    'Azerbaycan': (40.41, 49.87),     # Bakü
    'Romanya': (44.43, 26.10),        # Bükreş
    'Sırbistan': (44.79, 20.45),      # Belgrad
    'Polonya': (52.23, 21.01),        # Varşova
    'Rusya': (55.75, 37.62),          # Moskova
    'Avusturya': (48.21, 16.37),      # Viyana
    'Belçika': (50.85, 4.35),         # Brüksel
    'Hollanda': (52.37, 4.90),        # Amsterdam
    'Portekiz': (38.72, -9.13),       # Lizbon
    'Finlandiya': (60.17, 24.94),     # Helsinki
    'Estonya': (59.44, 24.75),        # Tallinn
    'Letonya': (56.95, 24.11),        # Riga
    'Litvanya': (54.69, 25.28),       # Vilnius
    'Çek Cumhuriyeti': (50.08, 14.44),# Prag
    'Hırvatistan': (45.81, 15.98),    # Zagreb
    'İsviçre': (46.95, 7.45),         # Bern
    'Danimarka': (55.68, 12.57),      # Kopenhag
    'İrlanda': (53.35, -6.26),        # Dublin
    'Bulgaristan': (42.70, 23.32),    # Sofya
    'Macaristan': (47.50, 19.04),     # Budapeşte
    'Slovenya': (46.06, 14.51),       # Ljubljana
    'Slovakya': (48.15, 17.11),       # Bratislava
    'İzlanda': (64.13, -21.82),       # Reykjavik
    'Arnavutluk': (41.33, 19.82),     # Tiran
    'Ermenistan': (40.18, 44.51),     # Erivan
    'Belarus': (53.90, 27.57),        # Minsk
    'Bosna-Hersek': (43.86, 18.41),   # Saraybosna
    'Kıbrıs': (35.17, 33.36),         # Lefkoşa
    'Gürcistan': (41.72, 44.79),      # Tiflis
    'Makedonya': (41.99, 21.43),      # Üsküp
    'Kuzey Makedonya': (41.99, 21.43),# Üsküp
    'Malta': (35.90, 14.51),          # La Valletta
    'Moldova': (47.01, 28.86),        # Kişinev
    'Karadağ': (42.44, 19.26),        # Podgoritsa
    'Avustralya': (-35.28, 149.13),   # Canberra
    'San Marino': (43.94, 12.45),
    'Andorra': (42.51, 1.52),
    'Monako': (43.73, 7.42),
    'Lüksemburg': (49.61, 6.13),
    'Fas': (34.02, -6.83),            # Rabat
    'Sırbistan-Karadağ': (44.79, 20.45),
    'Yugoslavya': (44.79, 20.45),     # Belgrad
}


def haversine_km(lat1, lon1, lat2, lon2):
    """İki koordinat arası büyük çember mesafesi (km)."""
    R = 6371.0  # Dünya yarıçapı
    rad1, rad2 = math.radians(lat1), math.radians(lat2)
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(rad1) * math.cos(rad2) * math.sin(dlon/2)**2
    return 2 * R * math.asin(math.sqrt(a))


def uzaklik_km(ulke1, ulke2):
    """İki ülke arası uzaklık (km). Bilinmiyorsa None."""
    if ulke1 == ulke2:
        return 0.0
    k1 = ULKE_KOORDINAT.get(ulke1)
    k2 = ULKE_KOORDINAT.get(ulke2)
    if k1 is None or k2 is None:
        return None
    return haversine_km(k1[0], k1[1], k2[0], k2[1])


def main_katilimci():
    print('📥 Eurovision katılımcılar indiriliyor...')
    r = requests.get(URL_KATILIMCI, timeout=60, allow_redirects=True)
    r.raise_for_status()
    df = pd.read_csv(io.StringIO(r.text))
    print(f'   Ham veri: {df.shape[0]} satır')

    df = df[(df['year'] >= 2000) & (df['year'] <= 2023)].copy()
    df = df.drop(columns=['lyrics', 'youtube_url', 'composers', 'lyricists',
                          'to_country_id'], errors='ignore')

    df['ulke'] = df['to_country'].map(ULKE_TR).fillna(df['to_country'])
    df = df.drop(columns=['to_country'])

    df = df.rename(columns={
        'year': 'yil',
        'performer': 'sanatci',
        'song': 'sarki',
        'place_contest': 'yarisma_yili_sirasi',
        'sf_num': 'yari_final_no',
        'running_final': 'final_cikis_sirasi',
        'running_sf': 'yarifinal_cikis_sirasi',
        'place_final': 'final_sira',
        'points_final': 'final_puan',
        'place_sf': 'yarifinal_sira',
        'points_sf': 'yarifinal_puan',
        'points_tele_final': 'tele_puan_final',
        'points_jury_final': 'juri_puan_final',
        'points_tele_sf': 'tele_puan_yarifinal',
        'points_jury_sf': 'juri_puan_yarifinal',
    })

    df['finale_kaldı'] = df['final_sira'].notna()

    # Ev sahibi: geçen yıl kazanan
    kazananlar = df[df['final_sira'] == 1].set_index('yil')['ulke'].to_dict()
    df['ev_sahibi_ulke'] = df['yil'].apply(lambda y: kazananlar.get(y - 1))
    df['ev_sahibi'] = df['ulke'] == df['ev_sahibi_ulke']

    # 🌍 YENİ: Ev sahibine uzaklık (km)
    df['ev_sahibi_uzaklik_km'] = df.apply(
        lambda r: uzaklik_km(r['ulke'], r['ev_sahibi_ulke']),
        axis=1,
    )

    df['ilk_10'] = (df['final_sira'] <= 10) & df['final_sira'].notna()

    sutun_sirasi = ['yil', 'ulke', 'sanatci', 'sarki', 'yari_final_no',
                    'final_cikis_sirasi', 'final_sira', 'final_puan',
                    'tele_puan_final', 'juri_puan_final',
                    'yarifinal_cikis_sirasi', 'yarifinal_sira', 'yarifinal_puan',
                    'finale_kaldı', 'ev_sahibi', 'ev_sahibi_ulke',
                    'ev_sahibi_uzaklik_km', 'ilk_10']
    df = df[[c for c in sutun_sirasi if c in df.columns]]

    print(f'\n📊 Final: {df.shape[0]} katılım × {df.shape[1]} sütun')
    print(f'   Ev sahibine uzaklık ortalaması: {df["ev_sahibi_uzaklik_km"].mean():.0f} km')
    print(f'   Türkiye katılımları: {df[df["ulke"] == "Türkiye"]["yil"].tolist()}')

    df.to_csv(CIKTI_KATILIMCI, index=False)
    print(f'✅ Kaydedildi: {CIKTI_KATILIMCI}')
    return df


def main_oy():
    print('\n📥 Eurovision oy verisi indiriliyor (büyük dosya, ~5 MB)...')
    r = requests.get(URL_OY, timeout=120, allow_redirects=True)
    r.raise_for_status()
    df = pd.read_csv(io.StringIO(r.text))
    print(f'   Ham veri: {df.shape[0]} satır')

    # 2000-2023 + finale göre filtre
    df = df[(df['year'] >= 2000) & (df['year'] <= 2023)].copy()
    # 'round' sütunu: 'final' = grand final, 'semi-final*' = yarı final
    # Sadece grand final oylarını al
    if 'round' in df.columns:
        df = df[df['round'] == 'final']

    # Türkçeleştir — ISO kodundan
    df['oy_veren_ulke'] = df['from_country_id'].str.lower().map(ISO_TR)
    df['oy_alan_ulke'] = df['to_country_id'].str.lower().map(ISO_TR)

    # Sütun seç
    sutunlar = ['year', 'oy_veren_ulke', 'oy_alan_ulke']
    if 'total_points' in df.columns:
        df['puan'] = df['total_points']
        sutunlar.append('puan')
    elif 'points' in df.columns:
        df['puan'] = df['points']
        sutunlar.append('puan')
    if 'tele_points' in df.columns:
        df['tele_puan'] = df['tele_points']
        sutunlar.append('tele_puan')
    if 'jury_points' in df.columns:
        df['juri_puan'] = df['jury_points']
        sutunlar.append('juri_puan')

    df = df.rename(columns={'year': 'yil'})
    sutunlar = ['yil' if s == 'year' else s for s in sutunlar]
    df = df[sutunlar].dropna(subset=['oy_veren_ulke', 'oy_alan_ulke'])

    # Aynı ülke kendine puan veremez (zaten yok ama güvenlik)
    df = df[df['oy_veren_ulke'] != df['oy_alan_ulke']]

    # Uzaklık ekle
    df['uzaklik_km'] = df.apply(
        lambda r: uzaklik_km(r['oy_veren_ulke'], r['oy_alan_ulke']),
        axis=1,
    )

    df = df.dropna(subset=['uzaklik_km'])
    print(f'\n📊 Final oy verisi: {len(df)} satır')
    print(f'   Yıllar: {df["yil"].min()} - {df["yil"].max()}')
    if 'puan' in df.columns:
        print(f'   Ortalama puan: {df["puan"].mean():.2f}')
        # Yakın komşu tipik puanı
        yakin = df[df['uzaklik_km'] < 1000]
        uzak = df[df['uzaklik_km'] > 3000]
        print(f'   <1000 km komşulara verilen ort puan: {yakin["puan"].mean():.2f}')
        print(f'   >3000 km uzaklara verilen ort puan: {uzak["puan"].mean():.2f}')

    df.to_csv(CIKTI_OY, index=False)
    print(f'✅ Kaydedildi: {CIKTI_OY}')


if __name__ == '__main__':
    main_katilimci()
    main_oy()
