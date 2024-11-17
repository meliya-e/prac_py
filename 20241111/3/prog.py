class Maze:
    def __init__(self, N):
        self.N = N
        self.maze = [['█' for _ in range(N)] for _ in range(N)]

    def __getitem__(self, item):
        if isinstance(item, slice):
            x0, y0, x1, y1 = item.start[0], item.start[1], item.stop[0], item.stop[1]
            return self._is_reachable(x0, y0, x1, y1)
        else:
            return self.maze[item[0]][item[1]]

    def __setitem__(self, item, value):
        if isinstance(item, slice):
            x0, y0, x1, y1 = item.start[0], item.start[1], item.stop[0], item.stop[1]
            
            for x in range(min(x0,x1), max(x0,x1)+1):
                for y in range(min(y0,y1), max(y0,y1)+1):
                    if x == x0 and abs(y-y0) == 1:
                        self.maze[x][y] = value
                    if y == y0 and abs(x - x0) == 1:
                        self.maze[x][y] = value
        else:
            self.maze[item[0]][item[1]] = value

    def _is_reachable(self, x0, y0, x1, y1):
        visited = set()
        queue = [(x0, y0)]
        
        while queue:
            x, y = queue.pop(0)
            if (x, y) == (x1, y1):
                return True
            visited.add((x, y))
            
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.N and 0 <= ny < self.N and \
                   self.maze[nx][ny] == '·' and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    
        return False


    def __str__(self):
        return '\n'.join([''.join(row) for row in self.maze])

import sys
exec(sys.stdin.read())
