info =            {'porcao':0,
                   'nome':'',
                   'valor energetico':0,
                   'carboidratos':0,
                   'proteinas':0,
                   'gorduras totais':0,
                   'gordura saturada':0,
                   'fibra':0,
                   'sodio':0,
                   'calcio':0,
                   'ferro':0}

unit = []

chaves = list(info.keys())

for k in chaves:
    if k == 'nome':
        info[k] = input(k + ': ')
        continue
    info[k] = float(input(k + ': '))

listaChave = info.keys()

densidadeEnergetica = info['valor energetico']/info['porcao']

if densidadeEnergetica <= 0.6:
    print('Alimento baixissimo calorico')
elif densidadeEnergetica > 0.6 and densidadeEnergetica <= 1.5:
    print('Alimento baixo calorico')
elif densidadeEnergetica > 1.5 and densidadeEnergetica <= 4:
    print('Alimento medio calorico')
elif densidadeEnergetica > 4:
    print('Alimento alto calorico')


for i in range(11):
    if list(info.values())[i] == info['nome'] or i==0:
        continue
    a = float(list(info.values())[i])/(float(info['porcao']))
    unit.append(a)

print(unit)

unit[1] = unit[1]*5
unit[2] = unit[2]*20
unit[3] = unit[3]*10
unit[4] = unit[4]*5
unit[5] = unit[5]*20
unit[6] = unit[6]*10
unit[7] = unit[7]*10
unit[8] = unit[8]*20

print(unit)
soma = 0
for i in range(9):
    if i == 0:
        continue
    soma += unit[i]
print(soma)
