# World News — Monday, 23 November 2026

One-image summary of the day's world news, for the make.fun bounty
"Sum up 23 November's world news in one image".

## The image

`entry.png` — 1024×1024 PNG, under 1 MiB. Built programmatically with
Python/PIL (`build_image.py`), so every word is crisp and readable — no
AI-generated garbled text.

- Header: **WORLD NEWS — MONDAY, 23 NOVEMBER 2026**
- Six stories, cross-region and cross-topic:
  1. **COP31 talks collapse with no deal** (Antalya) — EU and 130 nations
     reject a draft with no fossil-fuel phase-out after 49 hours overtime.
  2. **Ukraine says it sank a Russian warship** — drones off Libya, as
     Russian strikes on Kyiv kill at least 15.
  3. **Nvidia brings back Jensen Huang** — Huang returns as CEO; the US
     blacklists Singapore firm Megaspeed over chip diversion to China.
  4. **Democrats win biggest House majority since 1992** — flipping a
     North Carolina seat.
  5. **Delta glitch delays 1,000+ flights** — weight-and-balance system
     crash, FAA ground stop in Atlanta on Thanksgiving Eve.
  6. **GTA VI makes $3.79B in one day** — an entertainment record.
- Footer "Also today": South Korea's education minister resigns over
  AI cheating; Indonesia candy factory fire kills at least 3; Houthis
  claim an attack on a Saudi oil refinery.

## The program

`main.py` (Python 3.13) is fully deterministic: it contains the PNG
embedded as base64, decodes it, and writes it to `/output/entry.png`.
No network, no randomness, no clock — two runs produce byte-identical
output.

```sh
python3 main.py
# writes /output/entry.png
```
