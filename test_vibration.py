"""Tests for vibration.py. Testene er kravene: forventningerne må ikke ændres.

Tests markeret med xfail hører til et åbent issue. Når issuet er løst, fjernes
markeringen. strict=True betyder, at pipelinen fejler, hvis en xfail-test
pludselig består, så man ikke glemmer at fjerne markeringen.
"""

import pytest

from vibration import classify, is_anomaly, is_sensor_fault


def test_is_anomaly_at_warning_threshold():
    assert is_anomaly(7.1) is True


def test_is_anomaly_below_warning_threshold():
    assert is_anomaly(4.2) is False


@pytest.mark.parametrize(
    "vibration, expected",
    [
        (0.0, "normal"),
        (7.0, "normal"),
        (7.1, "warning"),
        (11.0, "warning"),
        (11.1, "critical"),
        (25.0, "critical"),
    ],
)
def test_classify(vibration, expected):
    assert classify(vibration) == expected


def test_classify_rejects_negative_values():
    with pytest.raises(ValueError):
        classify(-1.0)


# Issue #3: målinger over 50 mm/s er fysisk umulige og skyldes en defekt sensor.
@pytest.mark.parametrize(
    "vibration, expected",
    [
        (50.0, "critical"),
        (50.1, "sensor_fault"),
    ],
)
def test_classify_sensor_fault(vibration, expected):
    assert classify(vibration) == expected


def test_is_sensor_fault_at_threshold():
    assert is_sensor_fault(50.0) is False


def test_is_sensor_fault_above_threshold():
    assert is_sensor_fault(50.1) is True


def test_is_anomaly_at_sensor_fault_threshold():
    assert is_anomaly(50.0) is True


def test_is_anomaly_rejects_sensor_fault():
    assert is_anomaly(50.1) is False
