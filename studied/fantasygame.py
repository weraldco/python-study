# Inventory:
# 45 gold coin
# 1 rope
# 1 ruby
# 1 dagger
# Total number of items: 48

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
invent = {'gold coin': 42, 'rope': 1}

def addedToInvetory(inv, loot):
    dict ={}
    total_items = 0

    print("Inventory: ")
    for i in range(len(loot)):
        dict.setdefault(loot[i], 0)
        dict[loot[i]] = dict[loot[i]] + 1

    for k,v in dict.items():
        if k in inv:
            total = inv.get(k) + dict.get(k)
            inv[k] = total
        else:
            inv[k] = v
    
    for k,v in inv.items():
        print(str(v) + " " + k)

        # Total item summation
        total_items = total_items + inv.get(k)
    print()    
    print("Total number of items: " + str(total_items))   

new_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'arrow', 'arrow', 'arrow', 'arrow', 'arrow']
addedToInvetory(invent, dragonLoot)
addedToInvetory(invent, new_loot)
   
    

# print(inv)
# def addToInventory(inventory,addedItems):
#     print(dict)