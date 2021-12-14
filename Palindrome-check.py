def checkPalindrome(string_input):
    for i in range(0, len(string_input)//2):
        if string_input[0+i] != string_input[len(string_input)-1-i]:
            return False
    return True

user_var = input("Please enter a string to check:")
answer =  checkPalindrome(user_var)
if (answer):
    print("it is a palindrome string")
else:
    print("it is NOT a palindrome string")
