# Q12865 / 아주 평범한 배낭에 관한 문제.
'''
4 7
6 13
4 8
3 6
5 12
'''

import sys
input = sys.stdin.readline

N, K  = map(int, input().split())
stuff = [[0, 0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for _ in range(N):
    stuff.append(list(map(int, input().split())))
    

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0]
        value = stuff[i][1]
        
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])
print(knapsack[N][K])

'''
알고리즘
1) x축엔 가방 1~K 까지의 무게, y축은 물건 N개 개수 만큼의 배열을 만들어준다.

2) 행을 차례대로 돌며 다음과 같은 알고리즘을 수행해준다.

 

3-0) 현재 물건이 현재 돌고있는 무게보다 작다면 바로 [이전 물건][같은 무게] (knapsack[i-1][j]를 입력해준다.

3-1) 현재 물건을 넣어준다. 물건을 넣은 뒤의 남은 무게를 채울 수 있는 최댓값(knapsack[i-1][j-weight]을 위의 행에서 가져와 더해준다.

3-2) 현재 물건을 넣어주는 것보다. 다른 물건들로 채우는 값(knapsack[i-1][j])을 가져온다.

4) 3-1과 3-2 중 더 큰 값을 knapsack[i][j]에 저장해준다. 이 값은 현재까지의 물건들로 구성할 수 있는 가장 가치 높은 구성이다.

5) knapsack[N][K]는 곧, K무게일 때의 최댓값을 가리킨다.

 

수식
결국 수식으로 표현하면 다음과 같다.

knapsack[i][j] = max(현재 물건 가치 + knapsack[이전 물건][현재 가방 무게 - 현재 물건 무게], knapsack[이전 물건][현재 가방 무게])

knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

 

결국 아래와 같은 엑셀이 만들어진다.

 	 	0	1	2	3	4	5	6	7
w	v	 	 	 	 	 	 	 	 
6	13	 	0	0	0	0	0	13	13
4	8	 	0	0	0	8	8	13	13
3	6	 	0	0	6	8	8	13	14
5	12	 	0	0	6	8	12	13	14
 '''