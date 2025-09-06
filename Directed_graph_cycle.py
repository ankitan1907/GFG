
class Solution:
    def isCycle(self, V, edges):
        # code here
        
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        visited = [False] * V
        rec_stack = [False] * V

        def dfs(node):
            visited[node] = True
            rec_stack[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif rec_stack[neighbor]:
                    return True
            rec_stack[node] = False
            return False

        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True
        return False



