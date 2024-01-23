def criaString (lista):
    string = ''
    tamanho = len(lista)
    for i in range (tamanho):
        if i == 0:
            string = lista[0]
            continue
        string = string + ', ' + str(lista[i])
    print('a string é: ' + string)
    return string

lista = ('testando', 'teste', 1, 2, 3, True)
calcula = criaString(lista)
        
