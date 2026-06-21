"""
CEYE 2026 Yaz Kampı — Yardımcı Fonksiyonlar
================================================

Bu dosya, kamp boyunca öğrencilerin kendi notebook'larında kullanacağı
hazır fonksiyonları içerir. Amaç, öğrencilerin kod yazma yükünü
azaltıp veriye, modele ve sonuçlara odaklanmalarını sağlamaktır.

Kullanım (Colab'da):
    !cp /content/drive/MyDrive/STEM_yaz_kampi_2026/python_code/helper_tr.py .
    from helper_tr import *

Hazırlayan: Bengu — 2026
"""

import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    mean_squared_error,
    mean_absolute_error,
    r2_score,
)


# ============================================================
# 1. VERİ YÜKLEME ve ÖN İNCELEME
# ============================================================

def veri_yukle(dosya_yolu, indeks_sutunu=None):
    """
    Bir CSV dosyasını okuyup pandas DataFrame olarak döndürür.
    Sonunda satır/sütun sayısı ve ilk 5 satır otomatik basılır.

    Parametreler
    ------------
    dosya_yolu : str
        CSV dosyasının yolu (örn. "input_data/hava_durumu.csv")
    indeks_sutunu : str veya None
        İndeks olarak kullanılacak sütunun adı (örn. "tarih")

    Döndürür
    --------
    df : pandas.DataFrame
    """
    print(f"📂 '{dosya_yolu}' okunuyor...")
    df = pd.read_csv(dosya_yolu, index_col=indeks_sutunu)
    print(f"✅ Yüklendi: {df.shape[0]} satır × {df.shape[1]} sütun")
    print("\nİlk 5 satır:")
    print(df.head())
    return df


def veriyi_ozetle(df):
    """
    Bir DataFrame için genel özet bilgileri (sütun tipleri, eksik değerler,
    sayısal sütunlar için istatistikler) basar.

    Parametreler
    ------------
    df : pandas.DataFrame
    """
    print(f"📊 Veri boyutu: {df.shape[0]} satır × {df.shape[1]} sütun\n")
    print("Sütun tipleri:")
    print(df.dtypes)
    print(f"\nEksik değer sayısı (sütun başına):")
    print(df.isna().sum())
    print("\nSayısal sütunların özeti:")
    print(df.describe())


# ============================================================
# 2. GÖRSELLEŞTİRME (plotly tabanlı)
# ============================================================

def dagilim_grafigi(df, x_sutunu, y_sutunu, renk_sutunu=None, baslik="Dağılım Grafiği"):
    """
    İki sayısal sütun arasındaki dağılımı bir nokta grafiğiyle çizer.

    Parametreler
    ------------
    df : pandas.DataFrame
    x_sutunu : str — yatay eksene yerleşecek sütun
    y_sutunu : str — dikey eksene yerleşecek sütun
    renk_sutunu : str veya None — noktaların renklendirileceği kategori sütunu
    baslik : str

    Döndürür
    --------
    fig : plotly figürü
    """
    print(f"📈 Dağılım grafiği çiziliyor: {x_sutunu} - {y_sutunu}")
    fig = px.scatter(
        df, x=x_sutunu, y=y_sutunu, color=renk_sutunu,
        title=baslik,
        labels={x_sutunu: x_sutunu, y_sutunu: y_sutunu},
    )
    fig.show()
    return fig


def kutu_grafigi(df, kategori_sutunu, sayisal_sutun, baslik="Kutu Grafiği"):
    """
    Bir sayısal sütunun, kategori sütunundaki gruplara göre dağılımını
    kutu grafiği (boxplot) ile gösterir.
    """
    print(f"📦 Kutu grafiği: {sayisal_sutun} (gruplar: {kategori_sutunu})")
    fig = px.box(
        df, x=kategori_sutunu, y=sayisal_sutun, color=kategori_sutunu,
        points="all", title=baslik,
    )
    fig.show()
    return fig


def cubuk_grafigi(df, kategori_sutunu, deger_sutunu=None, baslik="Çubuk Grafiği"):
    """
    Bir kategorik sütunun değer sayılarını (deger_sutunu=None ise frekans)
    veya başka bir sütunun ortalamasını çubuk grafiği olarak çizer.
    """
    if deger_sutunu is None:
        sayim = df[kategori_sutunu].value_counts().reset_index()
        sayim.columns = [kategori_sutunu, "sayi"]
        fig = px.bar(sayim, x=kategori_sutunu, y="sayi", title=baslik)
    else:
        ortalama = df.groupby(kategori_sutunu)[deger_sutunu].mean().reset_index()
        fig = px.bar(ortalama, x=kategori_sutunu, y=deger_sutunu,
                     title=baslik + f" — {deger_sutunu} ortalaması")
    fig.show()
    return fig


