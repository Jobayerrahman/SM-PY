#7.Reverse a linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertInHead(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    #reverse fucntion
    def reserve(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

        
    #Print function of the linked_list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":

    linkedList = LinkedList()

    linkedList.insertInHead(2)
    linkedList.insertInHead(23)
    linkedList.insertInHead(23)
    linkedList.insertInHead(21)
    linkedList.insertInHead(32)
    linkedList.insertInHead(52)


    linkedList.printList()
    linkedList.reserve()
    linkedList.printList()