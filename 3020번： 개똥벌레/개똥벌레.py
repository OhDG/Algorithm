#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3020                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3020                           #+#        #+#      #+#     #
#    Solved: 2024/09/09 10:22:25 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

N, H = map(int, input().split())

# trick = [0 for _ in range(N)]
# for i in range(N):
#     trick[i] = int(input())

# print(trick)

down = [] # 석순
up = [] # 종유석

for i in range(N):
    if i % 2 == 0:
        down.append(int(input()))
    else:
        up.append(int(input()))

down.sort()
up.sort()

min_count = N
range_count = 0

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return start

for i in range(1, H + 1):
    down_count = len(down) - binary_search(down, i - 0.5, 0, len(down) - 1)
    top_count = len(up) - binary_search(up, H - i + 0.5, 0, len(up) - 1)

    if min_count == down_count + top_count:
        range_count += 1
    elif min_count > down_count + top_count:
        range_count = 1
        min_count = down_count + top_count

print(min_count, range_count)
