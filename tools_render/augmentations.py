# -*- coding: utf-8 -*-
"""
rendered/ önizlemelerine eklenen EĞİTSEL içerik.

Buradaki hücreler SADECE GitHub önizlemelerine eklenir; `notebooks/` içindeki
asıl Colab defterleri değişmez. Amaç:
  • her veri setini "akranlarına sunabilecek" kadar açıklamak (📂 Veriyi Tanıyalım),
  • üretilen HER grafik/istatistiğin ne anlama geldiğini açıklamak (📊),
  • öğrencilerin deneyebileceği VARYASYONLARI çalıştırılmış çıktılarıyla göstermek (🔧),
  • mini projeler için "neler yapılabilir + nasıl sunulur/yorumlanır" rehberi vermek (🎤).

Yapı:  AUG[notebook_adı] = [ {"after": <hücrede geçen benzersiz metin>,
                              "cells": [("markdown"|"code", kaynak), ...]}, ... ]
"""

# Her önizlemenin başına eklenen ortak afiş
PREVIEW_BANNER = """\
> 🤖 **Bu, defterin "çıktılı önizleme" sürümüdür.** Asıl çalışacağınız Colab defteri
> [`notebooks/`](../notebooks) klasöründe. Buraya, normal hücrelerin **arasına**:
> 📂 *veri açıklamaları*, 📊 *her grafiğin/istatistiğin ne anlattığı*, 🔧 *deneyebileceğiniz
> varyasyonlar* (çalıştırılmış hâlde) ve mini projelerde 🎤 *sunum rehberleri* eklendi.
> Bu eklemeler **alıntı kutularıyla** ayrılmıştır; siz de aynı şeyleri kendi defterinizde deneyebilirsiniz.
"""

# ────────────────────────────────────────────────────────────────────────────
AUG = {}

def P(md):
    """Tek markdown hücresi kısayolu."""
    return ("markdown", md)

def sunum_rehberi(govde):
    return ("## 🎤 Sunum & Yorumlama Rehberi\n\n"
            "> Bu bölüm, projeyi **son gün sunarken** ne anlatacağını ve sonuçları **nasıl "
            "yorumlayacağını** özetler. Ezberleme — kendi cümlelerinle anlat.\n\n" + govde)


# ====================== GÜN 1 ======================
AUG["gun1.ipynb"] = [
    {"after": "cubuk_grafigi(df, kategori_sutunu='bolge'",
     "cells": [
        P("🔧 **Aynı fonksiyon, farklı soru.** `cubuk_grafigi` yalnızca *saymakla* kalmaz; "
          "ona `deger_sutunu` verirsen her grubun **ortalamasını** çizer. Tek satırı değiştirerek "
          "bambaşka bir soruyu yanıtlıyoruz:"),
        ("code",
         "cubuk_grafigi(df, kategori_sutunu='bolge', deger_sutunu='nufus',\n"
         "              baslik='Bölgelere Göre ORTALAMA Nüfus')"),
        P("📊 **Nasıl yorumlanır?** Üstteki ilk grafik *“her bölgede kaç il var?”* diyordu; "
          "bu grafik *“o bölgelerdeki iller ne kadar kalabalık?”* diyor. İl **sayısı** çok olan bir "
          "bölge, **ortalama nüfusu** düşük olabilir. İki grafik farklı hikâye anlatır — doğru soruyu "
          "sormak, doğru grafiği seçmektir."),
     ]},
    {"after": "histogram(df, sutun='nufus'",
     "cells": [
        P("🔧 **Başka bir sütunu incele.** Histogramda tek değiştirmen gereken `sutun=`. "
          "Nüfus yerine **ortalama yaş** dağılımına bakalım:"),
        ("code", "histogram(df, sutun='ortalama_yas', baslik='İllerin Ortalama Yaş Dağılımı')"),
        P("📊 **Nasıl yorumlanır?** Histogramda **tepe** en sık görülen değerdir. Dağılım **sağa "
          "kuyruklu** mu (birkaç uç il), yoksa **simetrik** mi? Nüfus dağılımı birkaç dev şehir yüzünden "
          "sağa çok çarpıktır; yaş dağılımı genelde daha derli topludur."),
     ]},
    {"after": "dagilim_grafigi(df, x_sutunu='nufus', y_sutunu='dogurganlik_orani'",
     "cells": [
        P("🔧 **Renk ekle + tüm ilişkileri tek bakışta gör.**"),
        ("code",
         "dagilim_grafigi(df, x_sutunu='ortalama_yas', y_sutunu='dogurganlik_orani',\n"
         "                renk_sutunu='bolge',\n"
         "                baslik='Yaş – Doğurganlık (bölgeye göre renkli)')\n"
         "korelasyon_haritasi(df, baslik='Sayısal Sütunlar Arası İlişki Haritası')"),
        P("📊 **Korelasyon haritası nasıl okunur?** Her kare iki sütunun birlikte hareketini gösterir: "
          "**+1** (kırmızı) = birlikte artar; **−1** (mavi) = biri artarken diğeri azalır; **0** = ilişki yok. "
          "⚠️ Korelasyon *neden-sonuç* demek değildir."),
     ]},
]

