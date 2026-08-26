# BLACKOUT — Game Master Plan

> **Before modifying BLACKOUT, read this entire file and ASSET_AUDIT.md. After any approved major change, update GAME_MASTER_PLAN.md so future development can continue without relying on chat history.**

This file is the single source of truth for confirmed BLACKOUT gameplay, UI, progression, asset, and story decisions.

### Authority order

1. **Current working code and newer approved rules** are authoritative for implemented Games 1–5, the sequential route structure, Energy, Lives, Backpack, HUD, UI, audio, DEV mode, scoring, and current progression.
2. **`BLACKOUT_GRAMMAR_MASTER.md`** is the authoritative source for the originally approved grammar content and planned Games 1–12. It must remain in the repository unchanged as the original grammar/gameplay source.
3. Where the grammar master conflicts with the current implementation or newer approved rules, the current implementation/newer rule wins and the older rule is marked **SUPERSEDED** in this plan.
4. Future content is documented exactly as recovered. Route-dependent alternatives are not remapped into the newer sequential structure until explicitly approved.

## 1. Core game

- **Project name:** BLACKOUT
- **Format:** Browser-based educational survival and grammar game designed around a fixed, proportionally scaled 16:9 game viewport.
- **Persistent gameplay shell:** Shared HUD and shared gameplay architecture are reused across implemented games.
- **Lives:** Each normal question starts with 3 lives. Each wrong answer removes exactly 1 life. Reaching 0 lives launches the shared Emergency Rescue system. First Aid Kit is reserved for Lives, not Energy; no First Aid Kit consumption behavior is currently implemented.
- **Emergency Rescue:** Uses a fixed approved pool of 30 questions that must not be auto-generated. Each attempt randomly selects 5 unique questions, excluding all 5 questions used in the immediately previous attempt. At least 3 correct answers are required to continue. A failed rescue can be retried. Successful recovery behavior is adapted to the interrupted game.
- **Energy:** Starts at 100 and persists across questions, games, and routes. Correct answers cause no Energy loss. Every wrong normal-game answer removes exactly 5 Energy. Energy does not drain with time. At 0 Energy, gameplay is disabled until an available Energy supply is consumed; Water Bottle, Chocolate Bar, or Batteries restore Energy fully to the maximum of 100 and are removed from inventory. First Aid Kit is not an Energy item.
- **Score:** Every correct normal-game answer currently awards 100 points. Rescue answers do not award normal question points.
- **Timer:** Mission elapsed time starts when the mission begins and updates once per second.
- **Secrets:** Five persistent mission collectibles now drive the HUD from `0/5` through `5/5`. Each unique collectible can be collected once per mission and never enters the normal Backpack.
- **Backpack / inventory:** Four-slot inventory associated with Game 3 rewards: Water Bottle, First Aid Kit, Chocolate Bar, and Batteries. The HUD displays the collected count; the backpack popup displays collected and empty slots.
- **Route progression:** Sequential route map containing Service Tunnels, City Streets, and Main Bridge.
- **Project Nightfall:** The five collectible pickups, `5/5` confirmation, four-line decryption terminal, classified-file reveal, CASE SOLVED sequence, and single final MISSION COMPLETE flow are implemented.
- **Shared UI:** The current grammar games use the shared clean question panel at `assets/ui/question_panel_clean.png`; original UI artwork remains in `assets/ui/`.
- **Audio:** Exploration music begins after the initial user gesture. Ambience/music is lazy-started through the shared audio manager, with persistent music, SFX, and mute settings.

## 2. Current progression: Games 1–6

### Game 1 — Emergency Phone

- **Location / route:** Home Bedroom; the mission begins by interacting with the ringing emergency phone.
- **Grammar focus confirmed by question data:** Present Perfect, Past Simple, future with `will`, and Present Continuous in a blackout/emergency context.
- **Mechanic:** Four-option multiple choice using the shared A/B/C/D question-panel layout.
- **Questions / rounds:** 4.
- **Scoring:** +100 for each correct answer; maximum normal-question score is 400.
- **Energy effects:** Each wrong answer removes 5 energy. At 0, the shared energy-recovery overlay appears.
- **Life effects:** Each question resets to 3 lives; each wrong choice removes 1. At 0, Emergency Rescue begins.
- **Completion behavior:** Displays `SECURITY CHECK COMPLETE` / `GAME 1 COMPLETE`, then loads the Blackout Street transition and proceeds to Game 2 after the transition.
- **Important UI behavior:** Home scene includes a keyboard/clickable phone. Questions use the shared clean panel, shared answer slots, feedback, HUD, and per-question life reset.
- **Assets used:**
  - `assets/optimized/backgrounds/home_bedroom.webp`
  - `assets/optimized/interactive/phone.png`
  - `assets/ui/question_panel_clean.png`
  - shared HUD, life, feedback, inventory, rescue, and audio assets

### Game 2 — Street Signals

