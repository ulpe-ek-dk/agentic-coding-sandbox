# Ordliste

Fælles sprog for domænet: hvad begreberne betyder, og hvad de hedder i koden.
Reglerne, der bruger begreberne, står i [domain-rules.md](domain-rules.md).

Nye begreber tilføjes her i samme pull request, som indfører dem (se `AGENTS.md`).

| Begreb | Forklaring | Navn i koden |
| --- | --- | --- |
| Måling | En vibrationsmåling fra en gearkasse i en vindmølle, angivet i mm/s. | Parameteren `vibration` (`float`) |
| Klassifikation | Vurderingen af en måling som normal, warning, critical eller sensorfejl. | `classify()` |
| Normal | Målingen ligger under advarselsgrænsen. | `"normal"` |
| Warning | Målingen er forhøjet: på eller over advarselsgrænsen, men ikke over den kritiske grænse. | `"warning"` |
| Critical | Målingen er kritisk: over den kritiske grænse, men ikke en sensorfejl. | `"critical"` |
| Sensorfejl | Målingen er fysisk umulig for gearkassen og skyldes en defekt sensor, ikke en defekt mølle. | `"sensor_fault"`, `is_sensor_fault()` |
| Anomali | Målingen ligger på eller over advarselsgrænsen og er ikke en sensorfejl. Både warning og critical er anomalier. | `is_anomaly()` |
| Ugyldig måling | En negativ måling. Den er fysisk meningsløs og klassificeres ikke. | `ValueError` fra `classify()` |
| Advarselsgrænse | Grænsen, hvorfra en måling er forhøjet. | `WARNING_MM_S` |
| Kritisk grænse | Grænsen, over hvilken en måling er kritisk. | `CRITICAL_MM_S` |
| Sensorfejlsgrænse | Grænsen, over hvilken en måling er fysisk umulig og derfor en sensorfejl. | `SENSOR_FAULT_MM_S` |
