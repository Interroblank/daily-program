import random as rand

# Interroblank, 2020

class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

def makeTestList(length):
    if (length == 0):
        return None
    tempNode = Node(rand.randint(0, 100))
    tempNode.next = makeTestList(length - 1)
    return tempNode

def getListLength(node):
    if (node == None):
        return 0
    return 1 + getListLength(node.next)

def toLastElement(node, k): # CCI - 2.2
    it1 = node
    it2 = node
    for i in range(k):
        it2 = it2.next
    while (it2.next != None):
        it1 = it1.next
        it2 = it2.next
    return it1.data

def isPalindrome(node): # CCI - 2.6
    # Reverses the given list and compares.
    revList = None
    isPalin = True
    nodeCurr = node
    while (nodeCurr != None):
        tempNode = Node(nodeCurr.data)
        tempNode.next = revList
        revList = tempNode
        nodeCurr = nodeCurr.next
    while (revList != None):
        if (revList.data != node.data):
            isPalin = False
        revList = revList.next
        node = node.next
    return isPalin
