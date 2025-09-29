#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10828                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10828                          #+#        #+#      #+#     #
#    Solved: 2025/09/28 16:22:34 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

n = int(input())
result = [] 

for _ in range(n):
    input_arr = list(input().split())

    if input_arr[0] == 'push':
        result.append(input_arr[1])
    elif input_arr[0] == 'pop':
        if result:
            x = result.pop()
            print(x)
        else:
            print("-1")
    elif input_arr[0] == 'size':
        print(len(result))
    elif input_arr[0] == 'empty':
        if result:
            print('0')
        else:
            print('1')
    else:
        if result:
            x = result[len(result) - 1]
            print(x)
        else:
            print("-1")