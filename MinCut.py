import random
from copy import deepcopy

def min_cut(Graph):
    vertex = len(Graph)
    if (vertex > 2):
        #choose random endge
        a=  Graph.keys()
        random_vertex_1 = random.choice(a)
        i = Graph[random_vertex_1]
        random_vertex_2 = random.choice(i)

        #union vertex_1 and vertex_2
        Graph[random_vertex_1].extend(Graph[random_vertex_2])
        #remove self-loop
        while (random_vertex_1 in Graph[random_vertex_1]):
            Graph[random_vertex_1].remove(random_vertex_1)
        while (random_vertex_2 in Graph[random_vertex_1]):
            Graph[random_vertex_1].remove(random_vertex_2)

        #remove vertex_2
        del Graph[random_vertex_2]
        for i in Graph:
            for j in range(0, len(Graph[i])):
                if Graph[i][j] == random_vertex_2:
                    Graph[i][j] = random_vertex_1

        return min_cut(Graph)
    else:
        return len(Graph.values()[0])


def main():
    s = open("min_cut.txt","r").readlines()
    Graph = {}
    for line in s:
        tmp =[int(x) for x in line.split()]
        Graph[tmp[0]] =tmp[1:]
   
    res = []
    for i in range(40):
        Graph_copy = deepcopy(Graph)
        res.append(min_cut(Graph_copy))
    print res, "mim", min(res)

main()
