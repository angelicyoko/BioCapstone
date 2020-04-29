import csv
import json
import networkx as nx
import matplotlib.pyplot as plt

######################### READ DATA #########################

def graph_help(graph):

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

	plt.figure(figsize=(30, 10))
	plt.bar(sorted_out.keys(), sorted_out.values(), width=1)
	plt.xlabel('Regions of Cerebral Cortex')
	plt.ylabel('Degree (within hemisphere)')
	plt.title("Out Degree of Mouse Connectome")
	plt.savefig('out_degree.png')
	
	plt.figure(figsize=(30, 10))
	plt.bar(sorted_in.keys(), sorted_in.values(), width=1)
	plt.xlabel('Regions of Cerebral Cortex')
	plt.ylabel('Degree (within hemisphere)')
	plt.title("In Degree of Mouse Connectome")
	plt.savefig('in_degree.png')


	####################### STENGTH GRAPH #######################
	### Manisha's TODO ###
	#Input Strength Graph

	strengthIN = {}
	strengthOUT = {}
	for n in graph.nodes():
		if n in nodesI:
			sumIn = 0
			sumOut = 0
			for u,v,w in graph.in_edges(n, data=True):
				if v in nodesI:
					sumOut += w.get("weight")
			for u,v,w in graph.out_edges(n, data=True):
				if v in nodesI:
					sumIn += w.get("weight")
			strengthIN[n] = sumIn
			strengthOUT[n] = sumOut

	sorted_inD = {k: v for k, v in sorted(strengthIN.items(), key=lambda item: item[1])}
	sorted_outD = {k: v for k, v in sorted(strengthOUT.items(), key=lambda item: item[1])}

	#Input Strength Graph
	plt.figure(figsize=(30,10))
	plt.bar(sorted_inD.keys(), sorted_inD.values(), width=1)
	plt.xlabel('Regions of Cerebral Cortex')
	plt.ylabel('Strength (within hemisphere)')
	plt.title("In Strength of Mouse Connectome")
	plt.savefig('inStrength.png')

	#Output Strength
	plt.figure(figsize=(30,10))
	plt.bar(sorted_outD.keys(), sorted_outD.values(), width=1)
	plt.xlabel('Regions of Cerebral Cortex')
	plt.ylabel('Strength (within hemisphere)')
	plt.title("Out Strength of Mouse Connectome")
	plt.savefig('outStrength.png')
