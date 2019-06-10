import os

def main():
	while True:
		userphrase = (input("Please enter a word or phrase: ")).lower()
		os.system('clear')
		# Remove whitespace
		#userphrase = userphrase.split()
		#userphrase= userphrase.lower()
		userphrasetemp= userphrase.replace(' ', '')
		if userphrasetemp.isalpha():
			break
		else:
			print("Please only use a-z alphabet")
			
	userphrasehidden = []
	
	for i in range(len(userphrase)):
		if userphrase[i].isalpha():
			userphrasehidden.append('_ ')
		else:
			userphrasehidden.append('  ')
	
	print(''.join(userphrasehidden))
	
	wrongguess =0
	
	while True:
		if not '_ ' in userphrasehidden:
			print(f'you win, with {wrongguess} incorrect guesses')
			break
		character = letterguess()
		if guess(character, userphrase):
			indexed = guess(character, userphrase)
			userphrasehidden = hiddenchange(userphrasehidden, userphrase, indexed)
			print(''.join(userphrasehidden))
		else:
			wrongguess+=1
			print(f'You have had {wrongguess} incorrect guesses')
			

def hiddenchange(userphrasehidden, userphrase, indexed):
	for i in indexed:
		userphrasehidden[i] = userphrase[i]
	return userphrasehidden

def guess(guess, userphrase):
	if guess in userphrase:
		return [i for i, x in enumerate(userphrase)if x == guess]
		print(indices)
	else:
		return False
		
def letterguess():
	while True:
		guess = (input("Guess a letter: ")).lower()
		if len(guess) != 1 or not guess.isalpha():
			print("You need to enter just one letter")
		else:
			return guess

main()