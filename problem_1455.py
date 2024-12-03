# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

# Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is a prefix of any word in sentence.
# Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. 
# If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.
# A prefix of a string s is any leading contiguous substring of s.


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
