# Interroblank, 2020

def permuteCheck(str1, str2):
    colls = 0
    if(len(str1) == 0 and len(str2) == 0):
        return True
    if(len(str1) != len(str2)):
        return False
    permuteDict = {}
    for c in str1:
        permuteDict[c] = c
    for c in str2:
        if(c in permuteDict):
            colls += 1
    if (colls == len(str1)):
        return True
    return False # TODO: Consider case.
