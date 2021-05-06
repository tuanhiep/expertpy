# Solution 1

def powerset(array, idx=None):
    # Write your code here.
    if idx is None:
        idx = len(array) - 1
    if idx < 0:
        return [[]]
    ele = array[idx]
    subsets = powerset(array, idx - 1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [ele])
    return subsets


# Solution 2

def powerset(array):
    # Write your code here.
    subsets = [[]]
    for ele in array:
        for idx in range(len(subsets)):
            newElement = subsets[idx] + [ele]
            subsets.append(newElement)
    return subsets
