# BLACKOUT release preparation

Target: English-with-Svetlana/electricity_game. Publish the repository root.
Permanent Genially URL: https://English-with-Svetlana.github.io/electricity_game/

## Future releases

Install Node.js 18 or newer if necessary. In the project folder run:

```sh
node tools/prepare-release.mjs
```

Edit ordinary source files and assets normally. Never edit hashes manually.
Commit the generated index.html, style.css and release-assets.js along with changed
source/assets and .nojekyll in the separately authorized publishing phase.
The generator has no npm dependencies and uses paths relative to its own location.

Optional checks:

```sh
node tools/prepare-release.mjs --check --self-test
python3 tools/test-subpath.py
```

`--check` fails for missing or stale generated outputs. `--self-test` uses in-memory
copies with controlled byte changes; it never changes game artwork/audio/source.
Python 3 is needed only for the HTTP verification, not release preparation.

## Resource identities

Each canonical runtime file gets a relative URL with the first 20 hexadecimal
characters of its SHA-256 content digest, e.g. assets/.../file.webp?v=<digest>.
No asset bytes, names or dimensions change. No duplicate deployment directory,
service worker, runtime cache or remote service is added.

release-assets.js holds the generated URL map and loads before script.js.
The existing lossless image resolver first chooses the approved canonical WebP,
then applies its URL identity. The same resolver versions audio constants.
ASSETS, dynamic evidence/achievement paths and SECTION_ASSETS therefore use the
same URLs for preload, readiness and rendering. Directory roots stay relative
and unversioned. CSS URLs and HTML data-src use those same per-resource digests.

index.html references content hashes for script.js, generated style.css and
release-assets.js. A JS edit changes only the JS reference. A CSS edit changes
its stylesheet reference. An asset edit changes that asset's URL and the manifest
reference; CSS also changes if it refers to that asset. Unchanged large assets
retain their exact URLs. The stable entry page itself has no release suffix.
Regeneration is deterministic and independent of file modification times.

## Local verification on 2026-10-07

- 81 canonical image/audio files validated against the filesystem.
- All 20 section readiness groups validated against the generated URL map,
  including How to Play, routes, Rescue, checkpoint, evacuation, evidence,
  achievements, Nightfall and results.
- HTTP simulation served only /electricity_game/ from a temporary loopback server.
  Entry HTML, empty .nojekyll, all 81 assets and three JS/CSS resources returned
  successfully; all 84 resource response bodies matched their URL digests.
- Controlled A/B byte fixtures passed for script.js, style.css, one WebP and one
  MP3. Other asset URLs remained identical. Repeated generation was identical.
- JavaScript syntax check passed. All 41 approved lossless derivatives remain.
- No browser connection was available. Actual game loading, screen interactions,
  rendering/audio playback, a warm browser-cache A/B test and Genially iframe
  behavior remain unverified. HTTP and declarative resolver checks are not a
  substitute for those checks.

## Public repository review

No credential/token/private-key patterns, suspicious credential assignments,
environment credential files or absolute local machine paths were found in
project text/files. .git internals were excluded from the public-file audit.
This is a local pattern audit, not a guarantee about every historical commit.
Review the existing Git history before reusing it in a new public repository.

Nine .DS_Store files were found. Six are already tracked:

- .DS_Store
- assets/backgrounds/.DS_Store
- assets/interactive/.DS_Store
- assets/items/.DS_Store
- assets/reference/.DS_Store
- assets/sounds/.DS_Store

The other three are assets/.DS_Store, assets/ui/.DS_Store and
assets/optimized/.DS_Store. None were deleted or untracked. Ignore rules do not
exclude already tracked files: remove the six from the Git index before the
future public commit while retaining local copies if desired.

.gitignore now covers macOS/editor artifacts, environment files, logs, temporary
files, node_modules and Python cache directories. Runtime assets, generated
release-assets.js and .nojekyll are intentionally not ignored.

Recommendation B: keep the four PERFORMANCE_* reports locally and exclude them
from the public repository. They are internal snapshots/audits, include obsolete
resource inventories and baseline HTML, and are not needed to play or prepare a
release. They are currently untracked, now ignored and remain untouched on disk.
The release tool does not depend on them. Other existing master plans/artwork
remain; publishing the root makes committed documentation/source artwork publicly
accessible even though gameplay never requests master files.

Debug routes are gated by LOCAL_DEV_HOSTS (localhost and loopback addresses).
On GitHub Pages they do not activate, even with ?debug=game3, rescue,
rescue-signal, game10, game12 or ending. With no debug argument the existing
startup reaches normal START. Keeping the code is acceptable: it only controls
local in-memory review state, exposes no credentials and performs no privileged
remote action. No debug behavior was changed.

## Files changed by this preparation

Modified: .gitignore, index.html, script.js, style.css.
Created: .nojekyll, release-assets.js, tools/prepare-release.mjs,
tools/test-subpath.py, RELEASE_PREPARATION.md.

script.js changes are limited to URL resolution and canonical audio constants.
HTML/CSS changes are generated resource identities. Gameplay rules, grammar,
scoring, timing, audio gain, artwork/audio bytes and design were not edited.
Pre-existing modifications to gameplay/source/artwork and untracked optimized
assets were present at the start and were preserved.

## Remaining checks and next steps (not executed)

1. Finish browser QA under /electricity_game/, including START, How to Play,
   routes, supplies, Rescue, evidence, achievements, checkpoint, Final Evacuation,
   Nightfall and endings. Verify audio with a user gesture and the Genially iframe.
2. Check a real warm browser-cache A/B release. A previously cached HTML response
   or an already-open iframe cannot be forcibly refreshed by content hashing.
   The strategy guarantees fresh identities once the new entry HTML is obtained;
   it cannot override GitHub/Genially HTML caching or refresh an active session.
3. Review existing history and master documentation for intentional public sharing.
   Remove the six tracked .DS_Store entries from the index in the authorized commit
   phase; do not delete local artwork or optimization reports.
4. After separate approval, verify the new repository's initial branch/history.
   Set origin to https://github.com/English-with-Svetlana/electricity_game.git
   (git remote set-url origin ... if origin exists; git remote add origin ...
   otherwise). Confirm the destination before any push. Do not push to the old
   repository. Do not force-push if the new repository has existing commits.
5. Run node tools/prepare-release.mjs and the checks, review the exact staged
   files including all previously untracked runtime derivatives, then commit and
   push the intended main branch to the new repository. Authentication to that
   account must be valid; no credentials were changed in this preparation.
6. In the new repository's Settings > Pages, choose Deploy from a branch,
   branch main, folder /(root), and Save. See GitHub's official instructions:
   https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
7. Wait for the Pages build, verify the stable public URL and embed that URL in
   Genially. Future updates use the same preparation command and same page URL.

No commit, push, deployment, remote/account change or remote Pages activation
was performed. No interaction with the old remote was performed.
