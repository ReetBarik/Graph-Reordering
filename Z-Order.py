# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 07:20:30 2020

@author: reetb
"""


def decToBin(n, pad):
    s = format(n, pad)
    s = s[2:]
    s = list(s)
    return s

def padding(nodeEmbedding):
    pad = len(bin(max(nodeEmbedding)))
    return '#0' + str(pad) + 'b'

def generateZOrder(binaryList):
    bin = ''
    for i in range(len(binaryList[0])):
        for j in range(len(binaryList)):
            bin += binaryList[j][i]
    return int(bin,2)

def main():
    nodeEmbedding = [3, 2, 3, 2, 3]
    binaryList = []
    pad = padding(nodeEmbedding)
    
    for i in reversed(range(len(nodeEmbedding))):
        binaryList.append(decToBin(nodeEmbedding[i], pad))
        
    z = generateZOrder(binaryList)
    print(z)
    
if __name__ == "__main__":
    main()