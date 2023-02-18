# The following programme performs sorting on a given sequence by using the method of insertion sort.

a = input("Enter a sequence to be sorted: ").split(',')

def Insertion(a):
    Sorted = []
    for i in range(len(a)):
        Sorted.append(a[i])
        j = i
        while j > 0 and Sorted[j] < Sorted[j-1]:
            Sorted[j], Sorted[j-1] = Sorted[j-1], Sorted[j]
            j -= 1
    return Sorted


print(Insertion(a))

