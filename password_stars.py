"""
Password stars program
"""

LENGTH_MINIMUM = 10

password = input("Password: ")
length = len(password)

while length < LENGTH_MINIMUM:
    print("Password is too short!")
    password = input("Password: ")
    length = len(password)

print("*" * length)
