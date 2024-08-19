#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16953                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16953                          #+#        #+#      #+#     #
#    Solved: 2024/08/15 16:11:53 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
import sys

input = sys.stdin.readline()

A, B = map(int, input.split())
result = 1

while B > A:
    if B % 2 == 0:
        B /= 2
        result += 1
    elif B % 10 == 1:
        tmp = B // 10
        B = tmp
        result += 1
    else:
        result = -1
        break

if not A == B:
    result = -1

print(result)