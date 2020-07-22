# -*- coding: utf-8 -*-
"""
Created on Fri May 15 13:14:11 2020

@author: reetb
"""
import pandas as pd
import numpy as np
from scipy.spatial import distance
import networkx as nx
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import os
os.chdir('C:/Local/Coursework/Graph Ordering Research')

dataset = 'karate'

#G = nx.Graph(create_using = nx.DiGraph)
#G.add_edges_from([(1, 2),(2, 3),(3, 4),(4, 5),(5, 6),(6, 1),(1, 13),(13, 14),(14, 7),(7, 8),(8, 9),(9, 10),(10, 11),(11, 12),(12, 7),(5, 3),(3, 1),(5, 1),(5, 2),(4, 6),(3, 6),(4, 1),(7, 9),(12, 10),(8, 11),(12, 9),(7, 10),(8, 12),(8, 10)])


# ------------------- Following segment needs to be executed just once ------------------- #

G = nx.read_edgelist(dataset + ".edgelist", nodetype = int)

# Relabel nodes to start from zero
G = nx.convert_node_labels_to_integers(G, first_label = 0)    

#nx.write_edgelist(G,'test.edgelist', data=False)

df = pd.DataFrame(columns = ['Node 1', 'Node 2', 'Shortest Path'])

# setting the BFS depth
depth = 5
count = 0

# iterate over all nodes of the graph
for n in list(G):
    count += 1
    # BFS from Node 'n' till a depth of 'depth'
    l = list(nx.bfs_edges(G, source = n, depth_limit = depth))
    # flatten list of tuples (edges)
    l = [e for ele in l for e in ele]
    # List of all nodes visited (including 'n')
    l = set(l)
    l.remove(n)
    
    for i in l:
        if (i < n):
            # finding shortest path length for all (n, i) pair
            df = df.append(pd.DataFrame([[n, i, nx.shortest_path_length(G, i, n)]], columns = ['Node 1', 'Node 2', 'Shortest Path']), ignore_index=True)
    print('-----------------------')
    print(count)
    
df['Shortest Path'] = pd.to_numeric(df['Shortest Path'])

# ----------- Following segment to be excuted repeatedly for different l and d ----------- #
            
choice = 0
suffix = '16'

with open(dataset + '.emb', 'r') as file:
    data = file.read().replace('\n', ',')

data = data.split(',')

for i in range(len(data)):
    data[i] = data[i].split(' ')
    
data.pop(0)
data.pop(-1)

def node(e):
    return int(e[0],10)

data.sort(key = node)

for i in range(len(data)):
    data[i].pop(0)
    data[i] = [float(x) for x in data[i]]
    
# 'data' now has the embedding vector of node i at the i-th row

euclidean = []

for index, row in df.iterrows():
    euclidean.append(distance.euclidean(data[row['Node 1']], data[row['Node 2']]))

# Appending the L2 distance of the embeddings of each node pair in each row of the dataframe    
df['L2 Distance'] = euclidean    

grouped = df.groupby('Shortest Path')

stat = grouped['L2 Distance'].agg([np.mean, np.std])

if choice == 1:
    output = 'WalkLengthCorrelationStat' + suffix + '.png'
    t = 'Length of Walk: ' + suffix
else:
    output = 'DimensionalityCorrelationStat' + suffix + '.png'
    t = 'No of Dimensions: ' + suffix

ax1 = stat.plot(style=['o-','rx-'], title = t)
ax1.set_ylabel("L2 Distance")
ax1.get_figure().savefig(output, dpi = 100)

#ax1 = df.plot.scatter(x = 'L2 Distance', y = 'Shortest Path', c = 'DarkBlue', title = t).get_figure().savefig(output, dpi = 100)
