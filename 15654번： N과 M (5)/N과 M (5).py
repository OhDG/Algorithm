#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15654                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15654                          #+#        #+#      #+#     #
#    Solved: 2024/08/27 21:06:19 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

# input = sys.stdin.readline()

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
# print(arr)



def back():
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return
    
    for i in range(N):
        if arr[i] not in ans:
            ans.append(arr[i])
            back()
            ans.pop()

ans = []
back()