import fitz  # PyMuPDF
import subprocess
import os
import sys
import tempfile

TESSERACT = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_pdf(pdf_path, lang="ron+eng"):
    doc = fitz.open(pdf_path)
    full_text = []
    with tempfile.TemporaryDirectory() as tmpdir:
        for page_num in range(len(doc)):
            page = doc[page_num]
            mat = fitz.Matrix(2.5, 2.5)  # 2.5x zoom = ~180 DPI
            pix = page.get_pixmap(matrix=mat)
            img_path = os.path.join(tmpdir, f"page_{page_num+1}.png")
            pix.save(img_path)
            out_base = os.path.join(tmpdir, f"out_{page_num+1}")
            subprocess.run(
                [TESSERACT, img_path, out_base, "-l", lang, "--oem", "1", "--psm", "6"],
                capture_output=True
            )
            txt_path = out_base + ".txt"
            if os.path.exists(txt_path):
                with open(txt_path, encoding="utf-8") as f:
                    text = f.read().strip()
                if text:
                    full_text.append(f"--- Pagina {page_num+1} ---\n{text}")
    doc.close()
    return "\n\n".join(full_text)

base = r"C:\Users\Robert\Desktop\Examen-Licenta-Admitere-Master-CSIE\Admitere Master"

files = {
    "CSIE3": [
        (f"CSIE3_{year}", os.path.join(base, "CSIE_3", "Subiecte", f"CSIE3_{year}.pdf"))
        for year in [2024, 2023, 2022, 2021, 2020, 2019]
    ],
    "CSIE4": [
        (f"CSIE4_{year}", os.path.join(base, "CSIE_4", "Subiecte", f"CSIE4_{year}.pdf"))
        for year in [2024, 2023, 2022, 2021, 2020, 2019]
    ],
}

for program, pdfs in files.items():
    out_path = os.path.join(base, f"{'CSIE_3' if program=='CSIE3' else 'CSIE_4'}", f"Subiecte_OCR_{program}.txt")
    results = []
    for name, pdf_path in pdfs:
        print(f"Processing {name}...", flush=True)
        text = ocr_pdf(pdf_path)
        results.append(f"{'='*60}\n{name}\n{'='*60}\n{text}\n")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(results))
    print(f"Saved: {out_path}", flush=True)

print("DONE")
