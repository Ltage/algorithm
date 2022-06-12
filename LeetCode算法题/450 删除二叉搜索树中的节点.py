# https://leetcode.cn/problems/delete-node-in-a-bst/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        rootparent = TreeNode(left=root)

        # 存入值为key的节点与其父节点
        node = root
        key_node_parent = rootparent

        while node is not None and node.val != key:
            key_node_parent = node
            if key < node.val:
                node = node.left
            else:
                node = node.right

        # 未找到key值节点
        if node is None:
            return root

        # key节点没有孩子
        if node.left is None and node.right is None:
            if key_node_parent.left == node:
                key_node_parent.left = None
            else:
                key_node_parent.right = None

        # key节点只有左孩子
        if node.left is not None and node.right is None:
            if key_node_parent.left == node:
                key_node_parent.left = node.left
            else:
                key_node_parent.right = node.left

        # key节点只有右孩子
        if node.left is None and node.right is not None:
            if key_node_parent.left == node:
                key_node_parent.left = node.right
            else:
                key_node_parent.right = node.right

        # key节点有左右孩子
        if node.left is not None and node.right is not None:

            # 后继节点及其父节点(在右子树中查找)
            successor_node = node.right
            successor_node_parent = node

            while successor_node.left is not None:
                successor_node_parent = successor_node
                successor_node = successor_node.left

            # 后继节点为key的右孩子
            if node.right == successor_node:
                if key_node_parent.left == node:
                    key_node_parent.left = successor_node
                else:
                    key_node_parent.right = successor_node
                successor_node.left = node.left

            # 后继节点在key的右子树中但不是右孩子
            else:
                if key_node_parent.left == node:
                    key_node_parent.left = successor_node
                else:
                    key_node_parent.right = successor_node
                successor_node_parent.left = successor_node.right
                successor_node.left = node.left
                successor_node.right = node.right

        return rootparent.left
