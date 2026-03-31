class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = defaultdict(list)

        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        visited =set()
        
        def dfs(node, parent):
            visited.add(node)
            for nei in g[node]:
                if nei not in visited:
                    if dfs(nei,node):
                        return True
                elif nei!=parent:
                    return True
                
            return False
        return not dfs(0, -1) and len(visited) == n