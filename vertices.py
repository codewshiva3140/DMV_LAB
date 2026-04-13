import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G = nx.Graph()

# Add vertices (nodes)
G.add_nodes_from([1, 2, 3, 4])

# Add edges (connections)
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Draw graph
nx.draw(G, with_labels=True, node_color='lightblue', node_size=2000)

plt.title("Graph with Vertices and Edges")
plt.show()
