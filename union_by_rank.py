def FIND(x, rootlist):
    '''int, list of int -> int
    return root key of tree that include x
    '''
    if x == rootlist[x - 1]:
        return x
    else:
        return FIND(rootlist[x - 1], rootlist)
def UNIONbyRank(u, v, rootlist, ranklist):
    '''int, int, list of int, list of int -> list of int, list of int
    return unioned lists:  rootlist, ranklist
    '''
    root1 = FIND(u, rootlist)
    rank1 = ranklist[root1 - 1]
    root2 = FIND(v, rootlist)
    rank2 = ranklist[root2 - 1]
    #init new list
    Nrootlist = rootlist.copy()
    Nranklist = ranklist.copy()
    if rank1 > rank2: #compare rank
        Nrootlist[root2 - 1] = root1 #union
        if rank1 == rank2: 
            Nranklist[root1 - 1] = rank2 + 1 #rank update
    else:
        Nrootlist[root1 - 1] = root2
        if rank2 == rank1:
            Nranklist[root2 - 1] = rank1 + 1
    return Nrootlist, Nranklist