- **Location / route:** Blackout Street, before route selection.
- **Grammar focus confirmed by question data:** Present Simple, Present Continuous, Past Simple, and Present Perfect.
- **Mechanic:** Five four-option sentence-completion questions using the shared A/B/C/D panel.
- **Questions / rounds:** 5.
- **Scoring:** +100 for each correct answer; maximum normal-question score is 500.
- **Energy effects:** Each wrong answer removes 5 energy; shared energy recovery applies at 0.
- **Life effects:** Each question resets to 3 lives; each wrong choice removes 1. At 0, Emergency Rescue begins.
- **Completion behavior:** Displays `STREET SIGNALS COMPLETE` / `GAME 2 COMPLETE`, then transitions to the Supply Search introduction and Game 3.
- **Important UI behavior:** Long questions use the reusable centered question-sentence area. The Blackout Street background is dimmed behind the shared clean question panel. Internal `gameProgress` advances on successful normal questions and successful rescue substitution, although no separate question-panel counter is rendered.
- **Assets used:**
  - `assets/optimized/backgrounds/master_blackout_street.webp`
  - `assets/ui/question_panel_clean.png`
  - shared HUD, feedback, inventory, rescue, and audio assets

### Game 3 — Supply Search

- **Location / route:** Supermarket supply room, before route selection.
- **Grammar focus confirmed by question data:** Past Continuous, Present Perfect Passive, Past Perfect, and Present Simple Passive. The player supplies the complete verb form belonging in each blank.
- **Mechanic:** Typed-answer verb-form challenge. Input is normalized for case, surrounding whitespace, repeated spaces, and straight/curly apostrophes.
- **Questions / rounds:** 4.
- **Scoring:** +100 for each correct answer; maximum normal-question score is 400.
- **Energy effects:** Each wrong submission removes 5 energy; shared energy recovery applies at 0.
- **Life effects:** Each question resets to 3 lives; each wrong submission removes 1. At 0, Emergency Rescue begins.
- **Completion behavior:** Each completed question awards its linked supply. After all four supplies are secured, the game displays `SUPPLIES SECURED` / `GAME 3 COMPLETE` and opens Route Selection.
- **Important UI behavior:** Uses a text field and Check button over the shared panel. A `SUPPLY ACQUIRED` card appears; the item then shrinks, flies to the backpack center, fades, pulses the backpack, and updates the inventory counter. Successful rescue awards the interrupted question's supply and advances according to the existing rescue rules.
- **Rewards / assets used:**
  - Water Bottle — `assets/optimized/items/water_bottle.png`
  - First Aid Kit — `assets/optimized/items/first_aid_kit_open.png`
  - Chocolate Bar — `assets/optimized/items/chocolate_bar.png`
  - Batteries — `assets/optimized/items/batteries.png`
  - `assets/optimized/backgrounds/supermarket_supply_room.webp`
  - `assets/ui/question_panel_clean.png`
  - shared HUD, feedback, inventory, rescue, and audio assets

### Game 4 — Signal Scanner

- **Location / route:** Service Tunnels; first selectable route after Game 3.
- **Grammar focus confirmed by question data:** Present Perfect word order with `just`, Present Perfect Continuous with `for`, passive voice with a Past Simple time clause, and Present Perfect Passive with `already`.
- **Mechanic:** Choose the one grammatically correct complete sentence from four A/B/C/D options.
- **Questions / rounds:** 4.
- **Scoring:** +100 for each correct answer; maximum normal-question score is 400.
- **Energy effects:** Each wrong answer removes 5 energy; shared energy recovery applies at 0.
- **Life effects:** Each question resets to 3 lives; each wrong answer removes 1. At 0, Emergency Rescue begins.
- **Completion behavior:** Displays `SIGNAL RESTORED` / `SERVICE TUNNELS COMPLETE`, sets `serviceTunnelsCompleted = true`, and returns to Route Selection, where City Streets becomes available.
- **Important UI behavior:** Reuses the clean shared question panel and answer geometry. Game 4 applies shared per-question answer typography sizing so all four answers in a question use one size; Question 1 deliberately uses the same sizing reference as Question 2. Answers wrap within the widened text area to the right of the painted badges.
- **Assets used:**
  - `assets/optimized/backgrounds/metro_maintenance_room.webp`
  - `assets/ui/question_panel_clean.png`
  - shared HUD, feedback, inventory, rescue, and audio assets

### Game 5 — Error Detector

- **Location / route:** City Streets; unlocked after Service Tunnels is completed.
- **Grammar focus confirmed by question data:** Subject–verb agreement in Present Perfect Continuous, `yet` versus `already` in a negative Present Perfect sentence, Past Simple versus Present Perfect in a finished past event, and Past Simple with `ago`.
- **Mechanic:** The sentence is divided into four clickable phrase segments. The player selects the incorrect segment; on success, the corrected full sentence and correction are shown.
- **Questions / rounds:** 4.
- **Scoring:** +100 for each correct answer; maximum normal-question score is 400.
- **Energy effects:** Each wrong segment removes 5 energy; shared energy recovery applies at 0.
- **Life effects:** Each question resets to 3 lives; each wrong segment removes 1. At 0, Emergency Rescue begins. A successful rescue returns to the same Error Detector question under the current Game 5 rescue rule.
- **Completion behavior:** Displays `TRANSMISSION LOCATED` / `CITY STREETS COMPLETE`, sets `cityStreetsCompleted = true`, and returns to Route Selection, where Main Bridge becomes available.
- **Important UI behavior:** Uses the shared clean question panel with a Game-5-specific four-segment selection area. Correct feedback remains visible longer while the sentence changes to its corrected form.
- **Assets used:**
  - `assets/optimized/backgrounds/city_center.webp`
  - `assets/ui/question_panel_clean.png`
  - shared HUD, feedback, inventory, rescue, and audio assets

