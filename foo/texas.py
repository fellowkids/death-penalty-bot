from foo.timehelper import parse_texas_time, parse_date
from bs4 import BeautifulSoup
import requests

SOURCE_URL = "http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html"

def get_latest_inmates(as_of_date="Today"):
    """
    Returns inmates executed on as_of_date or afterwards
    """
    thedate = parse_date(as_of_date)
    inmates = get_inmates()
    x_inmates = []
    for i in inmates:
        if i['execution_date'] >= thedate:
            x_inmates.append(i)

    return x_inmates

def get_inmates():
    htmltxt = download_page()
    inmates = extract_inmates(htmltxt)
    # sort them
    return sorted(inmates, key=lambda x: x['execution_date'], reverse=True)

def download_page():
    resp =  requests.get(SOURCE_URL)
    return resp.text

def scrape_inmates(htmltxt):
    """
    htmltxt is a string

    return a list of dicts:
    {
        'first_name': 'John',
        'last_name': 'Doe',
        'execution_date': datetime(2016, 9, 12),
        'birth_date': datetime(2016, etc.),
        'race': 'W',
        'url': 'http://www.tdcj.state.tx.us/death_row/dr_info/johndoe.html'
    }

    """
    soup = BeautifulSoup(htmltxt, 'lxml')
    # ignore first row (headers)
    rows = soup.select('table.os tr')[1:]
    inmates = []
    for row in rows:
        cols = [td.text.strip() for td in row.select('td')]
        d = {}
        d['first_name'] = cols[3]
        d['last_name'] = cols[2]
        d['birth_date'] = convert_texas_date_string(cols[5])
        d['race'] = cols[6]
        d['execution_date'] = convert_texas_date_string(cols[0])

        inmates.append(d)
    return inmates


