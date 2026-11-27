# Forslag til de første issues

Opret dem på GitHub (Issues → New issue → "Opgave"). Kopiér titel og tekst.

---

## Issue 1: Implementér classify

**Problem**
Kontrolcentret skal kunne se, om en vibrationsmåling er normal, forhøjet eller kritisk.
`classify()` i `vibration.py` er ikke implementeret.

**Acceptkriterier**
- [ ] Under 7,1 mm/s giver "normal"
- [ ] Fra 7,1 til og med 11,0 mm/s giver "warning"
- [ ] Over 11,0 mm/s giver "critical"
- [ ] Negative værdier giver `ValueError`
- [ ] `xfail`-markeringen for issue #1 er fjernet, og `make check` er grøn

**Afgrænsning**
Grænseværdierne må ikke ændres. Ingen nye afhængigheder.

---

## Issue 2: Afvis fysisk umulige værdier som sensorfejl

**Problem**
En måling over 50 mm/s er fysisk umulig for gearkassen og skyldes en defekt sensor,
ikke en defekt mølle. Den må ikke klassificeres som "critical".

**Acceptkriterier**
- [ ] `classify()` giver "sensor_fault" for værdier over 50 mm/s
- [ ] Der er tests for 50,0 (critical) og 50,1 (sensor_fault)
- [ ] `make check` er grøn

**Afgrænsning**
Kun `vibration.py` og `test_vibration.py` ændres.

*Bemærk: her skal agenten selv skrive nye tests. Læg mærke til, om reglen i AGENTS.md
om ikke at ændre eksisterende forventninger bliver overholdt.*

---

## Issue 3: Gør grænseværdierne konfigurerbare pr. målepunkt

**Problem**
Forskellige målepunkter (fx gearkasse og generator) har forskellige grænser.

**Acceptkriterier**
- [ ] Grænserne ligger i en datastruktur pr. målepunkt i stedet for to konstanter
- [ ] Eksisterende tests består uændret
- [ ] Nye tests for mindst ét ekstra målepunkt
- [ ] `make check` er grøn

**Afgrænsning**
Ingen konfigurationsfiler eller databaser. Det skal være Python-kode.

*Bemærk: et større issue, hvor plan mode er nyttigt. Bed om en plan, før agenten ændrer noget.*
