import pprint

message = "The High Court has thrown out an attempt to prosecute Boris Johnson over claims he lied during the 2016 referendum campaign by saying the UK gave the EU £350m a week."

count = {}

for character in message:
	count.setdefault(character, 0)
	count[character] = count[character]+ 1
	
for k, v in count.items():
	print(f"{k} : {v}")
	
#pprint module prints dict out in readable format
pprint.pprint(count)

#Pformat formats to string (same result whe  printed though)
print(pprint.pformat(count))