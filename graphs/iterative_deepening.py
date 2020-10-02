"""
Finds paths in the following example map to illustrate Iterative Deepening Search:
http://www.cse.unsw.edu.au/~cs3411/16s1/tut/wk03romania.gif
"""
def ids(graph, start, goal):
	#dfs helper function to perform depth limited dfs			
	def dfs(graph, start, goal, depth, path):
		#if depth < 0 , it means node is not found with current depth given return -1 t indicate not found
		if(depth < 0):
			return -1
		path.append(start)
		if(start == goal):
			return path
		for i in graph[start]:
			tmp = dfs(graph, i[1], goal, depth-1, list(path)); 
			if(tmp != -1):
				return tmp
		#if any of the above dfs runs do not give path, then it means node does not exist and return -1
		return -1

	i = 0
	#try with different depths till first path to goal is found
	while True:
		tmp = dfs(graph, start, goal, i, [])
		if(tmp != -1):
			return tmp
		i+=1

if __name__ == "__main__":
	#A sample map of Romania (Taken from Chapter 3 of Russell & Norvig. Artificial Intelligence)
    graph={
        'Arad':[(75, 'Zerind'),(118, 'Timisoara'),(140, 'Sibiu')],
        'Zerind':[(75, 'Arad'), (71, 'Oradea')],
        'Oradea':[(71, 'Zerind'), (151, 'Sibiu')],
        'Sibiu':[(140, 'Arad'), (99, 'Fagaras'), (80, 'Rimnicu Vilcea'), (151, 'Oradea')],
        'Timisoara':[(118, 'Arad'), (111, 'Lugoj')],
        'Lugoj':[(111, 'Timisoara'), (70, 'Mehadia')],
        'Mehadia':[(70, 'Lugoj'), (75, 'Dobreta')],
        'Dobreta':[(75, 'Mehadia'), (120, 'Craiova')],
        'Craiova':[(120, 'Dobreta'), (146, 'Rimnicu Vilcea'), (138, 'Pitesti')],
        'Rimnicu Vilcea':[(80, 'Sibiu'), (97, 'Pitesti'), (146, 'Craiova')],
        'Fagaras':[(99, 'Sibiu'), (211, 'Bucharest')],
        'Pitesti':[(97, 'Rimnicu Vilcea'), (101, 'Bucharest'), (138, 'Craiova')],
        'Bucharest':[(101, 'Pitesti'), (211, 'Fagaras'), (90, 'Giurgiu'), (85, 'Urziceni')],
        'Giurgiu':[(90, 'Bucharest')],
        'Urziceni':[(85, 'Bucharest'), (98, 'Hirsova'), (142, 'Vaslui')],
        'Hirsova':[(86, 'Eforie'), (98, 'Urziceni')],
        'Eforie':[(86, 'Hirsova')],
        'Vaslui':[(92, 'Iasi'), (142, 'Urziceni')],
        'Iasi':[(92, 'Vaslui'), (87, 'Neamt')],
        'Neamt':[(87, 'Iasi')],
    }
    #finding the path between Arad and Bucharest, replace cities to find other paths
    idspath = ids(graph, 'Arad', 'Bucharest')
    print("\nPath Using Iterative Deepening Search : ")
    print(" -> ".join(idspath))
