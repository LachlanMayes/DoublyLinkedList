# Doubly Linked List


A comprehensive doubly linked list implementation in Python with full bidirectional traversal capabilities and extensive operations for data manipulation.

## Features

- **Bidirectional Navigation** - Traverse forward and backward through the list
- **Flexible Insertion** - Add nodes at head, tail, or any specific position
- **Multiple Search Methods** - Find nodes by value or position
- **Comprehensive Removal** - Remove nodes from any position or by value
- **Memory Efficient** - Dynamic size with proper node linking
- **Type Safe** - Clean Python implementation with proper error handling

## Installation

### Prerequisites

- Python 3.12 or higher

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/LachlanMayes/DoublyLinkedList.git
   cd doublelinkedlist
   ```

2. **Install the package**
   ```bash
   pip install -e .
   ```

3. **Verify installation**
   ```bash
   in the terminal cd to where you stored the DoublyLinkedList folder

   once in the folder:

   cd test

   then:

   python3 test_double_linked_list.py
   

## Quick Start

```python
from doublelinkedlist import Double_Linked_List

# Create a new doubly linked list
dll = Double_Linked_List()

# Add some data
dll.add_head_Node(10)      # Add to beginning
dll.add_tail_Node(20)      # Add to end
dll.add_tail_Node(30)

# Insert at specific position
dll.add_Node_at_position(15, 2)  # Insert 15 at position 2

# Access nodes
head = dll.get_head_Node()
tail = dll.get_tail_Node()
node_at_pos = dll.get_Node_at_position(1)

# Search for values
found_node = dll.get_Node_by_value(20)

# Remove nodes
dll.remove_head()                    # Remove first node
dll.remove_tail()                    # Remove last node
dll.remove_Node_at_position(1)       # Remove node at position 1
dll.remove_Node_with_value(15)       # Remove node with value 15

# Get list length
length = dll.get_length()
```

## API Reference

### Double_Linked_List Class

#### Constructor
```python
Double_Linked_List(length=0, head_Node=None, tail_Node=None)
```

#### Adding Nodes

| Method | Description | Parameters | Returns |
|--------|-------------|------------|---------|
| `add_head_Node(value)` | Add node at the beginning | `value`: Data for new node | None |
| `add_tail_Node(value)` | Add node at the end | `value`: Data for new node | None |
| `add_Node_at_position(value, position)` | Add node at specific position | `value`: Data, `position`: Index | None or error message |

#### Accessing Nodes

| Method | Description | Parameters | Returns |
|--------|-------------|------------|---------|
| `get_head_Node()` | Get first node | None | Node object or None |
| `get_tail_Node()` | Get last node | None | Node object or None |
| `get_Node_at_position(position)` | Get node at index | `position`: Index | Node object or error message |
| `get_Node_by_value(value)` | Find node with specific value | `value`: Value to search | Node object or error message |
| `get_length()` | Get number of nodes | None | Integer |

#### Removing Nodes

| Method | Description | Parameters | Returns |
|--------|-------------|------------|---------|
| `remove_head()` | Remove first node | None | Removed Node or None |
| `remove_tail()` | Remove last node | None | Removed Node or None |
| `remove_Node_at_position(position)` | Remove node at index | `position`: Index | Removed Node or error message |
| `remove_Node_with_value(value)` | Remove node with specific value | `value`: Value to remove | Value or error message |

### Node Class

#### Constructor
```python
Node(data, next_Node=None, prev_Node=None)
```

#### Node Methods

| Method | Description | Parameters | Returns |
|--------|-------------|------------|---------|
| `get_data()` | Get node's data | None | Any type |
| `set_data(data)` | Set node's data | `data`: New data value | None |
| `get_next_Node()` | Get next node | None | Node object or None |
| `set_next_Node(node)` | Set next node | `node`: Node object | None |
| `get_prev_Node()` | Get previous node | None | Node object or None |
| `set_prev_Node(node)` | Set previous node | `node`: Node object | None |

## Usage Examples

### Basic Operations

```python
from doublelinkedlist import Double_Linked_List

# Create and populate list
dll = Double_Linked_List()
for i in [1, 2, 3, 4, 5]:
    dll.add_tail_Node(i)

# Traverse forward
current = dll.get_head_Node()
while current:
    print(current.get_data(), end=" -> ")
    current = current.get_next_Node()
print("None")

# Traverse backward
current = dll.get_tail_Node()
while current:
    print(current.get_data(), end=" <- ")
    current = current.get_prev_Node()
print("None")
```

### Advanced Usage

```python
# Create a list of strings
dll = Double_Linked_List()
words = ["hello", "world", "python", "doubly", "linked"]

for word in words:
    dll.add_tail_Node(word)

# Insert at specific position
dll.add_Node_at_position("awesome", 2)

# Search and modify
node = dll.get_Node_by_value("python")
if isinstance(node, Node):
    node.set_data("PYTHON")

# Remove nodes with error handling
position_to_remove = 3
result = dll.remove_Node_at_position(position_to_remove)
if isinstance(result, str):
    print(f"Error: {result}")
else:
    print(f"Removed: {result.get_data()}")
```

## Testing

Run the comprehensive test suite to verify functionality:

```bash
python test/test_double_linked_list.py
```

The test suite includes:
- Empty list operations
- Node addition and removal
- Position-based operations
- Search functionality
- Edge cases (single node, two nodes)
- Data integrity verification
- Bidirectional traversal validation

### Test Output Example

```
🧪 DOUBLY LINKED LIST TEST SUITE 🧪

=== Testing Empty List ===
Length: 0
Head: None
Tail: None

=== Testing Adding Nodes ===
Adding 10 to head
Length: 1
Forward: [10]

✅ All tests completed!
```

## Error Handling

The implementation includes comprehensive error handling:

- **Invalid positions**: Returns descriptive error messages
- **Empty list operations**: Gracefully handles operations on empty lists
- **Value not found**: Returns informative messages when values don't exist
- **Boundary checks**: Validates positions against list length

## Performance Characteristics

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Add to head/tail | O(1) | O(1) |
| Add at position | O(n) | O(1) |
| Remove head/tail | O(1) | O(1) |
| Remove at position | O(n) | O(1) |
| Search by value | O(n) | O(1) |
| Get length | O(1) | O(1) |

## Project Structure

```
doublelinkedlist/
├── src/
│   └── doublelinkedlist/
│       ├── __init__.py
│       ├── double_linked_list.py
│       └── node.py
├── test/
│   └── test_double_linked_list.py
├── pyproject.toml
├── .python-version
└── README.md
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Write tests for new functionality**
4. **Ensure all tests pass**
   ```bash
   python test/test_double_linked_list.py
   ```
5. **Follow PEP 8 style guidelines**
6. **Submit a pull request**

## Roadmap

- [ ] Add iterator support (`__iter__`, `__next__`)
- [ ] Implement `__str__` and `__repr__` methods
- [ ] Add support for slicing operations
- [ ] Performance optimizations for large lists
- [ ] Add type hints throughout the codebase
- [ ] Create benchmarking suite

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by classic data structure implementations
- Built with Python 3.12 modern practices
- Comprehensive testing approach for reliability

---

⭐ **If you found this implementation helpful, please give it a star!** ⭐
