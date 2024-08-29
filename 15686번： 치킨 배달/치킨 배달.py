#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15686                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15686                          #+#        #+#      #+#     #
#    Solved: 2024/08/29 15:24:59 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# graph = [list(map(int, input().split())) for _ in range(N)]

home = []
dak = []
result = 1000000

for i in range(N):
    arr = list(map(int, input().split()))

    for r in range(N):
        if arr[r] == 1:
            home.append((i, r))
        elif arr[r] == 2:
            dak.append((i, r))

visited = [ False for _ in range(len(dak)) ]

def back(idx, cnt):
    global result

    if cnt == M:
        mini = 0

        for i in home:
            distance = 1000000
            
            for k in range(len(dak)):
                if visited[k]:
                    newDistance = abs(i[0] - dak[k][0]) + abs(i[1] - dak[k][1])
                    distance = min(distance, newDistance)
            
            mini += distance
        
        result = min(mini, result)
        return

    for i in range(idx, len(dak)):
        if not visited[i]:
            visited[i] = True
            back(i+1, cnt+1)
            visited[i] = False

back(0, 0)

print(result)