### Game 6 — Bridge Warning System

- **Location / route:** Main Bridge; entered after Service Tunnels and City Streets are completed in the current sequential route flow.
- **Approved variant:** Main Bridge Game 6 from `BLACKOUT_GRAMMAR_MASTER.md`. The Service Tunnels and City Streets Game 6 variants remain documented historical route alternatives and are not substituted into the current Main Bridge state.
- **Grammar focus:** Past Continuous with Past Simple Passive; Present Perfect with Present Simple; Past Perfect Passive with Past Simple; Present Perfect Continuous with Present Perfect Passive.
- **Mechanic:** Four physical warning-system modules. Each task embeds two typed verb-form controls in a bridge control console. A correct pair restores a module and advances the warning/barrier status.
- **Questions / rounds:** 4, using the exact approved Main Bridge Game 6 sentences and answers documented in Section 5.
- **Scoring:** +100 for each completed module; maximum normal-question score is 400.
- **Energy effects:** Correct pair costs 0 Energy. Each incorrect submission removes exactly 5 persistent Energy. The existing Energy recovery overlay and eligible inventory supplies are reused at 0.
- **Life effects:** Each module starts with 3 lives. Each incorrect submission removes 1 life. At 0, the existing Emergency Rescue opens; successful rescue returns to the same Game 6 module.
- **Completion behavior:** Displays `BRIDGE WARNING SYSTEM RESTORED ✓` / `GAME 6 COMPLETE`, followed by the next approved Main Bridge objective `ROOFTOP SIGNAL INTERCEPT`. Game 7 is not implemented and Main Bridge is not marked complete yet.
- **Important UI/animation behavior:** Cinematic bridge scene uses efficient CSS rain, fog/vignette, lightning, warning-light flicker, subtle background drift, module pulses, and physical status restoration. Removing the scene DOM through the shared `clearScreen()` cleanup removes the animation state without persistent animation loops or listeners. Reduced-motion rules remain supported.
- **Assets used:**
  - `assets/optimized/backgrounds/bridge.webp`
  - shared HUD, feedback, inventory, Energy recovery, Emergency Rescue, and audio assets
- **DEV shortcut:** `?dev=game6`, with optional current Energy override such as `?dev=game6&energy=10`; initializes completed prior routes and the four Game 3 inventory supplies.

### Game 7 — Rooftop Signal Intercept

- **Status:** IMPLEMENTED.
- **Location / route:** Main Bridge rooftops, immediately after Game 6.
- **Mechanic:** Four readable moving answer drones per question, with randomized flight lanes and varied speeds over efficient rain, fog, lightning, beacon, and distant-light effects.
- **Questions / rounds:** 4 fixed approved tasks. Correct answers lock one signal, award +100, and advance; wrong answers remain on the same task, remove 1 life and exactly 5 persistent Energy, and reuse existing recovery systems.
- **Completion behavior:** Displays `SIGNAL INTERCEPT COMPLETE ✓` / `EVACUATION CHANNEL ACQUIRED`, completes Main Bridge, and prepares `GAME 8 — RESTORE THE TIMELINE` without implementing Game 8.
- **Assets used:** `assets/optimized/backgrounds/rooftops.webp` and `assets/optimized/interactive/drone.png`.
- **DEV shortcut:** `?dev=game7`.

## 3. Route system

The current route sequence is strictly sequential:

1. **Service Tunnels**
   - Available immediately after Game 3.
   - Contains implemented Game 4 — Signal Scanner.
   - Completion sets `serviceTunnelsCompleted = true`.

2. **City Streets**
   - Locked until Service Tunnels is complete.
   - Contains implemented Game 5 — Error Detector.
   - Completion sets `cityStreetsCompleted = true`.

3. **Main Bridge**
   - Locked until City Streets is complete.
   - Becomes the final available route after Game 5.
   - Selecting it now enters the implemented Game 6 — Bridge Warning System.
   - Game 6 is completable, but Game 7 is not implemented, so Main Bridge is not yet marked complete.

### Current normal-play state at the implementation boundary

- Service Tunnels: implemented and completable.
- City Streets: implemented and completable.
- Main Bridge: unlockable/selectable; Game 6 is implemented, while later Main Bridge progression is not yet complete.
- An `ALL ROUTES COMPLETE` / `CITY NETWORK MAPPED` state exists for when all three completion flags are true, but current normal gameplay cannot reach it because Main Bridge still requires its later stage(s).

## 4. Confirmed future asset/mechanic sets — no game numbers assigned

These sets are confirmed by existing assets and their visible labels. Their final order, grammar content, and connection to Games 6–12 are not confirmed.

### A. Main Bridge set

- `assets/backgrounds/bridge.png`
- `assets/optimized/backgrounds/bridge.webp`
- `assets/interactive/car.png`
- `assets/optimized/interactive/car.png`
- `assets/items/city_map.png`
- `assets/optimized/items/city_map.png`
- `assets/items/tool_kit.png`
- `assets/optimized/items/tool_kit.png`
- Apparent concepts: damaged bridge route, vehicle/transport, navigation, repair or obstacle clearance.

