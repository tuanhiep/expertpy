# Solution 1

def multiStringSearch(bigString, smallStrings):
    # O(bns) time | O(n) space - where n is the number of small strings
    # b is the length of big string and s is the longest length of small string
    return [isIbBigString(bigString, smallString) for smallString in smallStrings]


def isIbBigString(bigString, smallString):
    for i in range(len(bigString)):
        if i + len(smallString) > len(bigString):
            break
        if isInBigStringHelper(bigString, smallString, i):
            return True
    return False


def isInBigStringHelper(bigString, smallString, startIdx):
    leftBigIdx = startIdx
    rightBigIdx = startIdx + len(smallString) - 1
    leftSmallIdx = 0
    rightSmallIdx = len(smallString) - 1
    while leftBigIdx <= rightBigIdx:

        if bigString[leftBigIdx] != smallString[leftSmallIdx] or bigString[rightBigIdx] != smallString[rightSmallIdx]:
            return False
        leftBigIdx += 1
        rightBigIdx -= 1
        leftSmallIdx += 1
        rightSmallIdx -= 1
    return True


# Solution 2

def multiStringSearch(bigString, smallStrings):
    # O(b^2 + ns)  time | O(b^2 + n) space
    modifiedSuffixTrie = ModifiedSuffixTrie(bigString)
    return [modifiedSuffixTrie.contains(string) for string in smallStrings]


class ModifiedSuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.populateModifiedSuffixTrieFrom(string)

    def populateModifiedSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    def insertSubstringStartingAt(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]

        return True


# Solution 3

def multiStringSearch(bigString, smallStrings):
    # O(ns + bs) time | O(ns) space
    trie = Trie()
    for string in smallStrings:
        trie.insert(string)
    containedStrings = {}
    for i in range(len(bigString)):
        findSmallStringsIn(bigString, i, trie, containedStrings)

    return [string in containedStrings for string in smallStrings]


def findSmallStringsIn(bigString, startIdx, trie, containedStrings):
    currentNode = trie.root
    for i in range(startIdx, len(bigString)):
        letter = bigString[i]
        if letter not in currentNode:
            break
        currentNode = currentNode[letter]
        if trie.endSymbol in currentNode:
            containedStrings[currentNode[trie.endSymbol]] = True


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def insert(self, string):
        node = self.root
        for i in range(len(string)):
            letter = string[i]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = string
