l = 0
m = 0
while True:
    print('Digite o seu cpf: ')
    cpf = input()
    if cpf == '':
        break
    list(cpf)
    for i in range(10, 1, -1):
        #calculando o l
        l = l + i*int(cpf[-i-1])
        #calculando o m
        m = m + i*int(cpf[-i])
    r = l%11
    R = m%11
    if r == 0 or r == 1:
        penultimo = 0
    else:
        penultimo = 11 - r
    if R == 0 or R == 1:
        ultimo = 0
    else:
        ultimo = 11 - R
    if penultimo == int(cpf[9]) and ultimo == int(cpf[10]):
        print('cpf válido!')
    else:
        print('cpf inválido!')

