def generateDocument(characters, document):
    # Write your code here.
    a_list = list(characters)
    for c in document:
        if c not in a_list:
            return False
        else:
            a_list.remove(c)

    return True
