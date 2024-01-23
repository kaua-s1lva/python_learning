stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def printStuff (inventory):
    print('inventory: ')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total += v
    print('total number of items: ' + str(item_total))

def addToInventory (inventory, addedItems):
    for items in addedItems:
        if items in inventory.keys():
            inventory[items] = 1 + inventory.get(items)
        else:
            inventory.setdefault(items, 1)       

printStuff(stuff)
addToInventory(stuff, dragonLoot)
printStuff(stuff)
