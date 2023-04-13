# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 수가 주어진다. 
# 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.


# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력 1 복사
# 5
# 5
# 2
# 3
# 4
# 1
# 예제 출력 1 복사
# 1
# 2
# 3
# 4
# 5

import sys
input = sys.stdin.readline

times = int(input())

#    ascending order : 오름차순    #
def IN(times: int):
    num_list = []
    
    for i in range(times):
        append_num = int(input())
        num_list.append(append_num)
    
    num_list.sort()
    
    for i in num_list:
        print(i)

IN(times)
