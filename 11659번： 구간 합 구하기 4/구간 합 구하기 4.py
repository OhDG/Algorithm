#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11659                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11659                          #+#        #+#      #+#     #
#    Solved: 2024/09/03 18:07:26 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arrN = list(map(int, input().split()))

arrM = [ list(map(int, input().split())) for _ in range(M)]

# print(arrN)
# print(arrM)

def prefix_sum():
    prefixSum = [0] * N
    prefixSum[0] = arrN[0]
    for i in range(1, N):
        prefixSum[i] = prefixSum[i-1] + arrN[i]
    return prefixSum

prefixSum = prefix_sum()

# print(prefixSum)
for s in range(M):
    if arrM[s][0] == 1:
        i = 0
        partSum = prefixSum[arrM[s][1]-1]
    else:
        i = arrM[s][0] - 2
        partSum = prefixSum[arrM[s][1]-1] - prefixSum[i]
    print(partSum)
