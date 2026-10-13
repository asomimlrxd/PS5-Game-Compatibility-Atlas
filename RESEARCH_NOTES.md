# Research notes — first Atlas snapshot

Research cutoff: 13 October 2026. This is a working synthesis, not a full systematic review of every language, site or firmware.

## Key findings from the sources

### Format labels must not be treated as universal compatibility rankings

The ShadowMountPlus maintainer documents `.ffpkg`/UFS as the general recommendation, `.exfat` as a compatibility path for some titles, and PFS (`.ffpfs`/`.ffpfsc`) as experimental. The Atlas keeps this guidance separate from per-game observations because users report outcomes that do not always match the general recommendation. Source: [ShadowMountPlus documentation](https://github.com/drakmor/ShadowMountPlus).

### Test duration matters

The APR/M.2 community thread lists several titles as working in exFAT or `.ffpfsc`, but its author explicitly says that most games were only started and tested for a few minutes and may still crash later. The Atlas marks these as preliminary instead of treating the original post's “working” section as proof of completion. Source: [APR game tests on M.2 expansion storage](https://www.reddit.com/r/PS5_Jailbreak/comments/1u0j90p/list_of_some_tested_apr_games_as_exfat_format_or/).

### Contradictory results are evidence too

- **Wolverine:** one report describes desync, texture issues and crashes with a folder setup, while another user says they completed the game in LZ4. These are separate reports with different contexts, not proof that LZ4 always fixes the game. Source: [FW 13.60 megathread](https://www.reddit.com/r/PS5_Jailbreak/comments/1x0pduz/megathread_ps5_games_on_fw_1360/).
- **Saros:** the internal SSD thread contains positive `.ffpkg` reports and a separate user report of audio issues with one setup; a later 13.60 report describes a long session with minor stutters/texture issues. Source: [Internal SSD compatibility thread](https://www.reddit.com/r/PS5_Jailbreak/comments/1ttp7p6/internal_ssd_games_compatibility_list/) and [FW 13.60 megathread](https://www.reddit.com/r/PS5_Jailbreak/comments/1x0pduz/megathread_ps5_games_on_fw_1360/).
- **Demon's Souls Remake:** the 13.60 thread has reports of stutter/audio distortion/crashes with exFAT, worse behaviour with `.ffpfsc`, and black screens for folder/`.ffpkg` attempts in that user's tests. These are setup-specific reports; the Atlas does not infer that every format fails on every firmware.
- **Spider-Man 2:** results differ by firmware and external medium. In the APR/M.2 thread, an external HDD was described as nearly unplayable due to stutter, while a faster USB flash medium had a different outcome. A separate 13.00 report describes a black screen with a folder on an external SSD. Source: [APR game tests on M.2 expansion storage](https://www.reddit.com/r/PS5_Jailbreak/comments/1u0j90p/list_of_some_tested_apr_games_as_exfat_format_or/) and [FW 13.60 megathread](https://www.reddit.com/r/PS5_Jailbreak/comments/1x0pduz/megathread_ps5_games_on_fw_1360/).
- **Astro Bot:** two comments in the APR/M.2 thread disagree about `.ffpfsc`: one says it did not pass the first screen; another says it played well in a different, incompletely documented setup. Both remain visible as low-confidence reports.
- **Ghost Master Resurrection:** ShadowMountPlus issue #66 reports a kernel panic with an `.ffpfsc` filename containing parentheses, followed by a report that removing the parentheses allowed it to load. This is a particular historical issue, not a universal claim about PFS images. Source: [ShadowMountPlus issue #66](https://github.com/drakmor/ShadowMountPlus/issues/66).
- **Assassin's Creed Shadows:** issue #116 reports a crash with Dolby Atmos that disappeared with Linear PCM in the author's specific setup. That points to an audio-output interaction, not a conclusion about `.exfat` compatibility in general. Source: [ShadowMountPlus issue #116](https://github.com/drakmor/ShadowMountPlus/issues/116).

## How not to interpret the totals

The 83 records are not a random sample and are not statistically representative. They come from community threads and issues that tend to discuss either unusually successful or problematic setups. Therefore, the Atlas does **not** publish percentages such as “X% compatible” and does not rank file formats by a raw count of positive reports.

The unit being recorded is a **reported configuration**, not just a game. A game can have several records because firmware, version, image format, storage, payload version or test duration differs.

## Source register

The Sources & Methodology section in the site is the canonical source register for this snapshot. Each indexed source has a direct link, source type, date, and notes about what could and could not be concluded from it. The public Google Sheets linked from the community thread was not ingested cell-by-cell because the accessible text view did not expose the complete result grid; the Atlas records this limitation rather than importing unverifiable values.
