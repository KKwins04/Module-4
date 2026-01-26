#Function to check whether first and last characters of a word match
def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("List of words with same first and last character")
    return ctr

count = match_words(['a1c', 'c3c', 'america', 'aa', '6246'])
print("Number of words with same starting and ending letter: ", count)