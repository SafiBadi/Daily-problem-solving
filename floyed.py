def floydWarshall(graph):
   
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
 
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min( dist[i][j], dist[i][k] + dist[k][j] )
    printSolution(dist)
 
 
def printSolution(dist):

    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print( "%7s" % ("INF"),end=" ")
            else:
                print( "%7d" % (dist[i][j]),end=" ")
            if j == V-1:
                print ("")

INF = 9
V = 6

graph = [
            [0,1, 1,INF,INF,INF], 
            [1,0,INF,INF,INF,INF], 
            [1,INF,0, 1, 1, 1], 
            [INF,INF,1,0,INF,INF], 
            [INF,INF,1,INF,0,INF], 
            [INF,INF,1,INF,INF,0]
        ]


floydWarshall(graph)