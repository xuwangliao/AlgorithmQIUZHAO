def bubble_sort(a):
   for i in range(len(a)):
       for j in range(i,len(a)):
           if a[i] > a[j]:
               a[i],a[j] = a[j], a[i]
   print(a)
bubble_sort(a)
