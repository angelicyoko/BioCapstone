import csv
import json
import networkx as nx
import matplotlib.pyplot as plt

######################### READ DATA #########################

def degree_help():
	print("we in degree help")
	data = []
	test = []
	with open('Dataset2.csv', encoding='utf-8', mode='r') as csvFile:
		read = csv.reader(csvFile)
		# start to record when begin = 3
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
						#	find = [i for i, v in enumerate(data) if v[0] == sub["start"] and v[1] == sub["target"]]
						#	find = find[0]
						#	y = list(data[find])
						#	y[2] += sub["binned_strength"]
						#	data[find] = tuple(y)
						# else:
						test.append(tuple_sub)
						data.append(tuple_sub_weight)
			begin += 1
		print("count is: " + str(count))

	## To Json ##

	# with open('final.json', 'w', encoding='utf-8') as f:
	#     json.dump(data, f, indent = 4)

	## read data ##
	'''
	f = open('out.json',)
	tuples = json.load(f)
	data = []
	for tupl in tuples: 
	    t = (tupl[0], tupl[1], tupl[2])
		data.append(t)
	f.close()
	'''

	# f = open('out.json',)
	# data = json.load(f)
	# f.close()

	################# STORE DATA INTO NETWORKX ##################
	### you will need variable "data" which will be a list of a bunch of tuples
	### For example: data = [('MOB_one', 'MOB_one', 0), ('MOB_one', 'MOB_two', 0)...]
	### tuple[0] is the start node
	### tuple[1] is the target node
	### tuple[3] is the weight (has already been casted to int)

	### Jack's TODO ###
	graph = nx.MultiDiGraph()
	for line in data:
		graph.add_edge(line[0], line[1], weight=line[2])
	# print("number of nodes: " + str(len(G.nodes())))
	# print("number of edges: " + str(G.number_of_edges()))
	# print("out degree: " + str(G.out_degree('FC')))
	# print("in degree: " + str(G.in_degree('FC')))
	# Uncomment this to show a basic plot of the graph
	# nx.draw(graph)
	# plt.show()

	####################### DEGREE GRAPH ########################
	### Ashley's TODO ###
	# List of 77 nodes that are included
	nodesI = ["ECT", "VISp", "VISal", "TEa", "VISpm", "SSs", "VISam", "VISrl", "SSp", "AUDv", "6b", "MOp", "VISlm",
			  "AUDp", "PTLp", "AUDpo", "VISpl", "AUDd", "VISli", "VISll", "VISlla", "ENTl", "ORBm", "PERI", "PIR", "LA",
			  "AIp", "PL", "BLAp", "ENTm", "EPd", "ILA", "BLAa", "COApm", "AIv", "CA1v", "VISC", "AId", "AOA", "TR",
			  "GU", "EPv", "PAA", "NLOT", "BMAp", "SUBv", "BMAa", "CA3", "COApl", "COAa", "NLOT3", "CA1d", "TTd",
			  "SUBd", "PA", "MOB", "TTv", "DG", "CA2", "IG", "AOB", "FC", "MOs", "RSPd", "CLA", "ACAv", "ORBv",
			  "RSPv.a", "ACAd", "ORBvl", "RSPv.b/c", "PAR", "POST", "RSPagl", "PRE", "ORBl", "RSPv", "ECT", "VISp",
			  "VISal", "TEa", "VISpm", "SSs", "VISam", "VISrl", "SSp", "AUDv", "6b", "MOp", "VISlm", "AUDp", "PTLp",
			  "AUDpo", "VISpl", "AUDd", "VISli", "VISll", "VISlla", "ENTl", "ORBm", "PERI", "PIR", "LA", "AIp", "PL",
			  "BLAp", "ENTm", "EPd", "ILA", "BLAa", "COApm", "AIv", "CA1v", "VISC", "AId", "AOA", "TR", "GU", "EPv",
			  "PAA", "NLOT", "BMAp", "SUBv", "BMAa", "CA3", "COApl", "COAa", "NLOT3", "CA1d", "TTd", "SUBd", "PA",
			  "MOB", "TTv", "DG", "CA2", "IG", "AOB", "FC", "MOs", "CLA", "RSPd", "ACAv", "ORBv", "ACAd", "RSPv.a",
			  "RSPv.b/c", "POST", "RSPagl", "PAR", "PRE", "ORBl", "ORBvl", "RSPv"]

	in_degree = {}
	out_degree = {}
	for node, degree in graph.in_degree(graph.nodes()):
		if node in nodesI:
			in_degree[node] = degree

	for node, degree in graph.out_degree(graph.nodes()):
		if node in nodesI:
			out_degree[node] = degree

	sorted_in = {k: v for k, v in sorted(in_degree.items(), key=lambda item: item[1])}
	sorted_out = {k: v for k, v in sorted(out_degree.items(), key=lambda item: item[1])}

	plt.figure(figsize=(40, 10))
	plt.bar(sorted_out.keys(), sorted_out.values())
	plt.savefig('out_degree.png')
	plt.xlabel('Nodes')
	plt.ylabel('degree')

	plt.figure(figsize=(40, 10))
	plt.bar(sorted_in.keys(), sorted_in.values())
	plt.savefig('in_degree.png')
	plt.xlabel('Nodes')
	plt.ylabel('degree')