### B. Railway / Train / Timeline set

- `assets/backgrounds/old_railway_station.png`
- `assets/optimized/backgrounds/old_railway_station.webp`
- `assets/backgrounds/metro_entrance.png`
- `assets/optimized/backgrounds/metro_entrance.webp`
- `assets/backgrounds/metro_platform.png`
- `assets/optimized/backgrounds/metro_platform.webp`
- Train imagery is embedded in the railway and metro backgrounds; no separate train sprite currently exists.
- `assets/ui/timeline_panel.png`
- Confirmed panel concept: **Timeline Challenge**, with three displayed timeline stages/rounds, three sentence areas, three tense selectors, and a Submit control.

### C. Moving Cargo / Blocks set

- `assets/interactive/conveyor_box.png`
- `assets/optimized/interactive/conveyor_box.png`
- Apparent concept: moving or selectable confidential cargo. The exact click, drag, sort, or avoidance interaction is not confirmed.

### D. Emergency Transmission set

- `assets/ui/emergency_transmission_panel.png`
- `assets/items/emergency_radio.png`
- `assets/optimized/items/emergency_radio.png`
- `assets/sounds/radio_static.mp3`
- `assets/sounds/countdown.wav`
- `assets/sounds/alarm.wav`
- `assets/sounds/warning.wav`
- Confirmed panel concept: timed three-gap grammar transmission challenge with signal status and a Submit Message control.

### E. Checkpoint / Access set

- `assets/backgrounds/hospital_emergency.png`
- `assets/optimized/backgrounds/hospital_emergency.webp`
- `assets/items/emergency_access_card.png`
- `assets/optimized/items/emergency_access_card.png`
- `assets/items/flashlight.png`
- `assets/optimized/items/flashlight.png`
- Apparent concepts: hospital emergency checkpoint, locked/access-controlled area, and dark-area exploration.

### F. Aerial / Moving Target set

- `assets/backgrounds/rooftops.png`
- `assets/optimized/backgrounds/rooftops.webp`
- `assets/interactive/drone.png`
- `assets/optimized/interactive/drone.png`
- `assets/interactive/helicopter.png`
- `assets/optimized/interactive/helicopter.png`
- Apparent concepts: rooftop surveillance, moving drone target, aerial arrival, or extraction. Exact mechanics are not confirmed.

### G. Final Survival / Extraction set

- `assets/backgrounds/highway.png`
- `assets/optimized/backgrounds/highway.webp`
- `assets/backgrounds/evacuation_point.png`
- `assets/optimized/backgrounds/evacuation_point.webp`
- `assets/interactive/helicopter.png`
- `assets/optimized/interactive/helicopter.png`
- `assets/sounds/final_escape.mp3`
- `assets/optimized/sounds/final_escape.mp3`
- `assets/ui/results_panel.png`
- Apparent concepts: highway escape, evacuation checkpoint, helicopter extraction, final escape sequence, and normal mission results.

### H. Project Nightfall / TRUE ENDING

- Secret location:
  - `assets/backgrounds/secret_lab_nightfall.png`
  - `assets/optimized/backgrounds/secret_lab_nightfall.webp`
- Five secret collectibles:
  1. Nightfall Core — `assets/collectibles/nightfall_core.png` and `assets/optimized/collectibles/nightfall_core.png`
  2. Nightfall Field Notes — `assets/collectibles/nightfall_field_notes.png` and `assets/optimized/collectibles/nightfall_field_notes.png`
  3. Nightfall Medallion — `assets/collectibles/nightfall_medallion.png` and `assets/optimized/collectibles/nightfall_medallion.png`
  4. Nightfall Processor — `assets/collectibles/nightfall_processor.png` and `assets/optimized/collectibles/nightfall_processor.png`
  5. Nightfall USB — `assets/collectibles/nightfall_usb.png` and `assets/optimized/collectibles/nightfall_usb.png`
- Unlock and discovery sounds:
  - `assets/sounds/nightfall_unlock.wav`
  - `assets/sounds/secret_found.wav`
- TRUE ENDING panel:
  - `assets/ui/nightfall_true_ending.png`
- Confirmed condition shown by the ending artwork: collecting all five secret items (`5/5`) unlocks the TRUE ENDING.
- Runtime placements are fixed as follows: Medallion in Home Bedroom, USB in Game 2 / Blackout Street, Processor in Game 4 / Service Tunnels, Field Notes in Game 6 / Main Bridge, and Core in Game 10 / Secret Laboratory.
- Collection state is stored in `state.collectedSecrets`; `state.secrets` mirrors its capped length for the persistent HUD. `secret_found.wav` plays for every unique pickup. The fifth pickup also plays `nightfall_unlock.wav` and displays `PROJECT NIGHTFALL — 5/5 SECRETS RECOVERED` without interrupting Game 10.
- After Game 12 evacuation completes, a `5/5` mission continues through the classified transmission, Nightfall decryption, classified reveal, CASE SOLVED, and final runtime results. Fewer than five secrets shows the approved incomplete-data fallback without creating another ending.

## 5. Originally approved Games 6–12

The exact approved grammar content below was recovered from `BLACKOUT_GRAMMAR_MASTER.md`.

### Structural status

