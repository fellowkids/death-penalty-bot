from texas_scraper import get_inmates
from datetime import datetime
from dateutil import parser

def make_story(reference_date, inmate):
    """
    reference_date is a datetime
    inmate is a dict
    """
    seconds_till = inmate['execution_date'].timestamp() - reference_date.timestamp()
    days_till = round(seconds_till / (60 * 60 * 24), 1)

    txt = """

    As of {date}, in {days} days, Texas will execute: {first_name} {last_name}
    """

    return txt.format(  date=reference_date.strftime('%Y-%m-%d'),
                        days=days_till, first_name=inmate['first_name'],
                      last_name=inmate['last_name'],)


def bot(datestr):
    refdate = parser.parse(datestr)

    inmates = get_inmates()
    sortedinmates = sorted(inmates, key=lambda x: x['execution_date'])
    # first inmate is most recent date
    story = make_story(refdate, sortedinmates[0])
    print(story)

