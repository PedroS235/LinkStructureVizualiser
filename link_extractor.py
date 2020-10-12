"""
This module is capable to extract all the links form a given URL
"""
from urllib import request
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests


def get_all_website_links(URL, internal_urls=[]):
    """
    Param : URL from the website to extract all the links
    """
    
    html_code = BeautifulSoup(requests.get(URL).content, "html.parser")
    for a in html_code.findAll('a'):
        href = a.get('href')
        if not urlparse(href).scheme and urlparse(href).path:
            parsed_url = urljoin(URL, href)
            if requests.get(parsed_url) and not parsed_url in internal_urls:
                internal_urls.append(parsed_url)
                print(len(internal_urls))
    return internal_urls

def crawl(URL, max_iterations=10):
    """
    Param: URL from a website | max_iteration defines how deep we extract links
    return a sorted list of all the internal urls
    """
    curr_iteration = 0
    all_internal_urls = [URL]
    
    for link in all_internal_urls:
        curr_iteration+=1
        print()
        print('ITERATION NR:', curr_iteration)
        print()
        if curr_iteration<=max_iterations:
            all_internal_urls = get_all_website_links(link, all_internal_urls)
        else: break
    all_internal_urls.sort()
    return all_internal_urls

