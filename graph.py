import csv
import json
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math

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
	plt.figure(figsize=(40,10))
	plt.bar(sorted_inD.keys(), sorted_inD.values())
	plt.savefig('inStrength.png')
	plt.xlabel('Nodes')
	plt.ylabel('Strength')

	#Output Strength
	plt.figure(figsize=(40,10))
	plt.bar(sorted_outD.keys(), sorted_outD.values())
	plt.savefig('outStrength.png')
	plt.xlabel('Nodes')
	plt.ylabel('Strength')



def rich_club_wd(CIJ, klevel=None):
	'''
	Parameters
	----------
	CIJ : NxN np.ndarray
		weighted directed connection matrix
	klevel : int | None
		sets the maximum level at which the rich club coefficient will be
		calculated. If None (default), the maximum level is set to the
		maximum degree of the adjacency matrix

	Returns
	-------
	Rw : Kx1 np.ndarray
		vector of rich-club coefficients for levels 1 to klevel
	'''
	nr_nodes = len(CIJ)
	# degree of each node is defined here as in+out
	deg = np.sum((CIJ != 0), axis=0) + np.sum((CIJ.T != 0), axis=0)

	if klevel is None:
		klevel = np.max(deg)
	Rw = np.zeros((klevel,))

	# sort the weights of the network, with the strongest connection first
	wrank = np.sort(CIJ.flat)[::-1]
	for k in range(klevel):
		SmallNodes, = np.where(deg < k + 1)
		if np.size(SmallNodes) == 0:
			Rw[k] = np.nan
			continue

		# remove small nodes with node degree < k
		cutCIJ = np.delete(
			np.delete(CIJ, SmallNodes, axis=0), SmallNodes, axis=1)
		# total weight of connections in subset E>r
		Wr = np.sum(cutCIJ)
		# total number of connections in subset E>r
		Er = np.size(np.where(cutCIJ.flat != 0), axis=1)
		# E>r number of connections with max weight in network
		wrank_r = wrank[:Er]
		# weighted rich-club coefficient
		if not (math.isnan(Wr / np.sum(wrank_r))):
			Rw[k] = Wr / np.sum(wrank_r)
			#print(Wr / np.sum(wrank_r))
	return Rw