#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 16:21:57 2018

@author: JmLozano
"""
# M[i]=[stage(0),parent(1),nodes_cond(2),path_nodes(3),path_coeff(4),net_coeff(5)]
import networkx as nx

'''
    0. CREATE GRAPH
'''

G = nx.Graph()
'''                                    # Create graph
elist = [(1, 2, 1),                                    # List edges and weights
         (1, 3, 1),
         (2, 4, 1),
         (2, 5, 1),
         (3, 4, 2),
         (3, 5, 2),
         (4, 6, 1),
         (5, 6, 1)]

'''

elist = [(1, 2, 1),                                    # Easier graph to try
         (1, 3, 1),
         (2, 4, 1),
         (3, 4, 2)]

G.add_weighted_edges_from(elist)                   # Add edges to graph
p = [0.1]*len(G.nodes)                               # Nodes' probability of failure


'''
    1. CLASS Stage
'''


class Stage:
    name = None
    parent = 0
    path_exists = False
    path_nodes = []
    scenario = []
    path_coeff = 0.0
    net_coeff = 0.0
    num_stages = 0
    # Constructor

    def __init__(self, name=None, parent=0, path_exists=False, path_nodes=[], scenario=[], path_coeff=0.0, net_coeff=0.0):
        self.name = name
        self.parent = parent
        self.path_nodes = path_nodes
        self.scenario = scenario
        self.path_coeff = path_coeff
        self.net_coeff = net_coeff
        Stage.num_stages += 1            # Increment the number of stages when adding a new stage

    # Methods


'''
    2. TREE FUNCTIONS
'''


def name_list(list):                        # Function to get all names from a tree
    group = []
    for i in range(len(list)):
        group.append(list[i].name)
    return group


def parent_list(list):                      # Function to get all scenarios from a tree
    group = []
    for i in range(len(list)):
        group.append(list[i].parent)
    return group


def path_exists_list(list):                 # Function to get all existance of paths from a tree
    group = []
    for i in range(len(list)):
        group.append(list[i].path_exists)
    return group


def path_nodes_list(list):                  # Function to get all path nodes from a tree
    group = []
    for i in range(len(list)):
        group.append(list[i].path_nodes)
    return group


def scenarios(list):                        # Function to get all scenarios from a tree
    group = []
    for i in range(len(list)):
        group.append(list[i].scenario)
    return group


# Build lists for coefficients
'''
    4. EXAMPLE PRINTS
'''
'''
tree = {'stage': [1], 'parent': [0], 'exist_path': [False],
        'sp_nodes': [[1, 2, 4, 6]], 'scenario': [['*']*len(G.nodes)]}
tree['stage'].append(2)  # To insert items into de dictionary
tree['scenario'].append([1, '*', '*', '*', '*', '*'])
scenario = tree['scenario'][0].copy
# print(tree['scenario'][1])
'''
tree = []
s1 = Stage(name=1, parent=0, path_exists=True, path_nodes=nx.shortest_path(G, 1, 4, weight='weight'), scenario=['*']*len(G.nodes), path_coeff=0.9**4, net_coeff=1)
s2 = Stage(s1.__dict__)   # Creates a copy of s1
s2.name = 2
s2.parent = 1
s2.path_nodes = [1, 1, 1, 1]
s3 = Stage(path_nodes=[2, 3, 4, 6])         # Creates an object just chaging the path_nodes from the original attributes
s4 = Stage(path_nodes=[1, 2, 4, 6])
tree = [s1, s2, s3, s4]

print(path_nodes_list(tree))
print(s1.__dict__)
print(s2.__dict__)
'''
for i in range(len(tree)):                  # Method to get all shortest pathnodes
    print(tree[i].sp_nodes)

print(help(Stage))                          #Get all class information
'''
