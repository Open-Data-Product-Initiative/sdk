# Codex behavior for this repo

## SDK release version rule

Before editing `index.html`, `llms.txt`, install instructions, release wording,
capability copy, or SDK metadata:

1. Run the release checker:

   ```bash
   python3 .codex/check-sdk-release.py --write
   ```

2. Treat PyPI as the installable package source of truth for
   `open-data-products`.

3. Treat the latest GitHub release for
   `Open-Data-Product-Initiative/odp-agent-sdk` as the release-note/source
   consistency check.

4. If the latest version changed, update all relevant public surfaces in this
   repo:

   - `sdk-release.json`
   - `index.html`
   - `llms.txt`

5. Do not claim or write the latest SDK version without checking live PyPI and
   GitHub first.

6. If live checks fail, say that explicitly and do not guess.

7. Keep OKF described as an external Markdown/frontmatter context bundle format,
   not as a fifth Open Data Products standard.
