class Node:
    def __init__(self,data):
        self.data = data
        self.head = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverseUtil(self,current,previous):
        #If last node mark it head
        if current.next is None:
            self.head = current

            current.next = previous
            return
        
        next = current.next

        current.next = previous

        self.reverseUtil(next,current)

    def reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head,None)
    
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == '__main__':

    linkedList = LinkedList()
    linkedList.push(9)
    linkedList.push(8)
    linkedList.push(7)
    linkedList.push(6)
    linkedList.push(5)
    linkedList.push(4)
    linkedList.push(3)
    linkedList.push(2)
    linkedList.push(1)
    linkedList.push(0)
    linkedList.push(-1)

    print("Given Linked List: ")
    linkedList.printList()

    linkedList.reverse()

    print("\nReversed Linked List: ")
    linkedList.printList()