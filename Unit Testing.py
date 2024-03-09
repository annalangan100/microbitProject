# test_sleep_monitor.py

import pytest
from sleep_monitor import calculate_sleep_score, get_sleep_advice, reduce_sleep_time, convert_temperature, get_sleep_data

def test_calculate_sleep_score():
    assert calculate_sleep_score(18, 25, 150) == 66.666666666
    assert calculate_sleep_score(10, 40, 170) == 66.666666666
    assert calculate_sleep_score(22, 10, 190) == 66.666666666
    assert calculate_sleep_score(30, 50, 220) == 100
    assert calculate_sleep_score(10, 10, 100) == 100
    assert calculate_sleep_score(15, 0, 0) == 100
    assert calculate_sleep_score(20, 30, 180) == 100

def test_get_sleep_advice():
    assert get_sleep_advice(18, 25, 150) == ["Lower the room temperature to improve sleep.", "Reduce noise levels by using earplugs or white noise machines."]
    assert get_sleep_advice(10, 40, 170) == ["Increase the room temperature to improve sleep.", "Reduce noise levels by using earplugs or white noise machines."]
    assert get_sleep_advice(22, 10, 190) == ["Dim the lights or use blackout curtains to reduce light exposure."]
    assert get_sleep_advice(30, 50, 220) == ["No specific advice for improving sleep based on the data."]
    assert get_sleep_advice(10, 10, 100) == ["No specific advice for improving sleep based on the data."]
    assert get_sleep_advice(15, 0, 0) == ["No specific advice for improving sleep based on the data."]
    assert get_sleep_advice(20, 30, 180) == ["No specific advice for improving sleep based on the data."]

# Add other test functions for the remaining functions

if __name__ == "__main__":
    pytest.main()
