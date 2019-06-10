

def makestring(spam):
	happy=''
	for i in range(len(spam)):
		happy = happy + spam[i] + ', '
	return happy
	
def main():
	spoon = ['a', 'b', 'c', 'd', 'e']
	print(makestring(spoon))
	print(type(makestring(spoon)))
	
main()