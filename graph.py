import csv
import json
import networkx as nx
import matplotlib.pyplot as plt

######################### READ DATA #########################

data = []
test = []
with open('Dataset2.csv', encoding='utf-8', mode = 'r') as csvFile:
	read = csv.reader(csvFile)
	#start to record when begin = 3
	begin = 0
	count = 0
	for line in read:
		if begin >= 3:
			sub = {}
			sub["start"] = str(line[1]) #+ "_" + str(line[0])
			sub["target"] = str(line[3]) #+ "_" + str(line[2])
			if str(line[0]) == str(line[2]):
				count += 1
				if sub['start'] == "" or sub['target'] == '':
					continue
				# sub["data_type"] = str(line[4]) if len(line[4]) != 0 else ""
				sub["binned_strength"] = int(line[5]) if len(line[5]) != 0 else ""
				if sub["binned_strength"] == "":
					break
				if sub["binned_strength"] == 0:
					continue
				tuple_sub_weight = (sub["start"], sub["target"], sub["binned_strength"])
				tuple_sub = (sub["start"], sub["target"])
				if tuple_sub in test:
					find = [i for i, v in enumerate(data) if v[0] == sub["start"] and v[1] == sub["target"]]
					find = find[0]
					y = list(data[find])
					y[2] += sub["binned_strength"]
					data[find] = tuple(y)
				else:
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
G = nx.MultiDiGraph()
G.add_edges_from(data)
print("number of nodes: " + str(len(G.nodes())))
# print(G.nodes())
print("number of edges: " + str(G.number_of_edges()))
print("out degree: " + str(G.out_degree('FC')))
print("in degree: " + str(G.in_degree('FC')))
# print(G.edges())
# Uncomment this to show a basic plot of the graph
# nx.draw(graph)
# plt.show()


####################### DEGREE GRAPH ########################
### Ashley's TODO ###



####################### STENGTH GRAPH #######################
### Manisha's TODO ###
#Input Strength Graph

in_degree = {}
out_degree = {}
in_strength = {}
out_strength = {}
for node, degree in G.in_degree(G.nodes()):
	in_degree[node] = degree

for node, degree in G.out_degree(G.nodes()):
	out_degree[node] = degree

for node, out, weight in G.out_edges(G.nodes()):
	print(weight)
	break
	out_strength[node] = weight.get("weight")

plt.figure(figsize=(40,10))
plt.bar(out_strength.keys(), out_strength.values())
plt.savefig('out_strength.png')
plt.xlabel('Nodes')
plt.ylabel('out_strength')