def histogram(df, sutun, baslik="Histogram"):
    """
    Tek bir sayısal sütunun dağılımını histogram olarak çizer.
    """
    fig = px.histogram(df, x=sutun, title=baslik, nbins=30)
    fig.show()
    return fig


def korelasyon_haritasi(df, baslik="Korelasyon Haritası"):
    """
    Tüm sayısal sütunlar arasındaki korelasyonu ısı haritası olarak çizer.
    Pearson korelasyonu kullanılır.
    """
    sayisal = df.select_dtypes(include=[np.number])
    korelasyon = sayisal.corr()
    fig = px.imshow(
        korelasyon, text_auto=".2f",
        color_continuous_scale="RdBu_r", zmin=-1, zmax=1,
        title=baslik,
    )
    fig.show()
    return fig


# ============================================================
# 3. MAKİNE ÖĞRENMESİ — VERİ HAZIRLAMA
# ============================================================

def egitim_test_bol(X, y, test_orani=0.2, rastgele_tohum=42):
    """
    Veriyi eğitim ve test kümelerine böler.

    Parametreler
    ------------
    X : pandas.DataFrame veya numpy array — öznitelikler
    y : pandas.Series veya numpy array — hedef etiket
    test_orani : float — test kümesinin oranı (varsayılan 0.2 = %20)
    rastgele_tohum : int — tekrarlanabilirlik için sabit sayı

    Döndürür
    --------
    X_egitim, X_test, y_egitim, y_test
    """
    X_egitim, X_test, y_egitim, y_test = train_test_split(
        X, y, test_size=test_orani, random_state=rastgele_tohum,
    )
    print(f"🪓 Eğitim: {X_egitim.shape[0]} örnek | Test: {X_test.shape[0]} örnek")
    return X_egitim, X_test, y_egitim, y_test


# ============================================================
# 4. SINIFLANDIRMA MODELLERİ
# ============================================================

def karar_agaci_egit(X_egitim, y_egitim, max_derinlik=3):
    """
    Bir karar ağacı sınıflandırıcısı eğitir.

    Parametreler
    ------------
    X_egitim, y_egitim : eğitim verisi
    max_derinlik : int — ağacın maksimum derinliği (yorumlanabilirlik için 3-5 önerilir)

    Döndürür
    --------
    model : eğitilmiş DecisionTreeClassifier nesnesi
    """
    print(f"🌳 Karar ağacı eğitiliyor (max_derinlik={max_derinlik})...")
    model = DecisionTreeClassifier(max_depth=max_derinlik, random_state=42)
    model.fit(X_egitim, y_egitim)
    print("✅ Eğitim tamamlandı.")
    return model


def rastgele_orman_egit(X_egitim, y_egitim, agac_sayisi=100):
    """
    Bir rastgele orman (Random Forest) sınıflandırıcısı eğitir.
    """
    print(f"🌲🌲🌲 Rastgele orman eğitiliyor ({agac_sayisi} ağaç)...")
    model = RandomForestClassifier(n_estimators=agac_sayisi, random_state=42)
    model.fit(X_egitim, y_egitim)
    print("✅ Eğitim tamamlandı.")
    return model


def model_degerlendir(model, X_test, y_test, sinif_adlari=None):
    """
    Eğitilmiş bir sınıflandırma modelini test verisi üzerinde değerlendirir.
    Doğruluk yüzdesini ve karmaşıklık matrisini gösterir.
    """
    tahminler = model.predict(X_test)
    dogruluk = accuracy_score(y_test, tahminler)
    print(f"🎯 Doğruluk: %{dogruluk * 100:.2f}")

    cm = confusion_matrix(y_test, tahminler)
    if sinif_adlari is None:
        sinif_adlari = [str(s) for s in np.unique(y_test)]

    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(
        cm, annot=True, fmt="d", cmap="Blues",
        xticklabels=sinif_adlari, yticklabels=sinif_adlari, ax=ax,
    )
    ax.set_xlabel("Tahmin")
    ax.set_ylabel("Gerçek")
    ax.set_title(f"Karmaşıklık Matrisi — Doğruluk: %{dogruluk * 100:.2f}")
    plt.tight_layout()
    plt.show()
    return dogruluk


