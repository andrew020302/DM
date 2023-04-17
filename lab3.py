from sys import maxsize
from itertools import permutations

V = 6


def travellingSalesmanProblem(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:

        current_pathweight = 0

        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        min_path = min(min_path, current_pathweight)
    return min_path



if __name__ == "__main__":
    graph = [[0, 35, 40, 54, 69, 87], [35, 0, 0, 87, 43, 0],
             [40, 0, 0, 79, 0, 54], [54, 87, 79, 0, 16, 0],
             [69, 43, 0, 16, 0, 0], [87, 0, 54, 0, 0, 0]]
    s = 0
    print('Мінімальний шлях:', travellingSalesmanProblem(graph, s))