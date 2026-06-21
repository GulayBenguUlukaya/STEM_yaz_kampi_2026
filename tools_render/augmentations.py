# -*- coding: utf-8 -*-
"""
rendered/ önizlemelerine eklenen EĞİTSEL içerik.

Buradaki hücreler SADECE GitHub önizlemelerine eklenir; `notebooks/` içindeki
asıl Colab defterleri değişmez. Amaç:
  • öğrencilerin deneyebileceği VARYASYONLARI çalıştırılmış çıktılarıyla göstermek,
  • aralara "nasıl yorumlanır?" rehberleri koymak,
  • mini projeler için "neler yapılabilir + nasıl sunulur/yorumlanır" bölümleri eklemek.

Yapı:  AUG[notebook_adı] = [ {"after": <hücrede geçen benzersiz metin>,
                              "cells": [("markdown"|"code", kaynak), ...]}, ... ]
"""

# Her önizlemenin başına eklenen ortak afiş
PREVIEW_BANNER = """\
> 🤖 **Bu, defterin "çıktılı önizleme" sürümüdür.** Asıl çalışacağınız Colab defteri
> [`notebooks/`](../notebooks) klasöründe. Buraya, normal hücrelerin **arasına**:
> 🔧 *deneyebileceğiniz varyasyonlar* (çalıştırılmış hâlde), 📊 *sonuçların nasıl
> yorumlanacağı* ve mini projelerde 🎤 *sunum rehberleri* eklendi. Bu eklemeler
> **yeşil/gri kutularla** ayrılmıştır; siz de aynı şeyleri kendi defterinizde deneyebilirsiniz.
"""

# ────────────────────────────────────────────────────────────────────────────
AUG = {}

# ====================== GÜN 1 ======================
AUG["gun1.ipynb"] = [
    {"after": "cubuk_grafigi(df, kategori_sutunu='bolge'",
     "cells": [
        ("markdown",
         "🔧 **Aynı fonksiyon, farklı soru.** `cubuk_grafigi` yalnızca *saymakla* kalmaz; "
         "ona `deger_sutunu` verirsen her grubun **ortalamasını** çizer. Tek satırı değiştirerek "
         "bambaşka bir soruyu yanıtlıyoruz:"),
        ("code",
         "cubuk_grafigi(df, kategori_sutunu='bolge', deger_sutunu='nufus',\n"
         "              baslik='Bölgelere Göre ORTALAMA Nüfus')"),
        ("markdown",
         "📊 **Nasıl yorumlanır?** Üstteki ilk grafik *“her bölgede kaç il var?”* diyordu; "
         "bu grafik *“o bölgelerdeki iller ne kadar kalabalık?”* diyor. İl **sayısı** çok olan bir "
         "bölge, **ortalama nüfusu** düşük olabilir (çok sayıda küçük il). İki grafik birbirinden "
         "farklı hikâye anlatır — doğru soruyu sormak, doğru grafiği seçmektir."),
     ]},
    {"after": "histogram(df, sutun='nufus'",
     "cells": [
        ("markdown",
         "🔧 **Başka bir sütunu incele.** Histogramda tek değiştirmen gereken şey `sutun=`. "
         "Nüfus yerine **ortalama yaş** dağılımına bakalım:"),
        ("code",
         "histogram(df, sutun='ortalama_yas', baslik='İllerin Ortalama Yaş Dağılımı')"),
        ("markdown",
         "📊 **Nasıl yorumlanır?** Histogramda **tepe** noktası en sık görülen değeri gösterir. "
         "Dağılım **sağa kuyruklu** mu (birkaç il çok yaşlı/genç), yoksa **simetrik** mi? "
         "Nüfus dağılımı genelde *birkaç dev şehir* yüzünden sağa çok çarpıktır; yaş dağılımı "
         "çoğunlukla daha derli topludur. Karşılaştırın!"),
     ]},
    {"after": "dagilim_grafigi(df, x_sutunu='nufus', y_sutunu='dogurganlik_orani'",
     "cells": [
        ("markdown",
         "🔧 **Renk ekle + tüm ilişkileri tek bakışta gör.** `renk_sutunu` ile noktaları bölgeye "
         "göre boyayabilir; `korelasyon_haritasi` ile de bütün sayısal sütunların ilişkisini "
         "tek karede görebilirsin:"),
        ("code",
         "dagilim_grafigi(df, x_sutunu='ortalama_yas', y_sutunu='dogurganlik_orani',\n"
         "                renk_sutunu='bolge',\n"
         "                baslik='Yaş – Doğurganlık (bölgeye göre renkli)')\n"
         "korelasyon_haritasi(df, baslik='Sayısal Sütunlar Arası İlişki Haritası')"),
        ("markdown",
         "📊 **Korelasyon haritası nasıl okunur?** Her kare iki sütunun birlikte hareketini "
         "gösterir: **+1** (koyu kırmızı) = *biri artarken diğeri de artar*; **−1** (koyu mavi) = "
         "*biri artarken diğeri azalır*; **0** = *ilişki yok*. Örneğin yaş ↑ iken doğurganlık ↓ "
         "ise bunu negatif (mavi) bir kare olarak görürsün. ⚠️ **Önemli:** korelasyon *neden-sonuç* "
         "demek değildir — iki şey birlikte değişiyor olabilir ama biri diğerinin **sebebi** olmayabilir."),
     ]},
]

