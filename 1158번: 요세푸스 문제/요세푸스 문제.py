#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1158                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1158                           #+#        #+#      #+#     #
#    Solved: 2025/09/23 16:53:34 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(range(1, n + 1))
ans = []
idx = 0

while arr:
    idx = (idx + k - 1) % len(arr)
    ans.append(arr.pop(idx))

print("<", end='')

for i in range(len(ans)):
    if i == (len(ans) - 1):
        print(ans[i], end='')
        break
    print(ans[i], end=', ')

print(">")