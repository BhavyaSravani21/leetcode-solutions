class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        rows=len(matrix)
        col=len(matrix[0])
        low=0
        high=rows*col-1
        while(low<=high):
            mid=(low+high)//2
            r=mid // col
            c=mid % col
            midvalue=matrix[r][c]
            if (midvalue==target):
                return True
            elif (midvalue<target):
                low=mid+1
            else:
                high=mid-1
        return False

        
