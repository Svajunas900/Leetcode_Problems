def isPrefixOfWord(sentence, searchWord):
        words = sentence.split()
        searchLength = len(searchWord)
        for index, word in enumerate(words):
            lengthWord = len(word)
            if searchLength > lengthWord:
                continue
            if word[:searchLength] == searchWord:
                return index+1
        return -1 

print(isPrefixOfWord("i love eating burger", "burg"))