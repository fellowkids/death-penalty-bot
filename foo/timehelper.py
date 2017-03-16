from datetime import datetime
from dateutil import parser

SECONDS_PER_DAY = 60 * 60 * 24

def count_days_between(start_date, finish_date):
    seconds_diff = finish_date.timestamp() - start_date.timestamp()
    return round(seconds_diff / SECONDS_PER_DAY, 1)

def count_weeks_between(start_date, finish_date):
    return round(count_days_between(start_date, finish_date) / 7, 1)


def parse_date(xdate):
    """
    xdate is 'Today', or any kind of human readable date string,
        or even a datetime

    returns datetime object
    """

    if xdate == 'Today':
        return datetime.today()
    elif type(xdate) is datetime:
        return xdate
    else:
        return parser.parse(xdate)


def parse_texas_time(tx_timestring):
    """
    datestr is a string that looks like '9/12/2017', i.e.
    what the Texas DoJ uses on its website.

    returns datetime object
    """
    return datetime.strptime(datestr, '%m/%d/%Y')

def pretty_date(dateobj):
    """
    dateobj is some datetime.datetime() object

    Returns human readable string
    """
    return strftime('%A, %d %B %Y %l:%M %p', dateobj)

