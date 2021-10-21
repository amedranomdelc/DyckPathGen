#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 14:41:41 2021

@author: amedranomdelc
"""
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        
def dyckPathsGraph(m: int, n: int):
    root = Node([{
        0: False,
        1: False,
        2: False
        }, 0, 0], None, None, None)
    
    queue = [root]
    for node in queue:
        x = node.val[1]
        y = node.val[2]
        if x + y < m + n:
            if x < m and 0 <= n*(x + 1) - m*(y):
                node.left = Node([{
                    0: False,
                    1: False,
                    2: False
                    }, x + 1, y], None, None, node)
                queue.append(node.left)
                
            if y < n and 0 <= n*(x) - m*(y + 1):
                node.right = Node([{
                    0: False,
                    1: False,
                    2: False
                    }, x, y + 1], None, None, node)
                queue.append(node.right)

    return root

def dyckPathsString(m: int, n: int):
    root = dyckPathsGraph(m, n)
    current = root
    builder = []
    ans = []
    
    while True:
        if current.val[0][0] == False:
            if current.left:
                current.val[0][0] = True
                current = current.left
                builder.append("0")
            else:
                current.val[0][0] = True
                
        elif current.val[0][1] == False:
            if current.right:
                current.val[0][1] = True
                current = current.right
                builder.append("1")
            else:
                current.val[0][1] = True
            
        elif current.val[0][2] == False:
            if current.val[1] + current.val[2] == m + n:
                ans.append("".join(builder))
                
            if current.parent:
                current.val[0][2] = True
                current = current.parent
                builder.pop()
            else:
                break
    
    return ans


m = int(input("Enter width:"))
n = int(input("Enter height:"))

if type(m) != int or type(n) != int:
    print("Please enter positive integer values which sum up to 16")
elif n < 1 or m < 1 or m + n > 17:
    print("Please enter positive integer values which sum up to 16")
else:
    strings = dyckPathsString(m, n)
    if m == 1 or n == 1:
        print("Here's the single Dyck path on a "+ str(m) + " x " + str(n) + " board. Enjoy!")
    else:
        print("Here are the " + str(len(strings)) + " Dyck paths on a "+ str(m) + " x " + str(n) + " board. Enjoy!")
    for string in strings:
        coord = [(0, 0)]
        for i in range(len(string)):
            if string[i] == "0":
                vertex = (coord[-1][0] + 1, coord[-1][1])
                coord.append(vertex)
            else:
                vertex = (coord[-1][0], coord[-1][1] + 1)
                coord.append(vertex)
        zip(*coord)
        plt.figure(figsize=(m+.5,n+.5))
        plt.plot(*zip(*coord))
        y = np.linspace(0, n, 10)
        x = np.linspace(0, m, 10)
        plt.plot(x, (n/m)*x, "-r")
        plt.axis("equal")
        plt.xticks(np.arange(0,m + 1,1))
        plt.yticks(np.arange(0,n + 1,1))
        plt.xlim(0, m)
        plt.ylim(0, n)
        plt.show()