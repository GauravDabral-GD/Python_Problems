# This program takes a number as an input and checks whether it is divisible by 7 or not.

a = input('Enter a number: ')

def DivisibleBy7(a):

    b = int(a)
    
    while b > 10:
        b  =  int(a[:len(a)-1]) - 2*(int(a[len(a)-1]))
        a = str(b)

    
    if b == 7 or b == 0:
        print(True)
    else:
        print(False)

DivisibleBy7(a)
