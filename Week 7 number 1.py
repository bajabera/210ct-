class Vertex():
    def __init__(self, value):
        self.value=value
        self.adjacent=[]
        
    def add_edge(self,vertex):
         self.adjacent.append(vertex)
         
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
        tail.add_edge(head)
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

    
        
if __name__ == "__main__":
    a=Graph()
    a.add_node('A')
    a.add_node('B')
    a.add_node('C')
    a.add_node('D')
    a.add_node('E')
    a.add_node('F')
    a.add_edge('A','B')
    a.add_edge('A','C')
    a.add_edge('A','D')
    a.add_edge('D','E')
    a.add_edge('E','B')
    a.add_edge('F','B')

    print(a)