- In the original master, a player chose one route and encountered route-specific Games 4–7. Therefore **Games 6 and 7 each have three approved route variants**.
- In the current implementation, routes are sequential: **Service Tunnels → City Streets → Main Bridge**. Games 4 and 5 use the current tested implementations, and Game 6 now uses the approved Main Bridge — Bridge Warning System variant.
- The approved Main Bridge Game 6 variant has now been selected for the current Main Bridge state. The remaining historical Game 6 alternatives and the final placement of Game 7 variants must not be combined, renumbered, or discarded without approval.
- Original Games 8–12 are shared after route convergence and are recovered without route ambiguity.
- Every recovered main game contains 4 tasks.

### Game 6 — approved route variants

#### Service Tunnels variant — Find the Mistake

- **Instruction:** `Find the mistake and correct it.`
- **Mechanic:** Select the incorrect phrase and provide/use its correction.
- **Rounds:** 4.

1. `We / have checked / the emergency generator / yesterday.`
   - Incorrect: `have checked`
   - Correct: `checked`
2. `The engineers / are working / on the power system / since 6 a.m.`
   - Incorrect: `are working`
   - Correct: `have been working`
3. `By the time / we entered the control room, / the backup generator / stopped.`
   - Incorrect: `stopped`
   - Correct: `had stopped`
4. `The damaged cables / repaired / two hours ago / by the maintenance team.`
   - Incorrect: `repaired`
   - Correct: `were repaired`

#### City Streets variant — Hospital Triage

- **Instruction:** `Complete both gaps with the correct verb forms.`
- **Location:** Hospital emergency area.
- **Mechanic:** Double-gap typed verb forms.
- **Rounds:** 4.

1. `The doctors ___ (treat) a patient when the emergency lights ___ (go) out.`
   - Accepted: `were treating / went`
2. `By the time the ambulance ___ (arrive), the doctors ___ already ___ (prepare) the emergency room.`
   - Accepted: `arrived / had already prepared`
3. `The medical team ___ (work) for six hours, and they ___ already ___ (help) more than fifty people.`
   - Accepted: `has been working / has already helped`
4. `Two patients ___ (bring) in an hour ago after a car ___ (crash) near the hospital.`
   - Accepted: `were brought / had crashed`

#### Main Bridge variant — Bridge Warning System

- **Instruction:** `Complete both gaps with the correct verb forms.`
- **Location:** Main Bridge warning/checkpoint stage.
- **Mechanic:** Double-gap typed verb forms.
- **Rounds:** 4.

1. `People ___ (cross) the bridge when the first warning ___ (send).`
   - Accepted: `were crossing / was sent`
2. `Sensors ___ (detect) a problem, but the bridge still ___ (look) stable.`
   - Accepted: `have detected / looks`
3. `The emergency barrier ___ already ___ (lower) when we ___ (reach) the checkpoint.`
   - Accepted: `had already been lowered / reached`
4. `Engineers ___ (study) the sensor data for an hour, but no safe route ___ (find) yet.`
   - Accepted: `have been studying / has been found`

### Game 7 — approved route variants

#### Service Tunnels variant — Conveyor Challenge

- **Instruction:** `Click the box with the correct answer.`
- **Mechanic:** Moving/selectable cargo boxes carrying answer choices.
- **Rounds:** 4.
- **Reward:** Flashlight.

1. `The emergency supplies ___ to the station right now.`
   - Options: `ARE BEING DELIVERED` / `ARE DELIVERING` / `HAVE BEEN DELIVERED` / `WERE DELIVERED`
   - Correct: `ARE BEING DELIVERED`
2. `The last supply train ___ before the blackout started.`
   - Options: `LEFT` / `HAS LEFT` / `HAD LEFT` / `WAS LEAVING`
   - Correct: `HAD LEFT`
3. `We ___ three emergency boxes so far.`
   - Options: `COLLECT` / `COLLECTED` / `ARE COLLECTING` / `HAVE COLLECTED`
   - Correct: `HAVE COLLECTED`
4. `The next emergency shipment ___ in twenty minutes.`
   - Options: `ARRIVES` / `ARRIVED` / `HAS ARRIVED` / `WILL ARRIVE`
   - Correct: `WILL ARRIVE`

#### City Streets variant — CCTV Search

- **Instruction:** `Use the time clues to complete each report.`
- **Mechanic:** Complete reports from CCTV/live-feed timestamps and time clues.
- **Rounds:** 4.

1. Clue: `CAM 01 — 21:15`
   - Sentence: `At 9:15 p.m., people ___ (run) out of the station.`
   - Accepted: `were running`
2. Clues: `21:20 — bridge warning received`; `21:25 — police arrived`
   - Sentence: `The bridge warning ___ (appear) before the police arrived.`
   - Accepted: `had appeared`
3. Clue: `LIVE FEED`
   - Sentence: `The police ___ just ___ (open) a new emergency route.`
   - Accepted: `have just opened`
4. Clue: `EVACUATION FORECAST`
   - Sentence: `Traffic on this road ___ (get) worse in the next hour.`
   - Accepted: `will get`

#### Main Bridge variant — Rooftop Signal Intercept

- **Instruction:** `Click the drone with the correct answer.`
- **Location:** Rooftops.
- **Mechanic:** Moving answer drones.
- **Rounds:** 4.

