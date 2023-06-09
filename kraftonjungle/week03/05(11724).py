# 연결 요소의 개수 (11724)

import sys
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    for i in adj[v]:
        if not visited[i]:
            dfs(i)
    
N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for j in range(1, N + 1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)
