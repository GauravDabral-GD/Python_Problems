# The following program takes a sequence of numbers as well as a sum as the input and returns 
# a slice of the sequence such that the values of the slice is equal to the sum provided as input.
# And if no such sequence is present, it returns -1.


a = list(map(lambda x: int(x), input("Enter a sequence of integers: ").strip().split(' ')))
sum = int(input("Sum : "))


def subsum(a,sum):
    for i in range(len(a)):
        currSum = 0  
        for j in range(i,len(a)):
            currSum += a[j]
            if currSum == sum:
                return(a[i:j+1])
    return -1

print(subsum(a,sum))