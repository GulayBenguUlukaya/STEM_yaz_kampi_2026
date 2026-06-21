"""
Malatya günlük hava durumu verisini Open-Meteo arşiv API'sinden çeker.
input_data/malatya_hava.csv olarak kaydeder.

Veri:
- Konum: Malatya (38.35°K, 38.33°D)
- Zaman aralığı: 2020-01-01 ... 2024-12-31 (1827 gün)
- Sütunlar: tarih, sicaklik_max, sicaklik_min, sicaklik_ort, yagis, ruzgar_max
- Türetilmiş sütunlar (öğrenciler için): ay, mevsim, hafta_gunu

Kaynak: Open-Meteo (CC-BY 4.0) — https://open-meteo.com/
"""
import requests
import pandas as pd

KONUMLAR = [
    {'lat': 38.35, 'lon': 38.33, 'isim': 'Malatya'},
    {'lat': 41.01, 'lon': 28.97, 'isim': 'İstanbul'},   # ılıman, kıyı
    {'lat': 39.91, 'lon': 41.27, 'isim': 'Erzurum'},    # yüksek rakım, soğuk
]
BASLANGIC = '2020-01-01'
BITIS = '2024-12-31'
CIKTI_MALATYA = '/sc/arion/scratch/ulukag01/STEM_yaz_kampi_2026/input_data/malatya_hava.csv'
CIKTI_TUM = '/sc/arion/scratch/ulukag01/STEM_yaz_kampi_2026/input_data/iller_hava.csv'


def mevsim_bul(ay):
    if ay in (12, 1, 2):
        return 'Kış'
    if ay in (3, 4, 5):
        return 'İlkbahar'
    if ay in (6, 7, 8):
        return 'Yaz'
    return 'Sonbahar'


def il_verisi_cek(konum):
    print(f"📥 {konum['isim']} hava verisi indiriliyor ({BASLANGIC} → {BITIS})...")
    r = requests.get(
        'https://archive-api.open-meteo.com/v1/archive',
        params={
            'latitude': konum['lat'],
            'longitude': konum['lon'],
            'start_date': BASLANGIC,
            'end_date': BITIS,
            'daily': 'temperature_2m_max,temperature_2m_min,temperature_2m_mean,'
                     'precipitation_sum,wind_speed_10m_max',
            'timezone': 'Europe/Istanbul',
        },
        timeout=60,
    )
    r.raise_for_status()
    data = r.json()['daily']

    df = pd.DataFrame({
        'tarih': pd.to_datetime(data['time']),
        'sicaklik_max': data['temperature_2m_max'],
        'sicaklik_min': data['temperature_2m_min'],
        'sicaklik_ort': data['temperature_2m_mean'],
        'yagis': data['precipitation_sum'],
        'ruzgar_max': data['wind_speed_10m_max'],
    })

    df['yil'] = df['tarih'].dt.year
    df['ay'] = df['tarih'].dt.month
    df['gun'] = df['tarih'].dt.day
    df['hafta_gunu'] = df['tarih'].dt.day_name()
    df['mevsim'] = df['ay'].apply(mevsim_bul)
    df['il'] = konum['isim']
    return df


def main():
    tum_iller = []
    for konum in KONUMLAR:
        df = il_verisi_cek(konum)
        tum_iller.append(df)
        print(f"   {konum['isim']}: {len(df)} gün, yıllık ort sıcaklık: "
              f"{df['sicaklik_ort'].mean():.1f}°C")

    # Malatya geriye uyumlu CSV
    malatya = next(d for d in tum_iller if d['il'].iloc[0] == 'Malatya')
    malatya.drop(columns=['il']).to_csv(CIKTI_MALATYA, index=False)
    print(f"\n✅ {CIKTI_MALATYA}")

    # Tüm iller birleşik CSV
    birlesik = pd.concat(tum_iller, ignore_index=True)
    birlesik.to_csv(CIKTI_TUM, index=False)
    print(f"✅ {CIKTI_TUM} ({len(birlesik)} satır)")
    print(f'\nİl başına yıllık ortalama sıcaklık:')
    print(birlesik.groupby(['il', 'yil'])['sicaklik_ort'].mean().round(1).unstack())


if __name__ == '__main__':
    main()
