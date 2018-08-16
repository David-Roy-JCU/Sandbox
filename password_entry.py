"""
David Roy
"""

MIN_LENGTH = 8

password = input("Enter password (min {} characters): ".format(MIN_LENGTH))
while len(password) < MIN_LENGTH:
    print("Password must be {} characters".format(MIN_LENGTH))
    password = input("Enter password (min {} characters): ".format(MIN_LENGTH))
print()
print("*" * len(password))
