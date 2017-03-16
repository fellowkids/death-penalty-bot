from foo.stories import tell_aggregate, tell_story
from foo.texas import get_latest_inmates
from foo.timehelper import parse_date


def bot(thedate='Today'): #startdate is None or a string
    message = {}
    thedate = parse_date(thedate)
    inmates = get_latest_inmates(as_of_date=thedate)

    # form the aggregate story
    aggstory = tell_aggregate(thedate, inmates)


    # form the story about the next to die
    # first inmate is most recent date
    next_inmate = inmates[0] # assume reverse chrono order
    next_story = tell_story(thedate, next_inmate)


    message['date'] = thedate
    message['aggregate'] = aggstory
    message['story'] = story

    return message

