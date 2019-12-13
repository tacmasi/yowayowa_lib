def DFS(graph, nodeTF, finish_times, node, SCCsizes, s):
    global SCC
    global t
    if s != 0:
        SCC = 0 #init
    nodeTF[node - 1] = True
    ##for each arc(node, edge) in graph:
    ####if j not yet explored
    ########DFS(G,j)
    for G in graph:
        if G[0] == node:
            if nodeTF[G[1] - 1] == False:
                nodeTF, finish_times, SCCsizes, _ = DFS(graph, nodeTF, finish_times, G[1], SCCsizes, 0)
    t += 1
    #print(t)
    #print("s,t= {0},{1}".format(s,t))
    finish_times[node - 1] = t ##node i's finishing time
    SCC += 1
    if s != 0: #if end
        print("s, SCC = {0}, {1}".format(s, SCC))
        SCCsizes.append(SCC)
    return nodeTF, finish_times, SCCsizes, s


