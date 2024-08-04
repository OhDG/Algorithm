#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1026                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1026                           #+#        #+#      #+#     #
#    Solved: 2024/08/03 15:54:11 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

n = int(input())

result = 0

arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrA.sort()
arrB.sort(reverse=True)

for i in range(n):
    result += arrA[i] * arrB[i]

print(result)
# arrA.sort()
# print(arrA)
# print(arrB)
# arrB.sort()

# for _ in range(n):
#     if min(arrA) == 0:
#         arrA.remove(min(arrA))
#         print(arrA)
#         print(arrB)

#         tmp = max(arrB)
#         arrB.remove(tmp)
#         result += 0
#         continue

#     if min(arrB) == 0:
#         arrB.remove(min(arrB))

#         tmp = max(arrA)
#         arrA.remove(tmp)
#         print(arrA)
#         print(arrB)
#         result += 0
#         continue

#     result += min(arrA) * min(arrB)
#     arrA.remove(min(arrA))
#     print(arrA)
#     print(arrB)
#     arrB.remove(min(arrB))
   
# print(result)

# 그냥 각 배열 sort해서 곱하면 되는거 아닌가? 했는데 0을 생각해야함
# 아 삽질했다 ㅜㅜ 걍 작은거 x 작은거 하면 제일 작겠지? 라는 생각을 함 ㅋㅋ