# ====================== GÜN 2 ======================
AUG["gun2.ipynb"] = [
    {"after": "dagilim_grafigi(penguen, x_sutunu='gaga_uzunluk_mm'",
     "cells": [
        ("markdown",
         "🔧 **Farklı iki ölçümle dene.** Türleri ayıran tek ölçüm yok. Başka iki sütun seçip "
         "ayrışmanın hâlâ olup olmadığına bak — modelin işini bu yüzden kolaylaştırırız:"),
        ("code",
         "dagilim_grafigi(penguen, x_sutunu='kanat_uzunluk_mm', y_sutunu='gaga_derinlik_mm',\n"
         "                renk_sutunu='tur', baslik='Farklı iki ölçüm — yine ayrışıyor mu?')"),
        ("markdown",
         "📊 **Nasıl yorumlanır?** Renk grupları (türler) **ayrı kümeler** oluşturuyorsa, o iki "
         "ölçüm türü ayırmak için *iyi ipuçlarıdır*. Kümeler iç içeyse o ölçümler tek başına yetersizdir. "
         "Model de tam olarak bunu yapar: en iyi ayıran ipuçlarını bulur."),
     ]},
    {"after": "karar_agaci_ciz(model, oznitelik_adlari=list(X.columns)",
     "cells": [
        ("markdown",
         "🔧 **Aynı veriye farklı model.** Tek bir karar ağacı yerine **rastgele orman** "
         "(yüzlerce ağacın oyu) deneyelim ve doğruluğu karşılaştıralım:"),
        ("code",
         "orman = rastgele_orman_egit(X_egitim, y_egitim)\n"
         "model_degerlendir(orman, X_test, y_test, sinif_adlari=list(orman.classes_))"),
        ("markdown",
         "📊 **Nasıl yorumlanır?** Rastgele orman çoğu zaman tek ağaçtan **biraz daha doğrudur**, "
         "çünkü birçok ağacın hatası birbirini dengeler. Bedeli: artık tek bir resimle çizemeyiz — "
         "yani **daha doğru ama daha az “açıklanabilir”**. Doğruluk mu, anlaşılırlık mı? Bu bir "
         "**ödünleşimdir (trade-off)** ve probleme göre seçilir (örn. tıpta açıklanabilirlik çok önemli)."),
     ]},
    {"after": "for derinlik in [1, 2, 5, 15]:",
     "cells": [
        ("markdown",
         "📊 **Yukarıdaki tabloyu nasıl okumalı? (Aşırı öğrenme / overfitting)** Derinlik arttıkça "
         "**Eğitim** doğruluğu genelde %100'e tırmanır — ağaç eğitim verisini *ezberler*. Ama asıl "
         "önemli olan **Test** sütunudur (modelin hiç görmediği veri). Eğitim yüksek ama test düşükse, "
         "model **ezberlemiş ama öğrenememiştir**. En iyi derinlik, *testin en yüksek olduğu* yerdir — "
         "daha fazlası işi bozar. Bu, makine öğrenmesinin en önemli dersidir. 🧠"),
     ]},
    {"after": "baslik='2024 Sıcaklık Tahmini'",
     "cells": [
        ("markdown",
         "📊 **Regresyon sonuçları nasıl yorumlanır?** Burada bir *sayı* tahmin ediyoruz, sınıf değil. "
         "Üç ölçüye bakın: **RMSE** = ortalama kaç derece yanıldık (küçük = iyi); **MAE** = benzer ama "
         "uç hatalara daha az duyarlı; **R²** = modelin değişimi ne kadar açıkladığı (1'e yakın = iyi, "
         "0 = ortalamayı söylemekten farksız). Grafikte noktalar kırmızı **y=x çizgisine** ne kadar "
         "yakınsa tahmin o kadar iyidir. 'Dünün sıcaklığı' gibi basit ipuçlarıyla bile yarını şaşırtıcı "
         "derecede iyi tahmin edebiliyoruz — çünkü hava *kademeli* değişir."),
     ]},
]

