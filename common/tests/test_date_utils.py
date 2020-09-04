import pytest
from common.utils.date_utils import get_working_hours
from datetime import date, datetime, time


test_period_data = [
    (
        datetime.combine(date(2020, 8, 20), time(8, 0, 0)),
        datetime.combine(date(2020, 8, 20), time(17, 0, 0)),
        8.0
    ),
    (
        datetime.combine(date(2020, 8, 20), time(8, 0, 0)),
        datetime.combine(date(2020, 8, 21), time(17, 0, 0)),
        16.0
    ),
    (
        datetime.combine(date(2020, 8, 28), time(8, 0, 0)),
        datetime.combine(date(2020, 8, 30), time(17, 0, 0)),
        8.0
    ),
    (
        datetime.combine(date(2020, 8, 28), time(8, 0, 0)),
        datetime.combine(date(2020, 8, 31), time(17, 0, 0)),
        16.0
    ),
    (
        datetime.combine(date(2020, 8, 20), time(16, 0, 0)),
        datetime.combine(date(2020, 8, 20), time(17, 0, 0)),
        1.0
    ),
    (
        datetime.combine(date(2020, 8, 20), time(14, 0, 0)),
        datetime.combine(date(2020, 8, 20), time(17, 0, 0)),
        3.0
    ),
    (
        datetime.combine(date(2020, 8, 20), time(13, 0, 0)),
        datetime.combine(date(2020, 8, 20), time(14, 0, 0)),
        0.0
    ),
    (
        datetime.combine(date(2020, 8, 29), time(8, 0, 0)),
        datetime.combine(date(2020, 8, 29), time(17, 0, 0)),
        0.0
    ),
    (
        datetime.combine(date(2020, 8, 20), time(4, 0, 0)),
        datetime.combine(date(2020, 8, 20), time(22, 0, 0)),
        8.0
    )]


class TestDateUtils:
    pytestmark = [pytest.mark.unit, ]

    @pytest.mark.parametrize("period_start,period_end,expected_result", test_period_data)
    def test_get_working_hours(self, period_start, period_end, expected_result):  # type: ignore
        actual_result: float = get_working_hours(period_start, period_end)
        assert actual_result == expected_result
