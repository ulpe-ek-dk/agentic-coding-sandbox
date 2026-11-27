"""Tests for vibration.py. Testene er kravene: forventningerne må ikke ændres.

Tests markeret med xfail hører til et åbent issue. Når issuet er løst, fjernes
markeringen. strict=True betyder, at pipelinen fejler, hvis en xfail-test
pludselig består, så man ikke glemmer at fjerne markeringen.
"""

import pytest

from vibration import classify, is_anomaly

ISSUE_1 = pytest.mark.xfail(strict=True, reason="Issue #1: classify er ikke implementeret")


def test_is_anomaly_at_warning_threshold():
    assert is_anomaly(7.1) is True


def test_is_anomaly_below_warning_threshold():
    assert is_anomaly(4.2) is False


@ISSUE_1
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


@ISSUE_1
def test_classify_rejects_negative_values():
    with pytest.raises(ValueError):
        classify(-1.0)
