class Vertex():
    def __init__(self, value):
        self.value=value
        self.adjacent=[]
        
    def add_edge(self,vertex):
         self.adjacent.append(vertex)
         #vertex.adjacent.append(self)
    def __eq__(self, test):
        return self.value==test

class Graph(Vertex):
    def __init__(self):
        self.nodelist=[]
        
    def add_node(self,value):
        self.nodelist.append(Vertex(value))
        

    def add_edge(self,head,tail):
        for i in self.nodelist:
            #if vertex in self.nodelist:
            if i ==head:
                head=i#getting the pointer that has value of head
            if i == tail:
                tail=i#getting the pointer that has the value of tail

        head.add_edge(tail)#connects the head to the tail. i.e. since its undirected, needs to be connected both ways like a linlked list
        tail.add_edge(head)#connects the tail to the head
        return None
        
    def __str__(self):
        '''
         automatically called when using the function print() on an object of the class Graph
        '''
        s=' '
        for i in self.nodelist:
            s+=str(i.value)+": "
            for j in i.adjacent:
                s+=str(j.value)+" "
            s+="\n"#jumps to new line
        return s
    def find_node(self,vertex):#Getting the object,vertex, from its corresponding value
        for i in self.nodelist:
            if i.value==vertex:
                return i
        

        
class Queue:#queue class with enqueue, dequeue and length of queue functions
    
    def __init__(self):
        self.queue=[]

    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        return self.queue.pop(0)
    def __len__(self):
        return len(self.queue)
    
class Stack:#stack class with push, pop and length of stack
    def __init__(self):
        self.stack=[]
        
    def push(self,value):
        self.stack.append(value)
        
    def pop(self):
        return self.stack.pop()

    def __len__(self):
        return len(self.stack)
    
    

        

    
    
def DFS(Graph, value):#starts at node with value, and explores a branch as far as possible before backtracking
    s=Stack()#uses stack class
    visited=[]
    vertex=Graph.find_node(value)
    s.push(vertex)
    while len(s)>0:
        u=s.pop()
        if u not in visited:
            visited.append(u)
            for e in u.adjacent:
                s.push(e)
    return visited

    
def BFS(Graph, value):#visits all nodes starting with node and then all its children
    q=Queue()#uses queue class
    visited=[]
    vertex=Graph.find_node(value)#gets the actual vertex object
    q.enqueue(vertex)
    while len(q)>0:
        u=q.dequeue()
        if u not in visited:
            visited.append(u)
            for e in u.adjacent:
                q.enqueue(e)
    return visited
    
        
if __name__ == "__main__":
    a=Graph()
    A=a.add_node('A')
    B=a.add_node('B')
    C=a.add_node('C')
    D=a.add_node('D')
    E=a.add_node('E')
    F=a.add_node('F')
    a.add_edge('A','B')
    a.add_edge('A','C')
    a.add_edge('A','D')
    a.add_edge('D','E')
    a.add_edge('E','B')
    a.add_edge('F','B')
    print(a)
    
    z=BFS(a,'C')
    print('\nBreadth first search')
    for i in z:
        print(i.value,end=" ")
    
    l=DFS(a,'D')
    print('\nDepth first search')
    for i in l:
        print (i.value,end=" ")
    
    
