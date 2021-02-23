#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:19:49 2021

@author: raghhav
"""

#Max Depth of N-ary Tree
#self.children returns a list of all the children of the parent
#The maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def depth(node):
            maxdepth = 0
            if (node == None):
                return 0
            elif (node.children == []):
                return (maxdepth +1)
            else:
                for child in node.children:
                    ch = depth(child)
                    maxdepth = max(maxdepth,ch)
                maxdepth += 1
                return maxdepth
        return(depth(root))