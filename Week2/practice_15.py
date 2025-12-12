sentence = input("Enter a sentence: ")

words = sentence.split()
frequency = {}

for w in words:
    w = w.lower()
    if w in frequency:
        frequency[w] += 1
    else:
        frequency[w] = 1

print(frequency)