# ====================== GÜN 2 ======================
AUG["gun2.ipynb"] = [
    {"after": "dagilim_grafigi(penguen, x_sutunu='gaga_uzunluk_mm'",
     "cells": [
        P("🔧 **Farklı iki ölçümle dene.** Türleri ayıran tek ölçüm yoktur:"),
        ("code",
         "dagilim_grafigi(penguen, x_sutunu='kanat_uzunluk_mm', y_sutunu='gaga_derinlik_mm',\n"
         "                renk_sutunu='tur', baslik='Farklı iki ölçüm — yine ayrışıyor mu?')"),
        P("📊 **Nasıl yorumlanır?** Renk grupları (türler) **ayrı kümeler** oluşturuyorsa o iki ölçüm "
          "türü ayırmak için iyi ipuçlarıdır. Kümeler iç içeyse tek başına yetersizdir. Model de tam "
          "bunu yapar: en iyi ayıran ipuçlarını bulur."),
     ]},
    {"after": "karar_agaci_ciz(model, oznitelik_adlari=list(X.columns)",
     "cells": [
        P("🔧 **Aynı veriye farklı model.** Tek ağaç yerine **rastgele orman** (yüzlerce ağacın oyu):"),
        ("code",
         "orman = rastgele_orman_egit(X_egitim, y_egitim)\n"
         "model_degerlendir(orman, X_test, y_test, sinif_adlari=list(orman.classes_))"),
        P("📊 **Nasıl yorumlanır?** Orman çoğu zaman tek ağaçtan **biraz daha doğrudur** ama tek resimle "
          "çizilemez — yani **daha doğru, daha az açıklanabilir**. Doğruluk mu, anlaşılırlık mı? Bu bir "
          "**ödünleşimdir** (tıpta açıklanabilirlik çok önemlidir)."),
     ]},
    {"after": "for derinlik in [1, 2, 5, 15]:",
     "cells": [
        P("📊 **Tabloyu nasıl okumalı? (Aşırı öğrenme / overfitting)** Derinlik arttıkça **Eğitim** "
          "doğruluğu %100'e tırmanır — ağaç veriyi *ezberler*. Asıl önemli olan **Test** sütunudur "
          "(görülmemiş veri). Eğitim yüksek ama test düşükse model **ezberlemiş ama öğrenememiştir**. "
          "En iyi derinlik, *testin en yüksek olduğu* yerdir."),
     ]},
    {"after": "baslik='2024 Sıcaklık Tahmini'",
     "cells": [
        P("📊 **Regresyon sonucu nasıl yorumlanır?** Burada bir *sayı* tahmin ediyoruz. **RMSE** = "
          "ortalama kaç derece yanıldık (küçük=iyi); **MAE** = benzer ama uç hatalara az duyarlı; "
          "**R²** = değişimin ne kadarını açıkladık (1=mükemmel, 0=ortalamayı söylemekten farksız). "
          "Grafikte noktalar kırmızı **y=x çizgisine** yaklaştıkça tahmin iyileşir."),
     ]},

    # ——— Sınıf içi etkinlikler: 🛠️ uygulama + 💬 tartışma ———
    {"after": "print('✅ Hazırız!')",
     "cells": [P(
        "> 🧑‍🏫 **Bu defterde iki yeni işaret var:**\n"
        "> - 🛠️ **Senin sıran** — *eşinle* kendi Colab defterinde yapacağın küçük kodlama görevleri.\n"
        "> - 💬 **Sınıfça tartışalım** — önce düşünüp sonra konuşacağın sorular.\n"
        ">\n"
        "> Yanlarındaki ⏱️ süreler öneridir — acele yok, denemek serbest, hata yapmak öğrenmenin parçası! 😊")]},
    {"after": "dogruluk = model_degerlendir(model, X_test, y_test, sinif_adlari=list(model.classes_))",
     "cells": [P(
        "### 🛠️ Senin sıran — eşinle dene · ⏱️ ~5 dakika\n\n"
        "Kendi Colab defterinde, ağacı eğiten satırdaki `max_derinlik=3` değerini önce **2**, sonra **5** "
        "yapın ve her seferinde `model_degerlendir`'i yeniden çalıştırın.\n\n"
        "- Doğruluk yükseldi mi, düştü mü?\n"
        "- Karmaşıklık matrisinde model **hangi iki türü** en çok karıştırıyor?\n\n"
        "Önce eşinizle **tahmin edin**, sonra çalıştırıp kontrol edin. 💡 *İpucu: yalnızca tek bir sayıyı değiştiriyorsunuz.*")]},
    {"after": "oznitelik_onemi_grafigi(model, oznitelik_adlari=list(X.columns), en_iyi_n=8)",
     "cells": [P(
        "### 🛠️ Senin sıran — eşinle dene · ⏱️ ~5 dakika\n\n"
        "Yukarıdaki grafikte **en önemli 2 öznitelik** hangisi? Şimdi kendi defterinizde bu iki ölçümü "
        "birbirine karşı çizin, renk olarak da türü verin:\n\n"
        "```python\n"
        "dagilim_grafigi(penguen, x_sutunu='...', y_sutunu='...', renk_sutunu='tur')\n"
        "```\n\n"
        "Türler gerçekten **ayrı kümeler** oluşturuyor mu? 💡 *İpucu: sütun adlarını grafikteki en uzun "
        "çubuklardan seçin (örn. `gaga_uzunluk_mm`).*")]},
    {"after": "Ağaç derinliğini artırınca",
     "cells": [P(
        "### 💬 Sınıfça tartışalım · ⏱️ 2 dk düşün, sonra paylaş\n\n"
        "Bir öğrenci sınava çalışırken bütün soruların cevabını **ezberlerse**, daha önce hiç görmediği "
        "*yeni* bir soruda ne olur?\n\n"
        "- Bu durum, ağaç derinleştikçe **eğitimde** çok iyi ama **testte** kötü olmasına nasıl benziyor?\n"
        "- Sizce **‘ezberlemek’** ile **‘öğrenmek’** arasındaki fark ne?\n\n"
        "Önce eşinizle konuşun, sonra birkaç grup fikrini sınıfla paylaşsın.")]},
    {"after": "🤔 Etik tartışma — sınıfça konuşun",
     "cells": [P(
        "### 💬 Tartışma soruları · ⏱️ 3 dk eşinle, sonra sınıfça\n\n"
        "1. Mantar modeli **%99 doğru** olsa bile, ormanda bulduğun gerçek bir mantarı yemek için ona "
        "güvenir miydin? Neden?\n"
        "2. Burada hangi hata daha **tehlikeli**: yenebilir bir mantara ‘zehirli’ demek mi, yoksa zehirli "
        "bir mantara ‘yenir’ demek mi?\n"
        "3. ‘Çok doğru ama %100 değil’ olan yapay zekâya başka **nerelerde** dikkatle güvenmeliyiz? "
        "(sürücüsüz arabalar, tıbbi teşhis, yüz tanıma…)\n\n"
        "Her grup bir soruyu seçip **1 cümlelik** cevabını sınıfa söylesin.")]},
    {"after": "Çıkan **RMSE** kaç",
     "cells": [P(
        "### 🛠️ Senin sıran — eşinle dene · ⏱️ ~7 dakika\n\n"
        "Kendi defterinizde `ozellikler` listesinden `'sicaklik_oncesi_7gun'` özelliğini **silin** ve "
        "modeli yeniden eğitip değerlendirin.\n\n"
        "- RMSE arttı mı, azaldı mı?\n"
        "- Yani **‘7 gün önceki sıcaklık’** yarını tahmin etmeye *yardım ediyor mu*?\n\n"
        "Önce tahmin edin, sonra deneyip görün. 💡 *İpucu: listeden bir satırı silmeniz yeterli; modeli "
        "kuran hücreyi tekrar çalıştırmayı unutmayın.*")]},
]

# ════════════════════════════════════════════════════════════════════
#                         MİNİ PROJELER
# ════════════════════════════════════════════════════════════════════

