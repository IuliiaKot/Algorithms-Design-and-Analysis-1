import sys
import threading

N = 875714
discover_vertex = []
finish = [int(0)]*N
leader = [int(0)] * N
finish_time = [int(0)]*N
size_scc = [0]*N

def dfs(G,vertex):
   global time, discover_vertex, finish, d, leader
   discover_vertex = [int(0)] * N
   time = 0
   for i in range(0, N):
       if (discover_vertex[i] == 0):
           dfs_visit(G,i)
   return leader

def dfs_visit(G,i):
    global time, discover_vertex, finish, size_scc, finish_time
    time = time + 1
    discover_vertex[i] = 1
    size_scc[i] = t
    #leader[i] = s
    for j in G[i]:
        if (discover_vertex[j] == 0):
            dfs_visit(G,j)

    discover_vertex[i] = 2
    time = time + 1
    finish[i] = time
    finish_time[i] = 0

def scc(G,G_reverse):
    #the first loop on reverse graph
    global size_scc, discover_vertex
    global  finish_time, finish, time, leader
    dfs(G, 0)

    #inizialisation()
    finish_time = finish
    discover_vertex = [int(0)] * N

    size_scc = [int(0)] * N
    
    k = 0
    while (max(finish_time) != 0):
        time= 0
        dfs_visit(G_reverse, finish_time.index(max(finish_time)))
        leader[k] = max(size_scc)
        for i in range(len(size_scc)):
            d[i] = 0
        k += 1
    
    leader.sort()
    return leader    
    
def main():
    s = open("scc.txt","r")
    G = []
    G_reverse = []
    for i in range(0,N):
        G.append([])
        G_reverse.append([])
    for i in s:
        v1,v2 = [int(x) for x in i.split()]
        G[v1-1].append(v2-1)
        G_reverse[v2-1].append(v1-1)

    s.close()
    res = scc(G, G_reverse)
    for i in range(len(res)-5, len(res)):
        print res[i]
if __name__ == '__main__':
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target = main)
    thread.start()
