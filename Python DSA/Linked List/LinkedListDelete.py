class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    
    def deleteFromBeginning(self):
        temp = self.head
        self.head = self.head.next


    def deleteNodeAtGivenPosition(self,position):
        if self.head is None:
            return
        index = 0
        current = self.head

        while current.next and index < position:
            previous = current
            current = current.next
            index += 1

            if index < position:
                pass

            elif index == 0:
                self.head = self.head.next
            
            elif index == position:
                previous.next = current.next

            else:
                print("\nIndex is out of the range")
            
        

    def printList(self):
        temp = self.head
        while(temp):
            print(" %d " % (temp.data), end=" ")
            temp = temp.next
            

if __name__ == "__main__":
    linkedList = LinkedList()

    linkedList.head = Node(0)
    secondNode = Node(1)
    thirdNode = Node(2)
    forthNode = Node(3)
    fifthNode = Node(4)

    linkedList.head.next = secondNode
    secondNode.next = thirdNode
    thirdNode.next = forthNode
    forthNode.next = fifthNode

    print("Created Linked List: ")
    linkedList.printList()

    print("\nDelete Node Beginning of the Linked List: ")
    linkedList.deleteFromBeginning()
    linkedList.printList()

    print("\nLinked List after Deletion at position 2: ")
    linkedList.deleteNodeAtGivenPosition(2)
    linkedList.printList()
        