sentence = "the cat and the hat and the bat"
counts = {}

for word in sentence.split():
    counts[word] = counts.get(word, 0) + 1

print(counts)
common_word = max(counts, key=counts.get)
print(common_word, counts[common_word])
