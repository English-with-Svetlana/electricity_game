# BLACKOUT --- Revised Game Flow

## Purpose

This document is the reference plan for the revised **BLACKOUT** game
flow.\
Use it as the source of truth when editing `script.js` and related
project files.

The goal is to shorten the game, remove repetitive intermediate screens,
preserve the strongest mechanics, and make the route from **START** to
**MISSION COMPLETE** clearer.

------------------------------------------------------------------------

## Core mechanics to keep

-   **Lives** --- 3 tries; a wrong answer costs 1 life.
-   **Energy** --- decreases as the player travels/progresses.
-   **Backpack** --- supplies collected in Supply Search can restore
    Energy.
-   **Evidence / Project Nightfall** --- collect 5 secret items to
    unlock the classified finale.
-   **Score / streak** may remain, but it is not a central mechanic.
-   Do **not** deduct Energy for wrong answers. Lives and Energy should
    remain separate systems.

------------------------------------------------------------------------

## START

Player starts the game and sees the simplified **HOW TO PLAY** screen.

It explains only:

-   **LIVES:** You have 3 tries. Wrong answer = lose 1 life.
-   **ENERGY:** Your energy goes down as you travel.
-   **BACKPACK:** Collect supplies. Use them to restore energy.
-   **EVIDENCE:** Find 5 secret items to uncover the truth.

Bottom objective:

> COMPLETE THE CHALLENGES AND REACH THE EVACUATION POINT!

### Remove

Remove the old 3-round memory mini-game at the beginning.\
After the opening/phone sequence, move directly into the main grammar
quest.

------------------------------------------------------------------------

## GAME 1 --- Emergency Phone

Keep the current **4 grammar tasks**.

After completion, remove `GAME 1 COMPLETE`.

Show only:

> EVACUATION ROUTE RECEIVED ✓

Then continue to Blackout Street.

------------------------------------------------------------------------

## GAME 2 --- Blackout Street / Street Signals

Intro:

> BLACKOUT STREET\
> Restore the street signals to continue.

Keep the current Street Signals mechanic and require **4 successful
tasks**.

Completion:

> STREET POWER RESTORED ✓

Remove repeated messages such as:

-   `GRID POWER 100%`
-   `STREET NETWORK RESTORED`
-   `GAME 2 COMPLETE`

Keep the relevant Project Nightfall evidence.

------------------------------------------------------------------------

## GAME 3 --- Supply Search

Intro:

> SUPPLY SEARCH\
> Collect 4 emergency supplies.\
> Use them later to restore your energy.

Keep the four supplies:

-   Water Bottle
-   First Aid Kit
-   Chocolate Bar
-   Batteries

They go into the Backpack.

Completion:

> SUPPLIES SECURED ✓

### Energy depletion

When Energy reaches 0:

> NO ENERGY!\
> Open your backpack and choose a supply.

The player chooses one collected, unused supply.\
That supply restores Energy to 100% and cannot be used again.

------------------------------------------------------------------------

## EVACUATION ROUTE MAP

The new `route_selection` image is **not a route-choice screen**.

It is an informational progress map:

> HOME ✓ → 1 SERVICE TUNNELS → 2 CITY CENTER → 3 MAIN BRIDGE → 4 RESCUE
> ZONE → 5 EVACUATION POINT

Remove the old logic that makes this screen appear to offer three
selectable routes.

------------------------------------------------------------------------

## GAME 4 --- Service Tunnels

Intro:

> SERVICE TUNNELS\
> Find the correct route.

Keep the current **4 tasks**.

Completion:

> ROUTE FOUND ✓

Keep the relevant Nightfall evidence.

------------------------------------------------------------------------

## GAME 5 --- City Streets / Error Detector

Intro:

> CITY STREETS\
> Trace the emergency transmission.

Keep the current Error Detector mechanic and **4 tasks**.

Completion:

> TRANSMISSION LOCATED ✓

Do not show `GAME 5 COMPLETE`.

------------------------------------------------------------------------

## GAME 6 --- Main Bridge

Intro:

