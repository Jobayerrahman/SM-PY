class Node:
    def __init__(self,data):
        self.data = data
        self.head = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def recursiveSearch(self,linkedList,key):
        
        if(not linkedList):
            return False
        
        if(linkedList.data == key):
            return True

        return recursiveSearch(linkedList.next, key)


if __name__ == '__main__':
    linkedList = LinkedList()

    linkedList.push(32)
    linkedList.push(22)
    linkedList.push(21)
    linkedList.push(33)
    linkedList.push(31)
    linkedList.push(35)
    linkedList.push(36)

    key = 36

    if linkedList.recursiveSearch(linkedList.head, key):
        print("Yes, Found it", key)
    else:
        print(key," Not Found!")