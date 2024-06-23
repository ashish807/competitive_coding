class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def create_linkedlist(self, data):
        node = Node(data)
        if(self.head == None):
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
    
    def get_all_element(self):
        travel = self.head
        while(travel != None):
            print(travel.data, " => ", end="")
            travel = travel.next
        print("NULL")




