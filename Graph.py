"""
This class creates a graph with the help of the library networkX and
then shows the graph in a visual image with the help of the library Matplotlib
"""
import networkx as nx
from matplotlib import pyplot as plt

class Graph():
    def __init__(self):
        """
        This is the constructor of this class Graph
        input: a list of nodes and edges to create a graph
        """
        #create an empty directed graph
        self.G = nx.DiGraph()

    def createNodeWAttr(self):
        """
        This functions add nodes to the graph 'G' with attributes size and color RGB
        """
        count = 0
        r=0
        g=1
        b=0
        for node in self.nodes:
            for edge in self.edges:
                if edge[0] == node:
                    count+=1
            self.G.add_node(node, size=count, r=r, g=g, b=b)

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

    def createEdgeWAttr(self):
        """
        This function add edges to the graph 'G' with attributes color RGB
        """
        r=0
        g=0.8
        b=0
        prev_edge = self.edges[0][0]
        self.G.add_edge(prev_edge, self.edges[0][1], r=r, g=g, b=b)
        for e in range(1, len(self.edges)):
            if e == len(self.edges)-2:
                if prev_edge != self.edges[e+1][0]:
                    if g>=0.2:
                        g-=0.2
                    elif r<=0.8:
                        r+=0.2
                    elif b<=0.8:
                        b+=0.2
                    else:
                        g = 0.5
                        b=0.5
                self.G.add_edge(self.edges[e+1][0], self.edges[e+1][1], r=r, g=g, b=b)         
                self.G.add_edge(self.edges[e][0], self.edges[e][1], r=r, g=g, b=b)         
            else:
                if prev_edge != self.edges[e][0]:
                    if g>=0.2:
                        g-=0.1
                    elif r<=0.8:
                        r+=0.1
                    elif b<=0.8:
                        b+=0.1
                    else:
                        g = 0.5
                        b=0.5
                    prev_edge = self.edges[e][0]
                self.G.add_edge(self.edges[e][0], self.edges[e][1], r=r, g=g, b=b)
                
    def drawGraph(self, nodes, edges, colorNodes_state='On', colorEdge_state='Off'):
        """
        This function will draw the graph 'G' and will assign
         the different parameters to the draw function
        """
        #define the variables
        self.nodes = nodes
        self.edges = edges

        #calls the function createNodesWAttr() to add the nodes to the graph 'G'
        self.createNodeWAttr()

        #creates a list with the corresponding sizes for nodes
        node_size=[]
        for node in self.G.nodes(data=True):
            node_size.append(300+10*node[1]['size'])

        if colorNodes_state == "On":
            #creates a list with corresponding colors for the nodes
            node_color=[]
            for node in self.G.nodes(data=True):
                node_color.append((node[1]['r'], node[1]['g'], node[1]['b']))
        else: 
            self.G.add_nodes_from(self.nodes)

        if colorEdge_state == "On":
            #calls the function createEdgesWAttr() to add the edges to the graph 'G'
            self.createEdgeWAttr()

            #creates a list with the corresponding colors for the edges
            edge_color=[]
            for edge in self.G.edges(data=True):
                edge_color.append((edge[2]['r'], edge[2]['g'], edge[2]['b']))
        else:
            #Adds the edges to the graph
            self.G.add_edges_from(self.edges)

        #draws the graph 'G'
        if colorNodes_state == 'On' and colorEdge_state == 'On':
            nx.draw(self.G, with_labels=False, width=2, node_size=node_size, node_color=node_color, edge_color=edge_color)
   
        elif colorNodes_state == 'On' and colorEdge_state == 'Off':
            nx.draw(self.G, with_labels=False, width=2, node_size=node_size, node_color=node_color)

        elif colorNodes_state == 'Off' and colorEdge_state == 'On':
            nx.draw(self.G, with_labels=False, width=2, node_size=node_size, edge_color=edge_color)
            
        else:
            nx.draw(self.G, with_labels=False, width=2, node_size=node_size)

    def showGraph(self):
        #show the graph 'G' with matplotlib
        plt.show()