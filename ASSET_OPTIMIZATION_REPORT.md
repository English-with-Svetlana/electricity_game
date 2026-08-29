# BLACKOUT — Asset Optimization Report

Optimization date: 2026-08-25. This phase created derivatives only. Original assets, `assets/ui/`, and game code were not modified.

## Summary

- Derivatives created: **46** (16 backgrounds, 9 items, 5 interactive objects, 5 collectibles, 6 achievements, 5 audio files).
- Original size for the optimized set: **150.05 MiB**.
- Optimized size: **27.99 MiB**.
- Space saved: **122.07 MiB** (**81.3%**).
- Background encoding: WebP quality 92 with composition-checked 16:9 output.
- Audio: ambience at 128 kbps MP3; music at 160 kbps MP3.
- True-alpha PNG sources retained alpha in their resized PNG derivatives.

## Mapping

| Original path | Optimized path | Original | Optimized | Dimensions | Reduction |
|---|---|---:|---:|---|---:|
| `assets/backgrounds/bridge.png` | `assets/optimized/backgrounds/bridge.webp` | 2.60 MiB | 0.39 MiB | 1536×1024 → 1536×864 | 85.2% |
| `assets/backgrounds/city_center.png` | `assets/optimized/backgrounds/city_center.webp` | 2.16 MiB | 0.25 MiB | 1672×941 → 1600×900 | 88.2% |
| `assets/backgrounds/evacuation_point.png` | `assets/optimized/backgrounds/evacuation_point.webp` | 2.52 MiB | 0.35 MiB | 1536×1024 → 1536×864 | 86.0% |
| `assets/backgrounds/highway.png` | `assets/optimized/backgrounds/highway.webp` | 2.29 MiB | 0.28 MiB | 1536×1024 → 1536×864 | 87.7% |
| `assets/backgrounds/home_bedroom.png` | `assets/optimized/backgrounds/home_bedroom.webp` | 1.62 MiB | 0.11 MiB | 1672×941 → 1600×900 | 93.3% |
| `assets/backgrounds/hospital_emergency.png` | `assets/optimized/backgrounds/hospital_emergency.webp` | 1.83 MiB | 0.16 MiB | 1672×941 → 1600×900 | 91.3% |
| `assets/backgrounds/master_blackout_street.png` | `assets/optimized/backgrounds/master_blackout_street.webp` | 2.11 MiB | 0.23 MiB | 1672×941 → 1600×900 | 89.1% |
| `assets/backgrounds/metro_entrance.png` | `assets/optimized/backgrounds/metro_entrance.webp` | 2.28 MiB | 0.28 MiB | 1672×941 → 1600×900 | 87.7% |
| `assets/backgrounds/metro_maintenance_room.png` | `assets/optimized/backgrounds/metro_maintenance_room.webp` | 2.26 MiB | 0.29 MiB | 1672×941 → 1600×900 | 87.2% |
| `assets/backgrounds/metro_platform.png` | `assets/optimized/backgrounds/metro_platform.webp` | 2.07 MiB | 0.22 MiB | 1672×941 → 1600×900 | 89.5% |
| `assets/backgrounds/old_railway_station.png` | `assets/optimized/backgrounds/old_railway_station.webp` | 2.36 MiB | 0.30 MiB | 1536×1024 → 1536×864 | 87.1% |
| `assets/backgrounds/rooftops.png` | `assets/optimized/backgrounds/rooftops.webp` | 2.51 MiB | 0.33 MiB | 1536×1024 → 1536×864 | 86.9% |
| `assets/backgrounds/secret_lab_nightfall.png` | `assets/optimized/backgrounds/secret_lab_nightfall.webp` | 2.34 MiB | 0.32 MiB | 1536×1024 → 1536×864 | 86.3% |
| `assets/backgrounds/supermarket_exterior.png` | `assets/optimized/backgrounds/supermarket_exterior.webp` | 2.42 MiB | 0.34 MiB | 1672×941 → 1600×900 | 85.9% |
| `assets/backgrounds/supermarket_interior.png` | `assets/optimized/backgrounds/supermarket_interior.webp` | 1.99 MiB | 0.20 MiB | 1672×941 → 1600×900 | 89.7% |
| `assets/backgrounds/supermarket_supply_room.png` | `assets/optimized/backgrounds/supermarket_supply_room.webp` | 2.07 MiB | 0.22 MiB | 1672×941 → 1600×900 | 89.3% |
| `assets/items/batteries.png` | `assets/optimized/items/batteries.png` | 2.62 MiB | 0.38 MiB | 1536×1024 → 640×426 | 85.6% |
| `assets/items/chocolate_bar.png` | `assets/optimized/items/chocolate_bar.png` | 1.78 MiB | 0.29 MiB | 1672×941 → 640×360 | 83.5% |
| `assets/items/city_map.png` | `assets/optimized/items/city_map.png` | 3.05 MiB | 0.45 MiB | 1536×1024 → 640×426 | 85.4% |
| `assets/items/emergency_access_card.png` | `assets/optimized/items/emergency_access_card.png` | 2.36 MiB | 0.33 MiB | 1536×1024 → 640×426 | 85.9% |
| `assets/items/emergency_radio.png` | `assets/optimized/items/emergency_radio.png` | 2.61 MiB | 0.40 MiB | 1536×1024 → 640×426 | 84.7% |
| `assets/items/first_aid_kit_open.png` | `assets/optimized/items/first_aid_kit_open.png` | 2.69 MiB | 0.41 MiB | 1536×1024 → 640×426 | 84.6% |
| `assets/items/flashlight.png` | `assets/optimized/items/flashlight.png` | 2.01 MiB | 0.28 MiB | 1536×1024 → 640×426 | 86.2% |
| `assets/items/tool_kit.png` | `assets/optimized/items/tool_kit.png` | 2.78 MiB | 0.43 MiB | 1536×1024 → 640×426 | 84.5% |
| `assets/items/water_bottle.png` | `assets/optimized/items/water_bottle.png` | 2.47 MiB | 0.36 MiB | 1024×1536 → 426×640 | 85.4% |
| `assets/interactive/car.png` | `assets/optimized/interactive/car.png` | 2.41 MiB | 0.53 MiB | 1536×1024 → 768×512 | 78.0% |
| `assets/interactive/conveyor_box.png` | `assets/optimized/interactive/conveyor_box.png` | 2.60 MiB | 0.57 MiB | 1536×1024 → 768×512 | 78.2% |
| `assets/interactive/drone.png` | `assets/optimized/interactive/drone.png` | 1.92 MiB | 0.37 MiB | 1536×1024 → 768×512 | 80.8% |
| `assets/interactive/helicopter.png` | `assets/optimized/interactive/helicopter.png` | 1.35 MiB | 0.32 MiB | 1672×940 → 768×431 | 76.4% |
| `assets/interactive/phone.png` | `assets/optimized/interactive/phone.png` | 1.66 MiB | 0.35 MiB | 1536×1024 → 768×512 | 78.9% |
| `assets/collectibles/nightfall_core.png` | `assets/optimized/collectibles/nightfall_core.png` | 2.61 MiB | 0.59 MiB | 1536×1024 → 768×512 | 77.4% |
| `assets/collectibles/nightfall_field_notes.png` | `assets/optimized/collectibles/nightfall_field_notes.png` | 2.63 MiB | 0.86 MiB | 1145×1374 → 640×768 | 67.2% |
| `assets/collectibles/nightfall_medallion.png` | `assets/optimized/collectibles/nightfall_medallion.png` | 2.10 MiB | 0.79 MiB | 1278×1230 → 768×739 | 62.3% |
| `assets/collectibles/nightfall_processor.png` | `assets/optimized/collectibles/nightfall_processor.png` | 2.70 MiB | 0.60 MiB | 1536×1024 → 768×512 | 77.6% |
| `assets/collectibles/nightfall_usb.png` | `assets/optimized/collectibles/nightfall_usb.png` | 1.91 MiB | 0.35 MiB | 1536×1024 → 768×512 | 81.9% |
| `assets/achievements/explorer.png` | `assets/optimized/achievements/explorer.png` | 2.58 MiB | 0.72 MiB | 1312×1199 → 640×585 | 72.2% |
| `assets/achievements/grammar_master.png` | `assets/optimized/achievements/grammar_master.png` | 2.40 MiB | 0.73 MiB | 1254×1254 → 640×640 | 69.6% |
| `assets/achievements/master_collector.png` | `assets/optimized/achievements/master_collector.png` | 2.67 MiB | 0.81 MiB | 1254×1254 → 640×640 | 69.7% |
| `assets/achievements/speed_runner.png` | `assets/optimized/achievements/speed_runner.png` | 2.47 MiB | 0.69 MiB | 1312×1199 → 640×585 | 71.9% |
| `assets/achievements/unstoppable.png` | `assets/optimized/achievements/unstoppable.png` | 2.56 MiB | 0.70 MiB | 1300×1209 → 640×595 | 72.9% |
| `assets/achievements/untouchable.png` | `assets/optimized/achievements/untouchable.png` | 2.57 MiB | 0.72 MiB | 1286×1223 → 640×608 | 71.9% |
| `assets/sounds/underground.wav` | `assets/optimized/sounds/underground.mp3` | 8.32 MiB | 0.50 MiB | 2117 kbps → 128 kbps | 93.9% |
| `assets/sounds/danger.mp3` | `assets/optimized/sounds/danger.mp3` | 8.63 MiB | 4.32 MiB | 320 kbps → 160 kbps | 50.0% |
| `assets/sounds/exploration.mp3` | `assets/optimized/sounds/exploration.mp3` | 3.04 MiB | 1.90 MiB | 256 kbps → 160 kbps | 37.5% |
| `assets/sounds/final_escape.mp3` | `assets/optimized/sounds/final_escape.mp3` | 3.24 MiB | 2.02 MiB | 256 kbps → 160 kbps | 37.5% |

## Quality verification

- All 16 WebP files successfully decoded and reported valid dimensions.
- All 25 item/interactive/collectible PNGs and all 6 achievement PNGs successfully decoded.
- All 5 MP3 derivatives completed full FFmpeg decode checks without errors; duration was preserved within normal MP3 encoder padding tolerance.
- Alpha-state comparison found no source-to-derivative mismatches.
- The 3:2 backgrounds were center-cropped by 80 pixels at the top and bottom to 1536×864. They were not stretched or upscaled. Visual inspection confirmed that major roads, signs, exits, platforms, doors, rooftop access, and laboratory terminals remain visible.
- Representative WebP backgrounds showed no obvious compression artifacts at quality 92.
- Achievement badge text remained readable at the selected sizes; the Grammar Master badge was inspected at 640×640.

## Manual review

The corrected Chocolate Bar, Emergency Access Card, and Helicopter sources and derivatives now contain genuine alpha transparency and no baked checkerboard. All backgrounds should still receive a final in-game composition review. Audio files passed technical decode and duration checks, but a human listening comparison is recommended before deployment.

No UI assets, original assets, `.DS_Store` files, or game source files were changed.
