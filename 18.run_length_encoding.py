def runLengthEncoding(string):
    # Write your code here.
    result = ''
    count = 0
    current = string[0]
    for i in range(len(string)):
        c = string[i]
        if c == current:
            count += 1
        else:
            result += split_9(count, current)
            count = 1
            current = c

    result += split_9(count, current)
    return result


def split_9(count, current):
    if count <= 9:
        return str(count) + current
    else:
        tmp = ''
        times = count // 9
        rest = count % 9
        for i in range(times):
            tmp += str(9) + current
        if rest > 0:
            tmp += str(rest) + current
        return tmp


def optimal_runLengthEncoding(string):
    # Write your code here.
    count = 0
    current = string[0]
    result = ''
    for i in range(len(string)):
        if string[i] == current:
            count += 1
        if count == 9:
            result += str(9) + current
            count = 0
        if string[i] != current:
            if count != 0:
                result += str(count) + current
            count = 1
            current = string[i]

    result += str(count) + current
    return result
