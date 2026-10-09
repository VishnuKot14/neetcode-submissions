class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            l, h = 0, len(matrix[i]) -1
            while l <= h:
                mid = (l + h) // 2
                if matrix[i][mid] < target:
                    l = mid + 1
                elif matrix[i][mid] > target:
                    h = mid - 1
                else:
                    return True
        
        return False