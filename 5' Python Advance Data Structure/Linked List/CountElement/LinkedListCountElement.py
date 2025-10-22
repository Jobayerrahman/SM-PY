#4.Find Length of a Linked List (Iterative and Recursive)

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

    def getCount(self):
        temp = self.head
        count = 0
        while(temp):
            count +=1
            temp = temp.next
        return count

    def getCountRecursive(self,node):
        if(not node):
            return 0
        else:
            return 1 + self.getCountRecursive(node.next)

if __name__ == "__main__":

    linkedList = LinkedList()

    linkedList.insertInHead(2)
    linkedList.insertInHead(23)
    linkedList.insertInHead(23)
    linkedList.insertInHead(21)
    linkedList.insertInHead(32)
    linkedList.insertInHead(52)

    print("Count of nodes is (Iterative): ", linkedList.getCount())

    print("Count of nodes is (Recursive): ", linkedList.getCountRecursive(linkedList.head))