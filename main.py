import random

user_words = input("Enter your password: ")

#chars which will be sanitized from input
bad_chars = [" "]

new_pass = ''

#replacing bad characters
for i in bad_chars:
    sanitized_string = user_words.replace(i, '')

string_len = len(sanitized_string)

while True:
	#generating a random password using the words entered by the user
	for i in range(string_len):
		#geberating a random position to get a random char from user enter strings
		char_pos = random.randint(0,string_len - 1)

		#if the char is already present in new pass then we will not inculde that char twice
		if sanitized_string[char_pos] in new_pass: continue
		new_pass = new_pass + sanitized_string[char_pos]

	print("Your Newly Generated pass:",new_pass)

	#prompting user if he wants to generate new one
	gen_new_pass = input("\nDo You want to generate new one again?\n Press Enter if you don't. Press Y if yes. ")
	if(gen_new_pass == ''): break
	new_pass = ''

#ToDo
#include special chars into the password to make it strong
