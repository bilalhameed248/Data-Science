class Node:
    def __init__(self, item):
        self.item=item
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_end(self,n):
        newNode=Node(n)
        if self.head:
            current=self.head
            while current.next:
                current=current.next
            current.next=newNode
        else:
            self.head=newNode
    
    def insert_at_start(self, n):
        newNode=Node(n)
        if self.head:
            current=self.head
            self.head=newNode
            newNode.next=current
        else:
            self.head=newNode
    

    def search_item(self, n):
        if self.head:
            current=self.head
            while current:
                if n==current.item:
                    found=True
                else:
                    found=False
                current=current.next
            return found
        else:
            print("\nlinklist is empty")
    
    def delete_item(self, n):
        if self.head:
            current=self.head
            prev=None
            while current:
                if n==current.item:
                    prev.next=current.next
                    delete=True
                else:
                    delete=False
                prev=current
                current=current.next
            return delete


    def print_all(self):
        current=self.head
        while current:
            print(current.item, end=" ")
            current=current.next

    def reverse(self):
        if self.head:
            current=self.head
            previous=None
            following=current.next
            while current:
                current.next=previous
                previous=current
                current=following
                if following:
                    following=following.next
            self.head=previous


if __name__=='__main__':
    linked_list=LinkedList()
    
    #insert item at end

    for i in range(6):
        linked_list.insert_at_end(i)
    
    #insert item at start

    for j in range(10,15):
        linked_list.insert_at_start(j)
    
    #print all list
    print("\nprint before delete")
    linked_list.print_all()
    
    #delete item from list
    is_delete = linked_list.delete_item(4)
    if is_delete==True:
        print("\nItem Delete")
    else: 
        print("\nItem not Found")


    #print list after Delete
    print("\nprint AFter Delete")
    linked_list.print_all()


    #search item in a lsit
    is_found=linked_list.search_item(55)
    if is_found==True:
        print("\nSearch Element Found")
    else:
        print("\nSearch Element Not Found")

    #print After Reverse
    print("\n\n Print AFter Reverse")
    linked_list.reverse()
    linked_list.print_all()
