class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n=numCourses
        v=[0]*n
        pv=[0]*n
        graph=[[] for i in range(n)]
        for c,d in prerequisites:
            graph[d].append(c)
        res=[]
        def dfs(node):
            v[node]=1
            pv[node]=1
            for nei in graph[node]:
                if v[nei]==0:
                    if dfs(nei):
                        return True
                elif pv[nei]==1:
                    return True
            pv[node]=0
            res.append(node)
            return False
        for i in range(n):
            if v[i]==0:
                if dfs(i):
                    return []
        return res[::-1]        
