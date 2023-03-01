# The following program finds a peak value in a given sequence.
# Peak value here refers to a value that is greater than its adjascent neighbours.
def peakval(a):
    if a == []:
        return("Empty sequence.")
    
    peaks = a[0]
    if a[0] > a[1]:
        if a[0] > peaks:
            peaks = a[0]

    if a[-1] > a[-2]:
        if a[-1] > peaks:
            peaks = a[-1]

    for i in range(len(a)-1):
        if a[i] >= a[i+1] and a[i] >= a[i-1]:
            peaks = a[i]

    return (peaks)

# use a variable instead of list peaks
l1 = [5,10,20,15] # 20
l2 = [10,90,15,2,23,20,67] # 20 or 90
l3 = [10,20,30,40]
l4 = [12,12,12,12,12]
l5 = []

print(peakval(l1))
print(peakval(l2))
print(peakval(l3))
print(peakval(l4))
print(peakval(l5))
    