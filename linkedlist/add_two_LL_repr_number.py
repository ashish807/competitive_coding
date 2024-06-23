
'''
https://leetcode.com/problems/add-two-numbers/description/
'''
from create_single import Node, SingleLinkedList

class Solution:
    def traverse_add(self, l1: Node, l2: Node):
        sum = ""
        carry = 0
        while(l1 is not None or l2 is not None):
            l1data, l2data = 0, 0
            if(l1 is not None):
                l1data = l1.data
                l1 = l1.next
            if(l2 is not None):
                l2data = l2.data
                l2 = l2.next
            div_mod= divmod(l1data + l2data + carry, 10)
            actual_sum = div_mod[1]
            carry = div_mod[0]
            sum = str(actual_sum) + sum
        if(carry >= 1):
            sum = str(carry) + sum
        return sum

            
    def reverse(self, head: Node)->int:
        reversedata = ""
        prev = None
        current = head
        while(current is not None):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        head = prev
        current = head
        while(current is not None):
            reversedata+= str(current.data)
            current = current.next
        return int(reversedata)
    
    def create_linked_list(self, number: str, head)->Node:
        node = Node(int(number))
        if(head is not None):
            node.next = head
        head = node
        return head
    
    def addTwoNumbers(self, l1: Node, l2: Node) -> Node:
        # first_reverse = self.reverse(l1)
        # second_reverse = self.reverse(l2)
        # final_sum = str(first_reverse + second_reverse)
        final_sum = self.traverse_add(l1, l2)
        head = None
        for i in final_sum:
            head = self.create_linked_list(i, head)
        return head

if __name__ == "__main__":
    sol = Solution()
    linkedList1 = SingleLinkedList()
    linkedList2 = SingleLinkedList()

    linkedList1.create_linkedlist(2)
    linkedList1.create_linkedlist(4)
    linkedList1.create_linkedlist(3)

    linkedList2.create_linkedlist(5)
    linkedList2.create_linkedlist(6)
    linkedList2.create_linkedlist(4)

    result:Node  = sol.addTwoNumbers(linkedList1.head, linkedList2.head)

    curr = result
    while(curr is not None):
        print(curr.data, "=> ", end="")
        curr =  curr.next
    print("Null")



        