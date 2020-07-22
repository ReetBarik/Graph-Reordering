# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
os.chdir('C:/Local/Coursework/Graph Ordering Research/Vertex Ordering Presentation 2/Resources')

import matplotlib.pyplot as plt
plt.style.use('ggplot')

x = [1750, 8214, 1260, 34, 2, 100, 8, 7300, 5162, 10000]
y = [27.3, 24.5, 16.7, 21.22, 23.07, 24, 20.05, 22.28, 26.2, 25.7]

y[:] = [num / max(y) for num in y]

y[:] = [1 - num for num in y]

n = ['MINLA(SA)', 'MLOGA(SA)', 'Gorder', 'RCM', 'DegSort', 'Rabbit', 'CHDFS', 'Slashburn', 'LDG', 'METIS']

z = [160, 160, 240, 400, 480, 640, 400, 80, 320, 560]

fig, ax = plt.subplots()
ax.scatter(x, y, s = z)

for i, txt in enumerate(n):
    ax.annotate(txt, (x[i], y[i]))
    
plt.xlabel('Cost of Reordering')
plt.ylabel('Quality of Reordering')
plt.title('Vertex Reordering Algorithm Space')

plt.savefig('ReorderingPlots.PNG', dpi = 1000)