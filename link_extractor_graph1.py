"""
This module is capable to extract all the links form a given URL
"""
from urllib import request
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

def get_all_website_links(URL, internal_urls=[]):
    """
    Param : URL from the website to extract all the links
    """
    
    html_code = BeautifulSoup(requests.get(URL).content, "html.parser")
    for a in html_code.findAll('a'):
        href = a.get('href')
        if not urlparse(href).scheme and urlparse(href).path:
            parsed_url = urljoin(URL, href)
            if not parsed_url in internal_urls:
                internal_urls.append(parsed_url)
                G.add_edge(URL, parsed_url)
    return internal_urls

def crawl(URL, max_iterations=3):
    """
    Param: URL from a website | max_iteration defines how deep we extract links
    return a sorted list of all the internal urls
    """
    curr_iteration = 0
    all_internal_urls = [URL]
    for link in all_internal_urls:
        curr_iteration+=1
        if curr_iteration<=max_iterations:
            all_internal_urls = get_all_website_links(link, all_internal_urls)
        else: break
    #all_internal_urls.sort()
    print(len(all_internal_urls))
    return all_internal_urls

crawl('https://wwwfr.uni.lu')
print(list(G.edges()))
nx.draw(G, with_labels=True, font_size='8')
plt.show()
#requests.get(parsed_url) and 
#https://infallible-varahamihira-e94f86.netlify.app
