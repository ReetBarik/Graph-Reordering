# -*- coding: utf-8 -*-
"""
Created on Tue May 12 17:08:49 2020

@author: reetb
"""

import os
os.chdir('C:/Local/Coursework/Graph Ordering Research')
import matplotlib.pyplot as plt
plt.style.use('ggplot')

import pandas as pd 

suffix = '24'

datafile = "Dimensionality" + suffix + ".csv"
output = 'DimensionalityCorrelation' + suffix + '.png'
t = 'Number of Dimensions: ' + suffix
dt = data = pd.read_csv(datafile)

ax1 = dt.plot.scatter(x='L2 Distance', y='Shortest Path', c='DarkBlue', title = t).get_figure().savefig(output, dpi = 100)

#x = ['250k', '500k', '750k', '1m', '1.25m', '1.5m', '1.75m', '2m', '2.25m', '2.5m']
#
#y = [4.3, 10.08, 15.91, 21.79, 28.5, 35.73, 41.07, 49.5, 56.2, 63.1]
#
#plt.plot(y, marker = 'o')
#plt.xticks(range(10) ,x)
#plt.ylabel('Time taken in seconds')
#plt.xlabel('Number of edges in input graph')
#plt.title('Scaling of Node2vec for different sized input graph')
#
#plt.savefig('Scaling.png', dpi = 100)