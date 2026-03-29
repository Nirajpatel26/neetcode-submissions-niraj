class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        p_qeue= deque()
        p_seen= set()
        a_qeue = deque()
        a_seen = set()

        r,c = len(heights),len(heights[0])

        for i in range(c):
            p_qeue.append((0,i))
            p_seen.add((0,i))
        
        for j in range(1,r):
            p_qeue.append((j,0))
            p_seen.add((j,0))

        for i in range(r):
            a_qeue.append((i,c-1))
            a_seen.add((i,c-1))

        for j in range(c):
            a_qeue.append((r-1,j))
            a_seen.add((r-1,j))
        
        def bfs(que,seen):
            while que:
                i,j=que.popleft()
                seen.add((i,j))
                for i_off, j_off in [(1,0),(0,1),(-1,0),(0,-1)]:
                    new_r,new_c=i+i_off,j+j_off
                    if 0<= new_r < r and 0<= new_c < c and heights[new_r][new_c] >= heights[i][j] and (new_r,new_c) not in seen:
                        seen.add((new_r,new_c))
                        que.append((new_r,new_c))

            return seen
        p_cord = bfs(p_qeue,p_seen)
        a_cord = bfs(a_qeue,a_seen)

        return list(p_cord.intersection(a_cord)) 

