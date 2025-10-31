def list_operations() :

    numbers = [10, 20, 30]
    print("Original list:", numbers)

    numbers.append(40)
    print("After append:", numbers)

    numbers.insert(1, 15)
    print("After insert:", numbers)

    numbers.remove(20)
    print("After remove:", numbers)

    numbers.pop()
    print("After pop:", numbers)

    numbers.sort()
    print("After sort:", numbers)

    numbers.reverse()
    print("After reverse:", numbers)
    
list_operations()