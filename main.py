import link_extractor
import networkx as nx
import matplotlib.pyplot as plt


class link_structure_visualizer():
    def __init__(self):
        self.G = nx.DiGraph()
        self.set_G_edges('https://wwwfr.uni.lu')
        self.display()

    def set_G_edges(self, url):
        #self.G.add_nodes_from(link_extractor.get_nodes())
        self.G.add_edges_from(link_extractor.crawl(url, 1))


    def display(self):
        nodes = link_extractor.get_nodes()
        print(nodes)
        node_color = []
        for n in self.G.nodes():
            if n =='https://wwwfr.uni.lu':
                node_color.append('orange')
            elif n == 'https://wwwfr.uni.lu/etudiants/demandes_d_admission_reinscriptions':
                node_color.append('blue')
            
        nx.draw(self.G, with_labels=True, node_size=25, node_color='r', edge_color='b')
        plt.show()
       
link_structure_visualizer()

