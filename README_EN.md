# PS5 Game Compatibility Atlas — English

The **PS5 Game Compatibility Atlas** organizes public reports about PS5 games in homebrew environments, cross-referencing firmware, format, storage, symptoms, test scope, and original sources.

## Run locally

From the project directory, run:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`. The site does not require a remote API or database.

## Included in this version

- 83 test reports across 46 game/title names.
- 18 public sources and 7 format guides.
- Search and filters by firmware, format, storage, and reported state.
- Portuguese (Portugal) and English, a dark theme, and responsive layout.
- Direct links to original sources; no game-download links are hosted.
- Local contribution form: records stay in the browser and can be exported as JSON. They are not sent to a server.
- Export curated reports as CSV or JSON.

## Interpreting results

Each record describes one setup and one observation; it does not establish universal compatibility. A short test is not a completed playthrough, and conflicting reports remain separate. Evidence quality describes how well a report is documented, not a statistical probability of success.

Current ShadowMountPlus documentation recommends `.ffpkg`/UFS for general use, describes `.exfat` as a compatibility option for some titles, and labels PFS (`.ffpfs`/`.ffpfsc`) experimental. Per-game reports may differ from these maintainer notes.

Read `METHODOLOGY.md` for source scope and limitations and `CONTRIBUTING.md` before adding data.
