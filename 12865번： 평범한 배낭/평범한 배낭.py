#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12865                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12865                          #+#        #+#      #+#     #
#    Solved: 2024/09/16 22:36:36 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [[0, 0]]

for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1): # 물품1번 부터 물품N번까지 하나씩 넣기 시도
    for j in range(1, K+1): # 최대 무게 j
        weight, value = arr[i][0], arr[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], value+dp[i-1][j-weight])

print(dp[N][K])