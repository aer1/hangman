import random

gallows = [
"""
__________
|        |
|
|
|
|
|
|_____

""",
"""
_________
|        |
|        0
|
|
|
|
""",
"""
_________
|        |
|        0
|        | 
|
|
|
|_____
""",
"""
_________
|        |
|        0
|       /| 
|     
|
|
|_____
""",
"""
_________
|        |
|        0
|       /|\ 
|     
|
|
|_____
""",
"""
_________
|        |
|        0
|       /|\ 
|       /     
|
|
|_____
""",
"""
_________
|        |
|        0
|       /|\ 
|       / \    
|
|
|_____
""",
"""
 ______        ____        ___  ___    ______
/  ____|      /    |      /   |/   |  |   ___|
|  |         / / | |     / /|   /| |  |  |__
|  |  _     / ____ |    / / |__/ | |  |   __|
|  |_| |   / /   | |   / /       | |  |  |___
\______/  /_/    |_|  /_/        |_|  |______|

 ______   _     _   ______   _______     ____________
/  __  \ | |   / / |   ___| |   __  \    |          |
| |  | | | |  / /  |  |__   |  |__| |    |   X  X   |
| |  | | | | / /   |   __|  |   __  /    |   ____   |
| |__| | | |/ /    |  |___  |  |  \ \    |  /    \  |
\______/ |___/     |______| |__|   \_\   |__________|
"""
]

you_win = [
"""
 __    __   _______   __    __
|  |  |  | /  ___  \ |  |  |  |
 \  \/  /  | |   | | |  |  |  |  
  \    /   | |   | | |  |  |  |
   |  |    | |   | | |  |  |  |
   |  |    | |___| | |  |__|  |
   |__|    \_______/  \______/
 
 __          __  _   __    _     ___________    
 \ \        / / | | |  \  | |   |           |
  \ \  /\  / /  | | |   \ | |   |   0   0   |
   \ \/  \/ /   | | | |\ \| |   |           |
    \  /\  /    | | | | \   |   |  \_____/  | 
     \/  \/     |_| |_|  \__|   |___________|
"""     
] 

# print gallows[0]
# print gallows[1]
# print gallows[2]
# print gallows[3]
# print gallows[4]
# print gallows[5]
# print gallows[6]

mystery_words = ["monty", "syntax", "decode", "dictionaries", "shell", "modules"]

letters_used = []

comp_choice = random.choice(mystery_words)
#print comp_choice

print "Welcome to hangman. " 
print "\nAre you ready to lose? "

user_guess_wrong = 0
user_max_wrong = len(gallows) - 1
guessed_word = "-" * len(comp_choice)

while (user_guess_wrong < user_max_wrong) and (guessed_word != comp_choice):
	letter_guessed = raw_input("Pick a letter: ")
	if (len(letter_guessed)) > 1: 
		print "Enter only one letter at a time." 
		letter_guessed = raw_input("Pick a letter: ")
	if (letter_guessed in letters_used):
		print "Letter already used, please try a different letter."	
		letter_guessed = raw_input("Pick a letter: ")
	letters_used.append(letter_guessed)
	print letters_used
	if letter_guessed in comp_choice:
		print ("This is correct, choose the next letter.")	
		new_word = ""
		for i in range (len(comp_choice)):
			if letter_guessed == comp_choice[i]:
				new_word += letter_guessed
			else: 
				 new_word += guessed_word[i]
		guessed_word = new_word
		print guessed_word
		print user_guess_wrong	
	else: 
		print ("I'm sorry, this letter is incorrect. Please try again.")
		print gallows [user_guess_wrong]
		user_guess_wrong += 1 
		
		


if user_guess_wrong == user_max_wrong:
	print gallows [user_guess_wrong]  
else: 
	print you_win[0]

print "The word was", comp_choice

raw_input ("Press the enter key to exit.") 


	













