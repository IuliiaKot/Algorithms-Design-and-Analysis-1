def quiksort(A, pivot, left):
    global count
    if (pivot == left):
        return A
    tmp = partition(A, pivot, left)
    quiksort( A, pivot, tmp - 1)
    count = count + (tmp - 1- pivot)
    quiksort(A, tmp, left)
    count = count  + (left - tmp)

    return count

def partition(A, pivot, left):
    choose_pivot = A[pivot]
    tmp = 0 
    i = pivot + 1
    for j in xrange(i, left):
        if (A[j] < choose_pivot):
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
            i = i + 1
    tmp = A[i - 1]
    A[i - 1] = A[pivot]
    A[pivot] = tmp

    return i
def main():
    f = open("1.txt")
    A = []
    for line in f:
        A.append(int(line))
    print A

    global count
    count = 0 
    result = quiksort(A, 0, len(A),)
    print ("f", count)
main()
