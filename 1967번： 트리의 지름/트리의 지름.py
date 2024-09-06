#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1967                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ohdonggyu <boj.kr/u/ohdonggyu>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1967                           #+#        #+#      #+#     #
#    Solved: 2024/09/06 16:28:23 by ohdonggyu     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

# print(tree)


def dfs(node, cost):
    global treezirm
    for tree_node, tree_weight in tree[node]:
        result_weight = cost + tree_weight

        if not visited[tree_node]:
            visited[tree_node] = True
            treezirm[tree_node] = result_weight
            dfs(tree_node, result_weight)
    
    return


# 루트(1)부터 제일 가중치 큰 노드 찾기

visited = [False] * (n+1)
visited[1] = True
treezirm = [0] * (n+1)

dfs(1, 0)
first, temp = 0, 0
for i in range(1, len(treezirm)):
    if visited[i]:
        if treezirm[i] > temp:
            temp = treezirm[i]
            first = i
        

print(first, treezirm)

visited = [False] * (n+1)
visited[first] = True
treezirm = [0] * (n+1)
dfs(first, 0)
print(max(treezirm))
# print(treezirm)