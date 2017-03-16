from foo.timehelper import count_days_between, count_weeks_between, pretty_date



def tell_story(thisdate, inmate):
    """
    inmate is a dict
    """
    xdays = count_days_between(thedate, inmate['execution_date'])

    story = """
    As of {date}, in {days} days, Texas will execute: {first_name} {last_name}
    """

    return story.format(
                        date=pretty_date(thisdate),
                        days=xdays_until,
                        first_name=inmate['first_name'],
                        last_name=inmate['last_name']
                    )

def tell_aggregate(thisdate, inmates):
    """
    inmates is a list of dicts, sorted in reverse chrono
    """

    finmate = inmates[-1]
    fdate = finmate['execution_date']

    avgx = round(count_weeks_between(thisdate, finmate) / len(inmates), 1)


    story = """
    From {start_date} to {end_date}, there are {inmate_count} Texas inmates awaiting execution.

    In other words, an {avg_count} of inmates executed per week.
    """

    return story.format(
            start_date=pretty_date(startdate),
            end_date=pretty_date(fdate),
            inmate_count=len(inmate_count),
            per_week=avgx
        )



