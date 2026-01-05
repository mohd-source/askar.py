def grade(score: int) -> str:
    if score >=90 :
        return "A+"

    elif score >=80:
        return "A"
    
    elif score >=70:
        return "B"
    
    elif score >=60:
        return "C"
    
    elif score >=50:
        return "D"
    
    elif score >=40:
        return "E"
    
    else:
        return "Fail"



a=1

result = []

n = int(input("Enter student numaber : \n"))


for i in range( 1, n + 1):
    
    name = input("What is Ur name : \n")
    print("The" , a , f"student name is : {name} \n")

    score = int(input("What is Ur score : \n"))
    print("The" , a , f"student score is : {score} \n")

    a +=1

    result.append((name, score, grade(score)))

print(result)




inventory = {}

while True:
    item = input("Enter item name (or type 'done' to finish): ")
    if item.lower() == 'done':
        break
    
    quantity = int(input(f"Enter quantity for {item}: "))
    inventory[item] = quantity

print("\nInventory List:")
for item, quantity in inventory.items():
    print(f"{item}: {quantity}")