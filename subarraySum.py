# This program takes a sequence of numbers as input as well as an integer 'sum' and returns the 
# subsequence if the their sum is equal to the given 'sum'.


a = input('List : ').split(' ')

for i in range(len(a)):
    a[i] = int(a[i])

sum = int(input("sum : "))


def subsum(a,sum):
    for i in range(len(a)):
        currSum = 0  
        for j in range(i,len(a)):
            currSum += a[j]
            if currSum == sum:
                return(a[i:j+1])
    return -1

print(subsum(a,sum))