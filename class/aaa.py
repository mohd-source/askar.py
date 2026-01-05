import random 

list = ["Py", "tho", "nPro", "gram", "ming"]
word = "".join(list)
l = list(word)
print(l)
print(random.shuffle())
print(word[:6], word[6:])
print(word)
print(word[::-1])
print(" Length of list's word is:",len(word))
