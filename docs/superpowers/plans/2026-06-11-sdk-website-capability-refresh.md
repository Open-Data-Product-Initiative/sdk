# SDK Website Capability Refresh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refresh the SDK landing page and agent-facing `llms.txt` so they reflect the current agent-ready SDK, selected guide paths, portfolio workflows, MCP, ARWS, Data Contracts, LLM generation, and cross-spec capabilities.

**Architecture:** This repository is a static single-page site. Keep the public web copy, navigation, sections, and footer links in `index.html`, and mirror the agent-routing summary in `llms.txt`.

**Tech Stack:** Static HTML, inline CSS, root-level assets, plain-text `llms.txt`.

---

### Task 1: Public Page Refresh

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Update metadata and navigation**

Adjust the page title, description, Open Graph text, Twitter text, and main navigation so the page centers the current SDK capabilities and includes a guide anchor.

- [ ] **Step 2: Refresh the hero**

Update the headline, lead copy, primary/secondary CTAs, terminal examples, and status counters to use current README command shapes: `validate`, `resources`, `manifest`, `serve`, `generate`, and `portfolio`.

- [ ] **Step 3: Expand capability blocks**

Replace the four-card capability summary with six cards: validate, explain/summarize, generate, discover resources, graph/vocabulary reasoning, and portfolio/Data Contract workflows.

- [ ] **Step 4: Add guide and portfolio sections**

Add a selective guide section grouped into Start, Generate, Reason, and Portfolio tracks. Add a portfolio feature block that explains `portfolio build`, `refresh`, `sync`, `localize`, and `explain`.

- [ ] **Step 5: Refresh footer links**

Add direct links to the upstream API reference, command guide, LLM generation guide, agent surface, Data Contract workflows, and course-style guides.

### Task 2: Agent Handoff Refresh

**Files:**
- Modify: `llms.txt`

- [ ] **Step 1: Mirror the website capability model**

Update the summary, use cases, command examples, MCP/ARWS notes, selected guide tracks, portfolio workflows, and docs links.

- [ ] **Step 2: Keep agent-specific cautions**

Preserve validation guidance, local/provider LLM distinction, and maintainer/resource links.

### Task 3: Verification

**Files:**
- Verify: `index.html`
- Verify: `llms.txt`

- [ ] **Step 1: Parse HTML**

Run `python3 -m html.parser index.html`. Expected: exit code 0 and no output.

- [ ] **Step 2: Check whitespace**

Run `git diff --check -- index.html llms.txt`. Expected: exit code 0 and no whitespace errors.

- [ ] **Step 3: Review changed files**

Run `git diff -- index.html llms.txt` and confirm the changes match the approved plan.
