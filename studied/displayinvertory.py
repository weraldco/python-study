# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62

inventory = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12,
    }

def displayInventory(inventory):
    total_item = 0
    for k, v in inventory.items():
        total_item += v
    print("Total number of items: " + str(total_item))

def d_item(k):
    print(str(inventory.get(k)) + " " + k)
    
print("Inventory: ")
d_item('arrow')
d_item('gold coin')
d_item('rope')
d_item('torch')
d_item('dagger')
displayInventory(inventory)