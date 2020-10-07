"""
This module is used to extract all the internal links
 of a webstie and store them in an array
"""

from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup as BS
import requests


class LinkExtractor():
    """
    This class contains all the functions needed to extract all the links
    """
    def __init__(self, url):
        """
        This is the constructor. It initializes the variable internal_url that
        is the one who will contain all the links
        """
        self.extract_all_website_links(url)
        self.internal_url = []

    @classmethod
    def is_external(cls, href):
        """
        Checks if the given href is external
        """
        return bool(urlparse(href).netloc)
    @classmethod
    def is_valid(cls, href):
        """
        Checks if the href is valid and if the url is not broken
        """
        return not href == '#' and not href == '/'

    def extract_all_webpage_links(self, url):
        """
        This function extracts all the internal links from URL and stores the in internal_url
        """
        soup = BS(requests.get(url).text, "html.parser")

        for link in soup.findAll('a'):
            href = link.get('href')
            parsed_url = urljoin(url, href)
            if self.is_valid(href):
                if not self.is_external(href):
                    if not parsed_url in self.internal_url:
                        self.internal_url.append(parsed_url)
        self.internal_url.sort()
        return self.internal_url

    def extract_all_website_links(self, url, max_search=10):
        """
        @params max_search: maximum iterations that this function will do
        This function extracts all the internal links of the URL in the internal_url list
        """
        count = 0
        links = self.extract_all_webpage_links(url)
        for link in links:
            count+=1
            print(count)
            self.extract_all_webpage_links(link)
            if count == max_search:
                break
        return self.internal_url

    def write_to_file(self, url):
        """
        Temporary function that converts the internal_url list in a .txt file
        """
        file = open('ExternalLinks.txt', 'w')
        #extract_all_website_links(url)
        self.extract_all_website_links(url)
        for link in self.internal_url:
            file.write(link+'\n')
        file.close()
