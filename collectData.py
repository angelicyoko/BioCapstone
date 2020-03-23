import csv
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
######################### READ DATA #########################
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
### tuple[3] is the weight (has already been casted to int)

### Jack's TODO ###
graph = nx.MultiDiGraph()
for line in data:
    if (line[2] != ""):
        graph.add_edge(line[0], line[1], line[2])
# Uncomment this to show a basic plot of the graph
# nx.draw(graph)
# plt.show()

####################### DEGREE GRAPH ########################
### Ashley's TODO ###
# graph degree in and degree out within hemisphere
degree_pairs = {}
all_in_one = []
all_in_two = []
all_in_three = []
all_out_one = []
all_out_two = []
all_out_three = []
nodes_one, nodes_two, nodes_three =  np.array_split(np.array(graph.nodes),3)
for node, degrees_in in graph.in_degree:
    listy = []
    if(node in nodes_one):
        listy.append(degrees_in)
        all_in_one.append(degrees_in)
    elif(node in nodes_two):
        listy.append(degrees_in)
        all_in_two.append(degrees_in)
    else:
        listy.append(degrees_in)
        all_in_three.append(degrees_in)

    degree_pairs[node] = listy
for node, degrees_out in graph.out_degree:
    if (node in nodes_one):
        listy.append(degrees_out)
        all_out_one.append(degrees_out)
    elif (node in nodes_two):
        listy.append(degrees_out)
        all_out_two.append(degrees_out)
    else:
        listy.append(degrees_in)
        all_out_three.append(degrees_out)


#make the bar graph here
fig, (ax, ax2, ax3) = plt.subplots(nrows = 3, ncols= 1, figsize = (30,30))
index = np.arange(103)
bar_width = 0.5
# graph 1
g1_in = ax.bar(index, all_in_one, bar_width, color='r', tick_label=nodes_one, label='0:102 Nodes In Degrees')
g1_out = ax.bar(index, all_out_one, bar_width, color='b', tick_label=nodes_one, label='0:102 Nodes Out Degrees')
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(24)
    tick.label.set_rotation('vertical')
ax.axes.legend(prop={'size': 35})
ax.set_title("0:102 Degree In (Red) vs Degree Out (Blue)")
ax.set_ylabel("Degrees")
ax.set_xlabel("0:102 Nodes")
# graph 2
g2_in = ax2.bar(index, all_in_two, bar_width, color='r', tick_label=nodes_two, label='103:205 Nodes In Degrees')
g2_out = ax2.bar(index, all_out_two, bar_width, color='b',tick_label=nodes_two, label='103:205 Nodes Out Degrees')
for tick in ax2.xaxis.get_major_ticks():
    tick.label.set_fontsize(24)
    tick.label.set_rotation('vertical')
ax2.axes.legend(prop={'size': 35})
ax2.set_title("102:205 Degree In (Red) vs Degree Out (Blue)")
ax2.set_ylabel("Degrees")
ax2.set_xlabel("102:205 Nodes")
# graph 3
g3_in = ax3.bar(index, all_in_three, bar_width, color='r', tick_label=nodes_three,  label='206:308 Nodes In Degrees')
g3_out = ax3.bar(index, all_out_three, bar_width, color='b', tick_label= nodes_three, label='206:308 Nodes Out Degrees')
for tick in ax3.xaxis.get_major_ticks():
    tick.label.set_fontsize(24)
    tick.label.set_rotation('vertical')
ax3.axes.legend(prop={'size': 35})
ax3.set_title("206:308 Degree In (Red) vs Degree Out (Blue)")
ax3.set_ylabel("Degrees")
ax3.set_xlabel("206:308 Nodes")

plt.show()




####################### STENGTH GRAPH #######################
### Manisha's TODO ###
