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

    def search(self,key):
        current = self.head

        while(current != None):
            if current.data == key:
                return True
            current = current.next
        
        return False

if __name__ == '__main__':
    linkedList = LinkedList()

    linkedList.push(32)
    linkedList.push(23)
    linkedList.push(35)
    linkedList.push(31)
    linkedList.push(37)
    linkedList.push(39)
    linkedList.push(33)


    key = 35

    if linkedList.search(key):
        print("Yes, Found it", key)
    else:
        print(key," Not Found!")