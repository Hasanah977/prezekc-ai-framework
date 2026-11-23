# PREZEKC AI — P01–P06 Acceptance Fixture

This package is a **synthetic demonstration**, not a real stakeholder study or evidence of an approved project. The fake approval values exist only to exercise the current PRD/SRS/RTM validator. Do not import these values into production project records.

## Install

Copy the `examples/acceptance/` directory and `tests/test_acceptance_workflow.py` into your repository, preserving paths. Do not overwrite existing files.

## Execute (PowerShell, repository root)

```powershell
python -m unittest discover -s tests -v
python tools/validate_framework.py --strict
python tools/extract_requirements.py --prd examples/acceptance/prd.md --srs examples/acceptance/srs.md --rtm examples/acceptance/rtm.md --output build/acceptance-v010
if ($LASTEXITCODE -ne 0) { throw 'Extraction failed' }
python tools/validate_requirements.py --prd build/acceptance-v010/prd.json --srs build/acceptance-v010/srs.json --rtm build/acceptance-v010/rtm.json --design examples/acceptance/design.json --strict
if ($LASTEXITCODE -ne 0) { throw 'Traceability validation failed' }
```

Choose a new output directory for subsequent runs: extraction refuses to overwrite prior output.

## Acceptance Boundary

Automated checks: fixture ID cross-references, approved-state metadata *shape*, PRD/SRS/RTM mappings, and existence of referenced design IDs. This does **not** verify the truth of simulated stakeholder inputs, actual authorization, full requirement semantics, correct architecture, or deployment capability. Human review of P01–P06 content is required for actual projects.

## Limitations

Current parser does not export conceptual data entities, full API contracts, or stakeholder/source evidence chains into JSON. Design references are supplied as a separate explicitly maintained design registry. This package does not claim a fully automated P01–P06 lifecycle.
