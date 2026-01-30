def reverse(s, e, arr):
    while s<e:
        arr[s], arr[e] = arr[e], arr[s]
        e-=1
        s+=1
    
    
    

def reverseArray(arr, k):
    reverse(0, len(arr)-1, arr)
    reverse(0, k-1, arr)
    reverse(k, len(arr)-1, arr)
    return arr

print(reverseArray([1,2,3,4,5,6,7], 3))