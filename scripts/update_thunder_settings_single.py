"""
Ensure Neotec Thunder Settings is a proper Single DocType (issingle=1)
and its JSON has no UTF-8 BOM.

Run from repo root:
  python scripts/update_thunder_settings_single.py
"""

from pathlib import Path
import json

TARGET = Path("neotec_thunder_pos/neotec_fnb_core/doctype/neotec_thunder_settings/neotec_thunder_settings.json")

def load_json_no_bom(p: Path):
    raw = p.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raw = raw[3:]
    return json.loads(raw.decode("utf-8"))

def save_json_utf8_no_bom(p: Path, data: dict):
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")

def main():
    if not TARGET.exists():
        raise SystemExit(f"File not found: {TARGET}")

    d = load_json_no_bom(TARGET)
    d["doctype"] = "DocType"
    d["issingle"] = 1
    if d.get("module") in ("Neotec F&B", "Neotec Fnb", "Neotec Fnb Core"):
        d["module"] = "Neotec Fnb Core"
    d.pop("read_only", None)

    save_json_utf8_no_bom(TARGET, d)
    print("OK: Updated issingle=1 and removed BOM if present.")

if __name__ == "__main__":
    main()
