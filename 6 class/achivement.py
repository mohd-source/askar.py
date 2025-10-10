p_name = input("Enter Player name: ") 
sport = str(input("Enter Sport name: "))
achiv = int(input("Enter Achivement: "))


if achiv < 10 and sport != "tanis":
    print()
    print()
    print(f"Player name = {p_name} \nSport       = {sport} \nAchivement  = {achiv} Achivement")


else:
    print()
    print("Player Must Has 20 achivement")
    print("Sport Must Have Tanis")