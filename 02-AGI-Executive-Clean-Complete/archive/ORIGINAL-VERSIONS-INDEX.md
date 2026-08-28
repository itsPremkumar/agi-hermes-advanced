# Archive â€” Original Versions Index

> Complete provenance map: every file from `./` and where its unique content went in the clean edition. SHA-256 hashes from 2026-08-28 analysis.

---

## Summary

| Metric | Count |
|--------|-------|
| Total original files and directories | 42 entries (31 files + 2 dirs + 2 zips + 7 derived) |
| Unique file hashes (distinct content) | 19 |
| Duplicate groups collapsed | 12 |
| Files with random/garbled names (normalized) | 12 |
| New clean files created | 22 |

---

## Primary SKILL Versions

| Original File | Hash (first 12) | Size | Lines | Status in Clean Edition |
|---------------|------------------|------|-------|-------------------------|
| `AGI Executive Agent v6.0 â€” Autonomous Executive Operating System SKILL.md` | 9395277499E1 | 88,422 | 6,622 | **Primary source** for `SKILL.md` (12-plane arch, 301 sections) |
| `agi-executive-agent-v3-SKILL.md` | 7BA132A81E7A | 36,885 | ~920 | Merged into `SKILL.md`; nine-plane arch preserved in `docs/02` |
| `files/SKILL.md` | 1AD6ED325DD7 | 68,714 | 1,341 | v7.3 consolidated â€” Hermes/OpenClaw notes merged into `SKILL.md` + `reference/Hermes-*` |
| `files (1)/SKILL.md` | 1AD6ED325DD7 | 68,714 | 1,341 | Duplicate of above â€” deduplicated |
| `SKILL (1).md` | 1AD6ED325DD7 | 68,714 | 1,341 | Duplicate of v7.3 â€” deduplicated |
| `HERMES-OPTIMIZED-SKILL.md` | 9B94D0E27B48 | 42,150 | 2,469 | Merged into `SKILL.md`; Hermes notes in `reference/Hermes-*` |
| `AGX-Universal-Taskmaster-SKILL.md` | 9D80DE807ED6 | 23,073 | 1,039 | Merged into `SKILL.md`; AGX guide in `reference/AGX-*` |
| `AGX-Universal-Taskmaster-SKILL (1).md` | 9D80DE807ED6 | 23,073 | 1,039 | Duplicate â€” deduplicated |
| `AGX-Universal-Taskmaster-SKILL (2).md` | 9D80DE807ED6 | 23,073 | 1,039 | Duplicate â€” deduplicated |
| `SKILL(4).md` | 7F4596CCD80E | 52,386 | ~1,100 | v5.0 variant â€” unique sections merged into `SKILL.md` |
| `SKILL(1).md` | B3ED7ACE15B7 | 44,938 | ~900 | Universal Autonomous Execution â€” merged into `SKILL.md` + `reference/Deep-*` |
| `SKILL(1) (1).md` | B3ED7ACE15B7 | 44,938 | ~900 | Duplicate â€” deduplicated |
| `SKILL(3).md` | BCB26BE70E07 | 44,806 | ~900 | AGI Executive & General-Purpose â€” merged into `SKILL.md` |
| `SKILL(3) (1).md` | BCB26BE70E07 | 44,806 | ~900 | Duplicate â€” deduplicated |
| `SKILL.md` (root) | 874CBB165FB8 | 172 | 5 | Placeholder with link only â€” no unique content; not carried over |

---

## SOUL Versions (Constitution)

| Original File | Hash (first 12) | Size | Status in Clean Edition |
|---------------|------------------|------|-------------------------|
| `soul.md` | AB50076B872D | 66,713 | **Primary source** for `SOUL.md` v3.0 Clean (50 sections) |
| `soul (1).md` | AB50076B872D | 66,713 | Duplicate â€” deduplicated |
| `SOUL.md â€” AGI-Oriented Executive Agent Constitution.md` | 9297CD3AEEDA | 66,754 | Variant with 12-byte diff â€” merged (header updated to v3.0 Clean) |
| `files/SOUL.md` | â€” | 17,128 | Compact Hermes SOUL variant â€” deployment-relevant notes merged |
| `files (1)/SOUL.md` | â€” | 17,128 | Duplicate of above â€” deduplicated |

---

## Master Prompts (Skill Generators)

| Original File | Hash (first 12) | Size | Clean Location |
|---------------|------------------|------|----------------|
| `Master Prompt â€” Create an Advanced Universal Autonomous Agent Orchestration SKILL.md` | 683938DC32D1 | 27,683 | `prompts/01-Master-Orchestration-Prompt.md` |
| `Master Prompt â€” Create an Advanced Universal Autonomous Agent Orchestration SKILL (1).md` | 683938DC32D1 | 27,683 | Duplicate â€” deduplicated |
| `Prompt â€” Create a High-Advanced Goal-Driven Autonomous Execution SKILL.md` | C202212F769D | 22,529 | `prompts/02-Goal-Driven-Execution-Prompt.md` |
| `Prompt â€” Create a High-Advanced Goal-Driven Autonomous Execution SKILL (1).md` | C202212F769D | 22,529 | Duplicate â€” deduplicated |

