#Node class
class Node:
    #Function to initialize the node object
    def __init__(self,data):
        self.data = data
        self.next = None

#Linked List class ontains a Node object
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    #Print function of the linked_list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':

    linked_list = LinkedList()

    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    linked_list.head.next = second;

    second.next = third;

    linked_list.printList()


'''
1.Linked List Insertion
2.Linked List Deletion (Deleting a given key)
3.Linked List Deletion (Deleting a key at given position)
4.Find Length of a Linked List (Iterative and Recursive)
5.Search an element in a Linked List (Iterative and Recursive)
6.Nth node from the end of a Linked List
7.Reverse a linked list

'''