def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


print(is_palindrome("Lagerregal"))  # should return True
print(is_palindrome("Palindrom"))  # should return False
