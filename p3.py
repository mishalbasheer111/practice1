words = ["ai", "python", "data"]

squares = [n * n for n in range(1, 11) if n % 2 == 0]
lengths = {word: len(word) for word in words}
letters = sorted(set("banana"))

print(squares)
print(lengths)
print(letters)
