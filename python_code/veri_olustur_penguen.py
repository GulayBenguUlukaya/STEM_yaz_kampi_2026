"""
Palmer Penguins veri setini Türkçe sütun adları ile input_data'ya kaydet.
Kaynak: seaborn (yerleşik), Allison Horst (CC-0)
"""
import seaborn as sns

df = sns.load_dataset('penguins').dropna()
df = df.rename(columns={
    'species': 'tur',
    'island': 'ada',
    'bill_length_mm': 'gaga_uzunluk_mm',
    'bill_depth_mm': 'gaga_derinlik_mm',
    'flipper_length_mm': 'kanat_uzunluk_mm',
    'body_mass_g': 'vucut_agirlik_g',
    'sex': 'cinsiyet',
})
# Türkçe değerler
# Tür adları bilimsel isim olduğu için olduğu gibi bırakıyoruz
df['cinsiyet'] = df['cinsiyet'].map({'Male': 'erkek', 'Female': 'dişi'})
# Adalar — Türkçe karşılıkları yok, olduğu gibi bırak

cikti = '/sc/arion/scratch/ulukag01/STEM_yaz_kampi_2026/input_data/penguenler.csv'
df.to_csv(cikti, index=False)
print(f'✅ {len(df)} penguen kaydedildi: {cikti}')
print(df.head())
print('\nTür dağılımı:', df['tur'].value_counts().to_dict())
