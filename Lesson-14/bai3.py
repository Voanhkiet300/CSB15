
s = input("Enter a string: ")

def is_palindrome(s):
    if s == s[::-1]:
        print("This is a palindrome.")
    else:
        print("This is not a palindrome.")


is_palindrome(s)