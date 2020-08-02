class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 二分的思想
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        left,right = 0,m*n-1
        while left <= right:
            pivot = (left+right)//2
            pivot_value = matrix[pivot//n][pivot%n]
            if pivot_value == target:
                return True
            if pivot_value < target:
                left = pivot + 1
            else:
                right = pivot - 1
        return False