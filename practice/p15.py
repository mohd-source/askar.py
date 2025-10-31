u_n = "askarashhad"
u_p = "Ak110"


input_u_n = input("Enter your username: ")
input_u_p = input("Enter your password: ")

if input_u_n == u_n and input_u_p == u_p:
    print("Login successful!")

elif input_u_n != u_n:
    print("Username not found.")
    print("login failed.")


elif input_u_p != u_p:
    print("Incorrect password.")
    print("login failed.")