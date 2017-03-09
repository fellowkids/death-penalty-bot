# Number of days until Texas's next scheduled execution
from datetime import datetime
from bs4 import BeautifulSoup
import requests


SOURCE_URL = "http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html"

def get_inmates():
    html = download_page()
    inmates = extract_inmates(html)

    return inmates


def download_page():
    resp =  requests.get(SOURCE_URL)
    return resp.text

def extract_inmates(htmltxt):
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


def convert_texas_date_string(datestr):
    """
    datestr is a string that looks like '9/12/2017'

    returns datetime object
    """
    return datetime.strptime(datestr, '%m/%d/%Y')


