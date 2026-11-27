"""Vurdering af vibrationsmålinger fra gearkasser i Intelligent IoT Solutions' vindmøller."""

WARNING_MM_S = 7.1  # fra denne værdi (mm/s) er vibrationen forhøjet
CRITICAL_MM_S = 11.0  # over denne værdi (mm/s) er vibrationen kritisk
# Over denne værdi (mm/s) er målingen fysisk umulig for gearkassen, så den
# skyldes en defekt sensor og ikke en defekt mølle.
SENSOR_FAULT_MM_S = 50.0


def is_sensor_fault(vibration: float) -> bool:
    """Returnér True, hvis målingen er så høj, at den må skyldes en defekt sensor.

    Grænsen vurderes kun her, så is_anomaly og classify altid er enige om,
    hvad der er en sensorfejl. Se issue #3.
    """
    return vibration > SENSOR_FAULT_MM_S


def is_anomaly(vibration: float) -> bool:
    """Returnér True, hvis vibrationen er på eller over advarselsgrænsen.

    En sensorfejl tæller ikke som en anomali: målingen siger intet om møllen,
    og den må ikke udløse en alarm for en mølle, der måske er i orden.
    """
    return vibration >= WARNING_MM_S and not is_sensor_fault(vibration)


def classify(vibration: float) -> str:
    """Klassificér en måling som "normal", "warning", "critical" eller "sensor_fault".

    Regler (fra kontrolcentret i Aalborg):
    - under 7,1 mm/s: "normal"
    - fra 7,1 mm/s til og med 11,0 mm/s: "warning"
    - over 11,0 mm/s til og med 50,0 mm/s: "critical"
    - over 50,0 mm/s: "sensor_fault" (fysisk umuligt, se issue #3)
    - negative værdier er ugyldige og skal give ValueError

    Se issue #1 og #3.
    """
    if vibration < 0:
        # En negativ vibration er fysisk meningsløs og tyder på en fejl i data,
        # så vi afviser den i stedet for at kalde den "normal".
        raise ValueError(f"Vibration kan ikke være negativ: {vibration} mm/s")
    # Sensorfejl tjekkes før "critical", så en defekt sensor ikke sender
    # teknikere ud til en mølle, der måske er i orden.
    if is_sensor_fault(vibration):
        return "sensor_fault"
    if vibration > CRITICAL_MM_S:
        return "critical"
    # Genbrug is_anomaly, så advarselsgrænsen kun vurderes ét sted.
    if is_anomaly(vibration):
        return "warning"
    return "normal"
