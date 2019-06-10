# inventory.py 
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 


def addToInventory(inventory, addedItems):
	for item in addedItems:
		inventory.setdefault(item, 0)
		inventory[item] += 1
	return inventory
	
inv = {'gold coin': 42, 'rope': 1} 
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] 


def displayInventory(inventory):
	print("Inventory:")
	item_total = 0 
	for k, v in inventory.items():
		 # FILL IN THE CODE HERE
		 print(f"{v} {k}")
		 item_total += v
	print("Total number of items: "+ str(item_total)) 
		 
inv = addToInventory(inv, dragonLoot)
print(inv)
displayInventory(inv)