# ####################### STENGTH GRAPH #######################
# ### Manisha's TODO ###
# #Input Strength Graph
#
# strengthIN = {}
# strengthOUT = {}
# for n in graph.nodes():
# 	if n in nodesI:
# 		sumIn = 0
# 		sumOut = 0
# 		for u,v,w in graph.in_edges(n, data=True):
# 			if v in nodesI:
# 				if(w.get("weight") == 7):
# 					sumOut += 10**0;
# 				elif(w.get("weight") == 6):
#                                          sumOut += 10**-0.333;
# 				elif(w.get("weight") == 5):
#                                          sumOut += 10**-0.66;
# 				elif(w.get("weight") == 4):
#                                          sumOut += 10**-1;
# 				elif(w.get("weight") == 3):
#                                          sumOut += 10**-2;
# 				elif(w.get("weight") == 2):
#                                          sumOut += 10**-3;
# 				elif(w.get("weight") == 1):
#                                          sumOut += 10**-4;
# 				else:
#                                          sumOut += 0;
# 		#print(graph.out_edges(n, data=True))
# 		for u,v,w in graph.out_edges(n, data=True):
# 			if v in nodesI:
# 				if(w.get("weight") == 7):
#                                          sumIn += 10**0;
# 				elif(w.get("weight") == 6):
#                                          sumIn += 10**-0.333;
# 				elif(w.get("weight") == 5):
#                                          sumIn += 10**-0.66;
# 				elif(w.get("weight") == 4):
#                                          sumIn += 10**-1;
# 				elif(w.get("weight") == 3):
#                                          sumIn += 10**-2;
# 				elif(w.get("weight") == 2):
#                                          sumIn += 10**-3;
# 				elif(w.get("weight") == 1):
#                                          sumIn += 10**-4;
# 				else:
#                                          sumIn += 0;
# 		strengthIN[n] = sumIn
# 		strengthOUT[n] = sumOut
#
# sorted_inD = {k: v for k, v in sorted(strengthIN.items(), key=lambda item: item[1])}
# sorted_outD = {k: v for k, v in sorted(strengthOUT.items(), key=lambda item: item[1])}
#
# #Input Strength Graph
# plt.figure(figsize=(40,10))
# plt.bar(sorted_inD.keys(), sorted_inD.values())
# plt.savefig('inStrength.png')
# plt.xlabel('Nodes')
# plt.ylabel('Strength')
#
# #Output Strength
# plt.figure(figsize=(40,10))
# plt.bar(sorted_outD.keys(), sorted_outD.values())
# plt.savefig('outStrength.png')
# plt.xlabel('Nodes')
# plt.ylabel('Strength')