# ─────────── Mini projeler için ortak "sunum & yorumlama" başlığı ───────────
def sunum_rehberi(govde):
    return ("## 🎤 Sunum & Yorumlama Rehberi\n\n"
            "> Bu bölüm, projeyi **son gün sunarken** ne anlatacağını ve sonuçları **nasıl "
            "yorumlayacağını** özetler. Ezberleme — kendi cümlelerinle anlat.\n\n" + govde)

# ====================== MİNİ 1 — UZAY ======================
AUG["mini_proje1_uzay.ipynb"] = [
    {"after": "baslik='Yıldız Tipine Göre Aday Sayısı (Kepler nereye baktı?)'",
     "cells": [
        ("markdown",
         "🔧 **Sayı yerine ORAN sor.** Yukarıdaki grafik 'hangi yıldıza kaç kez baktık' diyor. "
         "`deger_sutunu='gercek_gezegen'` verirsek her yıldız tipinde adayların **ne kadarının gerçek "
         "çıktığını** (başarı oranını) çizer:"),
        ("code",
         "cubuk_grafigi(uzay, kategori_sutunu='yildiz_tipi', deger_sutunu='gercek_gezegen',\n"
         "              baslik='Yıldız Tipine Göre GERÇEK Gezegen Oranı')"),
        ("markdown",
         "📊 **Nasıl yorumlanır?** Çok aday ≠ çok gerçek gezegen. Bir yıldız tipinde *az* aday olup "
         "*yüksek* oranda gerçek çıkabilir. Sunumda ikisini ayır: **'nereye baktık'** (sayı) ile "
         "**'ne bulduk'** (oran) farklı şeylerdir."),
     ]},
    {"after": "sinif_adlari=['Yanlış Pozitif', 'Gerçek 🪐']",
     "cells": [
        ("markdown",
         "📊 **Karmaşıklık matrisini bu projede nasıl okumalı?** Köşegen = doğru tahminler. "
         "Köşegen dışı iki hata **aynı değildir**: bir **yanlış pozitifi** 'gerçek' sanmak NASA'ya "
         "boşuna teleskop zamanı harcatır; **gerçek bir gezegeni** kaçırmak ise *yeni bir dünyayı* "
         "ıskalamak demektir. Hangi hatanın daha pahalı olduğunu sunumda tartış."),
        ("markdown",
         "🔧 **Modeli değiştir, karşılaştır.** Rastgele orman yerine tek bir karar ağacı ne yapıyor?"),
        ("code",
         "agac = karar_agaci_egit(X_egitim, y_egitim, max_derinlik=4)\n"
         "model_degerlendir(agac, X_test, y_test, sinif_adlari=['Yanlış Pozitif', 'Gerçek'])"),
        ("markdown",
         "📊 Genelde orman biraz daha doğrudur; ağaç ise *neden* öyle karar verdiğini gösterebilir. "
         "İki sonucu yan yana koymak güçlü bir sunum yapar."),
     ]},
    {"after": "baslik='Gerçek Gezegeni Ele Veren İpuçları'",
     "cells": [
        ("markdown",
         "📊 **Öznitelik önemi nasıl yorumlanır?** Çubuk ne kadar uzunsa, model o ipucuna o kadar "
         "güveniyor demektir. Burada genellikle **sinyal/gürültü oranı** ve **transit derinliği** öne "
         "çıkar — astronomi sezgisiyle uyumlu: net, güçlü, tekrarlayan bir sinyal *gerçek* bir gezegeni "
         "ele verir. ⚠️ 'Önemli' = *modele yararlı*; her zaman *fiziksel sebep* anlamına gelmez."),
     ]},
    {"after": "Adım 8: Sunum için notlarınız",
     "cells": [
        ("markdown", sunum_rehberi(
         "**🪐 Ana mesaj (bir cümle):** *“Binlerce Kepler adayının arasından, gerçek gezegenleri "
         "yanlış alarmlardan ayırmayı ve içlerinden Dünya benzerlerini bulmayı öğrendik.”*\n\n"
         "**Hangi grafikleri göster (sırayla):**\n"
         "1. Yıldız tipine göre aday **sayısı** + **oranı** → 'Kepler nereye baktı, ne buldu?'\n"
         "2. Yörünge vs yarıçap dağılımı → 'Sıcak Jüpiterler' köşesini işaret et.\n"
         "3. Karmaşıklık matrisi + doğruluk → modelin başarısı.\n"
         "4. Öznitelik önemi → 'gerçek gezegeni ele veren ipuçları'.\n"
         "5. Dünya benzeri liste → finalde merak uyandırır.\n\n"
         "**Her sonucu nasıl yorumla:**\n"
         "- Doğruluğu **baseline** ile kıyasla: 'her şeye yanlış-pozitif deseydik %__ tuttururduk; "
         "modelimiz %__ ile bunu geçti.'\n"
         "- Bir **yanlış pozitif** ve bir **kaçırılan gezegen** örneği göster; maliyetlerini karşılaştır.\n"
         "- 'En güvensiz adaylar' listesini *NASA'ya tekrar-bak listesi* olarak sun.\n\n"
         "**Sık yapılan yorumlama hataları:**\n"
         "- ❌ 'Model %95 doğru, demek ki kusursuz.' → Hangi **hata türünü** yaptığına bak.\n"
         "- ❌ 'Önemli öznitelik = gezegenin sebebi.' → Önem, *modele yararlılık*tır.\n"
         "- ❌ Aday **sayısı** ile gerçek **oranını** karıştırmak.")),
     ]},
]