# ====================== MİNİ 1 — UZAY ======================
AUG["mini_proje1_uzay.ipynb"] = [
    {"after": "uzay = veri_yukle('input_data/uzay_otegezegen.csv')",
     "cells": [P(
        "## 📂 Veriyi Tanıyalım — Kepler Ötegezegen Adayları\n\n"
        "Bu veri, NASA'nın **Kepler Uzay Teleskobu** gözlemlerinden türetilmiştir. Kepler, bir "
        "gezegen yıldızının önünden geçtiğinde yıldız ışığında oluşan minik **kararmayı (transit)** "
        "ölçer. Her satır böyle bir **aday sinyaldir** — ama her sinyal gerçek gezegen değildir!\n\n"
        "- **Satır sayısı:** 7.327 aday sinyal\n"
        "- **Gerçek gezegen oranı:** ~%37,5 (gerisi *yanlış pozitif*: yıldız lekesi, çift yıldız, gürültü…)\n"
        "- **Yaşanabilir bölgede:** yalnızca ~%4\n\n"
        "| Sütun | Anlamı |\n|---|---|\n"
        "| `yorunge_periyodu_gun` | Yıldız çevresinde 1 tur kaç gün (Dünya = 365) |\n"
        "| `transit_suresi_saat` | Geçişin kaç saat sürdüğü |\n"
        "| `transit_derinligi_ppm` | Yıldız ne kadar karardı — büyük = büyük gezegen |\n"
        "| `gezegen_yaricap_dunya` | Gezegenin yarıçapı (Dünya = 1) |\n"
        "| `yildiz_sicakligi_K` | Yıldız sıcaklığı (Kelvin; Güneş ≈ 5778) |\n"
        "| `denge_sicakligi_K` | Gezegenin tahmini sıcaklığı (Kelvin) |\n"
        "| `sinyal_gurultu_orani` | Sinyalin netliği — yüksek = güvenilir |\n"
        "| `yasanabilir_bolge` | Sıvı su olabilecek mesafede mi? (Doğru/Yanlış) |\n"
        "| `gercek_gezegen` | **HEDEF:** doğrulanmış gerçek gezegen mi? |\n\n"
        "💬 **Akranlarına anlat:** *“Teleskop binlerce ‘belki gezegen’ sinyali yakaladı; biz bunların "
        "hangisinin gerçek olduğunu ayırt etmeye ve içlerinden Dünya benzerlerini bulmaya çalışıyoruz.”*")]},
    {"after": "veriyi_ozetle(uzay)",
     "cells": [P(
        "📊 **`veriyi_ozetle` çıktısı ne diyor?** Satır/sütun sayısını, eksik değerleri ve her sayısal "
        "sütunun min–ortalama–max değerlerini verir. Burada bazı sütunların **çok geniş aralıklı** "
        "olduğuna dikkat: yarıçap 0,1'den 200.000'e gidiyor — yani veride hem küçük kayalık adaylar hem "
        "de dev (muhtemelen hatalı) ölçümler var. Modeli kurmadan önce bu **uç değerleri** bilmek önemlidir.")]},
    {"after": "uzay['yildiz_tipi'] = uzay['yildiz_sicakligi_K'].apply(yildiz_tipi)",
     "cells": [P(
        "📊 **Yıldız tipi tablosu ne anlatıyor?** Her yıldız tipinde kaç aday var, bunların ne oranı "
        "gerçek gezegen, ortalama yarıçap ve periyot ne. Yıldızlar sıcaklıklarına göre sınıflanır "
        "(M=kırmızı cüce → A=sıcak beyaz). Kepler bilinçli olarak çoğunlukla **Güneş benzeri (G/K)** "
        "yıldızlara baktı; bu yüzden onlar baskındır — yani veri *Kepler'in seçimini* yansıtır, evrenin "
        "tamamını değil. (Buna **örnekleme yanlılığı** denir.)")]},
    {"after": "baslik='Yıldız Tipine Göre Aday Sayısı (Kepler nereye baktı?)'",
     "cells": [
        P("🔧 **Sayı yerine ORAN sor.** `deger_sutunu='gercek_gezegen'` her tipte adayların ne kadarının "
          "**gerçek çıktığını** çizer:"),
        ("code",
         "cubuk_grafigi(uzay, kategori_sutunu='yildiz_tipi', deger_sutunu='gercek_gezegen',\n"
         "              baslik='Yıldız Tipine Göre GERÇEK Gezegen Oranı')"),
        P("📊 **Nasıl yorumlanır?** Çok aday ≠ çok gerçek gezegen. Az aday olup yüksek oranda gerçek "
          "çıkan bir tip olabilir. Sunumda **‘nereye baktık’** (sayı) ile **‘ne bulduk’** (oran) farkını ayır."),
     ]},
    {"after": "sicak_jupiter = uzay[",
     "cells": [P(
        "📊 **‘Sıcak Jüpiter’ avı ve dağılım grafiği ne gösteriyor?** Sıcak Jüpiter = yıldızına çok yakın "
        "(kısa periyot), Jüpiter kadar büyük bir gezegen; yüzeyinde kurşun bile erir. Dağılım grafiğinde "
        "**sol-üst köşe** (kısa periyot + büyük yarıçap) bu gezegenlerdir. Gerçek gezegenlerin rastgele "
        "değil, **fiziksel bir örüntü** oluşturması, verinin anlamlı olduğunu gösterir — sunumda "
        "‘rastgele gürültü değil, gerçek gök bilimi’ diyebilirsin.")]},
    {"after": "model = rastgele_orman_egit(X_egitim, y_egitim)",
     "cells": [
        P("📊 **Karmaşıklık matrisi bu projede nasıl okunur?** Satırlar **gerçek** sınıfı (Gerçek Gezegen / "
          "Gerçek Gezegen Değil), sütunlar modelin **tahminini** gösterir. Köşegen = doğru tahminler. Köşegen "
          "dışı iki hata **aynı değildir**: gerçek olmayan bir sinyali ‘gerçek gezegen’ sanmak NASA'ya boşuna "
          "teleskop zamanı harcatır; gerçek bir gezegeni kaçırmak ise *yeni bir dünyayı* ıskalamaktır. "
          "Doğruluğu mutlaka **baseline** (%62,5 ‘hepsine gerçek değil de’) ile kıyasla."),
        P("🔧 **Modeli değiştir, karşılaştır.** Rastgele orman yerine tek karar ağacı ne yapıyor?"),
        ("code",
         "agac = karar_agaci_egit(X_egitim, y_egitim, max_derinlik=4)\n"
         "model_degerlendir(agac, X_test, y_test,\n"
         "                  sinif_adlari=['Gerçek Gezegen Değil', 'Gerçek Gezegen'])"),
        P("📊 Genelde orman biraz daha doğrudur; ağaç ise *neden* öyle karar verdiğini gösterebilir."),
     ]},
    {"after": "baslik='Gerçek Gezegeni Ele Veren İpuçları'",
     "cells": [P(
        "📊 **Öznitelik önemi nasıl yorumlanır?** Çubuk ne kadar uzunsa model o ipucuna o kadar güveniyor. "
        "Burada genelde **sinyal/gürültü oranı** ve **transit derinliği** öne çıkar — astronomi sezgisiyle "
        "uyumlu: net, güçlü, tekrarlayan bir sinyal gerçek gezegeni ele verir. ⚠️ ‘Önemli’ = *modele "
        "yararlı*; her zaman fiziksel ‘sebep’ anlamına gelmez.")]},
    {"after": "yasanabilir = gercek_gezegenler[gercek_gezegenler['yasanabilir_bolge']]",
     "cells": [P(
        "📊 **Yaşanabilir bölge sayıları ne diyor?** Gerçek gezegenlerin yalnızca küçük bir kısmı sıvı su "
        "olabilecek mesafede. Bu çıktı, ‘ikinci Dünya’ aramanın neden bu kadar zor olduğunu **sayıyla** "
        "gösterir: binlerce adaydan yola çıkıp avuç içi kadar umut verici gezegene iniyoruz.")]},
    {"after": "dunya_benzeri = yasanabilir[",
     "cells": [P(
        "📊 **‘Dünya benzeri’ liste:** Yarıçap (0,8–1,5 Dünya) ve sıcaklık (250–350 K) filtreleriyle "
        "seçilen adaylar. Sunumun **en heyecan verici** anı: ‘işte potansiyel ikinci Dünyalar’. "
        "⚠️ ‘Benzeri’ ≠ ‘yaşam var’ — sadece boyut ve sıcaklık uygun demektir; atmosfer, su, kimya hâlâ bilinmiyor.")]},
    {"after": "uzay_clean['yildiz_id'] = uzay_clean['aday_id'].str.split",
     "cells": [P(
        "📊 **Çok-gezegenli sistemler:** Bir yıldızın etrafında birden çok gerçek gezegen olabilir. "
        "Tablo, ‘yıldız başına kaç gezegen’ dağılımını verir. Güneş sistemimizde **8** gezegen var; "
        "buradaki en kalabalık sistemle karşılaştırmak güzel bir sunum köprüsüdür.")]},
    {"after": "olasiliklar = model.predict_proba(X_test)",
     "cells": [P(
        "📊 **Modelin en güvensiz olduğu adaylar:** Olasılığı **%50'ye en yakın** olanlar — model resmen "
        "‘kararsız’. Bunlar NASA için ‘tekrar bak’ listesidir. Bir modelin yalnızca tahminini değil, "
        "**ne kadar emin olduğunu** da bilmek çok değerlidir: ‘bilmediğini bilen’ bir yapay zekâ daha güvenlidir.")]},
    {"after": "Adım 8: Sunum için notlarınız",
     "cells": [P(sunum_rehberi(
        "**🪐 Ana mesaj (bir cümle):** *“Binlerce Kepler adayından gerçek gezegenleri yanlış alarmlardan "
        "ayırmayı ve içlerinden Dünya benzerlerini bulmayı öğrendik.”*\n\n"
        "**Grafik sırası:** ① yıldız tipi (sayı + oran) → ② yörünge-yarıçap dağılımı (Sıcak Jüpiter köşesi) "
        "→ ③ karmaşıklık matrisi + doğruluk → ④ öznitelik önemi → ⑤ Dünya benzeri liste (final).\n\n"
        "**Yorumlama anahtarları:** doğruluğu **baseline** ile kıyasla; iki **hata türünü** ayır; "
        "‘en güvensiz adaylar’ı *tekrar-bak listesi* diye sun.\n\n"
        "**Sık hatalar:** ❌ ‘%95 doğru = kusursuz’ (hata türüne bak) · ❌ ‘önemli öznitelik = sebep’ · "
        "❌ aday **sayısı** ile gerçek **oranını** karıştırmak."))]},
]

