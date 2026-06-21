"""
Sentetik mantar veri seti — UCI Mushroom veri setinin yapısına benzer.
Kategorik öznitelikler kullanır, ikili sınıflandırma (yenir / zehirli).

NOT: Bu sentetik veridir, gerçek hayatta mantar tanımak için ASLA bu veriyi
kullanmayın. Eğitim amaçlıdır. Mantar uzmanına danışın!

Çıktı: input_data/mantarlar.csv
"""
import numpy as np
import pandas as pd

np.random.seed(42)
N = 1500
CIKTI = '/sc/arion/scratch/ulukag01/STEM_yaz_kampi_2026/input_data/mantarlar.csv'

# Öznitelikler ve değerleri (Türkçe)
SAPKA_RENGI = ['kahverengi', 'sarı', 'beyaz', 'kırmızı', 'gri', 'pembe']
SAPKA_SEKLI = ['yuvarlak', 'düz', 'çan', 'çıkıntılı', 'içbükey']
SOLUNGAC_RENGI = ['siyah', 'kahverengi', 'pembe', 'beyaz', 'çikolata']
KOKU = ['kokusuz', 'badem', 'anason', 'kreosot', 'baharatlı', 'küflü', 'çürük', 'tuzlu']
HABITAT = ['orman', 'çayır', 'kentsel', 'bahçe', 'gübre', 'odunluk']
HALKA_TIPI = ['tek', 'iki', 'yok', 'asılı']

# Gerçek mantarda 'koku' en güçlü tahmin edicidir
# Çürük/küflü/baharatlı/tuzlu/kreosot → genelde zehirli
# Kokusuz/badem/anason → genelde yenir
# Bunu sentetik veride de yansıtalım

zehirli_kokular = {'çürük', 'küflü', 'baharatlı', 'tuzlu', 'kreosot'}
zehirli_solungac = {'pembe', 'çikolata'}
zehirli_sapka_renkler = {'kırmızı', 'sarı'}

veri = []
for _ in range(N):
    sapka_r = np.random.choice(SAPKA_RENGI, p=[0.30, 0.20, 0.20, 0.10, 0.15, 0.05])
    sapka_s = np.random.choice(SAPKA_SEKLI, p=[0.35, 0.30, 0.15, 0.10, 0.10])
    solungac = np.random.choice(SOLUNGAC_RENGI, p=[0.20, 0.30, 0.10, 0.25, 0.15])
    koku = np.random.choice(KOKU, p=[0.30, 0.05, 0.05, 0.10, 0.15, 0.10, 0.15, 0.10])
    habitat = np.random.choice(HABITAT, p=[0.35, 0.20, 0.15, 0.10, 0.10, 0.10])
    halka = np.random.choice(HALKA_TIPI, p=[0.40, 0.15, 0.30, 0.15])

    # Olasılıklı zehir kuralı (gerçeğe yakın bir şekilde)
    zehir_skoru = 0
    if koku in zehirli_kokular:
        zehir_skoru += 4
    if koku in {'kokusuz', 'badem', 'anason'}:
        zehir_skoru -= 2
    if solungac in zehirli_solungac:
        zehir_skoru += 2
    if sapka_r in zehirli_sapka_renkler:
        zehir_skoru += 1
    if halka == 'yok':
        zehir_skoru += 1

    # Sigmoid ile olasılığa çevir + biraz gürültü
    olasilik = 1 / (1 + np.exp(-zehir_skoru * 0.7))
    sinif = 'zehirli' if np.random.random() < olasilik else 'yenir'

    veri.append({
        'sapka_rengi': sapka_r,
        'sapka_sekli': sapka_s,
        'solungac_rengi': solungac,
        'koku': koku,
        'habitat': habitat,
        'halka_tipi': halka,
        'sinif': sinif,
    })

df = pd.DataFrame(veri)
print(f'📊 {len(df)} mantar oluşturuldu')
print(f'\nSınıf dağılımı: {df["sinif"].value_counts().to_dict()}')
print(f'\nKoku başına zehirli oranı:')
print((df.groupby('koku')['sinif'].apply(lambda s: (s == 'zehirli').mean()) * 100).round(1).sort_values())

df.to_csv(CIKTI, index=False)
print(f'\n✅ Kaydedildi: {CIKTI}')
