from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta

from common.constants import LUNCH_END_TIME
from common.constants import LUNCH_START_TIME
from common.constants import WORK_HOURS_END
from common.constants import WORK_HOURS_START
from common.exceptions import InvalidOperationException


def get_working_hours(period_start: datetime, period_end: datetime) -> float:
    """Get the number of working hours in a given period

    Args:
        period_start(datetime): Date and time at the start of the period.
        period_end(datetime): Date and time at the end of the period.

    Returns:
        Working hours as a float.

    Raises:
        InvalidOperationException if the period start is older than the period end.
    """

    if period_start > period_end:
        raise InvalidOperationException("Period start can not come after the end date and time")

    start_date: date = period_start.date()
    start_time: time = period_start.time()
    end_date: date = period_end.date()
    end_time: time = period_end.time()

    working_hours: float = 0.0
    loop_date: date = start_date
    while loop_date <= end_date:
        if loop_date.weekday() < 5:  # Date is not a weekend
            loop_date_start: datetime = get_loop_date_start(loop_date, start_date, start_time)
            loop_date_end: datetime = get_loop_date_end(loop_date, end_date, end_time)

            loop_delta: timedelta = loop_date_end - loop_date_start
            loop_hours: float = 0.0
            if loop_date_start.time() >= time(14, 0, 0) or loop_date_end.time() <= time(12, 59, 59, 999999):
                loop_hours = loop_delta.total_seconds() / 3600
            else:
                loop_hours = (loop_delta.total_seconds() / 3600) - 1
            working_hours += loop_hours

        loop_date += timedelta(1)

    return working_hours


def get_loop_date_end(loop_date, end_date, end_time):
    if end_time >= LUNCH_START_TIME and end_time <= LUNCH_END_TIME:
        end_time = time(12, 59, 59, 999999)

    if loop_date == end_date and end_time < WORK_HOURS_END:
        loop_date_end = datetime.combine(end_date, end_time)
    else:
        loop_date_end = datetime.combine(loop_date, WORK_HOURS_END)
    return loop_date_end


def get_loop_date_start(loop_date, start_date, start_time):
    if start_time >= LUNCH_START_TIME and start_time <= LUNCH_END_TIME:
        start_time = time(14, 0, 0, 0)

    if loop_date == start_date and start_time >= WORK_HOURS_START:
        loop_date_start = datetime.combine(start_date, start_time)
    else:
        loop_date_start = datetime.combine(loop_date, WORK_HOURS_START)
    return loop_date_start