1. `A new evacuation point ___ near the river.`
   - Options: `HAS CREATED` / `WAS CREATING` / `HAS BEEN CREATED` / `IS CREATING`
   - Correct: `HAS BEEN CREATED`
2. `A rescue helicopter ___ over this building a few minutes ago.`
   - Options: `FLIES` / `IS FLYING` / `FLEW` / `HAS FLOWN`
   - Correct: `FLEW`
3. `Traffic ___ away from the bridge now.`
   - Options: `REDIRECTS` / `WAS REDIRECTED` / `HAS BEEN REDIRECTED` / `IS BEING REDIRECTED`
   - Correct: `IS BEING REDIRECTED`
4. `Keep the radio on. The rescue team ___ us when they are close.`
   - Options: `CONTACTS` / `CONTACTED` / `HAS CONTACTED` / `WILL CONTACT`
   - Correct: `WILL CONTACT`

### Game 8 — Restore the Timeline

- **Current status:** **IMPLEMENTED as Game 8 — TRAIN TIMELINE.** This newly approved implementation supersedes the older planned typed-answer description retained below for historical reference.
- **Current mechanic:** One locomotive plus four shuffled, slowly moving candidate wagons; the player drags 3 correct wagons into their required sentence order while 1 wagon is a distractor.
- **Wrong order / distractor:** The wagon is rejected and returned to the source track; existing Life, Energy, feedback, and recovery rules apply.
- **Task completion:** The railway signal turns green and the assembled train departs before the next of 4 fixed tasks begins. Direct development shortcut: `?dev=game8`.

- **Instruction:** `Use the timeline to complete the sentence.`
- **Mechanic:** Interpret ordered timestamps/events and type the required verb form or forms.
- **Rounds:** 4.
- **Associated confirmed asset:** `assets/ui/timeline_panel.png` visually provides three timeline event areas per displayed challenge; exact runtime composition still requires implementation decisions without changing the approved grammar.

1. Clues: `8:40 PM — Security guards left`; `8:55 PM — Blackout began`
   - Sentence: `The security guards ___ (leave) the station before the blackout began.`
   - Accepted: `had left`
2. Clues: `9:05 PM — Emergency message recorded`; `9:12 PM — Communication failed`
   - Sentence: `The emergency message ___ (record) before the communication system failed.`
   - Accepted: `had been recorded`
3. Clues: `10:00–10:30 — technicians repairing signal`; `10:15 — second power failure`
   - Sentence: `At 10:15, the technicians ___ (repair) the railway signal.`
   - Accepted: `were repairing`
4. Clues: `10:35 — rescue train departs`; `10:50 — we reach station`
   - Sentence: `By the time we ___ (reach) the station, the rescue train ___ (depart).`
   - Accepted: `reached / had departed`

### Game 9 — Emergency Radio

- **Current status:** **IMPLEMENTED.** Four staged transmissions use radio tuning, a slowly drifting frequency, shuffled channel selection, and final damaged-signal tuning before typed grammar restoration. Direct development shortcut: `?dev=game9`.

- **Instruction:** `Complete the missing part of each message.`
- **Mechanic:** Restore four radio messages/signals.
- **Rounds:** 4.
- **Completion text:** `4/4 SIGNALS RESTORED ✓`

1. `We have ___ three survivors near the river.`
   - Accepted: `found`
2. `The rescue boat ___ (move) along the river for the last forty minutes.`
   - Accepted: `has been moving`
3. `Another emergency shelter has ___ set up near the stadium.`
   - Accepted: `been`
4. `We ___ (send) your coordinates to the pilot as soon as we ___ (receive) your signal.`
   - Accepted: `will send / receive`
   - Required distinction: `as soon as we receive`, not `will receive`.

### Game 10 — Restore the Checkpoint

- **Current status:** **IMPLEMENTED.** Four sequential systems restore in the locked order `CAMERA → GATE → BEACON → ACCESS`, using mission-only Batteries, Tool Kit, beacon control, and Emergency Access Card interactions before the approved grammar challenges. Direct development shortcut: `?dev=game10`.

- **Structure:** Four modules in order: `CAMERA → GATE → BEACON → ACCESS`.
- **Rounds:** 4, using four different mechanics.
- **Completion text:** `CHECKPOINT RESTORED ✓`

1. **Camera — Find the Mistake**
   - Instruction: `Find the mistake and correct it.`
   - Display: `The security camera / isn't working since / the second power failure.`
   - Incorrect: `isn't working since`
   - Correct: `hasn't been working since`
   - Complete sentence: `The security camera hasn't been working since the second power failure.`
2. **Gate — Timeline / Type**
   - Instruction: `Type the correct verb form.`
   - Clues: `22:40 — guards lock gate`; `22:55 — communication fails`
   - Sentence: `The guards ___ (lock) the gate before communication failed.`
   - Accepted: `had locked`
3. **Beacon — Multiple Choice**
   - Instruction: `Choose the correct answer.`
   - Sentence: `A new emergency signal ___ from the rooftop right now.`
   - Options: `sends` / `has sent` / `was sent` / `is being sent`
   - Correct: `is being sent`
4. **Access — Double Gap**
   - Instruction: `Complete both gaps with the correct verb forms.`
   - Sentence: `The access code ___ (change) during the blackout, but we ___ just ___ (recover) the new one.`
   - Accepted: `was changed / have just recovered`

