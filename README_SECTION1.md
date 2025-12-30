# Section 1 Enhancement Pack (Foundation + Settings)

This pack adds:
- Desk Page: **Thunder POS Setup**
- Controller stub: **Neotec Thunder Settings**
- Script to force Settings DocType to Single (`issingle=1`) and remove UTF-8 BOM
- Hook snippet for `pages`

## Apply
1) Copy folders into your repo root (merge):
   - `neotec_thunder_pos/page/thunder_pos_setup/`
   - `neotec_thunder_pos/neotec_fnb_core/doctype/neotec_thunder_settings/`
   - `scripts/`

2) Merge `hooks_snippet.txt` into `neotec_thunder_pos/hooks.py`

3) Run:
   ```bash
   python scripts/update_thunder_settings_single.py
   ```

4) Commit & push:
   ```bash
   git add -A
   git commit -m "Section 1: Setup page + Settings single"
   git push
   ```

5) Frappe Cloud → Apps → Update App.

Generated: 2025-12-30 09:53:46
