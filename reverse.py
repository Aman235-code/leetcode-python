def reverse(x):
    rev = 0
    num = x

    if num < 0:
        val = -(int(str(abs(num))[::-1]))
        if val <= -2**31 or val >= 2**31-1:
            print("0")
            return
        else:
            print(val)
    
    while(num > 0):
        rem = num % 10
        num = num // 10
        rev = rev * 10 + rem 

    if rev <= -2**31 or rev >= 2**31-1:
        print("0")
    else:
        print(rev)
    

reverse(-2147483648)