> MAIN BRIDGE\
> Final ground sector. Restore the warning system.

Keep the current **4 tasks**, including the tasks that use two forms.

Completion:

> BRIDGE SYSTEM RESTORED ✓

Keep the relevant Nightfall evidence.

------------------------------------------------------------------------

## GAME 7 --- Rooftop Signal / Drone Intercept

Keep the current mechanic and **4 tasks**.

Completion:

> EVACUATION CHANNEL ACQUIRED ✓

Remove redundant completion/status screens.

------------------------------------------------------------------------

## GAME 8 --- Train Timeline

Keep the current Train Timeline / wagon mechanic and **4 tasks**.

After completion, do **not** show `MISSION COMPLETE`.

Replace the current long completion sequence with:

> RAILWAY ROUTE BLOCKED ⚠\
> Emergency radio signal detected.

Then continue directly to Emergency Radio.

------------------------------------------------------------------------

## GAME 9 --- Emergency Radio + Rescue Signal

Keep the current **4 Emergency Radio tasks**.

### Merge old Game 11 into this section

Remove the old separate **Game 11 --- Emergency Transmission** as an
independent game.

After the radio channel is restored, reuse its useful
helicopter/signal-zone mechanic here.

The helicopter appears and the player completes the signal interaction.

Completion:

> COORDINATES TRANSMITTED ✓\
> RESCUE HELICOPTER INBOUND

Do not create another full grammar block for old Game 11.

------------------------------------------------------------------------

## GAME 10 --- Restore Checkpoint

Intro:

> RESTORE THE CHECKPOINT\
> The rescue signal leads through a checkpoint linked to Project
> Nightfall.

Progress:

> CAMERA → GATE → BEACON → ACCESS

Keep the existing **4 tasks** and varied interactions.

Completion:

> CHECKPOINT RESTORED ✓

Keep the Nightfall Core/evidence.

Then continue toward Final Evacuation.

------------------------------------------------------------------------

## FINAL EVACUATION --- former Game 12

Intro:

> EVACUATION POINT\
> Prepare the systems for helicopter extraction.

Label:

> FINAL EVACUATION

Keep the four existing stages:

1.  REGISTER PASSENGERS
2.  LANDING LIGHTS
3.  SECURITY GATE
4.  LANDING ZONE

Do not call this `Game 12` in player-facing completion messages.

------------------------------------------------------------------------

## LIVES AND EMERGENCY RESCUE

Keep **3 Lives**.

A wrong answer costs 1 life.

When all lives are lost, replace the current 5-question rescue sequence with:

> EMERGENCY RESCUE  
> No lives left!  
> Answer one question correctly to continue.

### Important

Emergency Rescue must contain **exactly ONE extra grammar question/sentence at a time**.

- Correct answer → restore Lives and SKIP the failed main-quest task for progression. Advance exactly one task using the current block’s normal progression path; if it was the last task, close the block and continue to its normal next destination.
- Neither the skipped task nor Rescue awards normal score, correct-answer credit, first-attempt credit, or accuracy credit. Main-task mistakes remain in the statistics.
- Supply Search skips do not award supplies. Track missed supplies separately; if a later mandatory Energy recovery has no usable supplies, allow explicit recovery of one missed supply, followed by its normal Backpack use. This fallback prevents a dead end without grammar credit or an automatic Rescue reward.
- Final Evacuation skips resolve the active station for prerequisites and authorization, record it as Rescue clearance, and preserve missing-Evidence fallback; they do not award grammar credit.
- Focused checks must cover non-final and final skips, wrong Rescue retries, unchanged score/accuracy, single advancement, missed-supply recovery, and final-station authorization with missing Evidence.
- If the Rescue answer is wrong, do **not** start a 5-question test and do not end the game. Show another single Rescue sentence/question and keep the player in Emergency Rescue until one Rescue question is answered correctly.
- Remove the old 5-question Rescue.
- Remove the `3/5` requirement.
- Do not create another long rescue test.
- Do not deduct additional Energy for wrong answers.

---

