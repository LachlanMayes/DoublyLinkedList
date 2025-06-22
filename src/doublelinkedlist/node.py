class Node:
    # initialize
    def  __init__(self, data, next_Node = None, prev_Node = None):
        self.data = data
        self.next_Node = next_Node
        self.prev_Node = prev_Node

    # receive data e.g 1, t, the
    def get_data(self):
        return self.data
    
    # assign the data 
    def set_data(self, data):
        self.data = data

    #  sets the pointer of next_node of the current node
    def set_next_Node(self, next_node):
        self.next_Node = next_node

    # sets the pointer of prev_node of the current node
    def set_prev_Node(self, prev_node):
        self.prev_Node = prev_node
        
    # return the pointer to the next_node of current node 
    def get_next_Node(self):
        return self.next_Node
    
    # return the pointer to the prev_node of current node 
    def get_prev_Node(self):
        return self.prev_Node
    