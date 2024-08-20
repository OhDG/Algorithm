#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1697                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1697                           #+#        #+#      #+#     #
#    Solved: 2024/08/20 14:48:05 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())

time, method = 0, 0





# 동생 위치에서 시작해야할듯?

# 이동할 세 방법 a, b, c
dx = [1, -1, 2]

# 0이 안가본 곳, 10이 목적지
graph = [0 for _ in range(100001)]
graph[N] = 0

# 가장 빠른 -> bfs 만들어보기

def bfs(n, k):
    time = 0
    method = 0
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()

        for i in range(3):
            if dx[i] == 2:
                nx = x * 2
            else:
                nx = x + dx[i]

            if nx < 0 or nx > 100000:
                continue

            if nx == n:
                continue

            if graph[nx] == 0:
                graph[nx] = graph[x] + 1
                queue.append(nx)

            if nx == k:
                time = graph[nx]
                method += 1
        
        

    print(time)
    # print(method)

# if K < N:
#     time = N - K
#     method = 1
# elif K == N:
#     time = 0
#     method = 1
# else:
bfs(N, K)
