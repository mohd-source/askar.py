import re

string = "the quick brown fox jumps over the lazy dog"
pattren = "[a-n]"
result = re.findall(pattren, string)
print(result)




import re

regex = r"The"
string = "the quick brown fox " , "the lass"

