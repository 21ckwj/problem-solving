n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data:
    count += 1 # 현재 그룹에 포함된 모험가의 수

    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면, 그룹결성
        result +=1
        count =0

print(result)