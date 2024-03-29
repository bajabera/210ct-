class Node(object):
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None

class List(object):
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,n,x):
        #Not actually perfect: how do we prepend to an existing list?
        if n!=None:
            x.next=n.next
            n.next=x
            x.prev=n
            if x.next!=None:
                 x.next.prev=x              
        if self.head==None:
            self.head=self.tail=x
            x.prev=x.next=None
        elif self.tail==n:
             self.tail=x
    def display(self):
        values=[]
        n=self.head
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print ("List: "+",".join(values))
    def remove(self,n):#allows the removal of the head/tail node
        if n.prev!=None:
            n.prev.next=n.next
        else:
            self.head=n.next
        if n.next!=None:
            n.next.prev=n.prev
        else:
            self.tail=n.prev
    def remove_again(self,value1):#allows the removal of a node in the middle
        node = l.head
        while node!=l.tail:
            if node.value == value1:
                l.remove(node)
                l.display()
                break
            else:
                node = node.next
if __name__ == '__main__':
    l=List()
    l.insert(None, Node(4))
    l.insert(l.head,Node(6))
    l.insert(l.head,Node(8))
    l.insert(l.tail,Node(2))
    l.display()
    l.remove_again(6)
    
