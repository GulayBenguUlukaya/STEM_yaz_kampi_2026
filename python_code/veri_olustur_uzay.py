"""
NASA Exoplanet Archive'dan GERÇEK Kepler KOI verisi indirir.
Kepler uzay teleskobu (2009-2018) verisi, NASA halka açık.

Kaynak: https://exoplanetarchive.ipac.caltech.edu/
Lisans: NASA verileri kamuya açık
Tablo: cumulative (Kepler Object of Interest — KOI)

Çıktı: input_data/uzay_otegezegen.csv

Bu, sentetik veri DEĞİL — NASA Kepler uydusunun gerçek gözlemleri.
"""
import io
import requests
import pandas as pd

CIKTI = '/sc/arion/scratch/ulukag01/STEM_yaz_kampi_2026/input_data/uzay_otegezegen.csv'

# NASA TAP (Table Access Protocol) sorgusu
# Sadece CONFIRMED ve FALSE POSITIVE alıyoruz — CANDIDATE etiketi belirsiz
QUERY = """SELECT kepoi_name,koi_period,koi_duration,koi_depth,koi_prad,
                  koi_steff,koi_srad,koi_teq,koi_model_snr,koi_disposition
FROM cumulative
WHERE koi_disposition IN ('CONFIRMED','FALSE POSITIVE')
  AND koi_period IS NOT NULL
  AND koi_duration IS NOT NULL
  AND koi_depth IS NOT NULL
  AND koi_prad IS NOT NULL
  AND koi_steff IS NOT NULL
  AND koi_srad IS NOT NULL
  AND koi_model_snr IS NOT NULL"""


def main():
    print('📥 NASA Exoplanet Archive\'dan veri indiriliyor...')
    r = requests.get(
        'https://exoplanetarchive.ipac.caltech.edu/TAP/sync',
        params={'query': QUERY, 'format': 'csv'},
        timeout=120,
    )
    r.raise_for_status()
    df = pd.read_csv(io.StringIO(r.text))
    print(f'   Ham veri: {df.shape[0]} satır × {df.shape[1]} sütun')

    # Türkçe sütun adları + birim açıklaması
    df = df.rename(columns={
        'kepoi_name': 'aday_id',
        'koi_period': 'yorunge_periyodu_gun',
        'koi_duration': 'transit_suresi_saat',
        'koi_depth': 'transit_derinligi_ppm',
        'koi_prad': 'gezegen_yaricap_dunya',
        'koi_steff': 'yildiz_sicakligi_K',
        'koi_srad': 'yildiz_yaricap_gunes',
        'koi_teq': 'denge_sicakligi_K',
        'koi_model_snr': 'sinyal_gurultu_orani',
        'koi_disposition': 'durum',
    })

    # Etiketleri Türkçeleştir + boolean ekle
    df['gercek_gezegen'] = df['durum'] == 'CONFIRMED'
    df['durum'] = df['durum'].map({'CONFIRMED': 'Gerçek Gezegen', 'FALSE POSITIVE': 'Yanlış Pozitif'})

    # Yaşanabilir bölge bayrağı (basit Goldilocks: 200-320K + 0.5-2.5 Dünya yarıçapı)
    df['yasanabilir_bolge'] = (
        df['denge_sicakligi_K'].between(200, 320, inclusive='both')
        & df['gezegen_yaricap_dunya'].between(0.5, 2.5, inclusive='both')
    )

    # denge_sicakligi NaN olabilir — onu False olarak koru
    df['yasanabilir_bolge'] = df['yasanabilir_bolge'].fillna(False)

    # Kullanışlı sütun sırası
    sutun_sirasi = [
        'aday_id', 'yorunge_periyodu_gun', 'transit_suresi_saat',
        'transit_derinligi_ppm', 'gezegen_yaricap_dunya',
        'yildiz_sicakligi_K', 'yildiz_yaricap_gunes', 'denge_sicakligi_K',
        'sinyal_gurultu_orani', 'yasanabilir_bolge', 'gercek_gezegen', 'durum',
    ]
    df = df[sutun_sirasi]

    print(f'\n📊 Temizlenmiş veri: {df.shape[0]} aday × {df.shape[1]} sütun')
    print(f'   Gerçek gezegen oranı: %{df["gercek_gezegen"].mean()*100:.1f}')
    print(f'   Yaşanabilir bölge: {df["yasanabilir_bolge"].sum()} aday')
    gercek = df[df['gercek_gezegen']]
    yas_gerc = gercek['yasanabilir_bolge'].sum()
    print(f'   Yaşanabilir bölgedeki GERÇEK gezegen: {yas_gerc}')
    print(f'\nİlk 5 satır:')
    print(df.head().to_string(index=False))
    print(f'\nGerçek gezegenlerin SNR ortalaması: {df[df["gercek_gezegen"]]["sinyal_gurultu_orani"].mean():.1f}')
    print(f'Yanlış pozitiflerin SNR ortalaması : {df[~df["gercek_gezegen"]]["sinyal_gurultu_orani"].mean():.1f}')

    df.to_csv(CIKTI, index=False)
    print(f'\n✅ Kaydedildi: {CIKTI}')


if __name__ == '__main__':
    main()
