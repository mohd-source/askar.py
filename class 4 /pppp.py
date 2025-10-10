print("Hello World")

# print the traditional hello world

z = 2 + 15


a = 12 

print(float(a))
print()

print(int(True))
print(int(False))
print()

print(bool(1))
print(bool(0))
print()


c = 6 / 2
print(type(c))
print()


d = 6 // 2
print(type(d))
print()

print(type("hello" == "world"))
print()

d = "1001"
print(int(d))



e = 43 + 60
f = e / 3

print("\n" , f , "\n" , "\n" ,type(f))





name = "Askar Gamer"

print(name[0])
print()
for i in range(6 , 11):
    print(name[i])

print()
print(name[6 : 10])



print()
print(len(name))



print()
print(name[::2])


print()
print(name[0:5:2])

print()
state = name + " is a good gamer"

print(state) 

p = state.upper()

print()
print(p)


print()
state = name + " is a good gamer"
q = state.replace("gamer" , "Boy")

print(q) 

print()
state = name + " is a good gamer"
r = state.find("Askar")

print(r) 
print(int(True))
print(int(False))
print()

print(bool(1))
print(bool(0))
print()


c = 6 / 2
print(type(c))
print()


d = 6 // 2
print(type(d))
print()

print(type("hello" == "world"))
print()

d = "1001"
print(int(d))



e = 43 + 60
f = e / 3

print("\n" , f , "\n" , "\n" ,type(f))





name = "Askar Gamer"

print(name[0])
print()
for i in range(6 , 11):
    print(name[i])

print()
print(name[6 : 10])



print()
print(len(name))



print()
print(name[::2])


print()
print(name[0:5:2])

print()
state = name + " is a good gamer"

print(state) 

p = state.upper()

print()
print(p)


print()
state = name + " is a good gamer"
q = state.replace("gamer" , "Boy")

print(q) 

print()
state = name + " is a good gamer"
r = state.find("gamer")
print(int(True))
print(int(False))
print()

print(bool(1))
print(bool(0))
print()


c = 6 / 2
print(type(c))
print()


d = 6 // 2
print(type(d))
print()

print(type("hello" == "world"))
print()

d = "1001"
print(int(d))



e = 43 + 60
f = e / 3

print("\n" , f , "\n" , "\n" ,type(f))





name = "Askar Gamer"

print(name[0])
print()
for i in range(6 , 11):
    print(name[i])

print()
print(name[6 : 10])



print()
print(len(name))



print()
print(name[::2])


print()
print(name[0:5:2])

print()
state = name + " is a good gamer"

print(state) 

p = state.upper()

print()
print(p)


print()
state = name + " is a good gamer"
q = state.replace("gamer" , "Boy")

print(q) 

print()
state = name + " is a good gamer"
r = state.find("gamer")

print(r) 

print(r) 



import re
print()
s1 = "The bodygarde is best"

pattern = r"d"

result = re.search(pattern, s1)

if result:
    print("Match Found")
else:
    print("Match Not Found")