def Dijkstra(adj_list, s):
    S = [False] * len(adj_list)
    infinity = 1000000
    weights = [infinity] * len(adj_list)
    weights[s] = 0
    S[s] = True
    U = [] #set of visited vertices
    min_w = infinity
    vertex = 0

    while (not s in U):
  
        for i,j in adj_list[s]:
            if (not S[i]):
                weights[i] = min(weights[i], weights[s] + j)
        for v, w in adj_list[s]:
            if ( not S[v]):
                if (weights[v] < min_w):
                    min_w = weights[v]
                    vertex = v

        S[vertex] = True
        U.append(s)
        s = vertex
        min_w = infinity

    return weights

def main():
    adj_list = []
    s = open("1.txt","r").read().splitlines()

    for line in s:
        adj_list.append([])
        data = line.split()
        m = int(data[0]) - 1
        for i in data[1:]:
            nd, wh = i.split(',')
            n = int(nd) - 1
            w = int(wh)
            adj_list[m].append((n, w))
    result = Dijkstra(adj_list, 0)

    vertex = [7,37,59,82,99,115,133,165,188,197]
    for i in vertex:
        print result[i-1] 
main()