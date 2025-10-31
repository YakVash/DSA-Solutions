# Stack implementation in Python using List (Data Structure)
class Stack :

    def __init__(self) :

        self.items = [] # Initialize empty stack

    def isEmpty(self) :

        return len(self.items) == 0 # True if stack is empty
    
    def push(self, item) :

        self.items.append(item) # Add item to top of stack
        print(f"Item '{item}' pushed onto stack.")
    
    def pop(self) :

        if self.isEmpty() :

            print("Stack is empty! Cannot pop.")
            return None
        
        return self.items.pop() # Remove and return top element
    
    def peek(self) :

        if self.isEmpty() :

            print("Stack is empty! Nothing to peek.")
            return None
        
        return self.items[-1] # Return top element without removing
    
    def display(self) :

        if self.isEmpty() :

            print("Stack is empty!")

        else :

            print("Current Stack (Top → Bottom):", self.items[::-1])

# Main Program
stack = Stack()

while True :

    print("\n--- Stack Menu ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1 :

        element = input("Enter element to push: ")
        stack.push(element)

    elif choice == 2 :

        popped = stack.pop()

        if popped is not None :

            print(f"Popped element: {popped}")

    elif choice == 3 :

        top = stack.peek()

        if top is not None :

            print(f"Top element: {top}")

    elif choice == 4 :

        stack.display()

    elif choice == 5 :

        print("Exiting program...")
        break

    else :

        print("Invalid choice! Please enter a number between 1-5.")