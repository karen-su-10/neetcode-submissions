class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # convert 2 dimension into 1 dimension sorted array
        sorted_array =[]
        for row in matrix:
            for val in row:
                sorted_array.append(val)
        # use binary search
        left , right = 0, len(sorted_array) - 1
        while left <= right:
            p = left + (right - left)//2
            if sorted_array[p] == target:
                return True
            elif sorted_array[p] < target:
                left = p + 1
            else:
                right = p - 1
        return False
