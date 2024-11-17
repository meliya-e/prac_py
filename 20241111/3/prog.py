class Maze:
    def __init__(self, N):
        self.N = N
        self.field = [['█' for _ in range(N * 2  + 1)] for _ in range(N * 2  + 1)]
        
        for i in range(1, N * 2  + 1, 2):
            for j in range(1, N * 2  + 1, 2):
                self.field[i][j] = '.'
    
    def __str__(self):
        return '\n'.join(''.join(row) for row in self.field)
    
    def __getitem__(self, key):
        x0, y0, x1, y1 = key[0], key[1].start, key[1].stop, key[2]
        if x0 == x1:  
            return self.check_path(x0 * 2 + 1, min(y0, y1) * 2 + 1, x0 * 2 + 1, max(y0, y1)* 2 + 1)
        elif y0 == y1: 
            return self.check_path(min(x0, x1)* 2 + 1, y0 * 2 + 1, max(x0, x1)* 2 + 1, y0 * 2 + 1)
        elif x0 < x1 and y0 < y1:
            return self.check_path(x0 * 2 + 1, y0 * 2 + 1, x1* 2 + 1, y1 * 2 + 1)
        return False

    def check_path(self, x0, y0, x1, y1):
        visited = set()
        return self.check_neighbors(x0, y0, x1, y1, visited)

    def check_neighbors(self, x, y, target_x, target_y, visited):
        if (x, y) in visited:
            return False
        visited.add((x, y))
        if (x, y) == (target_x, target_y):
            return True
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if self.field[ny][nx] == '·':
                if self.check_neighbors(nx, ny, target_x, target_y, visited):
                    return True
        return False
    
    def __setitem__(self, key, value):
        
        x0, y0, x1, y1 = key[0], key[1].start, key[1].stop, key[2]
        if x0 == x1: 
            self.open_or_close(x0, min(y0, y1), x0, max(y0, y1), value)
        elif y0 == y1: 
            self.open_or_close(min(x0, x1), y0, max(x0, x1), y0, value)
    
    def open_or_close(self, x0, y0, x1, y1, value):
        for x in range(x0 * 2 + 1 , (x1 * 2 + 2)  ):
            for y in range(y0* 2 + 1, (y1 * 2 + 2) ):
                self.field[y ][x ] = value
                

import sys
exec(sys.stdin.read())
