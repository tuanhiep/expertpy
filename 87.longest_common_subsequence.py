# Solution 1
def longestCommonSubsequence(str1, str2):
    # O(nm*min(n,m)) time | O(nm*min(n,m)) space
    lcs = [[[] for ex in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for r in range(1, len(str2) + 1):
        for c in range(1, len(str1) + 1):
            if str2[r - 1] == str1[c - 1]:
                lcs[r][c] = lcs[r - 1][c - 1] + [str2[r - 1]]
            else:
                lcs[r][c] = max(lcs[r - 1][c], lcs[r][c - 1], key=len)
    return lcs[-1][-1]


# Solution 2

def longestCommonSubsequence(str1, str2):
    # O(nm) time | O(nm) space
    lengths = [[0 for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for r in range(1, len(str2) + 1):
        for c in range(1, len(str1) + 1):
            if str2[r - 1] == str1[c - 1]:
                lengths[r][c] = lengths[r - 1][c - 1] + 1
            else:
                lengths[r][c] = max(lengths[r - 1][c], lengths[r][c - 1])
    return buildSequence(lengths, str1)


def buildSequence(lengths, str1):
    sequence = []
    r = len(lengths) - 1
    c = len(lengths[0]) - 1
    while r != 0 and c != 0:
        if lengths[r][c] == lengths[r - 1][c]:
            r -= 1
        elif lengths[r][c] == lengths[r][c - 1]:
            c -= 1
        else:
            sequence.append(str1[c - 1])
            r -= 1
            c -= 1
    return list(reversed(sequence))


# Solution 3

def longestCommonSubsequence(str1, str2):
    # O(nm) time | O(nm) space
    lcs = [[[None, 0, None, None] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for r in range(1, len(str2) + 1):
        for c in range(1, len(str1) + 1):
            if str2[r - 1] == str1[c - 1]:
                lcs[r][c] = [str2[r - 1], lcs[r - 1][c - 1][1] + 1, r - 1, c - 1]
            else:
                if lcs[r - 1][c][1] > lcs[r][c - 1][1]:
                    lcs[r][c] = [None, lcs[r - 1][c][1], r - 1, c]
                else:
                    lcs[r][c] = [None, lcs[r][c - 1][1], r, c - 1]
    return buildSequence(lcs)


def buildSequence(lcs):
    sequence = []
    r = len(lcs) - 1
    c = len(lcs[0]) - 1
    while r != 0 and c != 0:
        currentEntry = lcs[r][c]
        if currentEntry[0] is not None:
            sequence.append(currentEntry[0])
        r = currentEntry[2]
        c = currentEntry[3]
    return list(reversed(sequence))