# ====================== MİNİ 2 — SAĞLIK ======================
AUG["mini_proje2_saglik.ipynb"] = [
    {"after": "veri = load_breast_cancer(as_frame=True)",
     "cells": [P(
        "## 📂 Veriyi Tanıyalım — Wisconsin Göğüs Kanseri\n\n"
        "Makine öğrenmesinin en ünlü **gerçek** veri setlerinden biridir. Bir tümörden iğneyle alınan "
        "hücre örneğinin **mikroskop görüntüsü** sayısallaştırılmış; her hücre çekirdeğinin boyutu, biçimi "
        "ve dokusu ölçülmüş. Her satır **bir hastadır**.\n\n"
        "- **Hasta sayısı:** 569\n"
        "- **Öznitelik (sütun):** 30 — 10 temel ölçümün *ortalama* (`mean`), *standart hata* (`error`) "
        "ve *‘en kötü’* (`worst`) değerleri\n"
        "- **Hedef:** `0 = kötü huylu (malignant)` → 212 hasta · `1 = iyi huylu (benign)` → 357 hasta\n\n"
        "| Ölçüm (10 temel) | Anlamı |\n|---|---|\n"
        "| `radius` (yarıçap) | Hücre çekirdeğinin büyüklüğü |\n"
        "| `texture` (doku) | Gri tonların pürüzlülüğü |\n"
        "| `perimeter` (çevre) | Çekirdeğin çevre uzunluğu |\n"
        "| `area` (alan) | Çekirdeğin kapladığı alan |\n"
        "| `smoothness` (pürüzsüzlük) | Kenar çizgisinin düzgünlüğü |\n"
        "| `compactness` (kompaktlık) | Çevre²/alan oranı |\n"
        "| `concavity` (içbükeylik) | Kenardaki çukurların derinliği |\n"
        "| `concave points` | İçbükey (çukur) nokta sayısı |\n"
        "| `symmetry` (simetri) | Çekirdeğin simetrikliği |\n"
        "| `fractal dimension` | Kenar çizgisinin karmaşıklığı |\n\n"
        "💡 Her ölçüm **3 biçimde** gelir: `mean radius` (ortalama), `radius error` (sapma), "
        "`worst radius` (en kötü/en büyük). Genelde **‘worst’** değerleri kanseri en iyi ele verir.\n\n"
        "💬 **Akranlarına anlat:** *“Bilgisayara bir tümörün hücre ölçümlerini veriyoruz; o da iyi huylu "
        "mu kötü huylu mu tahmin ediyor — gerçek doktorlara yardımcı olacak şekilde.”* ⚠️ Bu bir **eğitim** "
        "veri setidir; gerçek teşhisi her zaman bir hekim koyar.")]},
    {"after": "print(f'Kötü huylu: {kotu}",
     "cells": [P(
        "📊 **Sınıf dengesi + baseline ne diyor?** İyi huylu (~%63) kötü huyludan (~%37) fazla. "
        "**Baseline** = hiç düşünmeden herkese ‘iyi huylu’ deseydik ~%63 tutturuduk. Modelimiz bu çıtayı "
        "**geçmezse işe yaramaz**. Her sınıflandırma projesinde önce bu çıtayı belirle — yoksa yüksek "
        "doğruluk seni kandırır.")]},
    {"after": "baslik='Tümör Yarıçapı: Kötü Huylu vs İyi Huylu'",
     "cells": [
        P("🔧 **Başka bir ölçüme bak.** `sayisal_sutun`'u değiştir. Yarıçap iyi ayırıyordu; ya **doku**?"),
        ("code",
         "kutu_grafigi(veri_full, kategori_sutunu='sinif', sayisal_sutun='mean texture',\n"
         "             baslik='Tümör Dokusu: Kötü Huylu vs İyi Huylu')"),
        P("📊 **Kutu grafiği nasıl okunur?** Kutu, değerlerin orta %50'sini gösterir; çizgi ortancadır. "
          "İki kutunun **örtüşmesi** ne kadar azsa o ölçüm sınıfları o kadar iyi ayırır. Yarıçapın kutuları "
          "neredeyse hiç örtüşmezken dokununkiler daha çok örtüşür — yani yarıçap **tek başına** daha güçlü ipucudur."),
     ]},
    {"after": "Lojistik Regresyon: %{loj_d*100",
     "cells": [P(
        "📊 **Üç modeli nasıl karşılaştırmalı?** Tek bir test bölünmesindeki yüzde **şansa** bağlı olabilir "
        "(hangi hastalar teste düştü?). Bu yüzden bir sonraki adımdaki **cross-validation** daha güvenilirdir. "
        "Buradaki tek-test sonuçlarını ‘ilk izlenim’ olarak gör, kesin sanma.")]},
    {"after": "5-katlı cross-validation",
     "cells": [P(
        "📊 **‘± standart sapma’ ne demek?** Veriyi 5 parçaya bölüp 5 kez test ediyoruz. Ortalama = tipik "
        "başarı; **±** sonrası sayı = sonuçların ne kadar oynadığı. **Düşük ±** = kararlı, güvenilir; "
        "**yüksek ±** = ‘bazen iyi bazen kötü’. İki modelin ortalaması yakınsa **daha küçük ±** olanı seç — "
        "tıpta *tutarlılık* hayat kurtarır.")]},
    {"after": "fpr, tpr, esikler = roc_curve(y_test, olas)",
     "cells": [P(
        "📊 **ROC eğrisi + AUC nasıl yorumlanır?** Model bir *olasılık* üretir; ‘eşiği’ değiştirince doğru "
        "alarm ile yanlış alarm dengesi değişir. ROC bu dengeyi tüm eşikler için çizer; eğri **sol-üst köşeye** "
        "ne kadar yakınsa o kadar iyi. **AUC** (eğri altı alan) tek sayıyla özetler: **1,0 = mükemmel, "
        "0,5 = yazı-tura**. Sunumda ‘modelimiz hangi eşikte olursa olsun iyi’ demenin sayısal kanıtıdır.")]},
    {"after": "onem_df = pd.DataFrame({'oz': X.columns",
     "cells": [P(
        "📊 **En önemli 10 öznitelik:** Rastgele orman, kararlarında en çok hangi ölçümlere güvendiğini "
        "söyler. Genelde **‘worst’ (en kötü)** çekirdek ölçüleri öne çıkar — mantıklı, çünkü en anormal "
        "hücreler kanseri ele verir. Bu liste, bir sonraki adımdaki ‘az öznitelik yeter mi?’ sorusunun temelidir.")]},
    {"after": "for n in [3, 5, 10, 20, 30]:",
     "cells": [P(
        "📊 **‘Az öznitelik yeter mi?’ nasıl yorumlanır?** Çoğu zaman **5 ölçüm**, 30 ölçümün doğruluğunun "
        "neredeyse tamamını verir. Gerçek hayatta bunun anlamı büyük: her ölçüm **zaman, para ve hastaya "
        "işlem** demektir. ‘%1 doğruluk için 25 fazladan ölçüm değer mi?’ tam da bir mühendisin sorması "
        "gereken **maliyet-fayda** sorusudur.")]},
    {"after": "en_guvensiz = test_df.sort_values('guvensizlik').head(5)",
     "cells": [P(
        "📊 **En güvensiz hastalar:** Olasılığı **%50'ye yakın** olan hastalar; model kararsız. Gerçek bir "
        "sistemde bunlar **mutlaka bir uzmana yönlendirilmeli**. Yapay zekânın ‘bilmediğini bilmesi’ — yani "
        "emin olmadığını söyleyebilmesi — özellikle tıpta hayat kurtarır.")]},
    {"after": "cm = confusion_matrix(y_test, tahminler)",
     "cells": [P(
        "📊 **Karmaşıklık matrisi — hata türleri (bu projenin kalbi):** İki hata **asla eşit değildir**. "
        "**False Negative** (kötü huyluya ‘iyi’ demek) = kanseri kaçırmak = **ölümcül** ☠️. "
        "**False Positive** (iyiye ‘kötü’ demek) = gereksiz endişe / ek biyopsi = rahatsız edici ama "
        "telafi edilebilir. Bu yüzden tıbbi modeller bilerek **‘kanseri kaçırmamaya’** ayarlanır, gerekirse "
        "fazladan yanlış alarm pahasına.")]},
    {"after": "Adım 8: Sunum için notlarınız",
     "cells": [P(sunum_rehberi(
        "**🩺 Ana mesaj:** *“Tümör ölçümlerinden iyi/kötü huylu ayrımını yüksek doğrulukla yapabiliyoruz; "
        "ama sağlıkta asıl mesele doğruluk değil, **hangi hatayı yaptığın**.”*\n\n"
        "**Grafik sırası:** ① sınıf dengesi + baseline → ② kutu grafiği (ayrışma) → ③ cross-validation "
        "(en kararlı model) → ④ ROC + AUC → ⑤ karmaşıklık matrisi (**FN vs FP** tartışması).\n\n"
        "**Yorumlama anahtarları:** doğruluğu **baseline** ile kıyasla; **AUC**'yi ‘1=mükemmel, 0,5=rastgele’ "
        "ölçeğine oturt; FN'in FP'den neden daha tehlikeli olduğunu anlat.\n\n"
        "**Sık hatalar:** ❌ ‘yüksek doğruluk = iyi model’ (dengesiz veride yanıltıcı) · ❌ tek-testi kesin "
        "sanmak · ❌ iki hata türünü eşit saymak."))]},
]

