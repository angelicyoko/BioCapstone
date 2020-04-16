import csv
import json
import matplotlib.pyplot as plt
import networkx as nx

######################### READ DATA #########################
from graph import graph_help

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
print(clustering_coeff)




####################### Average Shortest Path Length #####################



####################### Global Efficiency ###############################



 
####################### Rich Club Analysis #######################
# TODO: Ashley
# rich club analysis is how densely a graph is connected, etc rich stick together
# nx.rich_club_coefficient(graph, normalized=True, Q=100, seed=None)
# NOTE: networkx rich club only works for undirected graphs
# found a research paper https://arxiv.org/abs/1103.2264 that takes a
# swing at directed rich club analysis, will try to understand their approach
