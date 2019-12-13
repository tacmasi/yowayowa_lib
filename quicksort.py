def QuickSort(array, ncomp, method = "median"):
    '''list of int -> list of int, int
    return sorted list and number of comparisons
    >>> f = open("problem5.6test2.txt","r")
    >>> m = f.read()
    >>> f.close()
    >>> r = m.splitlines()
    >>> g = []
    >>> for item in r:
    ...     g.append(int(item))
    ... 
    >>> QuickSort(g, 0, "first")[1]
    620
    >>> QuickSort(g, 0, "last")[1]
    573
    >>> QuickSort(g, 0, "median")[1]
    502
    '''
    if len(array) <= 1:
        return array, ncomp
    else:
        pivot, pivotID = ChoosePivot(array, method)
        Lside, Rside, compcnt = Partition(array, pivotID)
        Llist, Lncomp = QuickSort(Lside,0 , method)
        Rlist, Rncomp = QuickSort(Rside,0 , method)
        outList = Llist[:]
        outList.append(pivot)
        outList.extend(Rlist)
        return outList, (ncomp + compcnt + Lncomp + Rncomp)

def Partition(array, pivotID):
    '''list of int, int -> list of int, list of int, int
    return splited list at pivotID 
    (Leftside, Rightside), number of compare
    >>> Partition([1,2,3,4,5], 0)
    ([], [2, 3, 4, 5], 4)
    >>> Partition([1,2,3,4,5], 4)
    ([1, 2, 3, 4], [], 4)
    >>> Partition([1,2,3,4,5], 2)
    ([1, 2], [4, 5], 4)
    '''
    A = array[:]
    compcnt = 0
    pivot = A[pivotID]
    A[0], A[pivotID] = A[pivotID], A[0] #exchange
    #A.remove(pivot) #omit pivot from list
    #A.insert(0, pivot) # insert pivot at index 0
    i, j = 1, 1
    while j < len(A):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i] #swap
            i += 1
        j += 1
        compcnt += 1
    A[0], A[i-1] = A[i-1], A[0] #swap
    Lside = A[0:i - 1]
    Rside = A[i: ]
    return Lside, Rside, compcnt

def ChoosePivot(array, method = "median"):
    '''list of int, str -> int, int
    prerequisite: method in ("median", "first", "last")
    return pivot, pivotID
    >>> ChoosePivot([1,2,3,4])
    (2, 1)
    >>> ChoosePivot([1,2,3,4,5], "first")
    (1, 0)
    >>> ChoosePivot([1,2,3,4,5], "last")
    (5, 4)
    '''
    assert(method in ("median", "first", "last"))
    if method == "median":
        #median-of-3 method
        fst, fstidx  = ChoosePivot(array, method = "first")
        last, lastidx = ChoosePivot(array, method = "last")
        mid ,mididx = array[(len(array) - 1)//2], \
                (len(array) - 1)//2
        if last > fst > mid or last < fst < mid:
            return fst, fstidx
        elif fst > last > mid or fst < last < mid:
            return last, lastidx
        else:
            return mid, mididx
    elif method == "first":
        return array[0], 0
    elif method == "last":
        return array[-1], len(array) - 1


