# 🚀 STEAM Yaz Kampı 2026 — Veri Bilimi & Yapay Zekâ

Lise/ortaokul öğrencileri için Python, veri analizi ve makine öğrenmesine **sıfırdan** giriş.
Tüm defterler **Google Colab**'da, Türkçe ve adım adım çalışacak şekilde hazırlandı.

> 🆕 **Kodları ve çıktıları görmek için kurulum yapmana gerek yok.** Aşağıdaki
> [`rendered/`](rendered/) klasöründeki defterler çalıştırılmış hâlde — grafikler ve
> sonuçlar dâhil her şey doğrudan GitHub'da görünüyor.

> 👩‍🔬 **Önce eğitmeninizle tanışın:** [Eğitmen Tanıtımı — Gülay Bengü Ulukaya](EGITMEN_TANITIMI.md)
> (biyoinformatik nedir, gerçek hayatta ne işe yarar ve kod bilmek bütün bunları nasıl mümkün kılar?)

---

## 📒 Defterler

| Defter | Konu | Çalıştır (Colab) | Çıktılı önizleme |
|--------|------|:----------------:|:----------------:|
| **Gün 1** | Python'a ilk adım + veriye giriş | [`notebooks/gun1.ipynb`](notebooks/gun1.ipynb) | [👁️ önizleme](rendered/gun1.ipynb) |
| **Gün 2** | Yapay zekâ / makine öğrenmesi | [`notebooks/gun2.ipynb`](notebooks/gun2.ipynb) | [👁️ önizleme](rendered/gun2.ipynb) |
| **Mini Proje 1** | 🪐 Uzay — ötegezegenler | [`notebooks/mini_proje1_uzay.ipynb`](notebooks/mini_proje1_uzay.ipynb) | [👁️ önizleme](rendered/mini_proje1_uzay.ipynb) |
| **Mini Proje 2** | 🩺 Sağlık — tümör sınıflandırma | [`notebooks/mini_proje2_saglik.ipynb`](notebooks/mini_proje2_saglik.ipynb) | [👁️ önizleme](rendered/mini_proje2_saglik.ipynb) |
| **Mini Proje 3** | 🌍 İklim — CO₂ ve sıcaklık | [`notebooks/mini_proje3_iklim.ipynb`](notebooks/mini_proje3_iklim.ipynb) | [👁️ önizleme](rendered/mini_proje3_iklim.ipynb) |
| **Mini Proje 4** | 🎤 Eurovision — oylar ve ülkeler | [`notebooks/mini_proje4_eurovision.ipynb`](notebooks/mini_proje4_eurovision.ipynb) | [👁️ önizleme](rendered/mini_proje4_eurovision.ipynb) |
| **Mini Proje 5** | 🌦️ Hava durumu — illere göre | [`notebooks/mini_proje5_hava.ipynb`](notebooks/mini_proje5_hava.ipynb) | [👁️ önizleme](rendered/mini_proje5_hava.ipynb) |

Her grup son gün **bir mini projeyi** seçip sunar.

---

## 🏁 Nasıl Başlanır?

Öğrenciler için kurulum adımları **[BASLAMADAN_OKU.md](BASLAMADAN_OKU.md)** dosyasında
(klasörü Google Drive'a yükleme + Colab'da açma).

> 📂 **En kolay yol — hazır klasör:** Materyallerin tamamı şu Google Drive klasöründe:
> **[STEM_yaz_kampi_2026 (Google Drive)](https://drive.google.com/drive/folders/1P1Fbw8HsqRNeKXn1vft0LfKVPOwVzi_K?usp=sharing)**
> Klasörü aç → sağ üstten **"Drive'a kısayol ekle" / "Bir kopyasını oluştur"** ile kendi
> **Drive'ım** içine al, sonra Colab'da `notebooks/gun1.ipynb`'yi aç.

Kısaca:

1. Yukarıdaki **[Drive klasörünü](https://drive.google.com/drive/folders/1P1Fbw8HsqRNeKXn1vft0LfKVPOwVzi_K?usp=sharing)** aç (veya bu depoyu **Code → Download ZIP** ile indir).
2. `STEM_yaz_kampi_2026` klasörünü Google Drive'da **"Drive'ım"** içine al.
3. `notebooks/gun1.ipynb` dosyasını **Google Colab** ile aç ve hücreleri sırayla çalıştır.

📄 Yazılı kaynak: [Çalışma Kitapçığı](STEAM_Kampi_2026_Calisma_Kitapcigi.pdf)

---

## 📁 Depo Yapısı

```
STEM_yaz_kampi_2026/
├── notebooks/      # Colab defterleri (öğrencilerin çalıştıracağı asıl dosyalar)
├── rendered/       # Aynı defterlerin çıktılı (çalıştırılmış) önizlemeleri
├── input_data/     # Hazır veri kümeleri (.csv)
├── python_code/    # helper_tr.py yardımcı fonksiyonları + veri üreticiler
├── tools_render/   # rendered/ klasörünü üreten yerel çalıştırma aracı
└── BASLAMADAN_OKU.md
```

> ℹ️ `rendered/` içindeki defterler **otomatik çalıştırılmış kopyalardır** (yalnızca
> önizleme amaçlı). Asıl çalışma için `notebooks/` içindeki Colab sürümlerini kullanın —
> orijinaller hiç değiştirilmedi.

---

## 🔁 Önizlemeleri Yeniden Üretmek (isteğe bağlı)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install pandas numpy matplotlib seaborn scikit-learn scipy \
            "plotly<6" "kaleido==0.2.1" nbconvert nbformat nbclient ipykernel
python -m ipykernel install --prefix .venv --name python3
python tools_render/render_notebooks.py        # rendered/ klasörünü yeniden oluşturur
```

Araç, Colab'a özgü Google Drive bağlama hücresini yerelde çalışacak şekilde sadeleştirir,
plotly grafiklerini GitHub'da görünmesi için statik PNG'ye çevirir ve `input()` hücrelerini
örnek cevaplarla otomatik yanıtlar.

---

*Hazırlayan: Bengü — 2026* 🌱
