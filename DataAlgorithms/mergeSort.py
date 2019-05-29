def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        #diving the array into 2 parts
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i=j=k=0
        while i<len(L)and j<len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i=i+1
            else:
                arr[k]=R[j]
                j=j+1
            k=k+1

        print(arr)

mergeSort([3,4,1,7,2,6])
