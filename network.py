import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

network = nx.DiGraph()



valid_airports_file = open("covid_data.txt", "r")
valid_airports = {}

k = valid_airports_file.readline()
while k:
    curr = k.split(" ")
    try:
        valid_airports[curr[0]] = float(curr[1])
    except:
        print(k)
    k = valid_airports_file.readline()
    

in_file = open("flights.txt", "r")

line = in_file.readline()

while line:
    curr = line.split(" ")
    if not curr[2] == "" and curr[0] in valid_airports and curr[1] in valid_airports:
        network.add_edge(curr[0], curr[1], weight=float(curr[2]))
    line = in_file.readline()

print(network)

# connectivity = nx.all_pairs_node_connectivity(network)

# out_file = open("connectivity_clean.txt", "w")
# cleaned_data = {}
# for i in connectivity:
#     for k in connectivity[i]:
#         curr1 = i + " " + k
#         curr2 = k + " " + i
#         if (curr1 in cleaned_data) or (curr2 in cleaned_data):
#             continue
#         else:
#             cleaned_data[curr1] = connectivity[i][k]

# for j in cleaned_data:
#     out_file.write(j)
#     out_file.write(" ")
#     out_file.write(str(cleaned_data[j]))
#     out_file.write("\n")


# centrality = nx.betweenness_centrality(network)
# out_file = open("betweenness_full.txt", "w")
# for i in centrality:
#     out_file.write(i)
#     out_file.write(" ")
#     out_file.write(str(centrality[i]))
#     out_file.write("\n")


file = open("covid_data.txt")
line = file.readline()
tot_flights = {}

while line:
    tot_flights[line[0:3]] = float(line[4:])
    line = file.readline()

node_sizes = {}
for i in network.nodes():
    try:   
        node_sizes[i] = tot_flights[i]
    except:
        continue

sizes = []
for i in node_sizes:
    sizes.append(node_sizes[i] * 1000000)
print(str(len(sizes)))

fig = plt.figure()
ax = fig.add_subplot(111)
nx.draw_networkx(network, node_size=sizes, font_size=5)
plt.savefig("graph_with_sizes_covid.png")





# pos = nx.spring_layout(network, dim=3, seed=779)
# # Extract node and edge positions from the layout
# node_xyz = np.array([pos[v] for v in sorted(network)])
# edge_xyz = np.array([(pos[u], pos[v]) for u, v in network.edges()])

# # Create the 3D figure
# fig = plt.figure(frameon=False)
# ax = fig.add_subplot(111, projection="3d")

# # Plot the nodes - alpha is scaled by "depth" automatically
# ax.scatter(*node_xyz.T, s=100, ec="w")

# # Plot the edges
# for vizedge in edge_xyz:
#     ax.plot(*vizedge.T, color="tab:gray")


# def _format_axes(ax):
#     """Visualization options for the 3D axes."""
#     # Turn gridlines off
#     ax.grid(False)
#     # Suppress tick labels
#     for dim in (ax.xaxis, ax.yaxis, ax.zaxis):
#         dim.set_ticks([])


# _format_axes(ax)
# #fig.tight_layout()
# plt.savefig("3dgraph2.png")