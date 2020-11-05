"""
This module is capable to extract all the links form a given URL
"""
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests

#variable to store the different nodes categorized by groups (for graph)
nodes = [] # [{'id":'url', 'group':1}]

#variable to store the different edges categorized by values(wheights) (for graph)
edges = [] # [{'source":'url1', 'target':'url2', 'value':1}]

#stocks the differnts links without doubles 
links = []


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
    #html content of the webpage
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    for a_tag in soup.findAll('a'):
        #href that is in the <a> tag
        href = a_tag.get('href')
        #checks if the href is not empty
        if href !='' or href != None:
            #joins the href to the url
            href = urljoin(url, href)
            #no need: parsed_href = urlparse(href)
            #no need: href = parsed_href.scheme + '://' + parsed_href.netloc + parsed_href.path
            if isvalid(href) and domain_name in href:
                #checks if the href(url) is not broken
                #if requests.get(href):
                edges.append({'source':url, 'target':href, 'value':2})
                if not href in links:
                    nodes.append({'id':href, 'group':1})
                    links.append(href)

def crawl(url, max_iterations=6):
    """
    Param: URL from a website | max_iteration defines how deep we extract links
    return a sorted list of all the internal urls
    """
    curr_iteration = 0
    nodes.append({'id':url, 'group':1})
    links.append(url)
    for link in links:
        curr_iteration+=1
        print(curr_iteration)
        if curr_iteration<=max_iterations:
            get_website_links(link)
        else: break
    return edges

crawl('https://infallible-varahamihira-e94f86.netlify.app/')

#==========================================================
#networkX section

import networkx as nx
import matplotlib.pyplot as plt
#create a directed graph
G = nx.DiGraph()

#add the nodes to the graph G with attributes
for node in nodes:
    G.add_node(node['id'], group=node['group'])

#add edges to the graph G with wheights
for edge in edges:
    G.add_edge(edge['source'], edge['target'], value=edge['value'])

nx.write_edgelist(G, 'edge.txt')
"""
node_color = []
# for each node in the graph
for node in G.nodes(data=True):

    if 1 == node[1]['group']:
        node_color.append('blue')

node_size=[]
for node in G.nodes(data=True):
    if 1 == node[1]['group'] :
        node_size.append(500*1)
"""

"""
edge_color=[]

for edge in G.edges(data=True):
    if edge[2]['value']==1:
        edge_color.append('violet')
    if edge[2]['value']==2:
        edge_color.append('gray') 
"""

nx.draw(G, with_labels=False, width=2)
plt.show()
