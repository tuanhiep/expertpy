def minimumCharactersForWords(words):
    # O(n * l) time | O(c) space
    maximumCharacterFrequencies = {}

    for word in words:
        characterFrequencies = countCharacterFrequencies(word)
        updateMaximumFrequencies(characterFrequencies, maximumCharacterFrequencies)

    return makeArrayFromCharacterFrequencies(maximumCharacterFrequencies)


def countCharacterFrequencies(word):
    characterFrequencies = {}

    for character in word:
        if character not in characterFrequencies:
            characterFrequencies[character] = 1
        else:
            characterFrequencies[character] += 1

    return characterFrequencies


def updateMaximumFrequencies(characterFrequencies, maximumCharacterFrequencies):
    for character in characterFrequencies:
        frequency = characterFrequencies[character]
        if character not in maximumCharacterFrequencies:
            maximumCharacterFrequencies[character] = frequency
        else:
            maximumCharacterFrequencies[character] = max(frequency, maximumCharacterFrequencies[character])


def makeArrayFromCharacterFrequencies(maximumCharacterFrequencies):
    characters = []

    for character in maximumCharacterFrequencies:
        for i in range(maximumCharacterFrequencies[character]):
            characters.append(character)

    return characters