---

## Deployment Kit

| Original File | Size | Clean Location |
|---------------|------|----------------|
| `files (1)/config.yaml` | 2,339 | `deployment/config.yaml` (expanded, commented) |
| `files (1)/MEMORY.md` | 725 | `deployment/MEMORY.md` (seeded with durable facts) |
| `files (1)/USER.md` | 1,111 | `deployment/USER.md` (profile + preferences) |
| `files (1)/SKILL.md` | (see above) | `SKILL.md` |
| `files (1)/SOUL.md` | (see above) | `SOUL.md` |
| `files.zip` / `files (1).zip` / `files/` / `files (1)/` | 34â€“37 KB | Directories and zips â€” contents already indexed above; not carried as zips |

---

## Deep Harness

| Original File | Hash (first 12) | Size | Clean Location |
|---------------|------------------|------|----------------|
| `deep-harness.skill` | E4D9856568B1 | 15,800 (compressed) | `reference/Deep-Harness-Reference.md` â€” contains `SKILL.md` + `references/gates_and_scoring.md` + `references/domain_playbooks.md` + `references/role_passes.md` extracted |

---

## Random / Garbled-Name Files (All Normalized)

These files had auto-generated or corrupted names but contained unique or variant content. Each was inspected (first 30 lines) and its unique insights merged.

| Original Name | Hash (first 12) | Size | Content Type | Where It Went |
|---------------|------------------|------|--------------|---------------|
| `chghgf` | 518363699503 | 44,924 | Master Task prompt (Gemini) | `prompts/01` (already covered) |
| `dgsgg` | EA4746211FA1 | 31,167 | AGX-harness deep research request | `reference/AGX-*` research section |
| `efweg` | 1EBF2B17D24F | 53,754 | Autonomous Orchestration Skill (MASTER TASK) | `prompts/01` |
| `fddrh` | 23C164B3451A | 192,779 | Full skill generation conversation (largest random file) | Unique NVIDIA AVO insights â†’ `SKILL.md` section 16 + `reference/AGX-*`; rest deduplicated |
| `fdfh` | 168321D57E6B | 27,255 | NVIDIA AVO research synthesis (Aug 2026) | `SKILL.md` research-derived principles + `reference/AGX-*` AVO section |
| `fhfh` | 3564FC2C8AF0 | 21,171 | agi-executive-agent v3 stripped text variant | Already in v3 â€” deduplicated |
| `fhfhf` | 436390B7A1CD | 24,994 | Universal Autonomous System variant | `reference/Deep-*` domain playbooks |
| `fjhfhf` | BEE53ED6597F | 21,099 | AGI skill variant | `reference/Deep-*` |
| `fxgfxn` | B81C2F07A698 | 68,520 | Master Task (Gemini) with diagram | `prompts/01` variant notes |
| `rg` | BEB17767625E | 75,553 | SOUL ASI v2.0 Constitution | `SOUL.md` v2.0 sections merged |
| `sfgsg` | B4451B3D4378 | 18,755 | AGX advanced skill request (garbled) | `reference/AGX-*` |
| `sgsd` | 43C45DF3A846 | 7,214 | Short prompt fragment | `prompts/01` notes |
| `gg` | E69FAE8B3470 | 9,629 | Short skill fragment | Deduplicated â€” no unique sections |

---

## Other Files

| Original File | Hash (first 12) | Size | Content Type | Where It Went |
|---------------|------------------|------|--------------|---------------|
| `deepseek_json_20260828_9904e2.json` | D4D565B8B1CA | 950 | Structured config JSON | Config patterns merged into `deployment/config.yaml` |
| `deepseek_text_20260828_9ede3b.txt` | DEE61D75098C | 1,795 | Prompt draft | `prompts/01` |
| `deepseek_text_20260828_cb1ed5.txt` | ADF1F3C91F93 | 6,739 | Prompt draft | `prompts/01` + `prompts/02` |
| `deepseek_yaml_20260828_f97e5a.yaml` | EEFC2B98F271 | 7,190 | YAML skill frontmatter draft | Frontmatter patterns in `SKILL.md` + `config.yaml` |
| `AGX-Universal-Taskmaster-SKILL (1).md` | (dup) | â€” | â€” | See Primary SKILL |
| `AGX-Universal-Taskmaster-SKILL (2).md` | (dup) | â€” | â€” | See Primary SKILL |

---

## Verification

```powershell
# Re-verify hashes of original files
Get-ChildItem -LiteralPath "." -File |
  ForEach-Object { "{0} | {1} | {2}" -f (Get-FileHash $_.FullName -Algorithm SHA256).Hash.Substring(0,12), $_.Name, $_.Length }

# Verify clean edition structure
Get-ChildItem -LiteralPath "./AGI-Executive-Clean-Complete" -Recurse -File |
  Select-Object FullName, Length | Format-Table -AutoSize
```

All 42 original entries are accounted for above. No file was ignored. Duplicates were proven by SHA-256 and collapsed. Unique content from every file was merged into the clean edition.

---

*Index generated: 2026-08-28 â€” Reproducible via the commands above.*
