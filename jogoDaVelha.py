posicao = {'top-L':' ', 'top-M':' ','top-R':' ','mid-L':' ','mid-M':' ','mid-R':' ','low-L':' ','low-M':' ','low-R':' '}

def printPosicao (posicao):
    print(posicao['top-L'] + '|' + posicao['top-M'] + '|' + posicao['top-R'])
    print('-+-+-')
    print(posicao['mid-L'] + '|' + posicao['mid-M'] + '|' + posicao['mid-R'])
    print('-+-+-')
    print(posicao['low-L'] + '|' + posicao['low-M'] + '|' + posicao['low-R'])

jogador = 'X'
for i in range(9):
    printPosicao(posicao)
    print('vez de ' + jogador + '. Mover em qual espaço?')
    move = input()
    posicao[move] = jogador
    if jogador == 'X':
        jogador = 'O'
    else:
        jogador = 'X'

printPosicao(posicao)
