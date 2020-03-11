import csv
import json

######################### READ DATA #########################
data = []
with open('Dataset2.csv', encoding='utf-8', mode = 'r') as csvFile:
	read = csv.reader(csvFile)
	#start to record when begin = 3
	begin = 0
	for line in read:
		if begin >= 3:
			sub = {}
			sub["start"] = str(line[1]) + "_" + str(line[0])
			sub["target"] = str(line[3]) + "_" + str(line[2])
			sub["data_type"] = str(line[4]) if len(line[4]) != 0 else ""
			sub["binned_strength"] =   int(line[5]) if len(line[5]) != 0 else ""
			
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



####################### DEGREE GRAPH ########################
### Ashley's TODO ###



####################### STENGTH GRAPH #######################
### Manisha's TODO ###