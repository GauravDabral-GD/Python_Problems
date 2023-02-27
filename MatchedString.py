# The program checks for pairs of "( )" and retunrs true or false accordingly.

def matched(s):
    i,j = 0,0
    while i < len(s):
        if s[i] == '(':
            while j < len(s):
                if j>i:
                    if s[j] == ')':
                        j += 1
                        break
                    j += 1
                else:
                    j += 1
            else:
                return False
        i += 1
    else:
        return True

print(matched("a)*(?"))