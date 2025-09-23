#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3273                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3273                           #+#        #+#      #+#     #
#    Solved: 2025/09/22 22:18:06 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

x = int(input())

arr.sort()
l, r = 0, n - 1
cnt = 0

while l < r:
    s = arr[l] + arr[r]
    if s == x:
        cnt += 1
        l += 1
        r -= 1
    elif s < x:
        l += 1
    else:
        r -= 1

print(cnt)
    
# result = 0

# for i in range(n):
#     for k in range(i + 1, n):
#         if arr[i] + arr[k] == x:
#             result += 1


# print(result)