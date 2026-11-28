# Forretningsregler

Dette dokument samler reglerne for, hvordan vibrationsmålinger fra gearkasser vurderes,
og hvorfor reglerne findes. Det er skrevet til product owner, nye udviklere og agenter.

De præcise grænseværdier og grænsetilfælde står ikke her. Testene er kravene og er
præcise om dem, så hver regel henviser til den kode og de tests, der implementerer den.
Begreberne er forklaret i [glossary.md](glossary.md).

Ændres en regel, skal dette dokument og en test opdateres i samme pull request
(se `AGENTS.md`).

---

## R1: En måling klassificeres som normal, warning eller critical

**Regel:** En gyldig måling får én af tre klassifikationer ud fra to grænseværdier:
en advarselsgrænse og en kritisk grænse.

**Hvorfor:** Kontrolcentret skal kunne se, om en vibrationsmåling er normal, forhøjet
eller kritisk. Grænseværdierne er fastsat af kontrolcentret i Aalborg.

**Implementering:**
- Kode: `classify`, `is_anomaly`, `WARNING_MM_S` og `CRITICAL_MM_S` i `vibration.py`
- Tests: `test_classify`, `test_is_anomaly_at_warning_threshold` og
  `test_is_anomaly_below_warning_threshold` i `test_vibration.py`

---

## R2: Negative målinger afvises

**Regel:** En negativ måling er ugyldig og klassificeres ikke. `classify` afviser den
med en fejl.

**Hvorfor:** En negativ vibration er fysisk meningsløs og tyder på en fejl i data.
Den må ikke ende med at blive kaldt "normal".

**Implementering:**
- Kode: `classify` i `vibration.py`
- Test: `test_classify_rejects_negative_values` i `test_vibration.py`

---

## R3: Fysisk umulige målinger er sensorfejl, ikke critical

**Regel:** En måling over sensorfejlsgrænsen klassificeres som sensorfejl og ikke som
critical.

**Hvorfor:** En så høj måling er fysisk umulig for gearkassen. Den skyldes en defekt
sensor, ikke en defekt mølle, og må derfor ikke klassificeres som critical.

**Implementering:**
- Kode: `classify`, `is_sensor_fault` og `SENSOR_FAULT_MM_S` i `vibration.py`
- Tests: `test_classify_sensor_fault`, `test_is_sensor_fault_at_threshold` og
  `test_is_sensor_fault_above_threshold` i `test_vibration.py`

---

## R4: En sensorfejl er ikke en anomali

**Regel:** En måling, der er en sensorfejl, tæller ikke som en anomali, selvom den
ligger over advarselsgrænsen.

**Hvorfor:** Målingen siger intet om møllen. En defekt sensor må ikke udløse en alarm
for en mølle, der måske er i orden.

**Implementering:**
- Kode: `is_anomaly` og `is_sensor_fault` i `vibration.py`
- Tests: `test_is_anomaly_at_sensor_fault_threshold` og
  `test_is_anomaly_rejects_sensor_fault` i `test_vibration.py`
