"""import networkx as nx
import link_extractor as extractor
import matplotlib.pyplot as plt

links = extractor.crawl('https://infallible-varahamihira-e94f86.netlify.app')
#links = [1,2,3,4,5,6,7,8,9,10]
G = nx.Graph()
G.add_nodes_from(links)

plt.subplot(122)

nx.draw(G, with_labels=True, font_weight='bold')
#plt.subplot(122)
#nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')

plt.show()
print(list(G.nodes))"""