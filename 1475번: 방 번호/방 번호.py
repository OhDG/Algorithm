#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1475                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1475                           #+#        #+#      #+#     #
#    Solved: 2025/09/22 21:23:41 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

n = int(input())

counts = [0] * 10


for i in str(n):
    counts[int(i)] += 1

counts[6] += counts[9]
if counts[6] % 2 == 1:
    counts[6] += 1
    
counts[9] = 0
counts[6] //= 2 
# / 으로 나누면 float, // 으로 나눠야 Int

max = 0

for i in range(9):
    if counts[i] > max:
        max = counts[i]

print(max)