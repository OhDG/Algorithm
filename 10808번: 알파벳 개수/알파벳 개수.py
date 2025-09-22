#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10808                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10808                          #+#        #+#      #+#     #
#    Solved: 2025/09/22 20:32:01 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

s = input().strip()
# strip 안쓰면 \n 도 받아져서 list에서 outofindex 에러남

counts = [0] * 26

for ch in s:
    counts[ord(ch) - ord('a')] += 1

for x in range(len(counts)):
    print(counts[x], end=' ')

# print(*counts)