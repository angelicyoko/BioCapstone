import csv
import json
import matplotlib.pyplot as plt
import networkx as nx

######################### READ DATA #########################
from graph import degree_help

data = []
with open('Dataset2.csv', encoding='utf-8', mode='r') as csvFile:
    read = csv.reader(csvFile)
    # start to record when begin = 3
    begin = 0
    for line in read:
        if begin >= 3:
            sub = {}
            sub["start"] = str(line[1]) + "_" + str(line[0])
            sub["target"] = str(line[3]) + "_" + str(line[2])
            sub["data_type"] = str(line[4]) if len(line[4]) != 0 else ""
            sub["binned_strength"] = int(line[5]) if len(line[5]) != 0 else ""

            tuple_sub = (sub["start"], sub["target"], sub["binned_strength"])
            data.append(tuple_sub)
        begin += 1

################# STORE DATA INTO NETWORKX ##################
### you will need variable "data" which will be a list of a bunch of tuples
### For example: data = [('MOB_one', 'MOB_one', 0), ('MOB_one', 'MOB_two', 0)...]
### tuple[0] is the start node
### tuple[1] is the target node
### tuple[2] is the weight (has already been casted to int)
graph = nx.MultiDiGraph()
for line in data:
    if (line[2] != ""):
        graph.add_edge(line[0], line[1], weight=line[2])
# Uncomment this to show a basic plot of the graph
# nx.draw(graph)
# plt.show()

# List of 77 nodes that are included in the Degree and Strength Graphs Dataset
seventy_seven_nodes = ["ECT", "VISp", "VISal", "TEa", "VISpm", "SSs", "VISam", "VISrl", "SSp", "AUDv", "6b", "MOp",
                       "VISlm", "AUDp", "PTLp", "AUDpo", "VISpl", "AUDd", "VISli", "VISll", "VISlla", "ENTl", "ORBm",
                       "PERI", "PIR", "LA", "AIp", "PL", "BLAp", "ENTm", "EPd", "ILA", "BLAa", "COApm", "AIv", "CA1v",
                       "VISC", "AId", "AOA", "TR", "GU", "EPv", "PAA", "NLOT", "BMAp", "SUBv", "BMAa", "CA3", "COApl",
                       "COAa", "NLOT3", "CA1d", "TTd", "SUBd", "PA", "MOB", "TTv", "DG", "CA2", "IG", "AOB", "FC",
                       "MOs", "RSPd", "CLA", "ACAv", "ORBv", "RSPv.a", "ACAd", "ORBvl", "RSPv.b/c", "PAR", "POST",
                       "RSPagl", "PRE", "ORBl", "RSPv", "ECT", "VISp", "VISal", "TEa", "VISpm", "SSs", "VISam", "VISrl",
                       "SSp", "AUDv", "6b", "MOp", "VISlm", "AUDp", "PTLp", "AUDpo", "VISpl", "AUDd", "VISli", "VISll",
                       "VISlla", "ENTl", "ORBm", "PERI", "PIR", "LA", "AIp", "PL", "BLAp", "ENTm", "EPd", "ILA", "BLAa",
                       "COApm", "AIv", "CA1v", "VISC", "AId", "AOA", "TR", "GU", "EPv", "PAA", "NLOT", "BMAp", "SUBv",
                       "BMAa", "CA3", "COApl", "COAa", "NLOT3", "CA1d", "TTd", "SUBd", "PA", "MOB", "TTv", "DG", "CA2",
                       "IG", "AOB", "FC", "MOs", "CLA", "RSPd", "ACAv", "ORBv", "ACAd", "RSPv.a", "RSPv.b/c", "POST",
                       "RSPagl", "PAR", "PRE", "ORBl", "ORBvl", "RSPv"]

####################### DEGREE GRAPH ########################
degree_help()

####################### STENGTH GRAPH #######################
# Dictionary objects holding strength values ie. { 'MOD' : 25, ... }
strengthIN = {}
strengthOUT = {}
for n in graph.nodes():  # Iterate through nodes in the graph
    node = n.split("_")[0]
    if node in seventy_seven_nodes:
        hemisphere = n.split("_")[1]
        sumIn = 0
        sumOut = 0
        # Iterate through all the in edges of a node
        # Calculate the total in strength
        # Only consider edges in hemisphere ie (one->one, left->left, right->right)
        for u, v, w in graph.in_edges(n, data=True):
            name = v.split("_")[0]
            if name in seventy_seven_nodes:
                hem = v.split("_")[1]
                if hem == "one" and hemisphere == "one":
                    sumIn += w.get("weight")
                elif hem == "left" and hemisphere == "left":
                    sumIn += w.get("weight")
                elif hem == "right" and hemisphere == "right":
                    sumIn += w.get("weight")
        # Iterate through all the out edges of a node
        # Calculate the total out strength
        # Only consider edges in hemisphere (one->one, left->left, right->right)
        for u, v, w in graph.out_edges(n, data=True):
            name = v.split("_")[0]
            if name in seventy_seven_nodes:
                hem = v.split("_")[1]
                if hem == "one" and hemisphere == "one":
                    sumOut += w.get("weight")
                elif hem == "left" and hemisphere == "left":
                    sumOut += w.get("weight")
                elif hem == "right" and hemisphere == "right":
                    sumOut += w.get("weight")
        # Making sure there are no repeat nodes in the dictonary
        # MOD_one and MOD_left = MOD in the dictonary
        if node in strengthIN:
            strengthIN[node] = strengthIN.get(node) + sumIn
        else:
            strengthIN[node] = sumIn
        if node in strengthOUT:
            strengthOUT[node] = strengthOUT.get(node) + sumOut
        else:
            strengthOUT[node] = sumOut

# print(len(strengthOUT.keys()))
# Input Strength Graph
plt.figure(figsize=(40, 10))
plt.bar(strengthIN.keys(), strengthIN.values())
plt.savefig('inStrength.png')
plt.xlabel('Nodes')
plt.ylabel('Strength')

# Output Strength
plt.figure(figsize=(40, 10))
plt.bar(strengthOUT.keys(), strengthOUT.values())
plt.savefig('outStrength.png')
plt.xlabel('Nodes')
plt.ylabel('Strength')

####################### Rich Club Analysis #######################
# TODO: Ashley
# rich club analysis is how densely a graph is connected, etc rich stick together
# nx.rich_club_coefficient(graph, normalized=True, Q=100, seed=None)
# NOTE: networkx rich club only works for undirected graphs
# found a research paper https://arxiv.org/abs/1103.2264 that takes a
# swing at directed rich club analysis, will try to understand their approach
