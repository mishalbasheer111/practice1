word = "Programming"

print(word[::-1])
print(word[:3], word[-3:])
print(word.count("m"))

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("level"), is_palindrome("python"))
