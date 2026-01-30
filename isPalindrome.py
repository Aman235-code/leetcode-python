def isPalindrome(x):
    rev = 0
    rem = 0 
    temp = x

    if temp < 0:
        return False
    
    while temp > 0:
        rem = temp % 10
        temp = temp // 10
        rev = rev * 10 + rem 

    if x == rev:
        return True
    return False
    
       
print(isPalindrome(10))
