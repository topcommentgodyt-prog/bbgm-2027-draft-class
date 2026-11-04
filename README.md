# 2027 NBA Draft Class for Basketball GM

A custom [Basketball GM](https://basketball-gm.com) draft class of the real prospects for the 2027 NBA draft, with real headshots. It's updated daily: new players are added as they break onto the big boards, and the class also tracks risers, fallers, withdrawals and injuries.

## Import into BBGM

1. Download [`draft-class-2027.json`](https://github.com/topcommentgodyt-prog/bbgm-2027-draft-class/releases/latest/download/draft-class-2027.json) from the [latest release](https://github.com/topcommentgodyt-prog/bbgm-2027-draft-class/releases/latest), which also lists what changed.
2. In your league, go to **Draft → Draft Scouting**, find the 2027 class, and click **Import**.

Dated snapshots are in [`builds/`](builds/), and every change is logged with sources in [`CHANGELOG.md`](CHANGELOG.md).

## What's in it

- **Players:** board order, real height, weight, age, school/team and hometown, based on current mock drafts and big boards (Tankathon, FanSided, ESPN, CBS, SI, Bleacher Report and others).
- **Ratings:** estimates built with BBGM's own overall formula, from each player's scouting profile (shooter, rim protector, etc.), age and board position. They are not official in any way.
- **Headshots:** mostly ESPN, plus school, league and club photos, with backgrounds removed locally using [rembg](https://github.com/danielgatis/rembg) and embedded in the file, so there are no broken image links. Photos belong to their respective owners and are included for personal, non-commercial use.
- **Injuries:** current injuries go into BBGM's injury field, with estimated games out.

## Project layout

| File | Purpose |
|---|---|
| `prospects.json` | Source of truth: one entry per prospect (rank, bio, tags, image, injury, status) |
| `build.py` | Builds `draft-class-2027.json` from `prospects.json` |
| `process.py` | Cleans headshots: removes backgrounds, crops and converts to WebP |
| `headshots/raw`, `headshots/final` | Original and processed photos |

## Rebuilding locally

```bash
python3.11 -m venv .venv
.venv/bin/pip install "rembg[cpu]" pillow
.venv/bin/python -I process.py
.venv/bin/python -I build.py
```
