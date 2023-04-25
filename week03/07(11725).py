# 11725번 : 트리의 부모 찾기
# BFS - 

"""
문제 : 루트 없는 트리가 주어집니다! 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오!
입력 : 첫째 줄에 노드의 개수 N이 주어집니다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
출력 : 첫째 줄부터 N-1 개의 줄에 각 노드의 부모 노드 번호를 2번 노드 부터 순서대로 출력한다.

예제 입력 1
7
1 6
6 3
3 5
4 1
2 4
4 7

예제 출력 1
4
6
1
3
1
4
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
Tree = [[] for _ in range(N + 1)]
Parents = [0 for _ in range(N + 1)]
            
for _ in range(N-1):
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)
    
def DFS(start, tree, parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            DFS(i, tree, parents)
            
DFS(1, Tree, Parents)

for i in range(2, N + 1):
    print(Parents[i])
    
    
    # https://smartstore.naver.com/funkeys/products/8325320986
    # https://smartstore.naver.com/funkeys/products/8325259822
    # 한번 타건해보는게 제일 좋긴하지 나중에 ㄱㄱ