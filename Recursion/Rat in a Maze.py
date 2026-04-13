#Solution

class Solution:
    def findPath(self, m, n):
        result = []
        visited = [[False]*n for _ in range(n)]
        moves = [(1,0,'D'), (0,-1,'L'), (0,1,'R'), (-1,0,'U')]
        
        def isSafe(x, y):
            return (0 <= x < n and 0 <= y < n and 
                    not visited[x][y] and m[x][y] == 1)
        
        def solve(x, y, path):
            if x == n-1 and y == n-1:
                result.append(path)
                return
            
            for dx, dy, move in moves:
                nx, ny = x + dx, y + dy
                
                if isSafe(nx, ny):
                    visited[x][y] = True
                    solve(nx, ny, path + move)
                    visited[x][y] = False   
        
        if m[0][0] == 1:
            solve(0, 0, "")
        
        return result