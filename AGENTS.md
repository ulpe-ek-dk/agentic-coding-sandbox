# Regler for AI-agenter i dette repo

Denne fil er den fælles regelfil for alle agenter (Claude Code, Copilot, Codex m.fl.).
Værktøjsspecifikke filer (`CLAUDE.md`, `.github/copilot-instructions.md`) peger kun hertil.

## Rækkefølge for beslutninger

1. Issuet og dets acceptkriterier.
2. Testene. De er kravene, og forventningerne må ikke ændres.
3. Den eksisterende kode og konventionerne i repoet.
4. Etableret god praksis.

Er der en konflikt mellem dem, så stop og spørg i stedet for at vælge selv.

## Kommandoer

- Brug kun `make`-targets: `make setup`, `make lint`, `make test`, `make check`.
- Kald ikke pytest, ruff eller pip direkte, og opfind ikke egne kommandoer eller flag.

## Arbejdsgang

1. **Orientér dig:** læs issuet, kør `git status`, og læs de relevante filer.
2. **Planlæg:** beskriv kort, hvad du vil ændre, og hvordan du verificerer det. Vent på godkendelse.
3. **Branch:** arbejd på en ny branch fra `main`, navngivet `issue-<nr>-<kort-beskrivelse>`.
4. **Implementér:** lav den mindste ændring, der løser issuet.
5. **Verificér:** kør `make check`. Den skal være grøn.
6. **Commit og PR:** commit med en kort dansk besked, der nævner issuet (fx `Implementér classify (#1)`).
   Opret en pull request med `gh pr create` og udfyld skabelonen.
7. **Stop:** merge aldrig selv. Et menneske reviewer og merger.

## Regler for ændringer

- Du må ikke ændre forventede værdier i testene. Du må kun fjerne `xfail`-markeringen
  for det issue, du løser.
- Ændr ikke `Makefile`, `.github/` eller `AGENTS.md`, medmindre issuet beder om det.
- Tilføj ingen nye afhængigheder.
- Skriv kommentarer og docstrings på dansk, og forklar hvorfor, ikke kun hvad.

## Git og sikkerhed

- Push aldrig direkte til `main`, og brug aldrig `git push --force`.
- Læs, vis eller commit aldrig `.env`-filer, nøgler eller andre hemmeligheder.

## Definition of done

- `make check` er grøn lokalt.
- Pull requesten er oprettet, og CI er grøn.
- Du har rapporteret de kommandoer, du har kørt, og deres output.
  Påstå aldrig, at noget virker, uden at have kørt det.
