import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(y, x):
    queue = deque()
    queue.append([y,x])
    visited[y][x] = True

    while(queue):
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(0>nx or nx>=n or 0>ny or ny>=m):
                continue

            if graph[nx][ny] == 1 and not visited[nx][ny]:
                queue.append([nx,ny])
                visited[nx][ny] = True
        

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())

    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)