def firstNonRepeatingCharacter(string):
    # Write your code here.
    for i in range(len(string)):
        if string[i] != '~' and string[i] not in string[i + 1:]:
            return i
        elif string[i] != '~' and string[i] in string[i + 1:]:
            string = string.replace(string[i], '~')
    return -1


def firstNonRepeatingCharacterOptimal(string):
    # Write your code here.
    map = {}
    for c in string:
        if c not in map:
            map[c] = 1
        else:
            map[c] = map[c] + 1
    for i in range(len(string)):
        if map[string[i]] == 1:
            return i
    return -1
