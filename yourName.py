print('Digite seu cpf')

cpf = int(input())

eleven = cpf%10
ten = (cpf//10)%10
nine = (cpf//100)%10
eight = (cpf//1000)%10
seven = (cpf//10000)%10
six = (cpf//100000)%10
five = (cpf//1000000)%10
forth = (cpf//10000000)%10
three = (cpf//100000000)%10
two = (cpf//1000000000)%10
one = (cpf//10000000000)%10

penultimo = 0
ultimo = 0

l = 10*one + 9*two + 8*three + 7*forth + 6*five + 5*six + 4*seven + 3*eight + 2*nine
r = l%11

if r == 0 or r == 1:
    penultimo = 0
else:
    penultimo = 11 - r

print ('o penultimo é: ' + str(penultimo))

m = 10*two + 9*three + 8*forth + 7*five + 6*six + 5*seven + 4*eight + 3*nine + 2*ten
R = m%11
print(' o valor de m: ' + str(m))

if R == 0 or R == 1:
    ultimo = 0
else:
    ultimo = 11 - R

print ('o ultimo é: ' + str(ultimo))

if ten == penultimo and eleven == ultimo:
    print('cpf valido!')
else:
    print('cpf invalido')