# ====================== MİNİ 3 — İKLİM ======================
AUG["mini_proje3_iklim.ipynb"] = [
    {"after": "iklim = veri_yukle('input_data/iklim_co2.csv')",
     "cells": [P(
        "## 📂 Veriyi Tanıyalım — Ülkelerin CO₂ Tarihi\n\n"
        "Gerçek dünya verisine dayanan bu set; 9 ekonomi (Türkiye, Almanya, ABD, Çin, Hindistan, İran, "
        "Brezilya, Yunanistan) + **‘Dünya’** toplamı için **1950–2024** arası yıllık değerleri tutar. "
        "Her satır **bir ülke-yıl** kombinasyonudur.\n\n"
        "- **Satır sayısı:** 675 (ülke × yıl)\n"
        "- **Zaman aralığı:** 1950 – 2024 (75 yıl)\n"
        "- **Ana fikir:** Aynı veriyi **iki ölçüyle** okuyacağız (toplam vs kişi başı) — ve sıralamanın "
        "değişmesi bu projenin dersi\n\n"
        "| Sütun | Anlamı |\n|---|---|\n"
        "| `ulke`, `yil` | Ülke ve yıl |\n"
        "| `co2_milyon_ton` | Yıllık **toplam** CO₂ salımı (milyon ton) |\n"
        "| `co2_kisi_basi` | **Kişi başına** CO₂ (ton/kişi) — ‘adalet’ ölçüsü |\n"
        "| `co2_gsyh_basi` | Ekonomik üretim başına CO₂ (verimlilik) |\n"
        "| `nufus`, `gsyh` | Nüfus ve ekonomik büyüklük (GSYH) |\n"
        "| `enerji_kisi_basi` | Kişi başı enerji tüketimi |\n"
        "| `sicaklik_degisimi` | O ülkenin salımlarının küresel ısınmaya **kümülatif** katkısı (°C) |\n\n"
        "💬 **Akranlarına anlat:** *“Kim ne kadar karbon saldı? Ama ‘kim daha sorumlu?’ "
        "sorusunun cevabı, hangi ölçüye baktığına göre değişiyor.”*")]},
    {"after": "title='Türkiye Yıllık CO₂ Emisyonu (Milyon Ton)'",
     "cells": [
        P("📊 **Türkiye'nin CO₂ eğrisi ne anlatıyor?** Çizgi 1950'den 2024'e neredeyse sürekli **yukarı** "
          "gidiyor (kod altta ‘kaç kat arttığını’ da yazıyor). Çıkış/duraklama yıllarını tarihsel olaylarla "
          "(1973 petrol krizi, 2001 krizi, 2020 COVID) eşleştir — veriye **hikâye** katmak sunumu güçlendirir.\n\n"
          "🔧 **Başka bir ülkeyle kıyasla.** `ulke` filtresini değiştir; Türkiye artarken Almanya nasıl?"),
        ("code",
         "alm = iklim[iklim['ulke'] == 'Almanya']\n"
         "fig = px.line(alm, x='yil', y='co2_milyon_ton', markers=True,\n"
         "              title='Almanya Yıllık CO₂ Emisyonu (Milyon Ton)')\n"
         "fig.show()"),
        P("📊 Türkiye sürekli yükselirken Almanya **zirve yapıp düşüyor** — ‘gelişmekte olan’ ile "
          "‘sanayisini dönüştürmüş’ ülke farkı tek bakışta görünür."),
     ]},
    {"after": "veri_2019 = iklim[(iklim['ulke']==ulke) & (iklim['yil']==2019)]",
     "cells": [P(
        "📊 **COVID-2020 tablosu ne gösteriyor?** Her ülke için 2019→2020 **düşüşü** ve 2020→2021 "
        "**geri tepkisi**. Karantinalar emisyonu gerçekten düşürdü — ama ertesi yıl çoğu ülke geri sıçradı. "
        "Bu ‘doğal bir deney’: kimse bilerek emisyon kısmadı, dünya bir yıl yavaşladı. **İmplikasyon:** "
        "geçici davranış değişikliği geçici etki yapar; kalıcı düşüş için yapısal (enerji) dönüşüm gerekir.")]},
    {"after": "title='Kişi Başı CO₂ — ABD ve Almanya baskın, Çin orta'",
     "cells": [P(
        "📊 **Toplam mı, kişi başı mı? (Adalet sorusu)** Aynı veriyi iki şekilde ölçtük ve **sıralama "
        "değişti**. Toplam CO₂'de büyük nüfuslu ülkeler (Çin) önde; kişi başında az nüfuslu ama yoğun "
        "tüketen ülkeler (ABD) öne çıkar. ‘Kim daha sorumlu?’ sorusunun cevabı **hangi ölçüyü seçtiğine** "
        "bağlı — yani veride ‘tarafsız tek sayı’ diye bir şey yoktur.")]},
    {"after": "son_2024 = iklim[iklim['yil'] == 2024]",
     "cells": [P(
        "📊 **2024 sıralaması:** Tek tabloda hem toplam hem kişi başı sütununa bak. Çin **toplamda** açık ara "
        "birinci; ama **kişi başında** ABD çok daha yüksek. Bu, ‘en çok kirleten kim?’ sorusunun iki farklı "
        "ama ikisi de doğru cevabı olduğunu somutlaştırır — sunumda güçlü bir ‘adalet’ tartışması açar.")]},
    {"after": "tum_ulkeler['kumulatif_pay']",
     "cells": [P(
        "📊 **Pareto analizi:** Ülkeleri büyükten küçüğe sıralayıp kümülatif yüzdeyi topluyoruz. Genelde "
        "**az sayıda ülke**, toplamın çok büyük kısmını üretir (Pareto / 80-20 ilkesi). **İmplikasyon:** "
        "iklim çözümü büyük ölçüde en büyük birkaç salımcının eylemine bağlıdır — herkes eşit ölçüde sorumlu değil.")]},
    {"after": "Küresel Sıcaklığa Toplam Katkısı",
     "cells": [P(
        "📊 **CO₂ → sıcaklık katkısı:** Her ülkenin **tarihsel** salımlarının küresel ısınmaya toplam katkısı "
        "(°C). ‘Tarihsel’ kelimesi kilit: bugün az salan bir ülke, geçmişte çok salmışsa ısınmadan hâlâ "
        "sorumlu olabilir. Etki **birikimli** ve gecikmelidir — bir yılın değil, on yılların toplamıdır.")]},
    {"after": "zirve = alm.loc[alm['co2_milyon_ton'].idxmax()]",
     "cells": [P(
        "📊 **Almanya örneği:** Almanya zirvesini çoktan yapıp **düşüşe** geçmiş; Türkiye hâlâ **artışta**. "
        "Bu karşılaştırma ‘emisyon düşürmek mümkün mü?’ sorusuna somut bir **‘evet’** verir — ama bunun "
        "yenilenebilir enerji, verimlilik ve politika gerektirdiğini de gösterir.")]},
    {"after": "Lineer model 2050",
     "cells": [P(
        "📊 **Lineer tahmin nereye kadar güvenilir?** Düz çizgi geçmiş eğilimi uzatır; ama gerçekte politika, "
        "teknoloji ve anlaşmalar eğriyi **büker**. Modelin 2050 tahmini Türkiye'nin 2053 net-sıfır hedefiyle "
        "**çelişiyorsa**, bu modelin ‘yanlış’ olduğunu değil, **‘bugünkü gidişle hedefe ulaşılamayacağını’** "
        "gösterir. Tahmin bir kehanet değil, bir **uyarıdır**. ⚠️ Modeli eğitim aralığının çok dışına "
        "(2050) uzatmak her zaman risklidir.")]},
    {"after": "Adım 8: Sunum için notlarınız",
     "cells": [P(sunum_rehberi(
        "**🌍 Ana mesaj:** *“Türkiye'nin karbon hikâyesini gerçek veriyle anlattık; toplam-vs-kişi başı "
        "ölçüsünün adaleti nasıl değiştirdiğini ve bugünkü gidişin 2053 hedefiyle çeliştiğini gösterdik.”*\n\n"
        "**Grafik sırası:** ① TR tarihçesi (kırılmaları işaretle) → ② COVID düşüşü + geri tepki → ③ toplam vs "
        "kişi başı (adalet) → ④ Almanya vs Türkiye → ⑤ 2030/2050 tahmini vs Paris hedefi (final çelişki).\n\n"
        "**Yorumlama anahtarları:** artışı **‘kaç kat’** söyle; COVID düşüşünün **kalıcı olmadığını** vurgula; "
        "sıralamanın ölçüyle değiştiğini göster.\n\n"
        "**Sık hatalar:** ❌ ‘CO₂ ile sıcaklık aynı yıl artıyor’ (etki birikimli/gecikmeli) · ❌ lineer tahmini "
        "kesin gelecek sanmak · ❌ tek ölçü (yalnız toplam veya yalnız kişi başı) göstermek."))]},
]

