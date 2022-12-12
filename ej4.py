from itertools import permutations

def solver(graph, s, dict_of_names):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    final_path = []
    min_path = 10000000

    next_permutation = permutations(vertex)

    for i in next_permutation:
        current_pathweight = 0

        k = s
        current_path = []
        for j in i:
            current_pathweight += graph[k][j]
            current_path.append('{}-->{}'.format(dict_of_names[k],dict_of_names[j]))
            k = j

        current_pathweight += graph[k][s]
        current_path.append('{}-->{}'.format(dict_of_names[k],dict_of_names[s]))

        if current_pathweight < min_path:
            final_path = current_path
            min_path = current_pathweight

    return min_path, final_path


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

graph= [
[0, 675, 400, 166, 809, 720, 399, 233],
[675, 0, 540, 687, 179, 348, 199, 401],
[400, 540, 0, 107, 752, 521, 385, 280],
[166, 687, 107, 0, 111, 540, 990, 361],
[809, 179, 752, 111, 0, 206, 412, 576],
[720, 348, 521, 540, 206, 0, 155, 621],
[399, 199, 385, 990, 412, 155, 0, 100],
[233, 401, 280, 361, 576, 621, 100, 0]]

V = 8

s = 6

final_cost, path = solver(graph, s, dict_of_names)
print('El minimo costo posible es: {} para el camino {}'.format(final_cost, path))
