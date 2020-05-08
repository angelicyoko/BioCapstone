import csv
import json
import matplotlib.pyplot as plt
import networkx as nx
#import bct
import numpy as np
from numpy import mean
import pandas as pd

######################### READ DATA #########################
from graph import graph_help, rich_club_wd

data = []
test = []
with open('Dataset2.csv', encoding='utf-8', mode='r') as csvFile:
	read = csv.reader(csvFile)
	begin = 0
	count = 0
	for line in read:
		if begin >= 3:
			sub = {}
			sub["start"] = str(line[1])
			sub["target"] = str(line[3])
			if str(line[0]) == str(line[2]):
				count += 1
				if sub['start'] == "" or sub['target'] == '':
					continue
				sub["binned_strength"] = int(line[5]) if len(line[5]) != 0 else ""
				if sub["binned_strength"] == '':
					break
				if sub["binned_strength"] == 0:
					continue
				tuple_sub_weight = (sub["start"], sub["target"], sub["binned_strength"])
				tuple_sub = (sub["start"], sub["target"])
				if tuple_sub not in test:
					test.append(tuple_sub)
					data.append(tuple_sub_weight)
		begin += 1

################# STORE DATA INTO NETWORKX ##################
### you will need variable "data" which will be a list of a bunch of tuples
### tuple[0] is the start node
### tuple[1] is the target node
### tuple[2] is the weight (has already been casted to int)
graph = nx.DiGraph()
for line in data:
	if (line[2] != ""):
		num = int(line[2])
		if(line[2] == 7):
			num = 10**0;
		elif(line[2] == 6):
			num= 10**-0.333;
		elif(line[2] == 5):
			num= 10**-0.66;
		elif(line[2] == 4):
			num= 10**-1;
		elif(line[2] == 3):
			num= 10**-2;
		elif(line[2] == 2):
			num= 10**-3;
		elif(line[2] == 1):
			num= 10**-4;
		else:
			num= 0;
		graph.add_edge(line[0], line[1], weight=num)

####################### DEGREE AND STRENGTH GRAPH ########################
graph_help(graph)

####################### Clustering Coefficient ###################
clustering_coeff = nx.average_clustering(graph, weight="weight")
#print(clustering_coeff)




####################### Average Shortest Path Length #####################



####################### Global Efficiency ###############################
efficiency_graph = nx.DiGraph()
for line in data:
	if (line[2] != ""):
		num = int(line[2])
		if(line[2] == 7):
			num = 10**0;
		elif(line[2] == 6):
			num= 10**-0.333;
		elif(line[2] == 5):
			num= 10**-0.66;
		elif(line[2] == 4):
			num= 10**-1;
		elif(line[2] == 3):
			num= 10**-2;
		elif(line[2] == 2):
			num= 10**-3;
		elif(line[2] == 1):
			num= 10**-4;
		else:
			num= 0;
		num = -math.log(num)
		efficiency_graph.add_edge(line[0], line[1], weight=num)

total_path_length = 0
path_number = 0
all_paths = nx.all_pairs_dijkstra_path_length(efficiency_graph)
for n in all_paths:
	for target in n:
		if (type(target) is dict):
			for length in target:
				if (target[length] != 0):
					total_path_length = total_path_length + 1/target[length]
					path_number = path_number + 1
print("Global Efficiency: " + str(total_path_length/path_number))


 
####################### Rich Club Analysis #######################
# TODO: Ashley
# rich club analysis is how densely a graph is connected, etc rich stick together
# nx.rich_club_coefficient(graph, normalized=True, Q=100, seed=None)
#Note that graphs must be passed in as numpy.array rather than numpy.matrix. Other constraints/edge cases of the adjacency matrices
#(e.g. self-loops, negative weights) behave similarly to the matlab functions.
array_Graph = nx.to_numpy_array(graph) * 10000

#print(array_Graph)
#bct.richclub weighted and directed returns a vector of the rc coefficients for level 1
#print(rich_club_wd(array_Graph, None))
yoko = rich_club_wd(array_Graph, None)
l = [x for x in yoko if pd.notnull(x) and x >= 0.99]
np.set_printoptions(threshold=np.inf)
for x in l:
	print(x)

print("Total Nodes: ", len(l))
print("Mean: ",mean(l))


# check to see if bct weighted directed clustering is the same as ours
# print(mean(bct.clustering_coef_wd(array_Graph)))
# NOTE: networkx rich club only works for undirected graphs
# found a research paper https://arxiv.org/abs/1103.2264 that takes a
# swing at directed rich club analysis, will try to understand their approach



