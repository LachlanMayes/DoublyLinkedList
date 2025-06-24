import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from doublelinkedlist import Node, Double_Linked_List

def print_list_forward(dll):
    """Helper function to print list from head to tail"""
    current = dll.get_head_Node()
    values = []
    while current:
        values.append(current.get_data())
        current = current.get_next_Node()
    print(f"Forward: {values}")

def print_list_backward(dll):
    """Helper function to print list from tail to head"""
    current = dll.get_tail_Node()
    values = []
    while current:
        values.append(current.get_data())
        current = current.get_prev_Node()
    print(f"Backward: {values[::-1]}")

def test_empty_list():
    print("=== Testing Empty List ===")
    dll = Double_Linked_List()
    print(f"Length: {dll.get_length()}")
    print(f"Head: {dll.get_head_Node()}")
    print(f"Tail: {dll.get_tail_Node()}")
    print(f"Remove head: {dll.remove_head()}")
    print(f"Remove tail: {dll.remove_tail()}")
    print(f"Get node at position 0: {dll.get_Node_at_position(0)}")
    print(f"Get node by value 5: {dll.get_Node_by_value(5)}")
    print()

def test_adding_nodes():
    print("=== Testing Adding Nodes ===")
    dll = Double_Linked_List()
    
    # Add to head
    print("Adding 10 to head")
    dll.add_head_Node(10)
    print(f"Length: {dll.get_length()}")
    print_list_forward(dll)
    
    # Add to tail
    print("Adding 20 to tail")
    dll.add_tail_Node(20)
    print(f"Length: {dll.get_length()}")
    print_list_forward(dll)
    
    # Add more nodes
    dll.add_head_Node(5)
    dll.add_tail_Node(25)
    dll.add_head_Node(1)
    print("After adding 5 to head, 25 to tail, 1 to head:")
    print(f"Length: {dll.get_length()}")
    print_list_forward(dll)
    print_list_backward(dll)
    print()
    
    return dll

def test_position_operations(dll):
    print("=== Testing Position Operations ===")
    print("Current list:")
    print_list_forward(dll)
    
    # Add at various positions
    print("Adding 15 at position 3")
    dll.add_Node_at_position(15, 3)
    print_list_forward(dll)
    
    print("Adding 0 at position 0 (should add to head)")
    dll.add_Node_at_position(0, 0)
    print_list_forward(dll)
    
    print("Adding 30 at position 100 (should add to tail)")
    dll.add_Node_at_position(30, 100)
    print_list_forward(dll)
    
    print("Trying to add at position -1 (should give error)")
    result = dll.add_Node_at_position(99, -1)
    print(f"Result: {result}")
    
    # Get nodes at positions
    print(f"\nNode at position 0: {dll.get_Node_at_position(0).get_data()}")
    print(f"Node at position 3: {dll.get_Node_at_position(3).get_data()}")
    print(f"Node at position {dll.get_length()-1}: {dll.get_Node_at_position(dll.get_length()-1).get_data()}")
    print(f"Node at invalid position 100: {dll.get_Node_at_position(100)}")
    print()

def test_search_operations(dll):
    print("=== Testing Search Operations ===")
    print("Current list:")
    print_list_forward(dll)
    
    # Search by value
    values_to_search = [0, 15, 30, 99]
    for value in values_to_search:
        result = dll.get_Node_by_value(value)
        if isinstance(result, Node):
            print(f"Found node with value {value}: {result.get_data()}")
        else:
            print(f"Search for {value}: {result}")
    print()

def test_removal_operations():
    print("=== Testing Removal Operations ===")
    # Create a fresh list for removal tests
    dll = Double_Linked_List()
    values = [10, 20, 30, 40, 50]
    for val in values:
        dll.add_tail_Node(val)
    
    print("Starting list:")
    print_list_forward(dll)
    print(f"Length: {dll.get_length()}")
    
    # Remove head
    print("\nRemoving head:")
    removed = dll.remove_head()
    print(f"Removed: {removed.get_data()}")
    print_list_forward(dll)
    print(f"Length: {dll.get_length()}")
    
    # Remove tail
    print("\nRemoving tail:")
    removed = dll.remove_tail()
    print(f"Removed: {removed.get_data()}")
    print_list_forward(dll)
    print(f"Length: {dll.get_length()}")
    
    # Remove at position
    print("\nRemoving at position 1:")
    removed = dll.remove_Node_at_position(1)
    print(f"Removed: {removed.get_data()}")
    print_list_forward(dll)
    print(f"Length: {dll.get_length()}")
    
    # Remove by value
    print("\nRemoving node with value 20:")
    removed = dll.remove_Node_with_value(20)
    print(f"Removed: {removed}")
    print_list_forward(dll)
    print(f"Length: {dll.get_length()}")
    
    # Try to remove non-existent value
    print("\nTrying to remove non-existent value 99:")
    result = dll.remove_Node_with_value(99)
    print(f"Result: {result}")
    print()

def test_edge_cases():
    print("=== Testing Edge Cases ===")
    
    # Single node operations
    print("Single node tests:")
    dll = Double_Linked_List()
    dll.add_head_Node(42)
    print(f"Added single node: {dll.get_head_Node().get_data()}")
    print(f"Head == Tail: {dll.get_head_Node() == dll.get_tail_Node()}")
    
    removed = dll.remove_tail()
    print(f"Removed tail from single node list: {removed.get_data()}")
    print(f"List is now empty: {dll.get_head_Node() is None}")
    print(f"Length: {dll.get_length()}")
    
    # Two node operations
    print("\nTwo node tests:")
    dll.add_head_Node(100)
    dll.add_tail_Node(200)
    print_list_forward(dll)
    
    removed = dll.remove_head()
    print(f"Removed head: {removed.get_data()}")
    print(f"Remaining node: {dll.get_head_Node().get_data()}")
    print(f"Head == Tail: {dll.get_head_Node() == dll.get_tail_Node()}")
    print()

def test_data_integrity():
    print("=== Testing Data Integrity ===")
    dll = Double_Linked_List()
    
    # Build a list
    for i in range(1, 6):
        dll.add_tail_Node(i * 10)
    
    print("Original list:")
    print_list_forward(dll)
    
    # Check forward/backward consistency
    print("Checking forward/backward traversal consistency:")
    
    # Forward traversal
    forward_values = []
    current = dll.get_head_Node()
    while current:
        forward_values.append(current.get_data())
        current = current.get_next_Node()
    
    # Backward traversal
    backward_values = []
    current = dll.get_tail_Node()
    while current:
        backward_values.append(current.get_data())
        current = current.get_prev_Node()
    
    backward_values.reverse()
    
    print(f"Forward: {forward_values}")
    print(f"Backward: {backward_values}")
    print(f"Lists match: {forward_values == backward_values}")
    
    # Check head's previous and tail's next
    print(f"Head's previous is None: {dll.get_head_Node().get_prev_Node() is None}")
    print(f"Tail's next is None: {dll.get_tail_Node().get_next_Node() is None}")
    print()

def run_all_tests():
    print("🧪 DOUBLY LINKED LIST TEST SUITE 🧪\n")
    
    test_empty_list()
    dll = test_adding_nodes()
    test_position_operations(dll)
    test_search_operations(dll)
    test_removal_operations()
    test_edge_cases()
    test_data_integrity()
    
    print("✅ All tests completed!")

if __name__ == "__main__":
    run_all_tests()