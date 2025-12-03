class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target=abs(target)
        s=0
        step=0
        while (s<target or (s-target)%2!=0):
            step+=1
            s+=step
        return step

        

        
