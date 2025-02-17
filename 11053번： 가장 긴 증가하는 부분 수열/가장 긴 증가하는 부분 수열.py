#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11053                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11053                          #+#        #+#      #+#     #
#    Solved: 2024/09/20 15:34:54 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N = int(input())

arrA = list(map(int, input().split()))

result = []
maxArr = []


for j in range(N):
    result.append(arrA[j])

    for i in range(j+1, len(arrA)):
        result_len = len(result)

        if arrA[i] > result[result_len-1]:
            result.append(arrA[i])
    
    maxArr.append(len(result))
    result = []

# print(maxArr)
print(max(maxArr))
