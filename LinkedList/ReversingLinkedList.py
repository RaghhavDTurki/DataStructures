#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:25:18 2021

@author: raghhav
"""
# Question link : https://leetcode.com/problems/reverse-linked-list
#Reversing a Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # a-->b-->c-->d-->None
        if (head == None):
            return None
        else:
            prev = None
            curr = head  #->a
            next = None
            while(curr != None): #a b c d
                next = curr.next    #b c d None
                curr.next = prev    #a->None, b->a, c->b, d->c
                prev = curr         #a b c d
                curr = next         #b c d None
                
            return prev