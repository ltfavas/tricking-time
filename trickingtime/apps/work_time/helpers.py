import logging
from datetime import datetime, date, time
from decimal import Decimal

logger = logging.getLogger(__name__)


def generate_slug(date: datetime):

    return date.strftime("%d-%m-%Y")


def get_duration(start_time: time, end_time: time):
    logger.debug(f"Calculating time interval between {start_time.isoformat()}"
                 f" and  {end_time.isoformat()}"
                 )

    duration = datetime.combine(date.min, end_time) - \
        datetime.combine(date.min, start_time)
    return (datetime.min + duration).time()


def get_duration_decimal(time_var: time):
    logger.debug(f"Converting {time_var.isoformat()} into decimal value")
    return Decimal(time_var.hour) + (Decimal(time_var.minute) / Decimal(60))
