"""
Our World in Data CO2 verisinden Türkiye ve karşılaştırma ülkeleri için
sadeleştirilmiş bir CSV üretir.

Kaynak: https://github.com/owid/co2-data (CC-BY 4.0)
Çıktı: input_data/iklim_co2.csv
"""
import pandas as pd

URL = 'https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv'
ULKELER = ['Turkey', 'Germany', 'United States', 'China', 'India',
           'Brazil', 'Greece', 'Iran', 'World']
SUTUNLAR = ['country', 'year', 'population', 'gdp',
            'co2', 'co2_per_capita', 'co2_per_gdp',
            'energy_per_capita', 'temperature_change_from_co2']
CIKTI = '/sc/arion/scratch/ulukag01/STEM_yaz_kampi_2026/input_data/iklim_co2.csv'


def main():
    print(f'📥 OWID CO2 verisi indiriliyor...')
    df = pd.read_csv(URL)
    print(f'   Tüm veri: {df.shape[0]} satır')

    df = df[df['country'].isin(ULKELER)]
    df = df[df['year'] >= 1950]
    df = df[SUTUNLAR]

    # Türkçe sütun adları
    df = df.rename(columns={
        'country': 'ulke',
        'year': 'yil',
        'population': 'nufus',
        'gdp': 'gsyh',
        'co2': 'co2_milyon_ton',
        'co2_per_capita': 'co2_kisi_basi',
        'co2_per_gdp': 'co2_gsyh_basi',
        'energy_per_capita': 'enerji_kisi_basi',
        'temperature_change_from_co2': 'sicaklik_degisimi',
    })

    # Türkçe ülke adları
    ulke_eslesme = {
        'Turkey': 'Türkiye',
        'Germany': 'Almanya',
        'United States': 'ABD',
        'China': 'Çin',
        'India': 'Hindistan',
        'Brazil': 'Brezilya',
        'Greece': 'Yunanistan',
        'Iran': 'İran',
        'World': 'Dünya',
    }
    df['ulke'] = df['ulke'].map(ulke_eslesme)

    print(f'\n📊 Filtrelenmiş veri: {df.shape[0]} satır')
    print(f'   Ülkeler: {df["ulke"].unique().tolist()}')
    print(f'   Yıl aralığı: {df["yil"].min()} - {df["yil"].max()}')
    print(f'\nTürkiye son 5 yıl:')
    print(df[df['ulke'] == 'Türkiye'].tail(5).to_string(index=False))

    df.to_csv(CIKTI, index=False)
    print(f'\n✅ Kaydedildi: {CIKTI}')


if __name__ == '__main__':
    main()
