a = (input("Enter a sequence of numbers: ")).split(' ')

d = {}

def maxfreq(a):
    '''This function checks for the number in a sequence occuring with maximum frequency. '''

    for item in a:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1
        
    maxVal = max(d.values())
    maxKey = 0
    for key in d.keys():
        if d[key] == maxVal:
            maxKey = key
    
    return (f'{maxKey} has the maximum frequency, it appears {maxVal} times in the sequence.')

print(maxfreq(a))

            
