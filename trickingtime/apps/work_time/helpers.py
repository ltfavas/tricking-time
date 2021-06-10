from datetime import datetime, date, time
from decimal import Decimal


def generate_slug(date: datetime):

    return date.strftime("%d-%m-%Y")


def get_duration(start_time: time, end_time: time):

    duration = datetime.combine(date.min, end_time) - \
        datetime.combine(date.min, start_time)
    return (datetime.min + duration).time()


def get_duration_decimal(time_var: time):

    return Decimal(time_var.hour) + (Decimal(time_var.minute) / Decimal(60))
