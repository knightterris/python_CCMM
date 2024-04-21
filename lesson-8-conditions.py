# age = int(input("Enter your age: "))

# if age < 18:
#     print("You are not allowed to enter this site.")
# elif age >=18 and age < 50:
#     print("You are allowed to enter this site.")
# else:
#     print("You are not allowed to enter this site.")


# tired = input("Are you tired? Y/n")

# if tired == "Y":
#     print("You should rest.")
# elif tired == "n":
#     print("Keep coding.")
# else:
#     print("Invalid input.")

# Homework (Login System)

username = input("Enter your username: ")
password = input("Enter your password: ")

correct_user = "JohnDoe"
correct_pass = "Password123"

if username == correct_user and password == correct_pass:
    print("Login successful.")
# elif username == correct_user and password != correct_pass:
#     print("Incorrect password.")
# elif username != correct_user and password == correct_pass:
#     print("Incorrect username.")
elif (username == correct_user and password != correct_pass) or (username != correct_user and password == correct_pass):
    print("Incorrect username or password.")
else:
    print("Incorrect username and password.")

