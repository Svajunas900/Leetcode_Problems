def isPrefixOfWord(sentence, searchWord):
    words = sentence.split()
    result = [
        index + 1 for index,
        word in enumerate(words) if word.startswith(searchWord)]
    if result:
        return result[0]
    else:
        return -1


print(isPrefixOfWord("i love eating burger", "burg"))