def oznitelik_onemi_grafigi(model, oznitelik_adlari, en_iyi_n=10, baslik="Öznitelik Önemi"):
    """
    Karar ağacı veya rastgele orman gibi modellerin hangi öznitelikleri
    daha çok kullandığını gösteren çubuk grafik çizer.
    """
    if not hasattr(model, "feature_importances_"):
        print("⚠️ Bu modelde öznitelik önemi bilgisi yok.")
        return None

    onem = pd.DataFrame({
        "oznitelik": oznitelik_adlari,
        "onem": model.feature_importances_,
    }).sort_values("onem", ascending=False).head(en_iyi_n)

    fig = px.bar(
        onem, x="onem", y="oznitelik", orientation="h",
        title=baslik + f" (en önemli {en_iyi_n})",
        labels={"onem": "Önem", "oznitelik": "Öznitelik"},
    )
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    fig.show()
    return fig


def karar_agaci_ciz(model, oznitelik_adlari, sinif_adlari):
    """
    Bir karar ağacı modelini görsel olarak çizer.
    Sadece küçük ağaçlar için anlamlıdır (max_derinlik <= 4 önerilir).
    """
    fig, ax = plt.subplots(figsize=(16, 8))
    plot_tree(
        model, feature_names=oznitelik_adlari, class_names=sinif_adlari,
        filled=True, rounded=True, fontsize=10, ax=ax,
    )
    plt.title("Karar Ağacı Görselleştirmesi")
    plt.tight_layout()
    plt.show()


# ============================================================
# 5. REGRESYON MODELLERİ (sayısal tahmin)
# ============================================================

def lineer_regresyon_egit(X_egitim, y_egitim):
    """
    Bir lineer regresyon modeli eğitir.
    """
    print("📏 Lineer regresyon eğitiliyor...")
    model = LinearRegression()
    model.fit(X_egitim, y_egitim)
    print("✅ Eğitim tamamlandı.")
    return model


def regresyon_degerlendir(model, X_test, y_test, baslik="Tahmin vs Gerçek"):
    """
    Bir regresyon modelinin performansını ölçer ve tahmin-vs-gerçek
    grafiği çizer. Hata metrikleri (RMSE, MAE, R²) basılır.
    """
    tahminler = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, tahminler))
    mae = mean_absolute_error(y_test, tahminler)
    r2 = r2_score(y_test, tahminler)

    print(f"📊 RMSE (kök ortalama kare hata): {rmse:.3f}")
    print(f"📊 MAE  (ortalama mutlak hata) : {mae:.3f}")
    print(f"📊 R²   (açıklanan varyans)    : {r2:.3f}")

    df_tahmin = pd.DataFrame({"gercek": np.array(y_test).flatten(),
                              "tahmin": tahminler.flatten()})

    try:
        fig = px.scatter(
            df_tahmin, x="gercek", y="tahmin",
            title=baslik + f" (R² = {r2:.3f})",
            labels={"gercek": "Gerçek değer", "tahmin": "Tahmin edilen değer"},
            trendline="ols",
        )
    except (ImportError, ModuleNotFoundError):
        fig = px.scatter(
            df_tahmin, x="gercek", y="tahmin",
            title=baslik + f" (R² = {r2:.3f})",
            labels={"gercek": "Gerçek değer", "tahmin": "Tahmin edilen değer"},
        )
    # Mükemmel tahmin çizgisi (y=x)
    min_d = min(df_tahmin["gercek"].min(), df_tahmin["tahmin"].min())
    max_d = max(df_tahmin["gercek"].max(), df_tahmin["tahmin"].max())
    fig.add_trace(go.Scatter(
        x=[min_d, max_d], y=[min_d, max_d],
        mode="lines", name="Mükemmel tahmin",
        line=dict(color="red", dash="dash"),
    ))
    fig.show()
    return {"rmse": rmse, "mae": mae, "r2": r2}


# ============================================================
# 6. KÜÇÜK YARDIMCILAR
# ============================================================

def yas_hesapla(dogum_yili, olum_yili=None, mevcut_yil=2026):
    """
    Doğum yılı ve (varsa) ölüm yılından yaş hesaplar.
    Ölüm yılı bilinmiyorsa mevcut_yil kullanılır.
    """
    if olum_yili is None or pd.isna(olum_yili):
        olum_yili = mevcut_yil
    return olum_yili - dogum_yili


def turkce_say(sayi):
    """
    Bir sayıyı insan-okunaklı Türkçe biçimde verir (1234567 → '1.234.567').
    """
    return f"{int(sayi):,}".replace(",", ".")
