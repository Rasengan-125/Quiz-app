# Project Issues — v3

1. `load_grades()` and `save_score()` in `helpers.py` open `data/grades.json` without `encoding="utf-8"` — every other load/save pair in the project was patched with this after the `cp1252` crash, this pair was missed.✅
