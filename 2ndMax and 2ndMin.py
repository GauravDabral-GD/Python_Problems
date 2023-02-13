# This program takes a list as an input and returns the second maximum and second minimum value from the string.


l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [4,34,5,6,7,6,33,23,56,65]

def maxmin(a):

    a.remove(max(a))
    a.remove(min(a))
    print("2nd Max:", max(a))
    print("2nd Min:", min(a))

maxmin(l2)

