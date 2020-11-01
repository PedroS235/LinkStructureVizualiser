"""
This module is capable to extract all the links form a given URL
"""
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests

#variable to store the different nodes categorized by groups
nodes = [] # [{'id":'url', 'group':1}]
#variable to store the different edges categorized by values(wheights)
edges = [] # [{'source":'url1', 'target':'url2', 'value':1}]
links = []

value=1

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
    group_=1
    it=0
    for a_tag in soup.findAll('a'):
        it+=1
        group_+=1
        href = a_tag.get('href')
        if href !='' or href != None:
            href = urljoin(url, href)
            parsed_href = urlparse(href)
            href = parsed_href.scheme + '://' + parsed_href.netloc + parsed_href.path
            if isvalid(href) and domain_name in href:
                #if requests.get(href):
                if href in links:
                    edges.append({'source':url, 'target':href, 'value':2})
                else:
                    edges.append({'source':url, 'target':href, 'value':1})
                if not href in links:
                    #if requests.get(href): #I removed the checker for doubles
                    if(group_>=2):
                        group_ = 2
                    
                    nodes.append({'id':href, 'group':group_})
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

crawl('https://networkx.org/documentation/stable/reference/generators.html')

import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()

#add the nodes to the graph G with attributes
for node in nodes:
    G.add_node(node['id'], group=node['group'])

#add edges to the graph G with wheights
for edge in edges:
    G.add_edge(edge['source'], edge['target'], value=edge['value'])
"""
node_color = []
# for each node in the graph
for node in G.nodes(data=True):

    if 1 == node[1]['group']:
        node_color.append('blue')
    
    if 2 == node[1]['group']:
        node_color.append('orange')
    
    if 3 == node[1]['group']:
        node_color.append('yellow')
    if 4 == node[1]['group']:
        node_color.append('red')
    if 5 == node[1]['group']:
        node_color.append('green')
    if 6 == node[1]['group']:
        node_color.append('purple')
    if 7 == node[1]['group']:
        node_color.append('green')
    if 8 == node[1]['group']:
        node_color.append('purple')
    if 9 == node[1]['group']:
        node_color.append('green')
    if 10 == node[1]['group']:
        node_color.append('purple')

node_size=[]
for node in G.nodes(data=True):
    if 1 == node[1]['group'] :
        node_size.append(500*1)
    
    if 2 == node[1]['group']:
        node_size.append(200*1)
    
    if 3 == node[1]['group']:
        node_size.append(200*0.8)
    if 4 == node[1]['group']:
        node_size.append(200*0.7)
    if 5 == node[1]['group']:
        node_size.append(200*0.6)
    if 6 == node[1]['group']:
        node_size.append(200*0.5)
    if 7 == node[1]['group']:
        node_size.append(200*0.5)
    if 8 == node[1]['group']:
        node_size.append(200*0.5)
    if 9 == node[1]['group']:
        node_size.append(200*0.5)
    if 10 == node[1]['group']:
        node_size.append(200*0.5)
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
