"""Vurdering af vibrationsmålinger fra gearkasser i Intelligent IoT Solutions' vindmøller."""

WARNING_MM_S = 7.1  # fra denne værdi (mm/s) er vibrationen forhøjet
CRITICAL_MM_S = 11.0  # over denne værdi (mm/s) er vibrationen kritisk


def is_anomaly(vibration: float) -> bool:
    """Returnér True, hvis vibrationen er på eller over advarselsgrænsen."""
    return vibration >= WARNING_MM_S


def classify(vibration: float) -> str:
    """Klassificér en måling som "normal", "warning" eller "critical".

    Regler (fra kontrolcentret i Aalborg):
    - under 7,1 mm/s: "normal"
    - fra 7,1 mm/s til og med 11,0 mm/s: "warning"
    - over 11,0 mm/s: "critical"
    - negative værdier er ugyldige og skal give ValueError

    Se issue #1.
    """
    raise NotImplementedError("classify er ikke implementeret endnu (issue #1)")
