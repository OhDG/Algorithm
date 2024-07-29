#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1931                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1931                           #+#        #+#      #+#     #
#    Solved: 2024/07/26 01:34:53 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# import sys 
# n = int(input())
# arr = [ [0 for j in range(3)] for i in range(n) ]

# for i in range(n):
#     arr[i][0], arr[i][1] = input().split()
#     arr[i][0] = int(arr[i][0])
#     arr[i][1] = int(arr[i][1])
#     arr[i][2] = int(arr[i][1]) - int(arr[i][0])

# # str -> int로 변환해줘야 함


# # N 가지의 회의로 시작하는 모든 경우 다 돌아본다 -> 말이 안됨
# # for i in range(n):
# #     count = 0
# #     count += 1 # 회의 1

# #     for k in range(n):
# #         if arr[i][1] <= arr[k][0]:
# #             print()

# arr.sort(key=lambda x: (x[1], x[0]))
# # end 시간 기준으로 오름차순 정리, 같으면 회의 시간(end-start) 기준으로 오름차순 정리


# isFinished = True
# finalResult = 0

# for k in range(n):
#     result = 1
#     idx = k

#     while True:
#         isFinished = True
#         for i in range(idx+1, n):
#             if arr[idx][1] <= arr[i][0]:
#                 result += 1
#                 idx = i
#                 isFinished = False
#                 break
        
#         if isFinished == True:
#             break
    
#     if result > finalResult:
#         finalResult = result


# print(finalResult)

# # 1차 시도 -> 4가 나와야 하는데 6이 나왔음 완전 럭키비키

# # int로 형변환을 end-start 값만 해줬는데 sort가 적용되려면 start와 end도 int형으로 해줘야 한다!

# # 최대 회의가 무조건 인덱스 0 부터 시작한다는 보장이 없으므로 idx를 다 돌아줌

# # 이젠 시간 초과가 뜸

# # 위에서 idx를 돌아줄 때 기존에 result += 1 해줄 때 판단하는 idx와 명칭이 같아서 오류가 났었음


n = int(input())
arr = [ [0 for j in range(3)] for i in range(n) ]

for i in range(n):
    arr[i][0], arr[i][1] = input().split()
    arr[i][0] = int(arr[i][0])
    arr[i][1] = int(arr[i][1])
    arr[i][2] = int(arr[i][1]) - int(arr[i][0])
 
# str -> int로 변환해줘야 함


# N 가지의 회의로 시작하는 모든 경우 다 돌아본다 -> 말이 안됨
# for i in range(n):
#     count = 0
#     count += 1 # 회의 1

#     for k in range(n):
#         if arr[i][1] <= arr[k][0]:
#             print()

arr.sort(key=lambda x: (x[1], x[0]))
# end 시간 기준으로 오름차순 정리, 같으면 회의 시간(end-start) 기준으로 오름차순 정리
# 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
# 이 경우 때문에 회의 시간 기준으로 오름차순 정리하면 최대 회의 수 나올 수 없음
# ex) (0, 1) (2, 2) (1, 2) <-> (0, 1) (1, 2) (2, 2)
# 그래서? 회의 시간 대신 start 시간 기준으로 오름차순 정리해줌 

idx = 0
result = 1
isFinished = True

while True:
    isFinished = True
    for i in range(idx+1, n):
        if arr[idx][1] <= arr[i][0]:
            print(arr[i][0])
            result += 1
            idx = i
            isFinished = False
            break
    
    if isFinished == True:
        break

print(result)

# 1차 시도 -> 4가 나와야 하는데 6이 나왔음 완전 럭키비키

# int로 형변환을 end-start 값만 해줬는데 sort가 적용되려면 start와 end도 int형으로 해줘야 한다!
