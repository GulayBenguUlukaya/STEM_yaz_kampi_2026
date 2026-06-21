#!/usr/bin/env python3
"""
EGITMEN_TANITIMI.md icin biyoinformatik gorselleri uretir (matplotlib).
Ogrenci seviyesinde, Turkce etiketli, lisanssiz/temiz figurler.
Cikti: images/*.png
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

rng = np.random.default_rng(7)
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 13, "savefig.dpi": 130, "savefig.bbox": "tight"})

BASE_COLORS = {"A": "#2ecc71", "T": "#e74c3c", "G": "#3498db", "C": "#f1c40f"}


def save(fig, name):
    p = os.path.join(OUT, name)
    fig.savefig(p, facecolor="white")
    plt.close(fig)
    print("✅", name)


# 1) DNA bir koddur + dizileme "okumalari"
def fig_dna_reads():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 4.6),
                                   gridspec_kw={"height_ratios": [1, 1.4]})
    seq = "".join(rng.choice(list("ATGC"), 60))
    for i, b in enumerate(seq):
        ax1.text(i, 0, b, color=BASE_COLORS[b], fontfamily="monospace",
                 fontsize=15, fontweight="bold", ha="center", va="center")
    ax1.set_xlim(-1, 60); ax1.set_ylim(-1, 1); ax1.axis("off")
    ax1.set_title("DNA = 4 harfli bir kod  (A, T, G, C)  —  bir insanda ~3 milyar harf",
                  fontsize=13, fontweight="bold")

    # reads: long reference + short colored fragments
    ax2.hlines(0, 0, 60, color="#444", lw=3)
    ax2.text(30, 0.55, "Gerçek DNA dizisi (referans)", ha="center", fontsize=11, color="#444")
    y = -0.6
    for _ in range(14):
        start = rng.integers(0, 48)
        length = rng.integers(8, 13)
        ax2.add_patch(plt.Rectangle((start, y), length, 0.28,
                                    color=plt.cm.tab20(rng.integers(0, 20)), alpha=0.9))
        y -= 0.38
        if y < -5:
            y = -0.6
    ax2.set_xlim(-1, 60); ax2.set_ylim(-5.2, 1)
    ax2.axis("off")
    ax2.set_title("Dizileme makinesi DNA'yı MİLYONLARCA küçük parçaya böler — "
                  "bilgisayar bunları birleştirir ", fontsize=12)
    save(fig, "01_dna_okumalari.png")


# 2) Gen ifade isi haritasi (genes x samples)
def fig_heatmap():
    n_genes, n_s = 18, 12
    healthy = rng.normal(0, 0.6, (n_genes, n_s // 2))
    sick = rng.normal(0, 0.6, (n_genes, n_s // 2))
    # birkaç gen hastalıkta belirgin değişsin
    sick[2:6, :] += 2.2
    sick[12:15, :] -= 2.0
    data = np.hstack([healthy, sick])
    fig, ax = plt.subplots(figsize=(9, 6))
    im = ax.imshow(data, cmap="RdBu_r", aspect="auto", vmin=-3, vmax=3)
    ax.set_yticks(range(n_genes)); ax.set_yticklabels([f"Gen {i+1}" for i in range(n_genes)], fontsize=9)
    ax.set_xticks([n_s // 4, 3 * n_s // 4]); ax.set_xticklabels(["SAĞLIKLI\nörnekler", "HASTA\nörnekler"], fontsize=12, fontweight="bold")
    ax.axvline(n_s // 2 - 0.5, color="k", lw=2)
    cb = fig.colorbar(im, ax=ax, shrink=0.8)
    cb.set_label("Gen ne kadar 'açık'?  (kırmızı=çok, mavi=az)")
    ax.set_title("Gen İfade Isı Haritası\nHer satır bir gen, her sütun bir kişi — hangi genler farklı yanıyor?",
                 fontsize=12, fontweight="bold")
    save(fig, "02_gen_isi_haritasi.png")


# 3) Volkan grafigi (differential expression)
def fig_volcano():
    n = 1500
    log2fc = rng.normal(0, 1.0, n)
    pval = rng.uniform(0, 1, n)
    sig = np.zeros(n, bool)
    # birkaç gerçek "farklı" gen
    idx = rng.choice(n, 70, replace=False)
    log2fc[idx] += rng.choice([-1, 1], 70) * rng.uniform(2, 4, 70)
    pval[idx] = rng.uniform(1e-12, 1e-4, 70)
    nlp = -np.log10(pval + 1e-300)
    up = (log2fc > 1) & (nlp > 2)
    down = (log2fc < -1) & (nlp > 2)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(log2fc[~(up | down)], nlp[~(up | down)], s=8, color="#bbb", alpha=0.6, label="değişmeyen")
    ax.scatter(log2fc[up], nlp[up], s=16, color="#e74c3c", label="hastalıkta ARTAN")
    ax.scatter(log2fc[down], nlp[down], s=16, color="#3498db", label="hastalıkta AZALAN")
    ax.axvline(1, ls="--", color="#888"); ax.axvline(-1, ls="--", color="#888")
    ax.axhline(2, ls="--", color="#888")
    ax.set_xlabel("Değişim yönü ve büyüklüğü  (log2)")
    ax.set_ylabel("Ne kadar emin olabiliriz?  (-log10 p)")
    ax.set_title("'Volkan' Grafiği\n20.000 genin içinden 'suçlu' olabilecek birkaçını bulmak",
                 fontsize=12, fontweight="bold")
    ax.legend(loc="upper center", fontsize=10)
    save(fig, "03_volkan_grafigi.png")


# 4) Gen takimlari / ssGSEA bar
def fig_pathways():
    isimler = ["Hücre büyümesi", "İltihap", "Bağışıklık (savunma)",
               "DNA onarımı", "Enerji / metabolizma", "Hücre ölümü"]
    skor = np.array([2.3, 1.4, -0.4, -1.8, 0.7, -2.1])
    renk = ["#e74c3c" if s > 0 else "#3498db" for s in skor]
    order = np.argsort(skor)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.barh(np.array(isimler)[order], skor[order], color=np.array(renk)[order])
    ax.axvline(0, color="k", lw=1)
    ax.set_xlabel("Grup ne kadar aktif?  (sağ = aktif / sol = sessiz)")
    ax.set_title("Hangi gen grubu işbaşında?\n"
                 "Tümörde 'büyüme grubu' aşırı aktif — önemli bir ipucu! ",
                 fontsize=12, fontweight="bold")
    save(fig, "04_gen_gruplari.png")


# 5) Pipeline akis semasi
def fig_pipeline():
    fig, ax = plt.subplots(figsize=(12, 3.2))
    ax.set_xlim(0, 12); ax.set_ylim(0, 3); ax.axis("off")
    steps = [
        ("Dizileme\nmakinesi", "#fdebd0"),
        ("Ham veri\n(milyonlarca parça)", "#d6eaf8"),
        ("Temizle &\nbirleştir (pipeline)", "#d5f5e3"),
        ("Analiz\n(Python · R · bash)", "#e8daef"),
        ("Grafik &\nsonuç", "#fadbd8"),
    ]
    x = 0.3
    w, h, gap = 2.0, 1.6, 0.35
    centers = []
    for label, c in steps:
        box = FancyBboxPatch((x, 0.7), w, h, boxstyle="round,pad=0.08,rounding_size=0.15",
                             linewidth=1.5, edgecolor="#555", facecolor=c)
        ax.add_patch(box)
        ax.text(x + w / 2, 0.7 + h / 2, label, ha="center", va="center", fontsize=11, fontweight="bold")
        centers.append(x + w)
        x += w + gap
    for cx in centers[:-1]:
        ax.add_patch(FancyArrowPatch((cx, 1.5), (cx + gap, 1.5),
                     arrowstyle="-|>", mutation_scale=20, lw=2, color="#555"))
    ax.set_title("Bir biyoinformatikçinin günlük iş akışı  —  her adım KOD ile otomatik",
                 fontsize=13, fontweight="bold", pad=10)
    save(fig, "05_is_akisi.png")


if __name__ == "__main__":
    fig_dna_reads()
    fig_heatmap()
    fig_volcano()
    fig_pathways()
    fig_pipeline()
    print("\n🎉 Tüm görseller images/ klasörüne kaydedildi.")
