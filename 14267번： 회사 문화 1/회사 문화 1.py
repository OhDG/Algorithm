#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14267                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14267                          #+#        #+#      #+#     #
#    Solved: 2024/09/18 21:03:08 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

## dfs 방식
# import sys
# sys.setrecursionlimit(100000)
# input = sys.stdin.readline

# n, m = map(int, input().split())

# parent = list(map(int, input().split()))
# graph = [[] for _ in range(n+1)]

# for i in range(1, len(parent)):
#     graph[parent[i]].append(i+1)

# answer = [0] * (n+1)

# def dfs(x, cnt):
#     answer[x] += cnt
#     # print(answer)
#     for i in graph[x]:
#         # print(i)
#         dfs(i, cnt)

# for i in range(m):
#     u, cnt = map(int, input().split())
#     dfs(u, cnt)

# for i in range(1, len(answer)):
#     print(answer[i], end=' ')

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = [0] + list(map(int, input().split()))
point = [0] * (n + 1)

for i in range(m):         
    u, cnt = map(int, input().split())
    point[u] += cnt 

for i in range(2, n+1):    
    point[i] += point[parent[i]]
    
for i in range(1, len(point)):            
    print(point[i], end = ' ')
