# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:43:43 2020

@author: reetb
"""
import itertools
import pandas as pd
from scipy.spatial import distance
import networkx as nx
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import os
os.chdir('C:/Local/Coursework/Graph Ordering Research')

G = nx.read_edgelist("cnr.edgelist", nodetype = int)

G = nx.Graph()
G.add_edges_from([(1, 2),(2, 3),(3, 4),(4, 5),(5, 6),(6, 1),(1, 13),(13, 14),(14, 7),(7, 8),(8, 9),(9, 10),(10, 11),(11, 12),(12, 7),(5, 3),(3, 1),(5, 1),(5, 2),(4, 6),(3, 6),(4, 1),(7, 9),(12, 10),(8, 11),(12, 9),(7, 10),(8, 12),(8, 10)])

#shortestPath = list(nx.all_pairs_shortest_path_length(G))
#
#shortestPath.sort(key=lambda x:x[0])

with open('cnr.emb', 'r') as file:
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
    
df = pd.DataFrame(columns = ['Node 1', 'Node 2', 'L2 Distance', 'Shortest Path'])
    
for i,j in itertools.combinations(range(len(data)), 2):
    df = df.append(pd.DataFrame([[i, j, distance.euclidean(data[i], data[j]), nx.shortest_path_length(G, i + 1, j + 1)]], columns = ['Node 1', 'Node 2', 'L2 Distance', 'Shortest Path']), ignore_index=True)
    
suffix = '24'
output = 'DimensionalityCorrelation' + suffix + '.png'
t = 'Number of Dimensions: ' + suffix

ax1 = df.plot.scatter(x='L2 Distance', y='Shortest Path', c='DarkBlue', title = t).get_figure().savefig(output, dpi = 100)

#df.to_csv('Dimensionality24.csv', index = False)