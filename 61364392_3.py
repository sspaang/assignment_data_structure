def CheckSpacebar(userName):
        spacebarCount = userName.count(" ")
        while spacebarCount >= 1:
                print("Please enter your username again without spacebar.")
                userName = input("Enter your username: ")
                pwd = input("Enter your password: ")
                spacebarCount = userName.count(" ")
                CheckUserNameLenght(userName)

def CheckUserNameLenght(userName):
        while not(len(userName) >= 6 and len(userName) <= 20):
                print("Please enter your username again with 6-20 characters.")
                userName = input("Enter your username: ")
                pwd = input("Enter your password: ")
                CheckSpacebar(userName)

def Username_password():
    userName = input("Enter your username: ")
    pwd = input("Enter your password: ")
    CheckUserNameLenght(userName)
    CheckSpacebar(userName)  

print("Enter your username with 6-20 characters and no spacebar.")
Username_password()