# ====================== MİNİ 2 — SAĞLIK ======================
AUG["mini_proje2_saglik.ipynb"] = [
    {"after": "baslik='Tümör Yarıçapı: Kötü Huylu vs İyi Huylu'",
     "cells": [
        ("markdown",
         "🔧 **Başka bir ölçüme bak.** `sayisal_sutun` değerini değiştirmen yeterli. Yarıçap iyi "
         "ayırıyordu; ya **doku (texture)**?"),
        ("code",
         "kutu_grafigi(veri_full, kategori_sutunu='sinif', sayisal_sutun='mean texture',\n"
         "             baslik='Tümör Dokusu: Kötü Huylu vs İyi Huylu')"),
        ("markdown",
         "📊 **Nasıl yorumlanır?** İki kutunun **örtüşmesi** ne kadar azsa, o ölçüm iki sınıfı o kadar "
         "iyi ayırır. Yarıçapın kutuları neredeyse hiç örtüşmezken dokununkiler daha çok örtüşür — yani "
         "yarıçap **tek başına** daha güçlü bir ipucudur. Model birçok ölçümü *birleştirerek* daha da iyi sonuç verir."),
     ]},
    {"after": "Lojistik Regresyon: %{loj_d*100",
     "cells": [
        ("markdown",
         "📊 **Üç modeli nasıl karşılaştırmalı?** Tek bir test bölünmesindeki yüzde, **şansa** bağlı "
         "olabilir (hangi hastalar teste düştü?). Bu yüzden bir sonraki adımdaki **cross-validation** "
         "daha güvenilirdir. Buradaki tek-test sonuçlarını *kesin* sanma — 'ilk izlenim' olarak gör."),
     ]},
    {"after": "5-katlı cross-validation sonuçları",
     "cells": [
        ("markdown",
         "📊 **'± standart sapma' ne demek?** Veriyi 5 parçaya bölüp 5 kez test ediyoruz. Ortalama = "
         "tipik başarı; **±** sonrası sayı = *sonuçların ne kadar oynadığı*. **Düşük ±** = kararlı, "
         "güvenilir model; **yüksek ±** = 'bazen iyi bazen kötü', riskli. Sunumda iki modelin ortalaması "
         "yakınsa **daha küçük ±** olanı tercih et — tıpta *tutarlılık* hayat kurtarır."),
     ]},
    {"after": "for n in [3, 5, 10, 20, 30]:",
     "cells": [
        ("markdown",
         "📊 **'Az öznitelik yeter mi?' sonucu nasıl yorumlanır?** Çoğu zaman **5 ölçüm**, 30 ölçümün "
         "doğruluğunun neredeyse tamamını verir. Bunun *gerçek hayatta* anlamı büyük: her ölçüm "
         "**zaman, para ve hastaya işlem** demektir. '%1 doğruluk için 25 fazladan ölçüm değer mi?' "
         "sorusu, bir mühendisin sorması gereken türden bir **maliyet-fayda** sorusudur."),
     ]},
    {"after": "Adım 8: Sunum için notlarınız",
     "cells": [
        ("markdown", sunum_rehberi(
         "**🩺 Ana mesaj:** *“Tümör ölçümlerinden iyi/kötü huylu ayrımını yüksek doğrulukla yapabiliyoruz; "
         "ama sağlıkta asıl mesele doğruluk değil, **hangi hatayı yaptığın**.”*\n\n"
         "**Hangi grafikleri göster:**\n"
         "1. Sınıf dengesi + **baseline** → 'geçilmesi gereken çıta'.\n"
         "2. Kutu grafiği (yarıçap) → 'ölçümler sınıfları gerçekten ayırıyor'.\n"
         "3. Cross-validation karşılaştırması → 'en kararlı model hangisi'.\n"
         "4. ROC eğrisi + AUC → 'eşikten bağımsız başarı'.\n"
         "5. Karmaşıklık matrisi → **False Negative vs False Positive** tartışması (en kritik kısım).\n\n"
         "**Her sonucu nasıl yorumla:**\n"
         "- Doğruluğu **baseline %__** ile kıyasla; çıtayı geçtiğini göster.\n"
         "- **AUC**'yi 'mükemmel=1, rastgele=0.5' ölçeğine oturt.\n"
         "- **False Negative** (kanseri kaçırmak) = ölümcül; **False Positive** (boşuna endişe/ek test) "
         "= rahatsız edici ama telafi edilebilir. Bu yüzden tıpta modeli *kanseri kaçırmamaya* ayarlarız.\n\n"
         "**Sık yapılan yorumlama hataları:**\n"
         "- ❌ 'Yüksek doğruluk = iyi model.' → Dengesiz veride yanıltıcıdır; hata türüne bak.\n"
         "- ❌ Tek-test sonucunu kesin sanmak → cross-validation'a güven.\n"
         "- ❌ İki hata türünü eşit saymak → maliyetleri çok farklıdır.")),
     ]},
]