# ====================== MİNİ 4 — EUROVISION ======================
AUG["mini_proje4_eurovision.ipynb"] = [
    {"after": "esc = veri_yukle('input_data/eurovision.csv')",
     "cells": [P(
        "## 📂 Veriyi Tanıyalım — Eurovision (2000–2023)\n\n"
        "Bu projede **iki** gerçek veri seti birlikte kullanılır; her satırın ne olduğu farklıdır, dikkat:\n\n"
        "- **`eurovision.csv`** — her satır **bir ülkenin bir yıldaki katılımı** (916 satır, 50 ülke, 2000–2023)\n"
        "- **`eurovision_oylar.csv`** — her satır **‘X ülkesi → Y ülkesine kaç puan verdi’** (21.165 oy kaydı)\n\n"
        "| Sütun (`eurovision.csv`) | Anlamı |\n|---|---|\n"
        "| `ulke`, `yil`, `sanatci`, `sarki` | Kim, hangi yıl, hangi şarkıyla katıldı |\n"
        "| `final_sira` | Final sıralaması (**1 = birinci, küçük = iyi!**) |\n"
        "| `final_puan` | Finalde aldığı toplam puan |\n"
        "| `ev_sahibi` | O yıl ev sahibi mi? (Doğru/Yanlış) |\n"
        "| `ev_sahibi_uzaklik_km` | Ülkenin ev sahibine uzaklığı (km) |\n"
        "| `final_cikis_sirasi` | Sahneye kaçıncı sırada çıktı |\n"
        "| `tele_puan_final` / `juri_puan_final` | Halk (tele) ve jüri puanları |\n"
        "| `ilk_10` | İlk 10'a girdi mi? (model hedefi) |\n\n"
        "| Sütun (`eurovision_oylar.csv`) | Anlamı |\n|---|---|\n"
        "| `oy_veren_ulke` → `oy_alan_ulke` | Kim kime puan verdi |\n"
        "| `puan` | Verilen puan (0–12) |\n"
        "| `uzaklik_km` | İki ülke arası uzaklık (komşu oylaması için) |\n\n"
        "💡 Sıralamada **küçük sayı iyidir** (1 = şampiyon); grafiklerde y eksenini bu yüzden ters çeviririz.\n\n"
        "💬 **Akranlarına anlat:** *“Eurovision sadece şarkı yarışması mı, yoksa coğrafya ve siyaset de "
        "işin içinde mi? Gerçek veriyle bakacağız.”*")]},
    {"after": "veriyi_ozetle(esc)",
     "cells": [P(
        "📊 **Genel özet:** 916 katılım var ve bazı sütunlarda **eksik değerler** görürsün (örn. finale "
        "kalamayanların final puanı boştur). Bu bir hata değil, gerçeğin yansımasıdır — herkes finale çıkamaz. "
        "İleride bu yüzden ‘finale kalanlar’ı süzeceğiz.")]},
    {"after": "tr = esc[esc['ulke'] == 'Türkiye'].sort_values('yil')",
     "cells": [P(
        "📊 **Türkiye tablosu:** Yıl yıl sanatçı, şarkı, final sırası ve puanı. Verinin ‘ham’ hâlini görmek, "
        "grafiklere geçmeden önce neyle çalıştığını anlamanı sağlar — örn. 2003'teki 1.'liği (Sertab Erener) "
        "burada gözle bulabilirsin.")]},
    {"after": "title='Türkiye Eurovision Sıralaması (Düşük = İyi) — 2003 ZAFER!'",
     "cells": [
        P("📊 **Türkiye sıralama grafiği:** Y ekseni **ters** (1 = en üstte, çünkü 1. olmak iyidir). "
          "Çizginin inişli-çıkışlı olması ‘istikrarsızlık’, dibe yakın seyretmesi ‘istikrarlı başarı’ demektir.\n\n"
          "🔧 **Başka bir ülkenin hikâyesini çiz.** En başarılılardan İsveç nasıl?"),
        ("code",
         "isvec = esc[esc['ulke'] == 'İsveç'].sort_values('yil')\n"
         "fig = px.line(isvec, x='yil', y='final_sira', markers=True,\n"
         "              hover_data=['sanatci', 'sarki'],\n"
         "              title='İsveç Eurovision Sıralaması (Düşük = İyi)')\n"
         "fig.update_yaxes(autorange='reversed')\n"
         "fig.show()"),
        P("📊 İsveç sürekli üst sıralarda gezerken Türkiye daha **inişli çıkışlıdır**: *istikrar* mı yoksa "
          "*tek bir parlak yıl* mı — çizginin şekli bunu anlatır."),
     ]},
    {"after": "kazananlar = esc[esc['final_sira'] == 1]",
     "cells": [P(
        "📊 **En çok kazananlar:** İsveç ve Ukrayna başı çekiyor (3'er zafer); Türkiye'nin 1 zaferi var. "
        "Bu çıktı, ‘hangi ülkeler tarihsel olarak güçlü?’ bağlamını verir — ileride modelin neden bazı "
        "ülkeleri ‘avantajlı’ gördüğünü anlamana yardımcı olur.")]},
    {"after": "ev = finale_kalanlar[finale_kalanlar['ev_sahibi']]",
     "cells": [P(
        "📊 **Ev sahibi avantajı:** Ev sahibi ülkelerin ortalama sırası, diğerlerinden **belirgin daha "
        "iyidir** (sayı net bir fark gösteriyor). Sebep tartışmalı: sahne/prova avantajı, ev sahibi coşkusu "
        "ya da bölgesel oy. ⚠️ Sayı bir avantaj **gösterir** ama ‘neden’i **kanıtlamaz** (korelasyon ≠ neden).")]},
    {"after": "baslik='Sahnedeki Sıra vs Final Sıralaması'",
     "cells": [P(
        "📊 **Sahne çıkış sırası vs sıralama:** Sona doğru çıkan şarkılar jürinin/izleyicinin aklında daha "
        "taze kalabilir, bu yüzden hafif avantajlı olabilir. Grafikte net bir eğilim **var mı yok mu** ona bak — "
        "bazen ‘beklediğimiz etki veride görünmez’ ve bu da geçerli bir bulgudur.")]},
    {"after": "baslik='Jüri Puanı vs Halk (Tele) Puanı'",
     "cells": [P(
        "📊 **Jüri vs halk puanı:** Köşegen üstündeki şarkılarda ikisi anlaşır. Köşegenden **uzak** şarkılar, "
        "jüri ile halkın **anlaşmadığı** şarkılardır (biri çok sevdi, diğeri sevmedi). İlginç tartışma: "
        "uzman görüşü mü, halk oyu mu daha ‘doğru’? İki kitle her zaman aynı şeyi sevmez.")]},
    {"after": "baslik='Ev Sahibine Uzaklık vs Final Sıralaması'",
     "cells": [P(
        "📊 **Uzaklık vs sıralama:** Ev sahibine yakın ülkeler daha mı iyi sıralanıyor? Noktalarda hafif bir "
        "eğilim varsa, bu ‘komşu/bölge etkisinin’ ilk işaretidir. Bir sonraki hücrede bunu **sayıyla** test edeceğiz.")]},
    {"after": "yakin = finale_kalanlar[finale_kalanlar['ev_sahibi_uzaklik_km'] < 1500]",
     "cells": [P(
        "📊 **Yakın (<1500 km) vs uzak (>3000 km):** Grafikteki sezgiyi sayıya döküyoruz. Yakın ülkelerin "
        "ortalama sırası ve ‘ilk 10’ oranı daha iyiyse, coğrafyanın etkisi **somutlaşır**. Göz kararı değil, "
        "sayı konuşur — sunumda en ikna edici an budur.")]},
    {"after": "sinif_adlari=['Top 10 değil', 'Top 10!']",
     "cells": [P(
        "📊 **‘İlk 10’ modelinin doğruluğu nasıl yorumlanır?** Eurovision sonucu büyük ölçüde **öznel** "
        "(şarkı, sahne, jeopolitik). Bu yüzden doğruluk, kanser modeli kadar yüksek olmayabilir — ve bu "
        "**normaldir**. Önemli olan modelin **baseline'ı geçmesi** ve hangi faktörleri önemli bulduğudur. "
        "‘Düşük doğruluk = başarısız proje’ **değildir**; bazı olaylar doğası gereği zor tahmin edilir.")]},
    {"after": "Girmeyi Belirleyen Faktörler",
     "cells": [P(
        "📊 **Öznitelik önemi:** Model ‘ilk 10'a girmeyi’ en çok hangi faktörlerle açıklıyor? "
        "`ev_sahibi_uzaklik_km` üst sıralardaysa, coğrafyanın gerçekten önemli olduğunun **bir başka kanıtı** "
        "olur — yani farklı yöntemler (gruplama + model) aynı sonuca işaret eder, bu da bulgunu güçlendirir.")]},
    {"after": "oylar = veri_yukle('input_data/eurovision_oylar.csv')",
     "cells": [P(
        "📊 **Oy verisine geçiş:** 21.165 satırlık bu set ‘kim kime kaç puan verdi’yi tutar (ortalama puan "
        "~3,1). Artık ülke ortalamalarına değil, **ülkeler arası ilişkilere** bakacağız — komşu oylamasının "
        "asıl kanıtı buradadır.")]},
    {"after": "Komşu Oylama Etkisi",
     "cells": [P(
        "📊 **‘Komşu oylaması’ grafiği:** Çubuklar uzaklık arttıkça **düşüyorsa**, ülkeler coğrafi/kültürel "
        "olarak yakın komşularına ortalamadan **daha yüksek** puan veriyor demektir. Bu, müziğin yanında "
        "**kültür ve siyasetin** de oyları etkilediğinin sayısal kanıtıdır. ⚠️ Bu bir **eğilimdir**; her "
        "komşu çifti için geçerli olmak zorunda değildir.")]},
    {"after": "tr_az = oylar[(oylar['oy_veren_ulke'] == 'Türkiye')",
     "cells": [P(
        "📊 **Türkiye–Azerbaycan:** İki ülkenin birbirine verdiği ortalama puan, genel ortalamanın **çok "
        "üstünde**. Bu, soyut ‘komşu etkisi’ bulgusunun herkesin bildiği **somut** bir örneği — sunumda "
        "akılda kalır. ⚠️ Ortak dil/kültür/müzik zevki de bunu açıklayabilir; ‘torpil’ demeden önce düşün.")]},
    {"after": "Adım 9: Sunum için notlarınız",
     "cells": [P(sunum_rehberi(
        "**🎤 Ana mesaj:** *“Eurovision sadece müzik değil: ev sahibi avantajı, sahne sırası ve özellikle "
        "**komşu oylaması** sonuçları ölçülebilir biçimde etkiliyor.”*\n\n"
        "**Grafik sırası:** ① Türkiye tarihçesi (2003 zaferi, sıcak giriş) → ② en çok kazananlar → ③ uzaklık "
        "vs puan (komşu oylaması — **projenin yıldızı**) → ④ Türkiye–Azerbaycan örneği → ⑤ ‘ilk 10’ modeli + "
        "öznitelik önemi.\n\n"
        "**Yorumlama anahtarları:** komşu etkisini **sayıyla** söyle (‘0–500 km'ye verilen puan, 5000+ km'nin "
        "~__ katı’); ev sahibi avantajını ‘ortalama __ sıra iyileşme’ olarak ifade et; modelin düşük "
        "doğruluğunu **dürüstçe** açıkla.\n\n"
        "**Sık hatalar:** ❌ ‘komşu yüksek puan = kesin torpil’ (ortak kültür de olabilir) · ❌ tek ülkeden "
        "genel kural çıkarmak · ❌ modelin %100 olmamasını başarısızlık sanmak."))]},
]

