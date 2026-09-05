# from werkzeug.security import generate_password_hash
#
# password = input("Enter your admin password: ")
#
# hashed_password = generate_password_hash(password)
#
# print()
# print("Your password hash:")
# print(hashed_password)

from werkzeug.security import check_password_hash

stored_hash = "scrypt:32768:8:1$K6o2MZlQv8pwFlaj$cff475483cfe545ed27522202bf08dd790d4f9be85a9ef19ffd768fcf0dfcdad46ae92718502ff24eb6045cf03c1f38d7a9f4ed42afa00cda21ba794b912771d"

password = input("Enter password: ")

if check_password_hash(stored_hash, password):
    print("PASSWORD MATCH")
else:
    print("PASSWORD DOES NOT MATCH")