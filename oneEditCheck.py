# Interroblank, 2020

def oneEditCheck(str1, str2):
    colls = 0
    collDict = {}
    for c in str1:
        collDict[c] = c
    for c in str2:
        if (c in collDict):
            colls += 1
    if (colls == len(str1)):
        return True
    if (colls == len(str1) + 1 or colls == len(str1) - 1):
        return True
    return False # TODO: Doesn't work for empty 'str1' input.
