class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertInHead(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self,prev_node, new_data):
        if prev_node is None:
            print("The given previous node must in Linked List")
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertInLast(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while( last_node.next ):
            last_node = last_node.next
        
        last_node.next = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.head = Node(1)
    secondNode = Node(2)
    thirdNode = Node(4)

    linkedlist.head.next = secondNode
    secondNode.next = thirdNode

    linkedlist.insertInHead(0)

    linkedlist.printList()

    linkedlist.insertInLast(5)

    linkedlist.printList()

    linkedlist.insertAfter(secondNode, 3)

    linkedlist.printList()