# Memory

<!--
  Agent-curated, not hand-authored. Hermes writes durable facts here over
  time (gated by config.yaml's write_approval setting). Stays under the
  memory_char_limit set in config.yaml (~2200 chars / ~800 tokens by default)
  because this file is loaded into every session's context — it competes for
  the same space as everything else, so it should only ever hold what's
  actually worth that cost: durable facts, not a running log.

  Leave this mostly empty at the start. If you want to seed it, keep entries
  short, dated, and about things that are true across sessions (a project
  convention, a standing constraint) — not things that belong in a single
  conversation's working memory instead.
-->
