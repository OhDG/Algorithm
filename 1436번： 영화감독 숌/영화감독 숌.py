#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1436                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1436                           #+#        #+#      #+#     #
#    Solved: 2024/07/25 18:53:54 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

n = int(input())
count = 0
i = 0
while (True):
    i += 1
    # if "6666" in str(i):
    #     count += 1
    #     if n == count:
    #         print(i)
    #         break
    #     continue
    if "666" in str(i):
        count += 1
        if n == count:
            print(i)
            break