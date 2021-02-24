#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:18:02 2021

@author: raghhav
"""
# Question link : https://leetcode.com/problems/maximum-depth-of-binary-tree
# Max Depth of a Binary tree
# The maximum depth is the number of nodes along the 
# longest path from the root node down to the farthest leaf node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def depth(node):
            maxdepth = -1 
            if (node == None):
                return (maxdepth + 1)
            else:
                maxld = depth(node.left)
                maxrd = depth(node.right)
                
                maxdepth = max(maxld,maxrd,maxdepth) + 1
                return maxdepth
        return (depth(root))
            