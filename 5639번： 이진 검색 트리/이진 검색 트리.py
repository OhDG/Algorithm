#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5639                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5639                           #+#        #+#      #+#     #
#    Solved: 2024/09/05 17:11:16 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(20000)



# class Node:
#     def __init__(self, item):
#         self.val = item
#         self.left = None
#         self.right = None

# # 이진트리 만들기
# class BinaryTree:
#     # 초기값 head는 None
#     def __init__(self):
#         self.head = Node(None)
#         # self.postorder_list=[]

#     # 값 추가하기 head가 없을 경우
#     def add(self, item):
#         if self.head.val is None:
#             self.head.val = item

#         # head가 있으면 왼쪽배치 or 오른쪽배치
#         else:
#             self.__add_node(self.head, item)

#     # head가 있는 경우
#     def __add_node(self, cur, item):
#         # print('부모:', cur.val, '자식:', item)
#         # head 값이 크면 왼쪽으로
#         if cur.val >= item:
#             if cur.left is not None:
#                 self.__add_node(cur.left, item)
#             else:
#                 cur.left = Node(item)
#         # head 값이 작으면 오른쪽으로
#         else:
#             if cur.right is not None:
#                 self.__add_node(cur.right, item)
#             else:
#                 cur.right = Node(item)

#      # 후위순회
#     def postorder_traverse(self):
#         if self.head is not None:
#             self.__postorder(self.head)

#     def __postorder(self, cur):
#         if cur.left is not None:
#             self.__postorder(cur.left)

#         if cur.right is not None:
#             self.__postorder(cur.right)

#         # self.postorder_list.append(cur.val)
#         print(cur.val)



# nodes = []


# while True:
    # try:
    #     node = input().strip()
    #     nodes.append(int(node))
    # except:
    #     break

# # print(nodes)

# # 트리 만들기
# bst = BinaryTree()

# for i in range(len(nodes)):
#     bst.add(nodes[i])

# bst.postorder_traverse()



# def postorder(first, end):
#     if first > end:
#         return
    
#     mid = end + 1
    
#     for i in range(first + 1, end + 1):
#         if num_list[first] < num_list[i]:
#             mid = i
#             break
    
#     # print(mid, first, end)

#     postorder(first + 1, mid - 1)
#     postorder(mid, end)
#     print(num_list[first])

# postorder(0, len(num_list) - 1)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

num_list = []
while True:
    try:
        node = input().strip()
        num_list.append(int(node))
    except:
        break


def solution(A):
    if len(A) == 0:
        return
    
    tempL, tempR = [], []

    mid = A[0]

    for i in range(1, len(A)):
        if A[i] > mid:
            tempL = A[1:i]
            tempR = A[i:]
            break
        else:
            tempL = A[1:]

    solution(tempL)
    solution(tempR)
    print(mid)

solution(num_list)