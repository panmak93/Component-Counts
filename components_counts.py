"""
Name: Cheuk Pan, Mak
Compsci 220
Assignment 3
"""

import networkx as nx

class Assignment3:
	def components_counts(adj_dict):
		G = nx.Graph()
		G.add_nodes_from(adj_dict.keys())
		for outgoing_v in adj_dict:
			for ingoing_v in adj_dict[outgoing_v]:
				G.add_edge(outgoing_v, ingoing_v)
		return len(list(nx.connected_components(G)))
	
	output = ""
	while(True):
		line = input()
		if (line == "0") or (line == "\n") or (line == ""):
			break
		else:
			order = int(line)
			adj_dict = dict()
			counter = 0 
			while counter < order:
				adjacents = input()
				if ((adjacents == "\n") or (adjacents == "") or (adjacents == " ")):
					adj_dict[counter] = []
				else:
					adjacents.rstrip("\n")
					adjacent_list = adjacents.split()
					for adj in adjacent_list:
						adj = int(adj)
						if adj >= order:
							raise IndexError
						else:
							if counter in adj_dict:
								adj_dict[counter] += [adj]
							else:
								adj_dict[counter] = [adj]
				counter+=1
			output = output + str(components_counts(adj_dict)) + "\n"
		
	print(output.rstrip('\n'))