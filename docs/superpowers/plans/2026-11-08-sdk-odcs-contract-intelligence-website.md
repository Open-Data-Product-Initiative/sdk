# SDK ODCS and Data Contract Intelligence Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the verified Open Data Products SDK 0.6.5 ODCS-to-ODPS and Data Contract Intelligence workflows to the homepage, reference guide, and agent-facing guide without overstating automation.

**Architecture:** The repository is a static HTML website with a root landing page, a small static documentation set, and a root-level `llms.txt` guide. Keep the capability wording and exact CLI commands aligned across each surface. Add a standard-library regression test that rejects missing commands or an unsafe claim that contract intelligence creates or approves products automatically.

**Tech Stack:** Static HTML, plain text, JSON metadata, Python standard-library `unittest`, Git.

---

### Task 1: Add a copy-regression test before changing public content

**Files:**
- Create: `tests/test_sdk_capability_copy.py`
- Test: `tests/test_sdk_capability_copy.py`

- [ ] **Step 1: Write the failing test for the ODCS wrapper claim**

```python
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CapabilityCopyTests(unittest.TestCase):
    def test_odcs_wrapper_command_and_boundary_are_public(self):
        expected = (
            "open-data-products product wrap-contract --input contract.yaml "
            "--output product.yaml"
        )
        for filename in ("index.html", "docs/reference.html", "llms.txt"):
            content = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn(expected, content, filename)
            self.assertIn("validated ODPS 4.2 draft", content, filename)
```

- [ ] **Step 2: Run the test to confirm the existing website fails**

Run: `python3 -m unittest tests/test_sdk_capability_copy.py -v`

Expected: FAIL because the `wrap-contract` command and validated-draft wording are not yet on every required surface.

- [ ] **Step 3: Extend the test with the Data Contract Intelligence safeguards**

```python
    def test_contract_intelligence_command_report_and_review_boundary_are_public(self):
        expected = (
            "open-data-products portfolio discover-contracts ./contracts "
            "--output ./portfolio-discovery --json"
        )
        for filename in ("index.html", "docs/reference.html", "llms.txt"):
            content = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn(expected, content, filename)
            self.assertIn("offline HTML report", content, filename)
            self.assertIn("does not automatically create or approve data products", content, filename)
```

- [ ] **Step 4: Commit the red test**

```bash
git add tests/test_sdk_capability_copy.py
git commit -m "test: cover SDK contract capability copy"
```

### Task 2: Add the two release workflows to the landing page

**Files:**
- Modify: `index.html:7-19`
- Modify: `sdk-release.json:1-12`
- Modify: `index.html:1680-1683`
- Modify: `index.html:1732-1771`
- Modify: `index.html:1775-1835`

- [ ] **Step 1: Refresh the required release metadata**

Run: `python3 .codex/check-sdk-release.py --write`

Expected: PyPI `0.6.5`, GitHub `v0.6.5`, and `Versions match: True`; retain the refreshed `sdk-release.json` in the final website commit.

- [ ] **Step 2: Update homepage discovery copy without changing the product promise**

Add `ODCS-to-ODPS drafting` and `Data Contract Intelligence` to the description, keywords, Open Graph description, Twitter description, hero lead, and capability overview. Use these factual boundaries verbatim where the copy describes intelligence:

```text
evidence-backed Data Contract Intelligence with an offline HTML report and review-only opportunities
```

Do not describe the report as a dashboard or graph editor. Do not state that it creates or approves a data product.

- [ ] **Step 3: Keep all six existing example cards and append the ODCS draft card**

Append this card after the existing generation card:

```html
<article class="example-card">
  <small>Contract to product</small>
  <h3>Draft ODPS from an ODCS contract</h3>
  <p>Wrap ODCS 3.0, 3.1, and 3.2 contracts into a validated ODPS 4.2 draft. AI enrichment is optional; the command does not approve or publish a data product.</p>
<pre>open-data-products product wrap-contract --input contract.yaml --output product.yaml</pre>
</article>
```

- [ ] **Step 4: Append the Data Contract Intelligence card**

Append this card after the existing portfolio-workspace card so all current examples remain visible:

