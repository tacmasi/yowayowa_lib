def Dijkstra(graph, startnode):
    '''list of list of [int,int] -> list of int(length)
    return length list
    '''
    SPassLen = [0] * len(graph)
    x = [startnode]
    itr = 0
    #Main Loop:
    while len(x) != len(graph):
        itr += 1
        print(itr, x[-1])
        #among all edges(v,w) in edge
        #with v in X, w not in X,
        #l_vw = min(A[v] + l_vw)
        minedge = ''
        minsize = 1000000
        for tail in x:
            for edge in graph[tail - 1]:
                if (not edge[0] in x) and SPassLen[tail - 1] + edge[1] < minsize:
                    minedge, minsize = edge[0], SPassLen[tail - 1] + edge[1]
        if minedge != '':
            x.append(minedge)
            SPassLen[minedge - 1] = minsize
        if itr > 10**3:
            print('itr = 10*4')
            break
    return SPassLen


