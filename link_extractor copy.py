"""
This module is capable to extract all the links form a given URL
"""
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests
import networkx as nx
import matplotlib.pyplot as plt

#variable to store the different nodes categorized by groups (for graph)
nodes = [] # [{'id":'url', 'group':1}]
edges=[]

#create a directed graph
G = nx.DiGraph()

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
            parsed_href = urlparse(href)
            href = parsed_href.scheme + '://' + parsed_href.netloc + parsed_href.path
            if isvalid(href) and domain_name in href:
                #checks if the href(url) is not broken
                #if requests.get(href):
                
                edges.append((url, href))
                if href not in nodes:
                    nodes.append(href)

def crawl(url, max_iterations=1):
    """
    Param: URL from a website | max_iteration defines how deep we extract links
    return a sorted list of all the internal urls
    """
    curr_iteration = 0
    nodes.append(url)
    for node in nodes:
        curr_iteration+=1
        #print(curr_iteration)
        if curr_iteration<=max_iterations:
            get_website_links(node)
        else: break

crawl('https://www.python.org')



def setNodeAttr():
    count = 0
    r=0
    g=0.8
    b=0
    for node in nodes:
        for edge in edges:
            if edge[0] == node:
                count+=1
        G.add_node(node, size=count, r=r, g=g, b=b)
        
        if g>=0.2:
            g-=0.2
        elif r<=0.8:
            r+=0.2
        elif b<=0.8:
            b+=0.2
        else:
            g = 0.5
            b=0.5
        count=0

def setEdgeAttr():
    r=0
    g=1
    b=0
    prev_edge = edges[0][0]
    G.add_edge(edges[0][0], edges[0][1], r=r, g=g, b=b)
    for e in range(1, len(edges)-1):
        if e == len(edges)-2:
            if prev_edge != edges[e+1][0]:
                if g>=0.2:
                    g-=0.2
                elif r<=0.8:
                    r+=0.2
                elif b<=0.8:
                    b+=0.2
                else:
                    g = 0.5
                    b=0.5
            G.add_edge(edges[e+1][0], edges[1+1][1], r=r, g=g, b=b)
        else:
            if prev_edge != edges[e][0]:
                if g>=0.2:
                    g-=0.2
                elif r<=0.8:
                    r+=0.2
                elif b<=0.8:
                    b+=0.2
                else:
                    g = 0.5
                    b=0.5
            G.add_edge(edges[e][0], edges[e][1], r=r, g=g, b=b)
                    
setEdgeAttr()
#G.add_edges_from(edges)
setNodeAttr()

print(G.nodes())
node_size=[]
for node in G.nodes(data=True):
    node_size.append(300+10*node[1]['size'])

node_color=[]
for node in G.nodes(data=True):
    node_color.append((node[1]['r'], node[1]['g'], node[1]['b']))

edge_color=[]
for edge in G.edges(data=True):
    edge_color.append((edge[2]['r'], edge[2]['g'], edge[2]['b']))

nx.draw(G, with_labels=False, width=2, node_size=node_size, node_color=node_color, edge_color=edge_color)
plt.show()

#==========================================================
#networkX section
"""
#add the nodes to the graph G with attributes
for node in nodes:
    G.add_node(node['id'], group=node['group'])

#add edges to the graph G with wheights
for edge in edges:
    G.add_edge(edge['source'], edge['target'], value=edge['value'])

nx.write_edgelist(G, 'edge.txt')
"""
"""
node_color = []
# for each node in the graph
for node in G.nodes(data=True):

    if 1 == node[1]['group']:
        node_color.append('blue')
"""

"""
edge_color=[]

for edge in G.edges(data=True):
    if edge[2]['value']==1:
        edge_color.append('violet')
    if edge[2]['value']==2:
        edge_color.append('gray') 
"""

