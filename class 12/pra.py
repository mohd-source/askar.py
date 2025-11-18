import re

text = "steam up a computer science portal for stream up"
match= re.search(r'computer', text)

print("Match text: ", match)
print("Matched string: ", match.group())
print("Start index: ", match.start())
print("End index: ", match.end())