passwords = {}

while True:
    print('Write the name and the password: ')
    scan = input()
    if scan == '':
        break
    chave = (scan.split())[0]
    valor = (scan.split())[1]

    if chave in passwords.keys():
        print('Key registered, senha: ' + passwords[chave])
        print('Do you want to change? Y (yes) N (no): ')
        resposta = input()
        if resposta == 'Y' or resposta == 'y':
            passwords[chave] = valor
            print('Your new key ' + passwords[chave] + ' in ' + chave)
        else:
            continue
    else:
        passwords = {chave : valor}
        print(passwords)
