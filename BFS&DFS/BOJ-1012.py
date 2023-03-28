def bfs(x, y):
    queue = [[x, y]]
    while queue:
        x, y = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])
              
test_case = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(test_case):
    m, n, k = map(int, input().split())
    graph = [[0] * m for i in range(n)]
    cnt = 0
  
    for i in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
      
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                graph[i][j] = 0
                cnt += 1
    print(cnt)