### Game 11 — Emergency Transmission

- **Current status:** **IMPLEMENTED.** Four fixed two-input grammar packets unlock 15-second transmission windows in which the moving helicopter must be clicked inside the active signal zone. Misses and reconnects carry no penalties; grammar errors reuse existing rules. Helicopter ambience is Game-11-local, loops at exactly `0.06`, and stops on Rescue/exit. Direct development shortcut: `?dev=game11`.

- **Instruction:** `Complete the message with the correct verb forms.`
- **Mechanic:** Timed/countdown transmission restoration with double-gap messages.
- **Rounds:** 4.
- **Completion text:** `SIGNAL LOCKED`; `COORDINATES TRANSMITTED`; `RESCUE HELICOPTER INBOUND`.
- **Associated assets:** `assets/ui/emergency_transmission_panel.png`, emergency radio, radio static, countdown, alarm, and warning sounds.

1. `We ___ (try) to contact you for the last twenty minutes, but we ___ (not/receive) a response yet.`
   - Accepted: `have been trying / haven't received`
2. `We ___ (cross) the railway tracks when our radio signal ___ (interrupt).`
   - Accepted: `were crossing / was interrupted`
3. Clues: `21:48 — beacon stops`; `21:55 — team reaches checkpoint`
   - Sentence: `The emergency beacon ___ (stop) working before our team ___ (reach) the checkpoint.`
   - Accepted: `had stopped / reached`
4. `Your coordinates ___ (send) to the pilot as soon as the system ___ (confirm) your location.`
   - Accepted: `will be sent / confirms`

### Game 12 — Final Survival Challenge

- **Current status:** **IMPLEMENTED.** Direct development shortcut: `?dev=game12`.
- **Location:** Evacuation Point.
- **Heading:** `FINAL EVACUATION CLEARANCE`
- **Instruction:** `Complete all four tasks to authorize evacuation.`
- **Mechanic:** Four selectable environmental stations with clearance progress `0 → 25 → 50 → 75 → 100%`. Passenger registration uses multiple choice; landing lights use a typed form and sequential light activation; the security gate uses mistake selection/correction and a separately animated barrier; the landing zone requires pointer dragging three obstacles outside the marked area before its double-gap task.
- **Rounds:** 4.
- **Completion:** `CLEARANCE 100%`; `FINAL CLEARANCE COMPLETE ✓`; `EVACUATION AUTHORIZED`; helicopter arrival and evacuation.
- **Associated assets:** `assets/backgrounds/evacuation_point.png`, passenger terminal, landing lights, split security-gate base/barrier, conveyor box obstacles, helicopter, and the existing quiet helicopter ambience at `0.03`.

1. **Choose**
   - Sentence: `All passengers ___ and are ready for evacuation.`
   - Options: `register` / `registered` / `are registering` / `have been registered`
   - Correct: `have been registered`
2. **Type**
   - Sentence: `The helicopter ___ (circle) above the evacuation zone for several minutes.`
   - Accepted: `has been circling`
3. **Find the Mistake**
   - Display: `The gates / will open / as soon as / the pilot will give / the signal.`
   - Incorrect: `the pilot will give`
   - Correct: `the pilot gives`
   - Complete sentence: `The gates will open as soon as the pilot gives the signal.`
4. **Double Gap**
   - Sentence: `Before the helicopter ___ (arrive), the landing zone ___ (already/clear).`
   - Accepted: `arrived / had already been cleared`

## 6. Recovered supplemental systems

### Originally planned Emergency Rescue rules

The five rescue questions and the `3/5` success threshold match the current implementation. The following older outcome rules conflict with the current code and are **SUPERSEDED**:

- **SUPERSEDED:** Success granted `+1 Life` and set Energy to 50.
- **SUPERSEDED:** Failure used an Alternative Safe Route plus a time penalty and continued automatically.
- **Current authoritative behavior:** Successful rescue follows the current per-game continuation rules without the older automatic Life/Energy assignment. Failed rescue shows mission failure and permits retrying Emergency Rescue.

### Project Nightfall — Secret Challenge

- **Unlock condition:** Only at `5/5` secret collectibles.
- **Title:** `DECRYPT THE NIGHTFALL FILE`
- **Instruction:** `Complete all four gaps to unlock the classified file.`
- **Penalty rule:** No Energy or Lives are removed in this challenge.
- **Interaction:** Correct fields turn green and lock; incorrect fields remain editable.

Approved classified text and answers:

1. `The city ___ (experience) several unexplained power failures before tonight.`
   - Accepted: `had experienced` — Past Perfect
2. `Our engineers ___ (investigate) the energy network for the last six months.`
   - Accepted: `have been investigating` — Present Perfect Continuous
3. `Several hidden devices ___ (just/discover) beneath the city.`
   - Accepted: `have just been discovered` — Present Perfect Passive
4. `We believe the evidence you collected ___ (help) us uncover the truth.`
   - Accepted: `will help` — Future Simple

After 4/4:

- `DECRYPTION 100%`
- `CLASSIFIED FILE UNLOCKED`
- Play `assets/sounds/nightfall_unlock.wav`
- Display `PROJECT NIGHTFALL — TRUE ENDING`
- Award `MASTER COLLECTOR`