```html
<article class="example-card">
  <small>Data Contract Intelligence</small>
  <h3>Discover contract intelligence</h3>
  <p>Inventory local ODCS contracts, surface evidence-backed duplicates, gaps, overlaps, and review-only opportunities, then export structured results and an offline HTML report. It does not automatically create or approve data products.</p>
<pre>open-data-products portfolio discover-contracts ./contracts --output ./portfolio-discovery --json</pre>
</article>
```

- [ ] **Step 5: Run the focused regression test**

Run: `python3 -m unittest tests/test_sdk_capability_copy.py -v`

Expected: both tests still fail because the reference guide and `llms.txt` have not yet been updated; the homepage now satisfies its share of each assertion.

### Task 3: Align the reference guide and agent-facing guide

**Files:**
- Modify: `docs/reference.html:7, 53, 109-121`
- Modify: `docs/index.html:55-80`
- Modify: `llms.txt:5-31, 109-140`

- [ ] **Step 1: Add two focused reference-guide subsections**

Before the existing product-contract command list, add an ODCS wrapper subsection with this command and boundary:

```text
open-data-products product wrap-contract --input contract.yaml --output product.yaml

This writes a validated ODPS 4.2 draft. Optional enrichment adds proposals;
it does not approve or publish a data product.
```

Add a Data Contract Intelligence subsection with this command and outcome:

```text
open-data-products portfolio discover-contracts ./contracts --output ./portfolio-discovery --json

The output includes structured evidence and an offline HTML report. Opportunities
are review-only: the workflow does not automatically create or approve data products.
```

Keep the existing `open-data-products[contracts]` adapter instructions and product-level contract commands below the new subsections.

- [ ] **Step 2: Extend `llms.txt` across its capability, use-case, and CLI sections**

Add these exact command lines to the `Common workflows` block:

```text
open-data-products product wrap-contract --input contract.yaml --output product.yaml
open-data-products portfolio discover-contracts ./contracts --output ./portfolio-discovery --json
```

In the Data Contracts capability and `Use This For` lists, state that the SDK can draft a validated ODPS 4.2 product from ODCS 3.0–3.2 and can produce Data Contract Intelligence with an offline HTML report. Include this exact guardrail:

```text
It does not automatically create or approve data products.
```

- [ ] **Step 3: Add the how-to entry point**

Add a `Data Contract Workflows` card to `docs/index.html` that links to
`reference.html#data-contract-workflows` and tells readers that the reference
guide covers ODCS-to-ODPS drafting and evidence-backed contract intelligence
with an offline HTML report. Do not repeat the command block on this overview
page.

- [ ] **Step 4: Run the regression test and static validation**

Run: `python3 -m unittest tests/test_sdk_capability_copy.py -v`

Expected: PASS with two tests.

Run: `python3 -m json.tool sdk-release.json >/dev/null && git diff --check`

Expected: exit code 0.

- [ ] **Step 5: Commit the public capability refresh**

```bash
git add index.html docs/index.html docs/reference.html llms.txt sdk-release.json
git commit -m "Document SDK contract intelligence workflows"
```

### Task 4: Verify the release-backed content as a complete website change

**Files:**
- Verify: `index.html`
- Verify: `docs/reference.html`
- Verify: `llms.txt`
- Verify: `sdk-release.json`
- Verify: `tests/test_sdk_capability_copy.py`

- [ ] **Step 1: Recheck live release consistency**

Run: `python3 .codex/check-sdk-release.py`

Expected: `PyPI latest: 0.6.5`, `GitHub latest: v0.6.5`, and `Versions match: True`.

- [ ] **Step 2: Check exact public claims and guardrails**

Run:

```bash
rg -n -F 'open-data-products product wrap-contract --input contract.yaml --output product.yaml' index.html docs/reference.html llms.txt
rg -n -F 'open-data-products portfolio discover-contracts ./contracts --output ./portfolio-discovery --json' index.html docs/reference.html llms.txt
rg -n -F 'does not automatically create or approve data products' index.html docs/reference.html llms.txt
```

Expected: each command and the guardrail appear in all three public surfaces.

- [ ] **Step 3: Inspect the final patch and clean state**

Run:

```bash
git diff HEAD~2..HEAD --check
git status --short --branch
```

Expected: no whitespace errors and no uncommitted files after the implementation commits.
