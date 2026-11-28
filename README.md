# Agentic coding sandbox

Et lille øvelsesrepo til at lære at arbejde med AI-agenter (fx Claude Code) i en
kontrolleret arbejdsgang: issue → branch → plan → implementering → `make check` →
pull request → review → merge.

Domænet er en forenklet udgave af casen Intelligent IoT Solutions A/S: vibrationsmålinger
fra gearkasser i vindmøller klassificeres som normal, warning, critical eller sensor_fault.
Reglerne og begrundelserne står i `docs/domain-rules.md`, og begreberne i `docs/glossary.md`.

## Kom i gang

Kræver Python 3.10+ og `make`.

```bash
make setup   # opret .venv og installér pytest og ruff
make check   # lint og test
```

`make check` er grøn på `main`. Tests, der hører til åbne issues, er markeret med `xfail`.

## Filer

| Fil | Formål |
| --- | --- |
| `vibration.py` | Domænelogikken |
| `test_vibration.py` | Testene, som er kravene |
| `Makefile` | De eneste kommandoer, agenter må bruge |
| `AGENTS.md` | Fælles regler for alle agenter |
| `CLAUDE.md` | Importerer `AGENTS.md` til Claude Code |
| `.github/copilot-instructions.md` | Peger Copilot til `AGENTS.md` |
| `CONTRIBUTING.md` | Arbejdsgangen for mennesker og agenter |
| `.github/pull_request_template.md` | Skabelon til pull requests |
| `.github/ISSUE_TEMPLATE/opgave.md` | Skabelon til issues |
| `.github/workflows/ci.yml` | CI, der kører `make check` |
| `docs/domain-rules.md` | Forretningsreglerne og hvorfor de findes |
| `docs/glossary.md` | Domænets begreber og deres navne i koden |
| `docs/ISSUES.md` | Forslag til de første øvelser |
