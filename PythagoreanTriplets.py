# The following program takes an integer as an input and prints all 
# the possible pythgorean triplets of positive integers till that number.
def isTriplet(t):
        sorted(t)
        return t[0]**2 + t[1]**2 == t[2]**2

def pyTriplets(n):
    return tuple(filter(isTriplet, ((i,j,k) for i in range(1, n+1) for j in range(1, n+1) for k in range(1, n+1))))

a = int(input("Enter an Integer: "))
print(pyTriplets(a))