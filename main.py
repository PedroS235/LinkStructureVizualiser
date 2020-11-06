import graph
import webScrapper

class Main():
    def __init__(self):
        url = 'https://infallible-varahamihira-e94f86.netlify.app/'
        ws = webScrapper.WebScrapper(url)
        self.nodes = ws.getNodes()
        self.edges = ws.getEdges()
        graph.Graph(self.nodes, self.edges)
Main()      
