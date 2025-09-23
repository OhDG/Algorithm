#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1406                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1406                           #+#        #+#      #+#     #
#    Solved: 2025/09/23 14:50:54 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

left = list(input().strip())
right = []

m = int(input())

for _ in range(m):
    cmd = input().split()
    if cmd[0] == 'L' and left:
        right.append(left.pop())
    elif cmd[0] == 'D' and right:
        left.append(right.pop())
    elif cmd[0] == 'B' and left:
        left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[1])

result = left + right[::-1]

for i in range(len(result)):
    print(result[i], end='')

# result_text = "".join(result)

# print(result_text)