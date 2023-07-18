# The following program takes a string as an input and returns the minimun number of deletions required in that string to make it a palindrome. 
# The program will return 0 if the string is already a palindrome as number of deletion required will be 0.

a = input("Enter a string: ")

def isPalindrome(a):
    
    if a[::-1] == a[::]:
        return True
    else:
        return False
   
def minDel(a,l,r):

    if isPalindrome(a):
        return 0

    if r-l <= 1:
        return 1
    
    else:
        if a[l] == a[r]:
            return minDel(a,l+1,r-1)
        
        elif a[l] != a[r]:
            return 1 + min(minDel(a,l+1,r), minDel(a,l,r-1))


print(minDel(a,0,len(a)-1))






