a = [1,5,3,7,9,2,4]
def pivit(a,l,r):
    p=a[r]; count = l
    for i in range(l,r):
        if a[i] < p:
            a[count],a[i] = a[i],a[count]
            count+=1
    a[count],a[r] = a[r],a[count]
    return count

def quicksort(a,low,high):
    if low >= high:
        return
    if low < high:
        p=pivit(a,low,high)
        quicksort(a,low,p-1)
        quicksort(a,p+1,high)
quicksort(a,0,len(a)-1)
print(a)