# ====================== MİNİ 3 — İKLİM ======================
AUG["mini_proje3_iklim.ipynb"] = [
    {"after": "title='Türkiye Yıllık CO₂ Emisyonu (Milyon Ton)'",
     "cells": [
        ("markdown",
         "🔧 **Başka bir ülkeyle kıyasla.** `ulke` filtresini değiştirerek herhangi bir ülkenin "
         "eğrisini çizebilirsin. Türkiye hâlâ artarken Almanya'nın eğrisi nasıl?"),
        ("code",
         "alm = iklim[iklim['ulke'] == 'Almanya']\n"
         "fig = px.line(alm, x='yil', y='co2_milyon_ton', markers=True,\n"
         "              title='Almanya Yıllık CO₂ Emisyonu (Milyon Ton)')\n"
         "fig.show()"),
        ("markdown",
         "📊 **Nasıl yorumlanır?** Türkiye'nin eğrisi sürekli **yukarı** giderken Almanya'nınki bir "
         "**zirve yapıp düşüyor**. Aynı eksenlerle iki ülkeyi karşılaştırmak, 'gelişmekte olan' ile "
         "'sanayisini dönüştürmüş' ülke farkını tek bakışta anlatır."),
     ]},
    {"after": "title='Kişi Başı CO₂ — ABD ve Almanya baskın, Çin orta'",
     "cells": [
        ("markdown",
         "📊 **Toplam mı, kişi başı mı? (Adalet sorusu)** Aynı veriyi iki şekilde ölçtük ve **sıralama "
         "değişti**. **Toplam** CO₂'de büyük nüfuslu ülkeler (Çin) önde; **kişi başı**'nda ise az nüfuslu "
         "ama yoğun tüketen ülkeler öne çıkar. 'Kim daha çok sorumlu?' sorusunun cevabı, **hangi ölçüyü "
         "seçtiğine** bağlıdır — bu, veride 'tarafsız sayı diye bir şey yoktur' dersinin ta kendisidir."),
     ]},
    {"after": "Lineer model 2050",
     "cells": [
        ("markdown",
         "📊 **Lineer tahmin nereye kadar güvenilir?** Düz bir çizgi geçmişteki eğilimi uzatır; ama "
         "gerçek hayatta politikalar, teknoloji ve anlaşmalar eğriyi **büker**. Modelin 2050 tahmini ile "
         "Türkiye'nin 2053 net-sıfır hedefi **çelişiyorsa**, bu modelin 'yanlış' olduğunu değil, "
         "**'bugünkü gidişle hedefe ulaşılamayacağını'** gösterir. Tahmin bir *kehanet* değil, "
         "bir *uyarıdır*. ⚠️ Modeli eğitim aralığının çok dışına uzatmak (2050) her zaman risklidir."),
     ]},
    {"after": "Adım 8: Sunum için notlarınız",
     "cells": [
        ("markdown", sunum_rehberi(
         "**🌍 Ana mesaj:** *“Türkiye'nin karbon hikâyesini gerçek veriyle anlattık; toplam-vs-kişi başı "
         "ölçüsünün adaleti nasıl değiştirdiğini ve bugünkü gidişin 2053 hedefiyle çeliştiğini gösterdik.”*\n\n"
         "**Hangi grafikleri göster:**\n"
         "1. Türkiye CO₂ tarihçesi (artış) → tarihsel kırılmaları işaretle (petrol krizi, 2001, COVID).\n"
         "2. COVID-2020 düşüşü + geri tepki → 'doğal bir deney'.\n"
         "3. Toplam vs kişi başı (iki grafik yan yana) → **adalet** tartışması.\n"
         "4. Almanya vs Türkiye → 'düşürmek mümkün mü?'.\n"
         "5. 2030/2050 tahmini vs Paris hedefi → **çelişki** finali.\n\n"
         "**Her sonucu nasıl yorumla:**\n"
         "- Artışı **'kaç kat'** olarak söyle (örn. '8x arttı'), çıplak sayı yerine.\n"
         "- COVID düşüşünü **kalıcı değil** diye vurgula (geri tepki var).\n"
         "- Sıralamanın ölçüyle değiştiğini göster: 'Çin toplamda #1 ama kişi başında ortalarda'.\n\n"
         "**Sık yapılan yorumlama hataları:**\n"
         "- ❌ 'CO₂ ile sıcaklık aynı yıl artıyor, demek ki...' → etki **birikimlidir**, gecikmelidir.\n"
         "- ❌ Lineer tahmini kesin gelecek sanmak → o bir senaryodur, kehanet değil.\n"
         "- ❌ Sadece toplamı (veya sadece kişi başını) göstermek → tek ölçü eksik resimdir.")),
     ]},
]

