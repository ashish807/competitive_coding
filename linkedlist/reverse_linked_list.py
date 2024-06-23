from create_single import SingleLinkedList, Node

def insert_data(data:int, linkedList: SingleLinkedList):
    linkedList.create_linkedlist(data)

def reverse_linkedlist(linkedList:SingleLinkedList):
    prev = None
    current = linkedList.head
    while(current is not None):
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    linkedList.head = prev


if __name__ == "__main__":
    linkedList = SingleLinkedList()
    for i in range(10):
        linkedList.create_linkedlist(i)
    print("printing reverse...")
    reverse_linkedlist(linkedList)
    linkedList.get_all_element()


        
        
        
