# Reverse Words :- This program takes a list as an argument and returns the list in a reversed order.

a = 'My name is gaurav'

def revSentence(s):
    return ' '.join(reversed(s.split(' ')))



def revWords(a):
    j = len(a)
    b = ''
    for i in range(len(a)-1,-1, -1):
        if a[i] == ' ':
            b = b + a[i:j]
            j = i
        elif i == 0:
            b = b + ' ' + a[i:j]
            j = i

    return b

print(revWords(a))
print(revSentence(a))