#import time
#tic = time.time()
def insertSort(list):
    A = [2, -1, 3, 100, 5]
    j = 1
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i +1] = key
    print(A)
insertSort([2, -1, 3, 100, 5])
#toc = time.time()
#print(toc-tic)
