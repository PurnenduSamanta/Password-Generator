import p as p
from itertools import permutations
user_password = input("Enter your password: ")
bad_chars = [" "]
for i in bad_chars:
    user_password = user_password.replace(i, '')
for word in [''.join(p) for p in permutations(user_password)]:
    print(word)