## PROJECT NIGHTFALL / EVIDENCE

Keep **5 evidence items** and the existing fallback/respawn logic so a missed item cannot permanently block completion.

The player must never reach a dead end because an earlier evidence item was missed. Before the Nightfall Finale, the fallback logic must guarantee a real opportunity to obtain every missing evidence item and reach **5/5**. Preserve this behavior when removing or merging stages, especially when old Game 11 is removed.

First evidence message:

> SECRET EVIDENCE FOUND — 1/5  
> Find all 5 to unlock Project Nightfall.

Later evidence messages should be short:

> NIGHTFALL EVIDENCE FOUND — 2/5

Continue similarly for 3/5, 4/5 and 5/5.

Remove the long explanatory story messages after every evidence item.

If evidence is incomplete near the finale:

> PROJECT NIGHTFALL: 4/5  
> Find the missing evidence to unlock the classified file.

The game must then use the preserved fallback/respawn mechanism to give the player a real chance to collect the missing evidence. Do not allow the player to become stuck at this point.

When all five are collected:

> PROJECT NIGHTFALL UNLOCKED ✓

---

## PROJECT NIGHTFALL FINALE

Reduce the current Nightfall decryption from **4 grammar questions to
1**.

Use:

> We believe the evidence you collected \_\_\_ (help) us uncover the
> truth.

Correct answer:

> will help

Remove the old 0% / 25% / 50% / 75% / 100% multi-question progression.

After the correct answer, show a short Project Nightfall reveal and
proceed to the real ending.

Remove unnecessary intermediate screens such as repeated:

-   `CASE SOLVED`
-   `CLASSIFIED FILE UNLOCKED`
-   extra `CONTINUE` screens
-   duplicate completion announcements

------------------------------------------------------------------------

# MISSION COMPLETE

`MISSION COMPLETE` must appear **only once in the entire game**, at the
true ending after Final Evacuation and the Project Nightfall conclusion.

It must not appear after Train Timeline or any earlier stage.

------------------------------------------------------------------------

## General transition cleanup

Throughout the game:

-   Remove `GAME N COMPLETE` messages.
-   Remove repeated status screens when the next screen already
    communicates the result.
-   Remove unnecessary `NEXT OBJECTIVE` screens.
-   Prefer one short, story-relevant completion message per section.
-   Preserve the existing core mechanics unless this document explicitly
    says to change them.

------------------------------------------------------------------------

## Expected revised workload

Final target structure:

- **10 main gameplay blocks**
- **Final Evacuation** (the former Game 12), with its 4 existing stages
- **1 Nightfall decryption question**

The main gameplay blocks keep their agreed task structure unless this plan explicitly says otherwise.

Approximate mandatory grammar workload:

> **45 tasks instead of the previous ~53**

This keeps the game substantial while reducing repetition and fatigue.

---

# ASSET / OPTIMIZATION REQUIREMENTS

The user has **already replaced** these PNG files in the working
project:

-   `assets/ui/how_to_play.png`
-   `assets/ui/route_selection.png`

Do **not** restore or overwrite them with the old PNG versions.

The project also contains optimized WebP duplicates.

When implementing the revision:

1.  Take the **new PNG files currently present** in `assets/ui/`.
2.  Regenerate optimized WebP versions from those new PNGs.
3.  Replace:
    -   `assets/optimized/ui/how_to_play.webp`
    -   `assets/optimized/ui/route_selection.webp`
4.  Keep the `assets/optimized/` directory.
5.  Do not restore the old artwork.
6.  Verify that the game displays the new artwork after the optimized
    files are regenerated.

------------------------------------------------------------------------

## Implementation safety

When editing the project:

-   Preserve unrelated working mechanics, assets, audio, transitions and
    styles.
-   Do not rewrite the entire project unnecessarily.
-   Make only the changes required by this plan.
-   After implementation, run/build the game and test the complete flow
    from START to MISSION COMPLETE.
-   Check that there are no dead buttons, unreachable stages, old Game
    11 references, duplicate completion screens, or broken
    evidence/energy/lives logic.
