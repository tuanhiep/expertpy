def isValidSubsequence(array, sequence):
    # Write your code here.
    a_index = 0
    s_index = 0

    while a_index < len(array) and s_index < len(sequence):
        if array[a_index] == sequence[s_index]:
            s_index += 1
        a_index += 1
    return s_index == len(sequence)


def isValidSubsequence2(array, sequence):
    # Write your code here.
    index = 0
    found = False

    for num in sequence:
        found = False
        while index < len(array) and found == False:
            if num == array[index]:
                found = True
            index += 1

    return found


def isValidSubsequence3(array, sequence):
    # Write your code here.
    index = 0
    for num in array:
        if num == sequence[index]:
            index += 1
            if index == len(sequence):
                return True
    return False
