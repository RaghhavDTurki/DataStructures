#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 12:21:28 2021

@author: raghhav
"""
# Question Link : https://www.interviewbit.com/problems/intersection-of-linked-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    #If we start from the point where both lists are equidistant from the 
    #merge point we would have to iterate only once
    def getIntersectionNode(self, A, B):
        def getlen(node):
            curr = node
            count = 0
            while(curr != None):
                count += 1
                curr = curr.next
            return count
        
        m = getlen(A)
        n = getlen(B)
        d = n-m
        if (m>n): #swap both the lists
            temp = A
            A = B
            B = temp
            d = m - n
        for i in range(d):
            B = B.next
        while ((A != None) and (B != None)): #Now Both A and B are equidistant from the merge point 
            if (A == B):
                return A;
            else:
                A = A.next
                B = B.next
        return None