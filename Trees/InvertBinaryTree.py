#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:41:23 2021

@author: raghhav
"""
#Inverting a Binary Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(node):
            if node == None:
                return
            else:
                invert(node.left)
                invert(node.right)
                temp = node.left
                node.left = node.right
                node.right = temp
        invert(root)
        return root
            