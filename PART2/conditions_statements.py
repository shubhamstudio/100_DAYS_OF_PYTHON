# age = int(input("Enter your age: "))
# if age>=75:
#     print("You have to renew your license")
# elif age >= 18:
#     print("You can vote")
#     print("You can drive")
# else:
#     print("You can't vote and drive")

# color = input("Enter color: ")
# if color == "red":
#     print("stop")
# elif color == "yellow":
#     print("wait")
# elif color== "green":
#     print("GO")
# else:
#     print("Wrong color entered for traffic lights, try again")


# username = input("enter username: ")
# password = input("enter password: ")

# if (username == "admin" and password == "pass"):
#     print("Login Successful")
# elif (username != "admin"):
#     print("Wrong username, try again")
# elif (password != "pass"):
#     print("Wrong Password, try again")

'''Nesting'''
# username = input("enter username: ")
# password = input("enter password: ")

# if username == "admin" and password == "pass":
#     print("Login Successful (Admin)")
# elif username == "user" and password == "1234":
#     print("Login Successful (User)")
# else:
#     print("Wrong id or password")

# Match case

color = input("Enter color: ")

match color:
    case "Green":
        print("GO")
    case "Yellow":
        print("Wait")
    case "Red":
        print("STOP!")
    case _:
        print("Wrong color!")
