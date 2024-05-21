class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

    
if __name__ == '__main__':
    linkedList = LinkedList()

    linkedList.push(20)
    linkedList.push(22)
    linkedList.push(23)
    linkedList.push(24)
    linkedList.push(25)
    linkedList.push(26)
    linkedList.push(21)
    linkedList.push(27)
    linkedList.push(28)

    x = 23
    v = []

    temp = linkedList.head

    while(temp):
        v.append(temp.data)
        temp = temp.next
    
    print(v)

    if x in v:
        print("Yes, Found it", x)
    else:
        print(x," Not Found!")