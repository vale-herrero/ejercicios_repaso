import sys

def findMaxVertex(visited, weights):

	index = -1;

	maxW = -sys.maxsize;

	for i in range(V):

		if (visited[i] == False and weights[i] > maxW):
		
			maxW = weights[i];

			index = i;
	return index;

def printMaximumSpanningTree(graph, parent):

	MST = 0;

	for i in range(1, V):
	
		MST += graph[i][parent[i]];

	print("Peso del árbol máximo de expansión: ", MST);
	print();
	print("Arista \tPeso");

	for i in range(1, V):
		print(parent[i] , " - " , i , " \t" , graph[i][parent[i]]);

def maximumSpanningTree(graph):

	visited = [True]*V;

	weights = [0]*V;

	parent = [0]*V;

	for i in range(V):
		visited[i] = False;
		weights[i] = -sys.maxsize; 

	weights[0] = sys.maxsize;
	parent[0] = -1;

	for i in range(V - 1):

		maxVertexIndex = findMaxVertex(visited, weights);

		visited[maxVertexIndex] = True;
		for j in range(V):
			if (graph[j][maxVertexIndex] != 0 and visited[j] == False):

				if (graph[j][maxVertexIndex] > weights[j]):
				
					weights[j] = graph[j][maxVertexIndex];

					parent[j] = maxVertexIndex;

	printMaximumSpanningTree(graph, parent);


V = 8;

print('Punto a:')

dict_of_names = {
        0:'Iron Man',
        1:'Hulk',
        2:'Khan',
        3:'Thor',
        4:'Captain America',
        5:'Ant-Man',
        6:'Nick Fury - S.H.I.E.L.D.',
        7:'The Winter Soldier'
    }

graph = [
    [0, 6, 0, 1, 8, 7, 3, 2],
    [6, 0, 0, 6, 1, 8, 9, 1],
    [0, 0, 0, 1, 2, 1, 5, 0],
    [1, 6, 1, 0, 1, 5, 9, 3],
    [8, 1, 2, 1, 0, 2, 4, 5],
    [7, 8, 1, 5, 2, 0, 1, 6],
    [3, 9, 5, 9, 4, 1, 0, 1],
    [2, 1, 0, 3, 5, 6, 1, 0]];

print('Diccionario de nombres y vertices:', dict_of_names)
print('Grafo', graph)

print('\nPunto b:')
print('Árbol de expansión máximo:')
print(maximumSpanningTree(graph));

print('\nPunto c:')
maxEpisodios = max([max(vertices) for vertices in graph])
print('Número máximo de episodios entre dos personajes: {}'.format(maxEpisodios))

for ind, vertices in enumerate(graph):
    for ind2, peso in enumerate(vertices[:ind]):
        if peso == maxEpisodios:
            print('{} y {} comparten {} episodios juntos.'.format(dict_of_names[ind], dict_of_names[ind2], maxEpisodios))
        
print('\nPuntos d y e:') 

for ind, vertices in enumerate(graph):
    if sum(vertices) == 9:
        print('{} aparece en exactamente {} episodios de la saga'.format(dict_of_names[ind], 9))
