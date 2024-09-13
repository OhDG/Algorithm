#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2473                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2473                           #+#        #+#      #+#     #
#    Solved: 2024/09/13 16:02:12 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
import math
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

arr.sort()

result = [0, 0 ,0]
answer = math.inf

for i in range(N-2):
    start = i
    mid = i+1
    end = N-1

    while mid < end:
        sum = arr[start] + arr[mid] + arr[end]

        if abs(sum) < answer:
            answer = abs(sum)
            result = [arr[start], arr[mid], arr[end]]

        if sum > 0:
            end -= 1
        elif sum < 0:
            mid += 1
        else:
            break

print(result[0], result[1], result[2])