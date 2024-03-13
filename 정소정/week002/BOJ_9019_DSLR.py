import sys
input = sys.stdin.readline
from collections import deque

def bfs(a, b):
    visited = [False for _ in range(10001)]
    queue = deque()
    queue.append((a, ''))
    visited[a] = True

    while queue:
        number, test = queue.popleft()
        
        if number == b:
            return test

        d = number * 2 % 10000
        if not visited[d]:
            visited[d] = True
            queue.append((d, test + 'D'))
          
        s = (number - 1) % 10000
        if not visited[s]:
            visited[s] = True
            queue.append((s, test + 'S'))

        l = number // 1000 + number % 1000 * 10
        if not visited[l]:
            visited[l] = True
            queue.append((l, test + 'L'))

        r = number // 10 + number % 10 * 1000
        if not visited[r]:
            visited[r] = True
            queue.append((r, test + 'R'))

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a, b))