# ====================== MİNİ 5 — HAVA ======================
AUG["mini_proje5_hava.ipynb"] = [
    {"after": "hava = pd.read_csv('input_data/iller_hava.csv')",
     "cells": [P(
        "## 📂 Veriyi Tanıyalım — 3 İlin Hava Durumu (2020–2024)\n\n"
        "**Malatya, İstanbul ve Erzurum** için 5 yıllık **günlük** hava kayıtları. Her satır "
        "**bir ilin bir günüdür**.\n\n"
        "- **Satır sayısı:** 5.481 günlük gözlem (3 il × ~5 yıl)\n"
        "- **Zaman aralığı:** 2020 – 2024\n"
        "- **Şehirler bilerek farklı:** Erzurum yüksek-soğuk (ort ~7,5 °C), İstanbul ılıman-nemli "
        "(~15,4 °C), Malatya karasal (~15 °C)\n\n"
        "| Sütun | Anlamı |\n|---|---|\n"
        "| `il` | Şehir (Malatya / İstanbul / Erzurum) |\n"
        "| `tarih` | Gözlem günü |\n"
        "| `sicaklik_ort / min / max` | Günlük ortalama / en düşük / en yüksek sıcaklık (°C) |\n"
        "| `yagis` | Günlük yağış (mm) |\n"
        "| `ruzgar_max` | Günün en yüksek rüzgârı |\n"
        "| `yil, ay, gun, mevsim` | Tarih bilgileri (modelde ipucu olur) |\n\n"
        "💬 **Akranlarına anlat:** *“Dünün havasına bakıp yarını tahmin edebilir miyiz? Hangi şehir daha "
        "‘tahmin edilebilir’? Ve 5 yılda iklim ısındı mı?”*")]},
    {"after": "baslik='İl Bazlı Sıcaklık Dağılımı (5 yıl)'",
     "cells": [
        P("📊 **İl sıcaklık kutu grafiği:** Her ilin sıcaklık **dağılımını** (sadece ortalamayı değil) "
          "gösterir. Kutu ne kadar **uzunsa** o ilde sıcaklık o kadar çok oynar (karasal iklim). Erzurum'un "
          "hem düşük hem geniş olması beklenir.\n\n"
          "🔧 **Sıcaklık yerine yağışa bak.** Aynı fonksiyon, farklı sütun:"),
        ("code",
         "cubuk_grafigi(hava, kategori_sutunu='il', deger_sutunu='yagis',\n"
         "              baslik='İl Bazlı Ortalama Günlük Yağış')"),
        P("📊 En sıcak il en kurak olmak zorunda değildir; iklim sıcaklık + yağış + rüzgârın **birlikte** "
          "belirlediği bir resimdir. Bir şehri tek sayıyla değil, birkaç ölçüyle birden tanımla."),
     ]},
    {"after": "ozet = hava.groupby('il').agg({",
     "cells": [P(
        "📊 **İl özet tablosu:** Her ilin ortalama/min/max sıcaklığı, **değişkenliği (std)** ve toplam yağışı. "
        "**std (standart sapma)** = sıcaklığın ne kadar oynadığı; karasal illerde (Erzurum/Malatya) yüksek, "
        "deniz etkili İstanbul'da düşüktür. En sıcak ≠ en yağışlı — bu yüzden birkaç sütuna birden bakmak gerekir.")]},
    {"after": "title='3 İl — Yıllık Ortalama Sıcaklık (2020-2024)'",
     "cells": [P(
        "📊 **Yıllık ortalama trend:** 2020→2024 çizgileri genelde **yukarı** eğilimli — kısa pencerede bile "
        "bir ısınma sinyali. ⚠️ Ama 5 yıl, iklim için **çok kısadır**; bunu ‘kesin trend’ değil bir ‘gözlem’ "
        "olarak sun. Gerçek iklim trendleri için onlarca yıllık veri gerekir.")]},
    {"after": "veri_2020 = hava[(hava['il']==il) & (hava['yil']==2020)]",
     "cells": [P(
        "📊 **2020 vs 2024 farkı:** Her ilin iki yıl arasındaki ortalama sıcaklık değişimi (Δ). Hangi il en "
        "çok ısınmış görünüyor? ⚠️ Tek bir yıl çok değişken olabilir (örn. 2020 rastgele soğuk bir yıl olabilir), "
        "bu yüzden tek bir fark ‘şans mı, gerçek trend mi’ ayırmaz — birden çok yıla bakmak şarttır.")]},
    {"after": "title='Yıllık >35°C Gün Sayısı'",
     "cells": [P(
        "📊 **>35 °C aşırı sıcak gün sayısı:** İklim değişikliğinin en **somut** göstergelerinden biri. "
        "Ortalamalar yavaş değişir ama ‘uç olaylar’ daha çabuk artar. Yıllar içinde bu sayı yükseliyorsa; "
        "sağlık (sıcak çarpması), tarım ve enerji açısından gerçek bir sorundur — sunumda çarpıcı bir grafiktir.")]},
    {"after": "yagmurlu = df_il[df_il['yagis'] > 1]",
     "cells": [P(
        "📊 **Yağış–sıcaklık ilişkisi:** Yağmurlu günler genelde kuru günlerden **serindir** (bulutlar güneşi "
        "keser, yağmur havayı soğutur). Farkın büyüklüğü şehrin iklimine göre değişir. Basit ama gerçek bir "
        "fiziksel örüntü — ‘veride mantıklı ilişkiler buluyoruz’ demenin güzel bir örneği.")]},
    {"after": "3-gün tahmin",
     "cells": [P(
        "📊 **‘1-gün vs 3-gün’ sonucu:** 3-gün sonrası tahminin RMSE'si (hatası), 1-gün sonrasından **belirgin "
        "daha büyüktür**. Sezgisel: gelecek ne kadar uzaksa belirsizlik o kadar artar. Gerçek meteoroloji de "
        "bunu yaşar — bu yüzden 10 günlük tahminlere 5 günlük kadar güvenmeyiz. ‘Tahmin ufku uzadıkça doğruluk düşer.’")]},
    {"after": "for mev in ['Kış', 'İlkbahar', 'Yaz', 'Sonbahar']:",
     "cells": [P(
        "📊 **Mevsim bazında hata (RMSE):** Model her mevsimde aynı başarıda değil. Geçiş mevsimleri "
        "(ilkbahar/sonbahar) genelde daha **değişken** olduğundan tahmin zorlaşır; kararlı mevsimlerde "
        "(yaz/kış) hata düşer. **Ders:** tek bir ‘ortalama doğruluk’ her durumu yansıtmaz — detaya bakmak gerekir.")]},
    {"after": "Transfer maliyeti:",
     "cells": [P(
        "📊 **‘Transfer öğrenimi’ sonucu:** Malatya'da eğitilen model Malatya'da en iyi; başka illere "
        "uygulanınca hata **artar**. Artış, şehirler ne kadar *farklıysa* o kadar büyüktür (yüksek-soğuk "
        "Erzurum'da, ılıman İstanbul'a göre daha kötü). **Ders:** bir model **eğitildiği dünyaya** benzer "
        "veride iyi çalışır; çok farklı bir ortama taşınınca körelir — yapay zekânın en büyük tuzaklarından biri.")]},
    {"after": "en_sicak = test_2024.sort_values('sicaklik_ort', ascending=False).head(5)",
     "cells": [P(
        "📊 **En sıcak 5 gün ve hata:** Modelin **uç (en sıcak)** günlerdeki tahminini gerçekle karşılaştırıyoruz. "
        "Modeller genelde uç olayları **az tahmin eder** (her şeyi ortalamaya çeker); ‘hata’ sütunu pozitifse "
        "model günü ‘olduğundan serin’ söylemiş demektir. Bu, basit modellerin önemli bir sınırıdır — tam da "
        "sıcak hava dalgaları gibi en önemli günlerde zorlanır.")]},
    {"after": "Adım 9: Sunum için notlarınız",
     "cells": [P(sunum_rehberi(
        "**🌤️ Ana mesaj:** *“Geçmiş günlerin sıcaklığından yarını tahmin edebiliyoruz; ama tahmin ufku "
        "uzadıkça ve modeli başka şehre taşıdıkça doğruluk düşüyor — hem iklim ısınmasını hem de yapay zekânın "
        "sınırlarını görüyoruz.”*\n\n"
        "**Grafik sırası:** ① il sıcaklık (ve yağış) → ② yıllık trend (ısınma) → ③ >35 °C gün sayısı → "
        "④ 1-gün vs 3-gün RMSE → ⑤ transfer (Malatya→İstanbul/Erzurum).\n\n"
        "**Yorumlama anahtarları:** RMSE'yi **birimiyle** söyle (‘ortalama __ °C yanılıyoruz’); 5 yıllık "
        "ısınmayı **temkinli** yorumla; transfer hatasını ‘şehir farkı = model farkı’ diye açıkla.\n\n"
        "**Sık hatalar:** ❌ ‘5 yılda __°C ısındı = her yıl böyle ısınır’ · ❌ düşük RMSE'yi ‘havayı çözdük’ "
        "sanmak (yalnız *yakın* tahmin kolaydır) · ❌ bir şehrin modelini her yere uygun sanmak."))]},
]
