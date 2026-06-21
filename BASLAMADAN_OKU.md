# 🚀 BAŞLAMADAN OKU — Kuruluş Talimatları

STEAM Yaz Kampı 2026 • Veri Bilimi & Yapay Zekâ

Bu klasörü bilgisayarına indirdin. Kodları çalıştırmak için onu **Google Drive'a yükleyip Google Colab'da** açacağız. Aşağıdaki adımları sırayla takip et. (Takılırsan öğretmenine sor — herkes ilk gün buradan geçiyor. 😊)

> 📂 **En kolay yol — hazır klasör:** İndirmek/yüklemek yerine doğrudan şu Google Drive klasörünü kullanabilirsin:
> **https://drive.google.com/drive/folders/1P1Fbw8HsqRNeKXn1vft0LfKVPOwVzi_K?usp=sharing**
> Klasörü aç → sağ üstten **"Drive'a kısayol ekle" / "Bir kopyasını oluştur"** ile kendi **Drive'ım** içine al, sonra **3. Adım**'dan devam et. Bu yolu seçtiysen **1. ve 2. Adımları atlayabilirsin.**

---

## ⭐ EN ÖNEMLİ KURAL
Klasörün adı **tam olarak** şu olmalı:

```
STEM_yaz_kampi_2026
```

Büyük/küçük harf, alt çizgiler ve yazım birebir aynı olmalı. Adı değiştirirsen kodlar veriyi bulamaz. Klasör, Google Drive'ında **"My Drive" (Drive'ım) içine doğrudan** konmalı — başka bir klasörün içine değil.

Doğru yer şöyle görünmeli:
```
Drive'ım
 └── STEM_yaz_kampi_2026
      ├── notebooks
      ├── input_data
      └── python_code
```

---

## 1️⃣ Adım — (Gerekirse) Klasörü Aç (Unzip)
İndirdiğin dosya bir **.zip** ise üstüne sağ tıkla → **"Ayıkla / Çıkart" (Extract / Unzip)** de. İçinden `STEM_yaz_kampi_2026` klasörü çıkacak.

> 💡 .zip değil de klasör olarak indirdiysen bu adımı atla.

## 2️⃣ Adım — Klasörü Google Drive'a Yükle
1. Tarayıcıda **[drive.google.com](https://drive.google.com)** adresine git ve **grubunun Google hesabıyla** giriş yap (her grup için TEK hesap kullanın).
2. Solda **"My Drive" (Drive'ım)** sekmesine tıkla.
3. `STEM_yaz_kampi_2026` klasörünü, bilgisayarından **sürükleyip** bu pencereye bırak.
   - *Alternatif:* Sol üstteki **"+ Yeni" → "Klasör yükle"** ile de yükleyebilirsin.
4. Yükleme bitene kadar **bekle** (sağ altta ilerleme çubuğu görünür). İnternet hızına göre birkaç dakika sürebilir.

## 3️⃣ Adım — Google Colab'da Defteri Aç
1. Drive'da `STEM_yaz_kampi_2026` → **`notebooks`** klasörüne gir.
2. **`gun1.ipynb`** dosyasına **çift tıkla**.
3. Üstte **"Birlikte aç → Google Colaboratory"** (Open with → Google Colab) seçeneğine tıkla.
   - İlk seferde "Colab'ı bağla" diyebilir; **bağla/yükle** de ve tekrar dene.

> 💡 Başka yol: **[colab.research.google.com](https://colab.research.google.com)** → **Dosya → Defter aç → Google Drive** sekmesinden `gun1.ipynb`'yi seç.

## 4️⃣ Adım — İlk Hücreyi Çalıştır (Drive'ı Bağla)
Defter açılınca, **en üstten başlayarak** hücreleri sırayla çalıştır (▶️ düğmesi veya **Shift + Enter**).

İlk "Hazırlık" hücresini çalıştırınca:
- Bir izin penceresi açılır → **kendi Google hesabınla giriş yap** ve **"İzin ver" (Allow)** de.
- `✅ Her şey hazır!` yazısını görürsen kurulum tamamdır. 🎉

## 5️⃣ Adım — Çalışmaya Başla
Artık hücreleri sırayla çalıştırıp **Çalışma Kitapçığı'nı (kâğıt form)** doldurabilirsin. Defterdeki işaretler:

| İşaret | Anlamı |
|--------|--------|
| ✏️ | Sen değiştir |
| 🎯 | Senin sıran (alıştırma) |
| 📝 | Çalışma Kitapçığı'na yaz |
| 💡 | İpucu |

---

## 📅 Hangi Gün Hangi Defter?
| Gün | Defter |
|-----|--------|
| Gün 1 — Python ve Veri | `notebooks/gun1.ipynb` |
| Gün 2 — Yapay Zekâ (ML) | `notebooks/gun2.ipynb` |
| Mini Proje (son gün sunumu) | `notebooks/mini_proje1...5_*.ipynb` (grubunun seçtiği) |

---

## 🆘 Bir Sorun mu Var?
- **`FileNotFoundError` / "dosya bulunamadı"** → Klasör adı tam olarak `STEM_yaz_kampi_2026` mi? "My Drive" içinde, doğrudan kökte mi? İlk "Hazırlık" hücresini çalıştırdın mı?
- **"Drive'ı bağla penceresi çıkmadı"** → İlk hücreyi tekrar çalıştır; çıkan pencerede hesabını seçip izin ver.
- **Hücre çalışmıyor / takıldı** → Üst menüden **Çalışma zamanı → Çalışma zamanını yeniden başlat** (Runtime → Restart), sonra en baştan çalıştır.
- **Grafik görünmedi** → Hücreyi bir kez daha çalıştır.
- **`input()` hücresi bekliyor** → Bu normal; hücrenin altındaki kutuya yazıp **Enter**'a bas.

Kolay gelsin, başaracaksın! 💪
