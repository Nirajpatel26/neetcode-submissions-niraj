class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        order =[]

        for a,b in prerequisites:
            g[a].append(b)

        unvisited = 0
        visited = 2
        visiting = 1
        states = [unvisited]*numCourses

        def dfs(node):
            if states[node] == visiting :
                return False
            if states[node] == visited :
                return True
            states[node] = visiting

            for nei in g[node]:
                if not dfs(nei):
                    return False
            
            states[node] = visited
            order.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order