"""
TÜİK verilerine dayalı 81 il demografi tablosu oluşturur.
input_data/iller_demografi.csv dosyasına yazar.

Kaynaklar (yaklaşık 2023 değerleri):
- Nüfus: TÜİK ADNKS 2023
- Doğurganlık oranı: TÜİK 2022 Toplam Doğurganlık Hızı
- Ortalama yaş: TÜİK 2023 Yaş Yapısı

Bazı küçük yuvarlamalar yapılmıştır; kamp veri seti için kullanım amaçlıdır.
"""
import pandas as pd

veri = [
    # il, bolge, nufus, dogurganlik_orani, ortalama_yas
    ('İstanbul',      'Marmara',          15655924, 1.49, 33.5),
    ('Ankara',        'İç Anadolu',        5803482, 1.55, 33.7),
    ('İzmir',         'Ege',               4479525, 1.39, 36.2),
    ('Bursa',         'Marmara',           3214571, 1.62, 33.8),
    ('Antalya',       'Akdeniz',           2696249, 1.59, 34.4),
    ('Konya',         'İç Anadolu',        2330024, 2.07, 31.6),
    ('Adana',         'Akdeniz',           2270298, 1.92, 33.3),
    ('Şanlıurfa',     'Güneydoğu Anadolu', 2213964, 3.32, 24.5),
    ('Gaziantep',     'Güneydoğu Anadolu', 2154051, 2.50, 28.4),
    ('Kocaeli',       'Marmara',           2102907, 1.64, 32.5),
    ('Mersin',        'Akdeniz',           1916432, 1.67, 33.9),
    ('Diyarbakır',    'Güneydoğu Anadolu', 1818133, 2.74, 26.0),
    ('Hatay',         'Akdeniz',           1544640, 1.95, 31.9),
    ('Manisa',        'Ege',               1475716, 1.64, 35.7),
    ('Kayseri',       'İç Anadolu',        1452638, 2.04, 32.0),
    ('Samsun',        'Karadeniz',         1356079, 1.59, 36.0),
    ('Balıkesir',     'Marmara',           1257590, 1.42, 38.6),
    ('Kahramanmaraş', 'Akdeniz',           1116618, 2.30, 28.9),
    ('Van',           'Doğu Anadolu',      1128749, 3.16, 24.8),
    ('Aydın',         'Ege',               1148241, 1.51, 37.7),
    ('Denizli',       'Ege',               1080828, 1.66, 35.7),
    ('Sakarya',       'Marmara',           1098115, 1.86, 33.0),
    ('Tekirdağ',      'Marmara',           1167059, 1.55, 33.3),
    ('Muğla',         'Ege',                1066736, 1.45, 36.8),
    ('Eskişehir',     'İç Anadolu',         906617, 1.42, 35.5),
    ('Mardin',        'Güneydoğu Anadolu',   870374, 2.81, 25.6),
    ('Trabzon',       'Karadeniz',           818023, 1.59, 35.4),
    ('Malatya',       'Doğu Anadolu',        742725, 1.95, 31.4),
    ('Erzurum',       'Doğu Anadolu',        749754, 1.99, 30.0),
    ('Ordu',          'Karadeniz',           763190, 1.55, 36.7),
    ('Afyonkarahisar','Ege',                 751344, 1.83, 33.6),
    ('Sivas',         'İç Anadolu',          647069, 1.89, 33.6),
    ('Adıyaman',      'Güneydoğu Anadolu',  610484, 2.55, 27.6),
    ('Tokat',         'Karadeniz',           596454, 1.85, 33.6),
    ('Aksaray',       'İç Anadolu',          437935, 2.03, 30.4),
    ('Batman',        'Güneydoğu Anadolu',   642541, 3.04, 24.9),
    ('Çorum',         'Karadeniz',           524130, 1.65, 36.5),
    ('Osmaniye',      'Akdeniz',             559405, 1.76, 31.6),
    ('Düzce',         'Karadeniz',           409927, 1.75, 33.8),
    ('Kırıkkale',     'İç Anadolu',          274416, 1.65, 35.4),
    ('Karaman',       'İç Anadolu',          258838, 1.81, 34.5),
    ('Yozgat',        'İç Anadolu',          412848, 1.79, 33.0),
    ('Zonguldak',     'Karadeniz',           588510, 1.40, 38.6),
    ('Çanakkale',     'Marmara',             562565, 1.40, 38.5),
    ('Edirne',        'Marmara',             414714, 1.31, 38.6),
    ('Kırklareli',    'Marmara',             375422, 1.40, 37.7),
    ('Bilecik',       'Marmara',             228673, 1.46, 36.0),
    ('Yalova',        'Marmara',             299111, 1.54, 36.0),
    ('Karabük',       'Karadeniz',           257019, 1.48, 36.9),
    ('Bartın',        'Karadeniz',           201711, 1.49, 38.4),
    ('Kastamonu',     'Karadeniz',           382574, 1.53, 39.1),
    ('Sinop',         'Karadeniz',           218400, 1.42, 41.5),
    ('Bolu',          'Karadeniz',           322545, 1.51, 36.0),
    ('Amasya',        'Karadeniz',           338061, 1.61, 36.7),
    ('Giresun',       'Karadeniz',           450862, 1.46, 38.9),
    ('Rize',          'Karadeniz',           344016, 1.56, 36.9),
    ('Artvin',        'Karadeniz',           169543, 1.60, 36.9),
    ('Gümüşhane',     'Karadeniz',           144544, 1.74, 32.5),
    ('Bayburt',       'Karadeniz',            81910, 1.84, 31.8),
    ('Erzincan',      'Doğu Anadolu',        239238, 1.67, 33.9),
    ('Tunceli',       'Doğu Anadolu',         84660, 1.21, 39.0),
    ('Bingöl',        'Doğu Anadolu',        282556, 2.37, 27.2),
    ('Elazığ',        'Doğu Anadolu',        595638, 1.81, 33.0),
    ('Bitlis',        'Doğu Anadolu',        348345, 2.59, 25.7),
    ('Muş',           'Doğu Anadolu',        408809, 2.93, 24.6),
    ('Ağrı',          'Doğu Anadolu',        511238, 3.27, 24.0),
    ('Iğdır',         'Doğu Anadolu',        203594, 2.20, 28.6),
    ('Kars',          'Doğu Anadolu',        274829, 1.95, 31.5),
    ('Ardahan',       'Doğu Anadolu',         92819, 1.91, 35.6),
    ('Hakkari',       'Doğu Anadolu',        287625, 3.03, 24.4),
    ('Şırnak',        'Güneydoğu Anadolu',   570745, 3.49, 22.6),
    ('Siirt',         'Güneydoğu Anadolu',   330230, 3.07, 24.9),
    ('Kilis',         'Güneydoğu Anadolu',   147919, 2.10, 30.6),
    ('Niğde',         'İç Anadolu',          371000, 1.97, 30.9),
    ('Nevşehir',      'İç Anadolu',          310011, 1.79, 32.8),
    ('Kırşehir',      'İç Anadolu',          243042, 1.65, 35.8),
    ('Çankırı',       'Karadeniz',           201744, 1.46, 36.9),
    ('Kütahya',       'Ege',                 580701, 1.50, 35.5),
    ('Uşak',          'Ege',                 376742, 1.54, 35.4),
    ('Burdur',        'Akdeniz',             276923, 1.55, 35.7),
    ('Isparta',       'Akdeniz',             444914, 1.39, 35.6),
]

df = pd.DataFrame(veri, columns=['il', 'bolge', 'nufus', 'dogurganlik_orani', 'ortalama_yas'])
print(f'Veri seti: {df.shape[0]} il, {df.shape[1]} sütun')
print(f'Bölgeler: {df["bolge"].value_counts().to_dict()}')

cikti_yolu = '/sc/arion/scratch/ulukag01/STEM_yaz_kampi_2026/input_data/iller_demografi.csv'
df.to_csv(cikti_yolu, index=False)
print(f'✅ Kaydedildi: {cikti_yolu}')
