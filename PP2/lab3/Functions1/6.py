def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

x = "s a d a s d"
print(reverse_words(x))