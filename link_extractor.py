"""
This module is capable to extract all the links form a given URL
"""
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests

def links_extractor(URL, internal_urls=[]):
    """
    Param : URL from the website to extract all the links
    """
    response = requests.get(URL) #stores the html source code and returns the response
    if response:
        html_code = BeautifulSoup(response.content, "html.parser")
        for a in html_code.findAll('a'):
            href = a.get('href')
            if not urlparse(href).scheme and urlparse(href).path:
                parsed_url = urljoin(URL, href)
                if requests.get(parsed_url) and not parsed_url in internal_urls:
                    internal_urls.append(parsed_url)
    return internal_urls

def all_links_extractor(URL, max_iterations=10):
    """
    Param: URL from a website | max_iteration defines how deep we extract links
    return a sorted list of all the internal urls
    """
    curr_iteration = 0
    all_internal_urls = links_extractor(URL)
    
    for link in all_internal_urls:
        curr_iteration+=1
        if curr_iteration<=max_iterations:
            all_internal_urls = links_extractor(link, all_internal_urls)
    all_internal_urls.sort()
    return all_internal_urls

import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()
all_links_extractor('https://wwwfr.uni.lu')
pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())