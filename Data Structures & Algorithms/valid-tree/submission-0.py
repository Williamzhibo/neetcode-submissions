class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True 

        # if the n is trivial, its always true

        adj = { i: [] for i in range(n) } #building out our adjacency list

        for n1, n2 in edges: #building out adjacency graph so we can easily travers
            adj[n1].append(n2)
            adj[n2].append(n1)
        #building graph, then cycle detection using DFS/BFS, then ensure that it is connected -> meaning that we need the number of nodes that we visited to be equal to the number of expected notes 
        visit = set() #default we always do 

        def dfs(i, prev):
            if i in visit:
                return False #the second we detected a cycle, its not valid

            visit.add(i) #visit each node
            for j in adj[i]: #for each element in our list
                if j == prev: #
                    continue 
                if not dfs(j, i):
                    return False 
            return True 

        return dfs(0, -1) and n == len(visit)

