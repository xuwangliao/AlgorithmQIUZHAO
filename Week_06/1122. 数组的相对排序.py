class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {}
        for i in range(len(arr2)):
            dic[arr2[i]] = 0
        temp=[]
        for j in range(len(arr1)):
            if arr1[j] not in dic:
                temp.append(arr1[j])
            else:
                dic[arr1[j]]+=1
        res = []
        for i in arr2:
            res+=[i]*dic[i]
        res+=sorted(temp)
        return res