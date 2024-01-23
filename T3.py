v = {'x':'', 'y':'', 'z':''}
u = {'x':'', 'y':'', 'z':''}

def calculaVetor (vet1, vet2):
    vet = 0
    for i in vet1.keys():
        for j in vet2.keys():
            if i == j:
                vet += float(vet1[i])*float(vet2[i])
        
    return vet

for coordenada in v.keys():
    print('Digite a posicao ' + coordenada + ' do vetor v: ')
    v[coordenada] = input()

for coordenada in u.keys():
    print('Digite a posicao ' + coordenada + ' do vetor u: ')
    u[coordenada] = input()

resultado = calculaVetor(v, u)
print(resultado)
