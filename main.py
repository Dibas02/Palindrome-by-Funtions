def palin(num):
    t = num
    sum=0
    while t>0:
        digit = t%10
        sum = sum*10+digit
        t = t//10
    if sum == num:
        return "The number is palindrome"
    
    else:
        return "The number is not palindrome"
    




num = int(input("Enter a number: "))

print(palin(num))

#st