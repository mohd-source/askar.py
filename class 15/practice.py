# import re
# text = "Steam Up: A computer science portal for steam up"
# match = re.search(r'portal', text)
# print(match)
# print("matched text: ", match.group())
# print("start index: ", match.start())
# print("end index: ", match.end())




# import re
# pattern = r'portal' #raw string (s'.....')is best practice for regex patterns
# match = re.search(pattern, "Steam Up: A computer science \\ portal for steam up")
# print(match)
# if match:
#     print("Matched text:", match.group())




# #for using metacharacters in regex patterns
# import re
# s='Iqra.University'
# #without using \
# match = re.search(r'.', s) 
# print(match)
# #using \
# match = re.search(r'\.', s)
# print(match)




# import re
# string = "the quick brown fox jumps over the lazy dog"
# pattern = "[a-m]"
# result = re.findall(pattern, string)
# print(result)




# import re
# regex=r'^the'
# strings= ['the quick brown box', 'the lazy dog', 'a quick brown box']
# for string in strings:
#     if re.match (regex, string):
#         print(f"matched: {string}")
#     else:
#         print(f"not matched: {string}")




# import re
# string="Hello World!"
# pattern = r"World!$"
# match=re.search(pattern, string)
# if match:
#     print("match found!")
# else:
#     print('match not found.')




# import re

# string = "the quik brown fox jumps over the lazy dog"
# pattern = r"brown.fox.jumps"

# match = re.search(pattern, string)

# if match:
#     print("match found")


# else:
#     print("match not found")



# import re

# pattern = r"abc"
# string = ['ac', 'abc', 'bcd', 'abbd', 'xyz']

# match = [s for s in string if re.search(pattern, s)]
# print(match)


# import re

# pattern = r"a|c"
# string = ['ac', 'abc', 'bcd', 'abbd', 'xyz']

# match = [s for s in string if re.search(pattern, s)]
# print(match)


# import re

# pattern = r"ab*c"
# string = ['ac', 'abc', 'bcd', 'abbd', 'xyz']

# match = [s for s in string if re.search(pattern, s)]
# print(match)



# import re

# pattern = r"a{2,4}"
# string = ['aaac', 'abc', 'bcd', 'abbd', 'xyz']

# match = [s for s in string if re.search(pattern, s)]
# print(match)



# import re

# pattern = r"(a|b)cd"
# string = ['aaacd', 'abc', 'bcd', 'abbd', 'xyz']

# match = [s for s in string if re.search(pattern, s)]
# print(match)



# import re

# pattern = r"\d"
# string = ['aaacd', 'abc', '1bcd', '12', 'xyz']

# match = [s for s in string if re.search(pattern, s)]
# print(match)




# import re

# pattern = "\w"
# string = ['aaacd', 'abc', '1bcd', '1232', 'xyz']

# match = [s for s in string if re.search(pattern, s)]
# print(match)



import re

pattern = "\s"
string = ['aa acd', 'abc', '1bcd', '1232', 'mz']

match = [s for s in string if re.search(pattern, s)]
print(match)