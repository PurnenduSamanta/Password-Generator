from itertools import permutations

user_password = input("Enter your password: ")

#removing bad chars
bad_chars = [" "]
for i in bad_chars:
    user_password = user_password.replace(i, '')

#getting all the permutations of user entered input 
#and storing it into a list
for word in [''.join(p) for p in permutations(user_password)]:
    print(word)
