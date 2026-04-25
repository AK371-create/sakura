#!/usr/bin/env python3
"""残った記事から村上関連の段落・文を削除/書き換え。"""
import json
from pathlib import Path

ART = Path(__file__).parent.parent / "src" / "content" / "articles"


def clean_paragraph(p: str) -> str | None:
    """If paragraph mentions 村上 prominently, drop it. Otherwise return as-is."""
    has_murakami = "村上" in p
    if not has_murakami:
        return p
    # Count sentences (Japanese 。)
    sentences = [s.strip() for s in p.split("。") if s.strip()]
    # Drop sentences that mention 村上
    kept = [s for s in sentences if "村上" not in s]
    if not kept:
        return None  # whole paragraph was about murakami
    return "。".join(kept) + "。"


def process(path: Path) -> bool:
    d = json.loads(path.read_text(encoding="utf-8"))
    changed = False
    for lang_field in ("body_jp", "body_en"):
        body = d.get(lang_field)
        if not body:
            continue
        new_body = []
        for p in body:
            cleaned = clean_paragraph(p)
            if cleaned is None:
                changed = True
                continue
            if cleaned != p:
                changed = True
            new_body.append(cleaned)
        d[lang_field] = new_body
    # Also clean summary
    for fld in ("summary_jp", "summary_en"):
        s = d.get(fld, "")
        if "村上" in s or "Murakami" in s:
            cleaned = clean_paragraph(s) or s
            if cleaned != s:
                d[fld] = cleaned
                changed = True
    if changed:
        path.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    return changed


def main():
    changed_count = 0
    for f in sorted(ART.glob("*.json")):
        if process(f):
            print(f"  cleaned: {f.stem}")
            changed_count += 1
    print(f"Total updated: {changed_count}")


if __name__ == "__main__":
    main()