# ====================== MİNİ 4 — EUROVISION ======================
AUG["mini_proje4_eurovision.ipynb"] = [
    {"after": "title='Türkiye Eurovision Sıralaması (Düşük = İyi) — 2003 ZAFER!'",
     "cells": [
        ("markdown",
         "🔧 **Başka bir ülkenin hikâyesini çiz.** `ulke` filtresini değiştir. Eurovision'ın "
         "en başarılı ülkelerinden İsveç'in sıralaması nasıl görünüyor?"),
        ("code",
         "isvec = esc[esc['ulke'] == 'İsveç'].sort_values('yil')\n"
         "fig = px.line(isvec, x='yil', y='final_sira', markers=True,\n"
         "              hover_data=['sanatci', 'sarki'],\n"
         "              title='İsveç Eurovision Sıralaması (Düşük = İyi)')\n"
         "fig.update_yaxes(autorange='reversed')\n"
         "fig.show()"),
        ("markdown",
         "📊 **Nasıl yorumlanır?** Y ekseni **ters** (1 = en üstte, çünkü 1. olmak iyidir). İsveç'in "
         "çizgisi sürekli üst sıralarda gezerken Türkiye'ninki daha **inişli çıkışlıdır**. Bir ülkenin "
         "*istikrarı* mı yoksa *tek bir parlak yılı* mı var — çizginin şekli bunu anlatır."),
     ]},
    {"after": "sinif_adlari=['Top 10 değil', 'Top 10!']",
     "cells": [
        ("markdown",
         "📊 **Bu modelin doğruluğunu nasıl yorumlamalı?** Eurovision sonucu büyük ölçüde "
         "**öznel** (şarkı, sahne, jeopolitik). Bu yüzden buradaki doğruluk, kanser modeli kadar "
         "yüksek olmayabilir — ve bu **normaldir**. Önemli olan modelin *baseline'ı geçmesi* ve "
         "hangi faktörleri önemli bulduğudur. 'Düşük doğruluk = başarısız proje' **değildir**; "
         "bazı olaylar doğası gereği tahmin edilmesi zordur."),
     ]},
    {"after": "Komşu Oylama Etkisi — Uzaklık Arttıkça Verilen Puan Düşüyor",
     "cells": [
        ("markdown",
         "📊 **'Komşu oylaması' grafiği nasıl yorumlanır?** Çubuklar uzaklık arttıkça **düşüyorsa**, "
         "ülkeler coğrafi/kültürel olarak yakın komşularına ortalamadan **daha yüksek** puan veriyor "
         "demektir. Bu, müziğin yanında **kültür ve siyasetin** de oyları etkilediğinin sayısal kanıtıdır. "
         "Türkiye–Azerbaycan örneğini bunun *somut* bir vakası olarak sun. ⚠️ Yine de bu bir **eğilimdir**; "
         "her komşu çifti için geçerli olmak zorunda değildir."),
     ]},
    {"after": "Adım 9: Sunum için notlarınız",
     "cells": [
        ("markdown", sunum_rehberi(
         "**🎤 Ana mesaj:** *“Eurovision sadece müzik değil: ev sahibi avantajı, sahne sırası ve "
         "özellikle **komşu oylaması** sonuçları ölçülebilir biçimde etkiliyor.”*\n\n"
         "**Hangi grafikleri göster:**\n"
         "1. Türkiye'nin tarihçesi (2003 zaferi) → sıcak, kişisel giriş.\n"
         "2. En çok kazananlar → bağlam.\n"
         "3. Uzaklık vs puan (komşu oylaması) → **projenin yıldızı**, en çarpıcı bulgu.\n"
         "4. Türkiye–Azerbaycan örneği → soyut bulguyu somutlaştırır.\n"
         "5. 'İlk 10' modeli + öznitelik önemi → 'neler önemliymiş?'.\n\n"
         "**Her sonucu nasıl yorumla:**\n"
         "- Komşu etkisini **sayıyla** söyle: '0–500 km'ye verilen puan, 5000+ km'ye verilenin ~__ katı'.\n"
         "- Ev sahibi avantajını 'ortalama __ sıra iyileşme' olarak ifade et.\n"
         "- Modelin düşük doğruluğunu **dürüstçe** açıkla: sonuç kısmen öznel, bu beklenen bir şey.\n\n"
         "**Sık yapılan yorumlama hataları:**\n"
         "- ❌ 'Komşu yüksek puan veriyor = kesin torpil.' → Ortak kültür/dil/müzik zevki de olabilir (korelasyon ≠ neden).\n"
         "- ❌ Tek bir ülke örneğinden genel kural çıkarmak → eğilime **tüm veriyle** bak.\n"
         "- ❌ Modelin %100 olmamasını başarısızlık sanmak → bazı şeyler tahmin edilemez.")),
     ]},
]

