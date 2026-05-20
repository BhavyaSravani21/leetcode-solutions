class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        seenA = set()
        seenB = set()
        common = 0
        ans = []
        for i in range(len(A)):
            a = A[i]
            b = B[i]
            seenA.add(a)
            seenB.add(b)
            if a in seenB:
                common += 1
            if b in seenA and a != b:
                common += 1
            ans.append(common)
        return ans
        
