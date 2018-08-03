# BUBBLE SORT 

def bubbleSort(L):
    '''
    Because of the two nested loops (which can possibly be of linear complexity O(n))
    fns's order of growth is O(n^2)
    '''
    swap = False
    while not swap: # by the end of first loop, I'm sure that the biggest e is at the end -> O(n)
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                L[j-1], L[j], swap = L[j], L[j-1], False
    return L
# print(bubbleSort([x for x in range(20, 0, -1)]))

# SELECTION SORT -> O(n^2)
def selectionSort(L): # logic seems to be similar and opposite to Bubble sort
    suffixSt = 0
    while suffixSt != len(L): # after one loop the smallest e will be at the beggining
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
    return L
# print(selectionSort([x for x in range(100, 0, -1)]))

def insertionSort(L):
    for i in range(1, len(L)):
        j = i
        while j > 0 and L[j-1] > L[j]:
            L[j], L[j-1] = L[j-1], L[j] # SWAPING
            j-=1
    return L

print(insertionSort([x for x in range(50, 0, -1)]))

# MERGE SORT -> O(n log n)
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else: 
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def mergeSort(L): 
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L)//2
        left = mergeSort(L[:mid])
        right = mergeSort(L[mid:])
        return merge(left, right)

# print(mergeSort([x for x in range(50, 0, -1)]))