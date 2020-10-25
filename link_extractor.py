"""
This module is capable to extract all the links form a given URL
"""
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests



nodes = []
edges = []

def isvalid(url):
    """
    returns TRUE if the 'url' is valid and FALSE if the 'url is not valid
    """
    parsed = urlparse(url)
    return bool(parsed.scheme) and bool(parsed.netloc)

def get_website_links(url):
    """
    Returns all links that are found on 'url'
    """
    #domain name of the 'url' without the protocol
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    for a_tag in soup.findAll('a'):
        href = a_tag.get('href')
        if href !='' or href != None:
            href = urljoin(url, href)
            parsed_href = urlparse(href)
            href = parsed_href.scheme + '://' + parsed_href.netloc + parsed_href.path
            if isvalid(href):
                #if not href in internal_urls and domain_name in href:
                if domain_name in href:
                    #if requests.get(href): #I removed the checker for doubles
                    edges.append((url, href))
                    if not href in nodes:
                        nodes.append(href)
                        

def crawl(url, max_iterations=3):
    """
    Param: URL from a website | max_iteration defines how deep we extract links
    return a sorted list of all the internal urls
    """
    curr_iteration = 0
    nodes.append(url)
    for link in nodes:
        curr_iteration+=1
        print(curr_iteration)
        if curr_iteration<=max_iterations:
            get_website_links(link)
        else: break
    return edges

def get_nodes():
    return nodes