#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1806                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1806                           #+#        #+#      #+#     #
#    Solved: 2024/09/12 18:40:48 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

N, S = map(int, input().split())

arr = list(map(int, input().split()))


slow, fast = 0, 0
sum = 0
min_length = 1e9

while True:
    if sum >= S:
        min_length = min(min_length, fast - slow)
        sum -= arr[slow]
        slow += 1
    elif fast == N:
        break
    else:
        sum += arr[fast]
        fast += 1
    

if min_length == 1e9:
    print(0)
else:
    print(min_length)