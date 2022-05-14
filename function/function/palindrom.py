def isPalindrome(s):
    return s == s[::-1]
    
s = "mom"
ans = isPalindrome(s)
 
if ans:
    print("Palindrome")
else:
    print("Not a palindrome")