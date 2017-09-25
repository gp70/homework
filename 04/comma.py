items = []
while True:
    print('Enter item ' + str(len(items) + 1) +
      '   (Enter nothing to stop)')
    item = input()
    if item == '':
        break
    items = items + [item]
    
print(items)

for i in range(len(items) - 1):
    if items[i] == items[len(items) - 1]:
        break
    items[i] += ', '
    
items[len(items) - 1] = 'and ' + items[len(items) - 1]

print(items)

items2 = ''

for i in items:
    items2 += i
    
print(items2)


