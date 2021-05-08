# O(w * nlog(n)) time | O(wn) soace where w is number of words
# and n is the length of the longest word
def groupAnagrams(words):
    # Write your code here.
    buckets = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord not in buckets:
            buckets[sortedWord] = [word]
        else:
            buckets[sortedWord].append(word)
    return list(buckets.values())
