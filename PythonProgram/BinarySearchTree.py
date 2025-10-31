# Define a Node class
class Node :

    def __init__(self, data) :

        self.data = data
        self.left = None
        self.right = None

# Binary Search Tree Class
class BinarySearchTree :

    def __init__(self) :

        self.root = None

    # Insert a node into the BST
    def insert(self, data) :

        if self.root is None : 

            self.root = Node(data)

        else :

            self._insert(self.root, data)

    def _insert(self, current, data) : 

        if data < current.data :

            if current.left is None :

                current.left = Node(data)

            else :

                self._insert(current.left, data)

        elif data > current.data :

            if current.right is None :

                current.right = Node(data)

            else :

                self._insert(current.right, data)

        else :

            print(f"Duplicate value {data} ignored")

    # Search for a value in BST
    def search(self, value) :

        return self._search(self.root, value)
    
    def _search(self, current, value) :

        if current is None :

            return False
        
        if value == current.data :

            return True
        
        elif value < current.data :

            return self._search(current.left, value)
        
        else :

            return self._search(current.right, value)
        
    # Inorder traversal for sorting
    def inorder(self) :

        print("Sorted elements (Inorder Traversal):")
        self._inorder(self.root)
        print()

    def _inorder(self, current) :

        if current :

            self._inorder(current.left)
            print(current.data, end=" ")
            self._inorder(current.right)

bst = BinarySearchTree()
# Insert elements
elements = [50, 30, 70, 20, 40, 60, 80]
for e in elements :

    bst.insert(e)
    
# Display sorted order
bst.inorder()

# Search for values
x = int(input("Enter value to search: "))

if bst.search(x) :

    print(f"{x} found in the tree.")

else :

    print(f"{x} not found in the tree.")