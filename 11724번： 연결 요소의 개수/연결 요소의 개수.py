#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11724                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11724                          #+#        #+#      #+#     #
#    Solved: 2024/08/19 21:44:01 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
import sys

# input = sys.stdin.readline()

N, M = map(int, sys.stdin.readline().split())

arr = []
graph = [ [] for _ in range(N+1) ]

for i in range(M):
    arr.append(list(map(int, sys.stdin.readline().split())))

    graph[arr[i][0]].append(arr[i][1])
    graph[arr[i][1]].append(arr[i][0])

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False for _ in range(N+1)]
count = 0

for i in range(1, N+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count)