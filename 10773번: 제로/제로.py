#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10773                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10773                          #+#        #+#      #+#     #
#    Solved: 2025/09/29 16:25:21 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

k = int(input())

arr = []

for _ in range(k):
    m = int(input())
    if m != 0:
        arr.append(m)
    else:
        arr.pop()

sum = 0

for i in range(len(arr)):
    sum += arr[i]

print(sum)