The approved content is implemented as one four-row terminal. Correct rows lock independently and advance the classified reveal by 25%; wrong answers remain editable without Life or Energy penalties. Completing all four rows awards the confirmed `MASTER COLLECTOR` achievement, reveals the classified story, and proceeds to the single final mission-results screen.

## 7. Superseded master-plan conflicts

The following older master rules must not overwrite the current tested game:

- **Global count:** The master says every main mini-game has 4 tasks. Current Game 2 has 5 and remains unchanged.
- **Game 2:** The master has four different Street Signals questions, the instruction `Choose the correct signal.`, and completion `STREET NETWORK RESTORED`. Current five-question Game 2, current instruction, and current completion flow take priority.
- **Game 3:** The master includes `already` in the stated accepted answer for the First Aid Kit question. Current displayed two-blank sentence and accepted code answer `have been packed` take priority.
- **Game 4:** The master describes a Service Tunnels time-marker matching task followed by a random typed gap. Current tested Signal Scanner is a four-question correct-sentence multiple-choice game and takes priority.
- **Game 5:** The master defines three route-dependent Game 5 concepts: Moving Drones, Supermarket Security, and Repair the Car. Current tested Game 5 is City Streets — Error Detector and takes priority.
- **Routes:** The master says one player chooses one route and Games 4–7 depend on that route. Current sequential progression `SERVICE TUNNELS → CITY STREETS → MAIN BRIDGE` takes priority.
- **One-play total:** The master's 48-task total assumes one chosen route. It is not authoritative for the newer sequential route structure.
- **Emergency Rescue outcomes:** The older Life/Energy reset and Alternative Safe Route rules are superseded as documented above.
- **Energy:** Current persistent, non-time-draining Energy rules and exact `-5` wrong-answer cost take priority over any older or implied behavior.

## 8. Development log

### 2026-08-26

- Established `GAME_MASTER_PLAN.md` as the permanent single source of truth for major BLACKOUT decisions.
- Confirmed from current code that Games 1–5 are implemented.
- Confirmed that normal route progression currently completes Service Tunnels and City Streets, then reaches and unlocks Main Bridge.
- Confirmed that Main Bridge gameplay is not implemented yet.
- Audited and grouped existing future gameplay, location, item, interactive, audio, Project Nightfall, and ending assets without assigning unconfirmed game numbers.
- Initially recorded Games 6–12 as requiring recovery or confirmation.
- Read the complete 1,068-line `BLACKOUT_GRAMMAR_MASTER.md` and established it as the authoritative original grammar/gameplay source beneath the current tested implementation and newer approved rules.
- Recovered and documented the exact approved Games 6–12 questions, answers, instructions, mechanics, and completion concepts.
- Preserved the unresolved mapping of the three route-specific Game 6 and Game 7 variants rather than guessing how they fit the newer sequential route order.
- Recorded all identified conflicts with current Games 1–5, sequential routes, Energy, and Emergency Rescue as superseded older rules.
- Implemented current Game 6 — Bridge Warning System as the approved Main Bridge route variant, with four exact double-gap grammar tasks, current global penalties/recovery, cinematic bridge effects, route entry, completion handoff, and `?dev=game6` testing support.
- Implemented Main Bridge Game 7 — Rooftop Signal Intercept with four locked moving-drone tasks, existing penalties/recovery, Main Bridge completion, Game 8 handoff, and `?dev=game7` testing support.
- Implemented the five Project Nightfall environmental collectibles with persistent per-mission duplicate-safe state, HUD `0/5` integration, shared pickup presentation, pickup/unlock sounds, fixed scene placements, and DEV scene histories; the Nightfall challenge and TRUE ENDING remain deliberately unlaunched.
- Implemented the post–Game 12 Project Nightfall ending flow, including the classified transition, one-screen four-line decryption challenge, progressive file decoding, classified story, CASE SOLVED moment, actual Score/Time results, earned-only achievement display, complete PLAY AGAIN reset, and `?dev=nightfall` / `?dev=ending` shortcuts.
- Updated Nightfall line 3 and its decoded story to the approved plural-device wording; the complete classified file now remains visible until CONTINUE, and the final results use the cinematic evacuation background with expanded statistics and achievement presentation.
- Refined the classified-file reveal into a centered futuristic terminal with a 6–8 second character-by-character report, blinking cursor, delayed CONTINUE control, and the five evidence assets arranged systematically around—but never over—the terminal.
- Added duplicate-safe fallback opportunities for missed Nightfall IDs: Medallion in Game 2, USB in Game 4, Processor in Game 6, Field Notes in Game 10, and every still-missing ID in Game 12. Game 12 departure now waits at `PROJECT NIGHTFALL SIGNAL DETECTED` until the player clicks the remaining visible secrets; nothing is awarded automatically.

## 9. Continuity rule

Before starting any future BLACKOUT task:

1. Read this entire file.
2. Read `ASSET_AUDIT.md`.
3. Read `BLACKOUT_GRAMMAR_MASTER.md` when working on grammar content or planned Games 6–12.
4. Preserve confirmed locked gameplay and UI architecture unless an explicit approved request changes it.
5. After any approved major gameplay, UI, progression, asset, or story change, update this file in the same development step.
6. Record only confirmed decisions; label unresolved material clearly instead of guessing.
