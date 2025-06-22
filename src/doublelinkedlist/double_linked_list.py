from .node import Node

''' Notes 
functions: add_head_Node, add_tail_Node, add_Node_at_position ,get_length, get_tail_Node, get_head_Node, 
get_Node_by_value, get_Node_at_position, remove_head, remove_tail, remove_Node_by_value, remove_Node_at_position, remove_Node_with_value
'''

class Double_Linked_List:
    #initialize
    def __init__(self, length = 0, head_Node = None, tail_Node = None):
        self.head_Node = head_Node
        self.tail_Node = tail_Node
        self.length = length

    # return the length of the doubly list
    def get_length(self):
        return self.length

    # adds to the doubly list a new head Node
    def add_head_Node(self, new_head_value):
        new_head =  Node(new_head_value)
        current_head = self.head_Node
        if self.head_Node == None:
            self.head_Node = new_head
            self.tail_Node = new_head
            
        else:
            current_head.set_prev_Node(new_head)
            new_head.set_next_Node(current_head)
            self.head_Node = new_head
        
        self.length += 1

    # adds to the doubly linked list a new tail Node
    def add_tail_Node(self, new_tail_value):
        new_tail = Node(new_tail_value)
        current_tail = self.tail_Node

        if current_tail == None:
            self.tail_Node = new_tail
            self.head_Node = new_tail


        else:
            current_tail.set_next_Node(new_tail)
            new_tail.set_prev_Node(current_tail)
            self.tail_Node = new_tail

        self.length += 1 

    # return's the head Node
    def get_head_Node(self):
        return self.head_Node
    
    # return's the tail Node
    def get_tail_Node(self):
        return self.tail_Node

    # adds node at a certain position
    def add_Node_at_position(self, new_node_value, position):
        count = 0
        current_node = self.head_Node
        new_node = Node(new_node_value)

        if position == 0:
            self.add_head_Node(new_node_value)

        elif position < 0:
            return "Error invalid postion"           
        
        elif position > self.length :
            self.add_tail_Node(new_node_value)
        
        else:
            while position != count:
                current_node = current_node.get_next_Node()
                count += 1
            prev_node = current_node.get_prev_Node()
            new_node.set_next_Node(current_node)
            new_node.set_prev_Node(prev_node)
            prev_node.set_next_Node(new_node)
            current_node.set_prev_Node(new_node)
            self.length += 1

        
    # return's the node at the desired position
    def get_Node_at_position(self, position):
        count = 0
        current_Node = self.head_Node
        if current_Node == None:
            return "The list is empty."
        
        elif position > self.length - 1 or position < 0:
            return f"Invalid position the length of the list is: {self.length}"
        
        while count != position and current_Node != None:
                current_Node = current_Node.get_next_Node()
                count += 1
            
        return current_Node
            
    # return's the node with the desired value     
    def get_Node_by_value(self, value):
        current_Node = self.head_Node
        if current_Node == None:
            print("The list is empty.")

        else:
            while current_Node != None:
                if current_Node.get_data() != value:
                    current_Node = current_Node.get_next_Node()
                    
                
                else:
                    return current_Node
                
                
        return "Value does not exist in list."

    # removes the head node in the doubly list
    def remove_head(self):
        if self.head_Node == None:
            return None
        current_Node = self.head_Node 
        self.head_Node =  current_Node.get_next_Node()
        current_Node.set_next_Node(None)
        if self.head_Node != None:
            self.head_Node.set_prev_Node(None)
        self.length -= 1
        return current_Node

    # removes the tail Node in the doubly list 
    def remove_tail(self):
        if self.tail_Node == None:
            return None
        
        elif self.tail_Node == self.head_Node:
            return self.remove_head()
        remove_tail_Node = self.tail_Node
        self.tail_Node = remove_tail_Node.get_prev_Node()
        remove_tail_Node.set_prev_Node(None)
        self.tail_Node.set_next_Node(None)
        self.length -= 1
        return remove_tail_Node
    
    # removes the node at the desired position
    def remove_Node_at_position(self, position):
        if position < 0 or position >= self.length:
            return "Invalid position"
        
        elif position == 0:
            return self.remove_head()
        
        elif position == self.length - 1:
            return self.remove_tail()

        current_node = self.head_Node
        count = 0
        while count != position:
            current_node = current_node.get_next_Node()
            count += 1
        prev_Node = current_node.get_prev_Node()
        next_Node = current_node.get_next_Node()
        next_Node.set_prev_Node(prev_Node)
        prev_Node.set_next_Node(next_Node)
        current_node.set_next_Node(None)
        current_node.set_prev_Node(None)
        self.length -= 1
        return current_node
    
    # removes the node with the desired value
    def remove_Node_with_value(self, value):
        current_node = self.head_Node

        if self.head_Node == None:
            return "List is empty."
        
        elif value == self.head_Node.get_data():
            return self.remove_head().get_data()

        elif value == self.tail_Node.get_data():
            return self.remove_tail().get_data()
        
        while current_node != None and current_node.get_data() != value:
            current_node = current_node.get_next_Node()
        
        if current_node == None:
            return "Value not in list."

        prev_Node = current_node.get_prev_Node()
        next_Node = current_node.get_next_Node()
        next_Node.set_prev_Node(prev_Node)
        prev_Node.set_next_Node(next_Node)
        current_node.set_next_Node(None)
        current_node.set_prev_Node(None)
        
        self.length -= 1
        return current_node.get_data()


 