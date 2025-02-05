

def dfs(isla, start, treasure):
    fila = len(isla)
    columna = len(isla[0])
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [start]  
    distancias = [[-1 for _ in range(columna)] for _ in range(fila)]
    distancias[start[0]][start[1]] = 0
    
    while stack:
        x, y = stack.pop()
        if (x, y) == treasure:
            return distancias[x][y]
        
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < fila and 0 <= ny < columna and isla[nx][ny] != 1 and distancias[nx][ny] == -1:
                stack.append((nx, ny))  
                distancias[nx][ny] = distancias[x][y] + 1
    
    return -1

isla = [
    ['X', 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 'T', 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
]

start = (0, 0)
treasure = (5, 5)

res = dfs(isla, start, treasure)
print("Distancia mínima para llegar al tesoro:", res)