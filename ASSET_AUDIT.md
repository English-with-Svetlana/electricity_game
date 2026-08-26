# BLACKOUT — Phase 1 Asset Performance Audit

Audit date: 2026-08-25. Original assets were inspected recursively and left untouched.

## Inventory and totals

- 62 PNG images: **141.90 MiB** total.
- 22 audio files (`.wav` and `.mp3`): **66.27 MiB** total.
- Approximate combined image/audio payload: **208.17 MiB**.
- All expected asset categories are present. Sound files correctly live in `assets/sounds/`.
- No duplicate gameplay filenames were found. Finder metadata files (`.DS_Store`) occur in several folders and should be excluded from deployment.

## Ten largest assets

| Asset | Current size | Dimensions/type |
|---|---:|---|
| `assets/sounds/city_rain.wav` | 31.88 MiB | WAV |
| `assets/sounds/danger.mp3` | 8.63 MiB | MP3 |
| `assets/sounds/underground.wav` | 8.32 MiB | WAV |
| `assets/sounds/final_escape.mp3` | 3.24 MiB | MP3 |
| `assets/items/city_map.png` | 3.05 MiB | 1536×1024 PNG, transparency |
| `assets/sounds/exploration.mp3` | 3.04 MiB | MP3 |
| `assets/items/tool_kit.png` | 2.78 MiB | 1536×1024 PNG, transparency |
| `assets/ui/inventory_panel.png` | 2.75 MiB | 1536×1024 PNG, transparency |
| `assets/ui/double_gap_panel.png` | 2.71 MiB | 1672×941 PNG, transparency |
| `assets/ui/find_mistake_panel.png` | 2.70 MiB | 1672×941 PNG, transparency |

## Image findings

Backgrounds are 1536×1024 or 1672×941 and typically 1.6–2.6 MiB each. The 1672×941 assets closely match 16:9 and are moderately oversized for a 1200×675 viewport, which is reasonable for display-density headroom. The 1536×1024 backgrounds are 3:2 and require cropping under `cover`; a future optimized derivative should use a composition-checked 16:9 crop rather than mechanical distortion.

Most item, interactive, collectible, and achievement PNGs are 1254–1536 pixels wide and roughly 1.5–3.1 MiB even though their expected on-screen size is commonly 100–350 pixels. These are the clearest resize candidates. Transparency is present on most of these cutouts and must be preserved. `chocolate_bar.png` and `emergency_access_card.png` are RGB rather than RGBA despite behaving like item art; their visible backgrounds must be checked before selecting a future format.

Text-bearing UI panels range from about 1.4–2.9 MiB. They should retain enough resolution for sharp lettering; only lossless or high-quality visually verified derivatives are recommended.

## Recommended derivatives (approval required)

| Category/assets | Proposed target | Proposed format | Estimated reduction |
|---|---|---|---:|
| RGB backgrounds, visually checked individually | about 1600×900 for 1672×941; composition-safe 1600×900 derivative for 1536×1024 | high-quality WebP | 45–70% |
| Large transparent items and interactive objects | 512–768 px longest edge, based on maximum display size | optimized PNG; transparent WebP only after visual/compatibility QA | 55–80% |
| Achievement icons | 512×512 or 640×640 | optimized transparent PNG/WebP after QA | 60–80% |
| Collectibles | 640–900 px longest edge, preserving fine detail | optimized transparent PNG/WebP after QA | 45–70% |
| Full-screen text-bearing UI | retain current dimensions initially | optimized PNG or lossless WebP after side-by-side text QA | 15–40% |
| `city_rain.wav`, `underground.wav` | retain duration/channels only as needed | browser-compatible compressed ambience (for example MP3) | 80–95% |
| Existing large MP3 tracks | retain masters, evaluate bitrate/duration | lower-bitrate MP3 derivative after listening test | 25–60% |

Potential aggregate reduction is approximately **110–155 MiB** (roughly 53–74%), subject to visual and listening QA. No optimized copies have been created.

## Loading risks and Phase 1 response

The complete library is far too large for eager iframe loading. The Phase 1 loader requests only Start, How to Play, Home, HUD, Life, Phone, Question, and Feedback images. Audio begins only after a user gesture; small SFX are loaded on demand. Large ambience/music and all route/later-game art do not block startup.

## Path and filename checks

- Actual filenames match the specification's known lists, including mixed `.wav`/`.mp3` sound extensions.
- Correct relative sound root is `assets/sounds/`; no root `sounds/` folder exists or is needed.
- `.DS_Store` files are the only suspicious non-game assets found and are safe candidates for deployment exclusion later.
- Original artwork and audio remain unchanged.
