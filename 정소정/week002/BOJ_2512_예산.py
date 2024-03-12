import sys
input = sys.stdin.readline

n = int(input())
money = list(map(int, input().split()))
m = int(input())

start, end = 0, max(money)

while start <= end:
    mid = (start + end) // 2
    ans = 0
    for i in money:
        if i > mid:
            ans += mid
        else:
            ans += i

    if ans <= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)