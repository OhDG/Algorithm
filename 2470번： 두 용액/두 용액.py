#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2470                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2470                           #+#        #+#      #+#     #
#    Solved: 2024/09/12 19:44:54 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

arr.sort()


# print(arr)
# [-99, -2, -1, 4, 98]

# target = 0

# 형식 1 앞에서 시작하는 포인터, 끝에서 시작하는 포인터

# pointer1, pointer2 = 0, len(arr)-1

# while True:
#     if arr[pointer1] + arr[pointer2] > target:
#         tmp_sum = arr[pointer1] + arr[pointer2]
#         pointer2 -= 1
        
#         if abs(tmp_sum) < abs(arr[pointer1] + arr[pointer2]):
#             print(arr[pointer1], arr[pointer2+1])
#             break

#     elif arr[pointer1] + arr[pointer2] < target:
#         tmp_sum = arr[pointer1] + arr[pointer2]
#         pointer1 += 1

#         if abs(tmp_sum) < abs(arr[pointer1] + arr[pointer2]):
#             print(arr[pointer1-1], arr[pointer2])
#             break

#     else:
#         print(arr[pointer1], arr[pointer2])

start = 0
end = N-1

answer = abs(arr[start] + arr[end])
result = [arr[start], arr[end]]

while start < end:
    sum = arr[start] + arr[end]
    
    if abs(sum) < answer:
        answer = abs(sum)
        result = [arr[start], arr[end]]

    if sum > 0:
        end -= 1
    elif sum < 0:
        start += 1
    else:
        break

print(result[0], result[1])