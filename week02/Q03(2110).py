# 문제
# 도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
# 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 
# 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.
# 출력
# 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.

# 예제 입력 1
# 5 3
# 1
# 2
# 8
# 4
# 9
# 예제 출력 1
# 3
import sys
input = sys.stdin.readline

# input 값 setting
house_location = []

house, iptime = map(int, input().split())
for i in range(int(house)):
    house_location.append(int(input()))
house_location.sort()

# binary_search location setting / 정답 셋팅(-1)
left, right = 1, house_location[-1] - house_location[0]
answer = - 1

while(left <= right):
    mid = (left + right) // 2 # ? 왜 미드를 구하는지에 대한 ? 
    setting = 1 # 공유기 셋팅 대수 3이 꽉차면 한칸 줄임
    iptime_location = house_location[0] # 공유기 로케이션 셋 house_location[0] -> 1
    
    for i in range(1, house): #집의 개수 많큼 움직임 (ex:5) -> range(1, 5)
        distance = house_location[i] - iptime_location # 거리 측정으로 가장 인접한 공유기 사이의 최대 거리 출력.
        if distance >= mid: #거리가 미드의 값보다 많으면 공유기를 설치?
            iptime_location = house_location[i] 
            setting += 1
    if setting >= iptime:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
        
print(answer)