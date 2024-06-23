'''
https://leetcode.com/problems/intersection-of-two-linked-lists/description/
'''
from create_single import Node, SingleLinkedList

class Solution:
    def getIntersectionNode(self, headA: Node, headB: Node) -> Node:
        unique_node = set()
        currA = headA
        while(currA is not None):
            unique_node.add(currA)
            currA = currA.next
        currB = headB
        while(currB is not None):
            if(currB in unique_node):
                break
            currB = currB.next
        print(currB)
        return currB
