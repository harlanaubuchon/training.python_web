##mashup.py
import requests
from bs4 import BeautifulSoup

#GET == requests.get(url, **kwargs)
#POST == requests.post(url, **kwargs)

import requests

def fetch_search_results(
    query=None, minAsk=None, maxAsk=None, bedrooms=None
    ):
    incoming = locals().copy()
    base = 'http://seattle.craigslist.org/search/apa'
    search_params = dict(
        [(key, val) for key, val in incoming.items()
                    if val is not None])
    if not search_params:
        raise ValueError("No valid keywords")

    resp = requests.get(base, params=search_params, timeout=3)
    resp.raise_for_status() #<- no-op if status==200
    return resp.content, resp.encoding



def parse_source(html, encoding='utf-8'):
    parsed = BeautifulSoup(html, from_encoding=encoding)
    return parsed



if __name__ == '__main__':
    html, encoding = fetch_search_results(
        minAsk=500, maxAsk=1000, bedrooms=2
    )
    doc = parse_source(html, encoding)
    print doc.prettify(encoding=encoding)