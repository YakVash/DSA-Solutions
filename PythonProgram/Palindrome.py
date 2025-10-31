def is_palindrome(s) :
    
    if s == s[::-1] :

        return True
    
    else :

        return False
    
string = input("Enter a string: ")

if is_palindrome(string) :

    print("Palindrome")

else :

    print("Not a palindrome")