# ====================== MİNİ 5 — HAVA ======================
AUG["mini_proje5_hava.ipynb"] = [
    {"after": "baslik='İl Bazlı Sıcaklık Dağılımı (5 yıl)'",
     "cells": [
        ("markdown",
         "🔧 **Sıcaklık yerine yağışa bak.** Aynı `cubuk_grafigi` ile her ilin **ortalama yağışını** "
         "karşılaştıralım — şehirler sadece sıcaklıkla değil, nemle de ayrışır:"),
        ("code",
         "cubuk_grafigi(hava, kategori_sutunu='il', deger_sutunu='yagis',\n"
         "              baslik='İl Bazlı Ortalama Günlük Yağış')"),
        ("markdown",
         "📊 **Nasıl yorumlanır?** En sıcak il en kurak olmak zorunda değildir; iklim, sıcaklık + yağış + "
         "rüzgârın **birlikte** belirlediği bir resimdir. Bir şehri tanımlarken tek bir sayıya değil, "
         "**birkaç ölçüye** birden bakmak gerekir."),
     ]},
    {"after": "3-gün tahmin",
     "cells": [
        ("markdown",
         "📊 **'1-gün vs 3-gün' sonucu nasıl yorumlanır?** 3-gün sonrası tahminin RMSE'si (hatası) "
         "1-gün sonrasından **belirgin biçimde büyüktür**. Sebebi sezgisel: gelecek ne kadar uzaksa, "
         "*belirsizlik* o kadar artar. Gerçek meteoroloji de tam olarak bunu yaşar — bu yüzden 10 günlük "
         "tahminlere 5 günlük kadar güvenmeyiz. Sunumda bunu 'tahmin ufku uzadıkça doğruluk düşer' diye anlat."),
     ]},
    {"after": "Transfer maliyeti:",
     "cells": [
        ("markdown",
         "📊 **'Transfer öğrenimi' sonucu nasıl yorumlanır?** Malatya'da eğitilen model Malatya'da en "
         "iyi; başka illere uygulandığında hata **artar**. Artış miktarı şehirler ne kadar *farklıysa* o "
         "kadar büyüktür (örn. yüksek-soğuk Erzurum'da, ılıman İstanbul'a göre daha kötü). Ders: bir model "
         "**eğitildiği dünyaya** benzer veride iyi çalışır; çok farklı bir ortama taşındığında körelir. "
         "Bu, yapay zekânın gerçek hayattaki en büyük tuzaklarından biridir."),
     ]},
    {"after": "Adım 9: Sunum için notlarınız",
     "cells": [
        ("markdown", sunum_rehberi(
         "**🌤️ Ana mesaj:** *“Geçmiş günlerin sıcaklığından yarını tahmin edebiliyoruz; ama tahmin "
         "ufku uzadıkça ve modeli başka şehre taşıdıkça doğruluk düşüyor — hem iklim ısınmasını hem de "
         "yapay zekânın sınırlarını görüyoruz.”*\n\n"
         "**Hangi grafikleri göster:**\n"
         "1. İl bazlı sıcaklık (ve yağış) → şehirleri tanıt.\n"
         "2. Yıllık ortalama trend (2020→2024) → **ısınma** gözlemi.\n"
         "3. >35°C aşırı sıcak gün sayısı → somut, çarpıcı.\n"
         "4. 1-gün vs 3-gün RMSE → 'tahmin ufku' dersi.\n"
         "5. Transfer (Malatya→İstanbul/Erzurum) → 'model nerede çalışır?' dersi.\n\n"
         "**Her sonucu nasıl yorumla:**\n"
         "- RMSE'yi **birimiyle** söyle: 'ortalama __ °C yanılıyoruz'.\n"
         "- 5 yıllık ısınmayı *temkinli* yorumla: 'kısa bir pencere; trend için daha çok yıl gerekir'.\n"
         "- Transfer hatasını 'şehir farkı = model farkı' diye açıkla.\n\n"
         "**Sık yapılan yorumlama hataları:**\n"
         "- ❌ '5 yılda __°C ısındı = her yıl böyle ısınacak.' → Kısa pencereden uzun trend çıkmaz.\n"
         "- ❌ Düşük RMSE'yi 'havayı çözdük' sanmak → yalnızca *yakın* tahmin kolaydır.\n"
         "- ❌ Bir şehrin modelini her yere uygun sanmak → transfer maliyeti gerçektir.")),
     ]},
]
