'''
Given a linked list, rearrange the node values such that they appear in alternating
low ➔ high ➔ low ➔ high ➔ ... form.
For example, given 1 ➔ 2 ➔ 3 ➔ 4 ➔ 5, you should return 1 ➔ 3 ➔ 2 ➔ 5 ➔ 4.
'''
from create_single import Node, SingleLinkedList

def rearrange_node(first, second, prev,  is_low):
    next_second_node = second.next
    if((is_low and first.data > second.data) or (not is_low and first.data < second.data)):
        first.next = second.next
        second.next = first
        if(prev is not None):
            prev.next = second
            prev = second
    else:
        prev = first
        first = first.next
    second = next_second_node
    return first, second, prev, not is_low
    

def rearrage(head: Node):
    is_low = True
    first = head
    second = head.next
    prev = None
    while(second is not None):
        first, second, prev, is_low = rearrange_node(first, second, prev, is_low)
    return head


if __name__ == "__main__":
    linkedList = SingleLinkedList()
    for i in range(1, 6):
        linkedList.create_linkedlist(i)
    head = rearrage(linkedList.head)
    linkedList.get_all_element()


        
                

            



