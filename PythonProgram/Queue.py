# Queue implementation in Python using List (Data Structure)
class Queue :
    
    def __init__(self) :

        self.items = [] # Initialize empty queue
    
    def isEmpty(self) :

        return len(self.items) == 0 # True if queue is empty
    
    def enqueue(self, item) :

        self.items.append(item) # Add item at the rear
        print(f"Item '{item}' enqueued into queue.")

    def dequeue(self) :

        if self.isEmpty() :

            print("Queue is empty! Cannot dequeue.")
            return None
        
        return self.items.pop(0) # Remove from the front
    
    def peek(self) :

        if self.isEmpty() :

            print("Queue is empty! Nothing to peek.")
            return None
        
        return self.items[0] # Return front element without removing
    
    def display(self) :

        if self.isEmpty() :

            print("Queue is empty!")

        else :

            print("Current Queue (Front → Rear):", self.items)

# Main Program
queue = Queue()

while True :

    print("\n--- Queue Menu ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek (Front Element)")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1 :

        element = input("Enter element to enqueue: ")
        queue.enqueue(element)

    elif choice == 2 :

        removed = queue.dequeue()

        if removed is not None :

            print(f"Dequeued element: {removed}")

    elif choice == 3 :

        front = queue.peek()

        if front is not None :

            print(f"Front element: {front}")

    elif choice == 4 :

        queue.display()

    elif choice == 5 :

        print("Exiting program...")
        break

    else :

        print("Invalid choice! Please enter a number between 1-5.")