#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1068                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1068                           #+#        #+#      #+#     #
#    Solved: 2024/08/29 20:10:01 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N = int(input())

parentNode = list(map(int, input().split()))
deleteNode = int(input())
nums = [deleteNode]
visited = []
tree = [ [] for _ in range(N) ]
root = 0 # 루트 노드

# 트리 만들기

for i in range(N):
    if parentNode[i] == -1:
        root = i
        visited.append(i)
    else:
        if i not in nums:
            index = parentNode[i]
            if index in nums:
                nums.append(i)
            else:
                visited.append(i)
                tree[index].append(i)


leaf_node_count = 0

# print(visited)
# print(tree)

def dfs(root):
    global leaf_node_count
    
    if tree[root] == []:
        leaf_node_count += 1
    else:
        for i in tree[root]:
            dfs(i)


if deleteNode != root:
    dfs(root)

print(leaf_node_count)


# # 삭제할 노드, 삭제할 부모를 가진 노드 제외해서 트리 만듦
# for i in range(N):
#     if parentNode[i] == -1:
#         continue
#     if i == deleteNode:
#         continue
#     if parentNode[i] == deleteNode:
#         continue
#     if parentNode[parentNode[i]] == deleteNode:
#         continue
    
#     tree[parentNode[i]].append(i)


# for i in range(N):
#     if tree[i] == []:
#         continue
#     else:
#         for k in tree[i]:
#             if tree[k] == []:
#                 result += 1

# if deleteNode == 0:
#     result = 0
# # print(tree)
# print(result)