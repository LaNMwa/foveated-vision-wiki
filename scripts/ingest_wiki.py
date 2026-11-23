#!/usr/bin/env python3
"""Read the five user-provided paper PDFs and build a PRIVATE, page-indexed research corpus.

This is a deterministic PDF retrieval index, not a live LLM service. Keep the full-text index private.
"""
import argparse, hashlib, json, re
from pathlib import Path
import fitz

PAPERS = [
    ("P1", "VisionMode", "VisionMode_2017.pdf"),
    ("P2", "FOVEA", "FOVEA_2021.pdf"),
    ("P3", "RPR", "RPR_2021.pdf"),
    ("P4", "TuMag", "TuMag_2021.pdf"),
    ("P5", "D-SWIM", "D-SWIM_2019.pdf"),
]

def ingest(source_dir, out_file):
    entries, metadata = [], []
    for paper_id, short_name, filename in PAPERS:
        path = Path(source_dir) / filename
        if not path.is_file(): raise FileNotFoundError(f"Missing PDF {paper_id}: {path}")
        raw = path.read_bytes()
        with fitz.open(path) as pdf:
            pages = len(pdf)
            usable = 0
            for i, page in enumerate(pdf):
                t = re.sub(r"\s+", " ", page.get_text("text")).strip()
                entries.append({"paper": paper_id, "name": short_name, "pdf_page": i+1, "text": t})
                usable += bool(t)
        if usable < pages - 1: raise ValueError(f"Too many unreadable pages: {paper_id}")
        metadata.append({"id": paper_id, "name": short_name, "file": filename,
                         "pages": pages, "searchable_pages": usable,
                         "sha256": hashlib.sha256(raw).hexdigest()})
        print(f"INGEST PASS {paper_id} {short_name}: {pages} pages, searchable {usable}, sha256 {metadata[-1]['sha256'][:12]}")
    index = {"type": "private-PDF-page-index", "method": "PyMuPDF extraction + keyword retrieval",
             "papers":metadata, "pages":entries}
    Path(out_file).parent.mkdir(parents=True, exist_ok=True)
    Path(out_file).write_text(json.dumps(index,ensure_ascii=False),encoding="utf-8")
    print(f"INDEX READY: {len(metadata)} papers / {len(entries)} pages -> {out_file}")
    return index

def search(index, text, limit=5):
    q=text.lower().strip()
    toks=[t for t in re.findall(r"[a-z0-9]+",q) if len(t)>2]
    if not toks:return []
    results=[]
    for p in index['pages']:
        hay=p['text'].lower()
        score=sum(hay.count(t) for t in toks) + 12 * (q in hay)
        if score:
            positions=[hay.find(t) for t in toks if t in hay]
            pos=min(positions) if positions else 0
            excerpt=p['text'][max(0,pos-60):min(len(hay),pos+250)]
            results.append((score,p['paper'],p['pdf_page'],excerpt))
    results.sort(key=lambda z:(-z[0],z[1],z[2]))
    return results[:limit]

def main():
    ap=argparse.ArgumentParser(description="Ingest/search five local research paper PDFs")
    sp=ap.add_subparsers(dest="cmd",required=True)
    x=sp.add_parser('ingest');x.add_argument('--source-dir',required=True);x.add_argument('--out',required=True)
    y=sp.add_parser('query');y.add_argument('--index',required=True);y.add_argument('--text',required=True);y.add_argument('--limit',type=int,default=5)
    z=ap.parse_args()
    if z.cmd=='ingest':ingest(z.source_dir,z.out)
    else:
        index=json.loads(Path(z.index).read_text(encoding='utf-8'))
        rows=search(index,z.text,z.limit)
        for score,p,pageno,excerpt in rows:
            print(f'[{p} PDF p.{pageno}] score={score}: {excerpt}')
        if not rows: print('No evidence found. Recheck the paper; do not invent answers.')

if __name__=='__main__':main()
