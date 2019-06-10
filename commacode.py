spam = ['apples', 'bananas', 'tofu', 'cats']
spam=['apples', 'cats']


def comma(spam):
	commacode = ''
	for i in range(len(spam)):
		if len(spam) == 2:
			commacode = spam[0] + ' and ' + spam[1]
			break
		if i ==0:
			commacode = spam[i]
		elif i == len(spam) -2:
			commacode += ', '+ spam[i] + ' and '
		elif i == len(spam) - 1:
			commacode += spam[i]
		else:
			commacode += ', ' + spam[i]
	return commacode
	
def main():
	print(comma(spam))
	
main()