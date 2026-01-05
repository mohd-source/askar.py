# text = input("Enter a prompt containing an expression in parentheses: ")


# # print(" 1. Add\n 2. Sub\n 3. Multi\n 4. Devide\n 5. Exit")
# # print()
# # print()

# # c = int(input("What do u want to do ...(1-4)\n"))


# # if c == 1:
# start = text.index("(") + 1
# end = text.index(")")
# expr = text[start:end].replace(" ", "") 
# num1, num2 = expr.split("+")
# result = int(num1) + int(num2)
# print("Result:", result)




# elif c == 2:

#     start = text.index("(") + 1
#     end = text.index(")")

#     expr = text[start:end].replace(" ", "") 


#     num1, num2 = expr.split("-")

#     result = int(num1) - int(num2)
#     print("Result:", result)



# elif c == 3:
#     start = text.index("(") + 1
#     end = text.index(")")

#     expr = text[start:end].replace(" ", "") 


#     num1, num2 = expr.split("*")

#     result = int(num1) * int(num2)
#     print("Result:", result)

    



# elif c == 4:
    
#     start = text.index("(") + 1
#     end = text.index(")")

#     expr = text[start:end].replace(" ", "") 


#     num1, num2 = expr.split("/")

#     result = int(num1) / int(num2)
#     print("Result:", result)


# elif c == 5:
#     exit







# pwd = str(input("Enter any password of lenth 11: "))

# # print(len(pwd))
# # print(pwd[5:6])
# rules = [
#     len(pwd) ==  11,
#     any(c.isupper() for c in pwd),
#     any(c.islower() for c in pwd),
#     any(c.isdigit() for c in pwd),
#     any(not c.isalnum() for c in pwd),
#     pwd[:5].isalpha(),
#     pwd[5:6].isdigit(),
#     pwd[-1] in "!@#$%"
# ]

# print("Valid pass" if all(rules) else "Invalid pass")
    



resp = "name == steams ;; age == 27 ;; score == 88 ;; country == pak"

pairs = resp.split(";;")
clean_data = {}

for p in pairs:
    key, val = p.split("==")
   
  
    if val.isdigit():
        int(val)
        print(val[2])
   
    clean_data[key] = val

print(clean_data)

    








# print(clean_data)
# print(clean_data["age"])
# print(clean_data["score"])
# # for p in parts:
#     # Skip empty strings
#     if not p.strip():
#         continue
    
#     # Ensure the part contains '==' exactly once
#     if "==" not in p:
#         continue

#     key_val = p.split("==")
    
#     # Ensure the split gives exactly 2 items
#     if len(key_val) != 2:
#         continue

#     key, val = key_val

#     # Skip empty keys
#     if not key.strip():
#         continue
    


    




