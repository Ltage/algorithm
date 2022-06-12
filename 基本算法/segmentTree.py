# 线段树


def builtTree(arr, tree, start, end, node):
    if start == end:
        tree[node] = arr[start]
        return
    mid = (end - start) // 2 + start
    node_left = 2 * node + 1
    node_right = 2 * node + 2
    builtTree(arr, tree, start, mid, node_left)
    builtTree(arr, tree, mid + 1, end, node_right)
    tree[node] = tree[node_left] + tree[node_right]


def updateTree(arr, tree, start, end, node, idx, val):
    if start == end:
        arr[idx] = val
        tree[node] = val
        return
    mid = (end - start) // 2 + start
    node_left = 2 * node + 1
    node_right = 2 * node + 2
    if start <= idx <= mid:
        updateTree(arr, tree, start, mid, node_left, idx, val)
    else:
        updateTree(arr, tree, mid + 1, end, node_right, idx, val)
    tree[node] = tree[node_left] + tree[node_right]


def queryTree(arr, tree, start, end, node, q_left, q_right):
    print(start, end)
    if q_left > end or q_right < start:
        return 0
    if q_left == q_right:
        return tree[node]
    if q_left <= start and q_right >= end:
        return tree[node]
    mid = (end - start) // 2 + start
    node_left = 2 * node + 1
    node_right = 2 * node + 2
    sum_left = queryTree(arr, tree, start, mid, node_left, q_left, q_right)
    sum_right = queryTree(arr, tree, mid + 1, end, node_right, q_left, q_right)
    sum_query = sum_left + sum_right
    return sum_query


if __name__ == '__main__':
    array = [1, 3, 5, 7, 9, 11]
    tree = [0] * 15
    builtTree(array, tree, 0, len(array) - 1, 0)
    print(tree)
    # updateTree(array, tree, 0, len(array) - 1, 0, 4, 6)
    # print(tree)
    print(queryTree(array, tree, 0, len(array) - 1, 0, 2, 5))
