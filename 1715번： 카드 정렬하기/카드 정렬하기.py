#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1715                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1715                           #+#        #+#      #+#     #
#    Solved: 2024/08/05 20:45:57 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
import heapq

hq = []
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    k = int(input())
    heapq.heappush(hq, k)

# arr = [int(input()) for i in range(N) ]

result = 0

# 두개 뽑고 다시 힙에 넣고 반복하는 총 횟수 2N-2
# 근데? for문 한 사이클에 A, B 두 개를 pop 하니 K = n - 1 이어야 함 
# K = (2 * N - 2) / 2
K = N - 1 
for _ in range(K):
    A = heapq.heappop(hq)

    B = heapq.heappop(hq)
    tmp = A + B
    result += tmp
    heapq.heappush(hq, tmp)

print(result)