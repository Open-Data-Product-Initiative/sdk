# SDK website: ODCS drafting and Data Contract Intelligence

## Goal

Make the public SDK website accurately expose the two user-facing capabilities
available in the verified `open-data-products` 0.6.5 release:

- draft a validated ODPS 4.2 product from an ODCS 3.0, 3.1, or 3.2 contract;
- discover Data Contract Intelligence and export its evidence-backed offline
  HTML report.

## Chosen presentation

Retain all six existing homepage examples and add two cards. The example grid
therefore has eight cards; the added cards make the release's most material
contract capabilities visible without removing validation, generation, MCP, or
portfolio workflows.

## Public surfaces

1. Update homepage metadata and capability copy so ODCS-to-ODPS drafting and
   Data Contract Intelligence are discoverable in search and agent-facing
   summaries.
2. Add homepage example cards with the verified CLI commands:

   ```text
   open-data-products product wrap-contract --input contract.yaml --output product.yaml
   open-data-products portfolio discover-contracts ./contracts --output ./portfolio-discovery --json
   ```

3. Extend `docs/reference.html` with focused guidance for both workflows,
   including their outputs and boundaries.
4. Update `llms.txt` so agents receive the same capability and provenance
   constraints as human readers.

## Accuracy boundaries

- ODCS wrapping creates a validated ODPS draft; it does not approve or publish
  a data product. AI enrichment is opt-in.
- Data Contract Intelligence retains source evidence, identifies duplicates,
  overlaps, shared technical resources, and metadata/interface gaps. Its
  opportunities are review-only; it does not automatically create or approve
  data products.
- The visual report is a self-contained offline HTML report, not a live graph
  editor or a monitoring dashboard.

## Validation

- Run the required release checker and confirm PyPI and GitHub still agree on
  0.6.5.
- Confirm both exact commands and the review-only boundary appear in the
  homepage, reference documentation, and `llms.txt` where applicable.
- Confirm the legacy examples remain, no stale release label or conflict marker
  is introduced, JSON metadata remains valid, and `git diff --check` passes.
