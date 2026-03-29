class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g= defaultdict(list)

        for a,b in prerequisites:
            g[a].append(b)
        
        unvisited = 0
        visited = 2
        visiting = 1
        states = [unvisited]*numCourses

        def dfs(node):
            state = states[node]
            if state == visited:
                return True
            elif state == visiting:
                return False
            
            states[node]= visiting
            for nei in g[node]:
                if not dfs(nei):
                    return False
            states[node] = visited
            return True

            pass
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
