"""
This class is responsible of scrapping a website and extracting all
the differents links from it. 
"""
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests

class WebScrapper():
    def __init__(self, url, nbr_iterations=1):
        """
        input: 
            - url = URL of the website
            - nbr_iterations = number of times to crawl the website (default value:1)
        """
        self.url = url
        self.nbr_iterations = nbr_iterations
        #variable to store the links as nodes for the graph
        self.nodes = []
        #variable to store the links as edges for the graph
        self.edges = []
        self.crawl(url)
        print('run')
    
    def getNodes(self):
        """
        returns the nodes
        """
        return self.nodes

    def getEdges(self):
        """
        returns the edges
        """
        return self.edges

    def is_valid(self, url):
        """
        input: - url = URL/link of a website
        return: -True if URL contains a protocol and a domain
        """
        parsed = urlparse(url)
        return bool(parsed.scheme) and bool(parsed.netloc)
    
    def scrapper(self, url):
        """
        This funtion scrapes the a webpage and extracts the links(href) and stores them
        to the varibles nodes and edges

        input: - url = URL/link of a website
        """

        #domain name of the 'url' without the protocol
        domain_name = urlparse(url).netloc
        #html content of the webpage
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')

        for a_tag in soup.findAll('a'):
            #href that is in the <a> tag
            href = a_tag.get('href')
            #checks if the href is non empty
            if href !='' or href != None:
                #joins the href to the url
                href = urljoin(url, href)
                #parses the href
                parsed_href = urlparse(href)
                #cleans the href
                href = parsed_href.scheme + '://' + parsed_href.netloc + parsed_href.path
                if self.is_valid(href) and domain_name in href:
                    #checks if the href(url) is not broken
                    if requests.get(href):
                        self.edges.append((url, href))
                        if href not in self.nodes:
                            self.nodes.append(href)
    
    def crawl(self, url):
        """
        This function crawls a website and scrapes all the links from it.

        input: - url = URL/link of a website
        """
        #variable to keep track of the current number of iterqtions
        curr_iteration = 0
        #adds the url to the list nodes
        self.nodes.append(url)
        for link in self.nodes:
            curr_iteration+=1
            if curr_iteration>self.nbr_iterations:
                break
            self.scrapper(link)
    
    def writeNodesEdgesToAFile(self):
        """
        This funtions writes to a nodes.txt file, the nodes from the graph 'G',
        and to a edges.txt file, the edges from the graph 'G'. 
        """  
        nodes_file = open('nodes.txt', 'w')
        edges_file = open('edges.txt', 'w')
        for node, edge in self.nodes, self.edges:
            nodes_file.write(node, '\n')
            edges_file.write(edge, '\n')