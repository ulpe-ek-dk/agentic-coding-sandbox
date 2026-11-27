# Arbejdsgang

Den samme arbejdsgang gælder for mennesker og agenter.

## Fra issue til merge

1. **Issue:** hver opgave starter som et GitHub-issue med problem, acceptkriterier og afgrænsning
   (brug skabelonen "Opgave").
2. **Branch:** `git switch -c issue-<nr>-<kort-beskrivelse>` fra en opdateret `main`.
3. **Plan:** skriv kort, hvad der skal ændres, og hvordan det verificeres. En agent skal vente på godkendelse.
4. **Implementering:** den mindste ændring, der løser issuet.
5. **Verifikation:** `make check` lokalt.
6. **Pull request:** `gh pr create`. Udfyld skabelonen, og skriv `Closes #<nr>`, så issuet lukkes ved merge.
7. **Review:** et menneske læser diffen og tjekker, at CI er grøn.
8. **Merge:** med *Squash and merge*. Slet branchen bagefter.

## Hvad man ser efter i et review

- Løser ændringen issuet, og kun det?
- Er testenes forventninger uændrede?
- Er ændringen lille nok til at forstå?
- Er kommentarerne på dansk og forståelige?
- Er der nye afhængigheder, hemmeligheder eller ændringer i `Makefile` eller `.github/`?
- Kan du selv forklare koden? Hvis ikke, så spørg agenten, før du merger.
