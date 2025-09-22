#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2577                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2577                           #+#        #+#      #+#     #
#    Solved: 2025/09/22 21:14:50 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline


a = int(input())
b = int(input())
c = int(input())

cal = a * b * c

counts = [0] * 10

for ch in str(cal):
    counts[int(ch)] += 1

for x in range(len(counts)):
    print(counts[x])