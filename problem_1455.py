def isPrefixOfWord(sentence, searchWord):
    words = sentence.split()
    for index, word in enumerate(words):
        if word.startswith(searchWord):
            return index+1
    return -1


print(isPrefixOfWord("i love eating burger", "burg"))
