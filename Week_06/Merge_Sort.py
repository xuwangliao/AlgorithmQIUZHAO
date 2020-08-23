
def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)// 2
        l = arr[:mid]
        r = arr[mid:]
        merge_sort(l)
        merge_sort(r)
        merge(arr,l,r)

def merge(arr,arr1,arr2):
    i,j,k = 0,0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i+=1
        else:
            arr[k] = arr2[j]
            j+=1
        k+=1
    while i<len(arr1):
        arr[k]=arr1[i]
        i+=1
        k+=1
    while j<len(arr2):
        arr[k]=arr2[j]
        j+=1
        k+=1

a = [1,5,3,7,12,11,13,19,9,2,4]
merge_sort(a)
print(a)