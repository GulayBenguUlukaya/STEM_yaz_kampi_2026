#!/usr/bin/env python3
"""
STEAM Kampı — Notebook render aracı.

Orijinal notebook'ları (Colab + Google Drive için yazılmış) DEĞİŞTİRMEDEN,
yerel olarak çalıştırıp çıktılarıyla birlikte `rendered/` klasörüne kaydeder.
Böylece GitHub'da kod + çıktı görünür.

- Colab kurulum hücresi yerelde çalışacak biçimde sadeleştirilir.
- plotly grafikleri statik PNG olarak gömülür (GitHub JavaScript'i göstermez).
- input() içeren hücreler örnek cevaplarla otomatik yanıtlanır.
"""
import os
import re
import sys
import copy
import nbformat
from nbclient import NotebookClient

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from augmentations import AUG, PREVIEW_BANNER

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NB_DIR = os.path.join(REPO_ROOT, "notebooks")
OUT_DIR = os.path.join(REPO_ROOT, "rendered")

# Notebook'a özel input() cevapları (sıra önemli)
INPUT_ANSWERS = {
    "gun1.ipynb": ["Zeynep", "2010"],
}

COLAB_LINE_PATTERNS = [
    "google.colab",
    "drive.mount",
    "/content/drive",
    "os.chdir(",
    "Klasördeyiz",
]

INIT_CODE = """\
import os, sys, warnings
warnings.filterwarnings("ignore")
os.chdir(REPO_ROOT_PLACEHOLDER)
sys.path.insert(0, os.getcwd())
import matplotlib
get_ipython().run_line_magic("matplotlib", "inline")  # matplotlib grafiklerini (karmaşıklık matrisi, ağaç) göm
import plotly.io as pio
pio.renderers.default = "png"          # plotly grafiklerini statik PNG yap
pio.templates.default = "plotly_white"
# input() icin otomatik cevap: user-namespace'te 'input' tanimlayarak
# ipykernel'in her hucrede yeniden kurdugu builtins.input'u golgeleriz.
_answers = iter(ANSWERS_PLACEHOLDER)
def input(prompt=""):
    try:
        a = next(_answers)
    except StopIteration:
        a = ""
    print(f"{prompt}{a}")               # Colab gibi: soru + cevap gorunsun
    return a
"""


def is_colab_setup_cell(src: str) -> bool:
    return "google.colab" in src or "drive.mount" in src


def localize_setup_cell(src: str) -> str:
    """Colab'a özel satırları çıkar, geri kalanı koru."""
    kept = []
    for line in src.splitlines():
        if any(p in line for p in COLAB_LINE_PATTERNS):
            continue
        kept.append(line)
    return "\n".join(kept).strip() + "\n"


def _new_cell(ctype: str, src: str):
    if ctype == "markdown":
        return nbformat.v4.new_markdown_cell(src)
    return nbformat.v4.new_code_cell(src)


def apply_augmentations(nb, nb_name: str):
    """
    Eğitsel hücreleri ekler:
      • her defterin başına ortak önizleme afişi (ilk hücreden sonra),
      • AUG[nb_name] içindeki 'after' çapalarının ardına varyasyon/yorum hücreleri.
    Çapalar yalnızca ORİJİNAL hücrelerle eşleştirilir (eklenenler tekrar eşleşmez).
    """
    inserts = AUG.get(nb_name, [])
    used = set()
    new_cells = []
    for idx, cell in enumerate(nb.cells):
        new_cells.append(cell)
        if idx == 0:  # başlıktan hemen sonra önizleme afişi
            new_cells.append(_new_cell("markdown", PREVIEW_BANNER))
        src = "".join(cell.get("source", "")) if isinstance(cell.get("source"), list) else cell.get("source", "")
        for k, ins in enumerate(inserts):
            if k in used:
                continue
            if ins["after"] in src:
                for ctype, csrc in ins["cells"]:
                    new_cells.append(_new_cell(ctype, csrc))
                used.add(k)
                break  # bir hücre = en fazla bir çapa
    nb.cells = new_cells
    for k, ins in enumerate(inserts):
        if k not in used:
            print(f"⚠️  {nb_name}: çapa bulunamadı -> {ins['after'][:50]!r}", flush=True)


def render(nb_name: str):
    src_path = os.path.join(NB_DIR, nb_name)
    nb = nbformat.read(src_path, as_version=4)

    # 1) Colab kurulum hücresini yerelleştir
    for cell in nb.cells:
        if cell.cell_type == "code" and is_colab_setup_cell("".join(cell.source)):
            cell.source = localize_setup_cell("".join(cell.source))

    # 1.5) Eğitsel içerik ekle (varyasyonlar + yorumlama + sunum rehberleri)
    apply_augmentations(nb, nb_name)

    # 2) Gizli init hücresi ekle (çalıştırma sonrası silinecek)
    answers = INPUT_ANSWERS.get(nb_name, [])
    init_src = (INIT_CODE
                .replace("REPO_ROOT_PLACEHOLDER", repr(REPO_ROOT))
                .replace("ANSWERS_PLACEHOLDER", repr(answers)))
    init_cell = nbformat.v4.new_code_cell(source=init_src)
    init_cell.metadata["tags"] = ["__render_init__"]
    nb.cells.insert(0, init_cell)

    # 3) Çalıştır
    client = NotebookClient(
        nb,
        timeout=300,
        kernel_name="python3",
        resources={"metadata": {"path": REPO_ROOT}},
        allow_errors=False,
    )
    print(f"▶️  {nb_name} çalıştırılıyor ...", flush=True)
    client.execute()

    # 4) Gizli init hücresini çıkar
    nb.cells = [c for c in nb.cells
                if "__render_init__" not in c.get("metadata", {}).get("tags", [])]

    # 5) Kaydet
    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, nb_name)
    nbformat.write(nb, out_path)
    n_imgs = sum(
        1
        for c in nb.cells if c.cell_type == "code"
        for o in c.get("outputs", [])
        if "image/png" in o.get("data", {})
    )
    print(f"✅ {nb_name} -> rendered/  ({n_imgs} grafik)", flush=True)


if __name__ == "__main__":
    names = sys.argv[1:] or sorted(
        f for f in os.listdir(NB_DIR) if f.endswith(".ipynb")
    )
    failures = []
    for n in names:
        try:
            render(n)
        except Exception as e:
            failures.append((n, repr(e)[:400]))
            print(f"❌ {n} HATA: {repr(e)[:400]}", flush=True)
    if failures:
        print("\n=== BAŞARISIZ ===")
        for n, e in failures:
            print(f"- {n}: {e}")
        sys.exit(1)
    print("\n🎉 Tüm notebook'lar render edildi.")
