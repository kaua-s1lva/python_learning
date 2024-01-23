catNames = []
while True:
    print('Digite o gato ' + str(len(catNames) + 1) + ' : ')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
for i in range (len(catNames)):
    print('O gato ' + str(len(catNames)) + ' é ' + catNames[i])
