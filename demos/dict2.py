def diplayInventory(items) :
    print('Inventory:')
    total = 0
    for k, v in items.items() :
        print(k + ' : ' + str(v))
        total += v
    print('Total items: ' + str(total))

def addToInventory(inv,itemList) :
    for item in itemList :
        inv.setdefault(item, 0)
        inv[item] += 1
        


def testDiplayInventory() :
    items = {'rope' : 1, 'torch' : 6, 'gold coins' : 40,
             'dagger' : 2, 'arrow' : 10}
    diplayInventory(items)
    print('add list *************')
    addToInventory(items, ['rope','dagger','rope'])
    diplayInventory(items)

testDiplayInventory()
