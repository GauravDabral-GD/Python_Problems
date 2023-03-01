# Given program takes a sequence of numbers as an input and returns
# the sum of square of all the numbers in the sequence.

a = list(map(lambda x: int(x), input("Enter a sequence: ").strip().split(' ')))

sqSum = sum([i**2 for i in a if i%2 == 0])
print(a)
print("Sum:", sqSum)
