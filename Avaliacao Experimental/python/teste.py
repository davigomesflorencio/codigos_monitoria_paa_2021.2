import time
import random 
import sys
import timeit

from numpy import NINF


def bubbleSort(arr):
    for passnum in range(len(arr)-1,0,-1):
        for i in range(passnum):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def rec(n):
    if(n<=1):
        return 1
    else:
        return rec(n-1)+rec(n-1)

def proc(N):
    prev=0
    # varN=[]
    # tempos=[]

    while(True):
        a = [x for x in range(N)] 
        random.shuffle(a)
        
        # start = time.time()
        start = timeit.default_timer()
        # bubbleSort(a)
        rec(a)

        end = timeit.default_timer()
        # end = time.time()

        t = end-start
        print("N = ",N," Time ",t)
        # " -- prev =",end=" ")
        # varN.append(N)
        # tempos.append(t)
        # print(varN,"---",tempos)
        # if(prev>0):
        #     print(t/prev)
        
        prev=t
        N=N+1

def soma(vec):
    n = len(vec)
    cont = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if(vec[i]+vec[j]+vec[k]==0):
                    cont+=1
    return cont
        

def teste(N):
    a=[random.randint(-N,N) for x in range(N)]

    start = time.time()
    # teste 
    soma(a)

    end = time.time()

    print(end-start)

if __name__ == '__main__':
    random.seed(123456)
    N = int(sys.argv[1])
    print("N = ",N) 
    proc(N)
    