#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1946                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1946                           #+#        #+#      #+#     #
#    Solved: 2024/08/04 23:47:10 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
t = int(input())

# isSatisfied = True
for i in range(t):
    
    n = int(input())

    result = n
    # arr = [ [ 0 for _ in range(2) ] for _ in range(n) ]

    # for k in range(n):
    #    arr[k][0], arr[k][1] = map(int, input().split())

    arr = [ list(map(int, input().split())) for _ in range(n)]



    # for m in range(n):
    #     isSatisfied = True
    #     for s in range(n):
    #         if m == s:
    #             continue

    #         if arr[m][0] > arr[s][0] and arr[m][1] > arr[s][1]:
    #             isSatisfied = False
    #             break
        
    #     if isSatisfied == True:
    #         result += 1
    
    # print(result)

# VSCode에서는 테스트 맞는데 백준에서 시간초과 뜸

# input() 대신 sys.stdin.readline 이용해서 다시 시도 -> 그래도 안됨

# 중첩 for문을 줄이는 방법을 찾는다.. -> 잘 모르겠다 ㅜㅜ


    ###### 만족하지 않는 사람 찾기 -> 전체에서 빼기
    isSatisfied = False
    arr.sort()

    king = arr[0]
    for z in range(1, n):
        if king[1] < arr[z][1]:
            result -= 1
        else:
            king = arr[z]

    print(result)


