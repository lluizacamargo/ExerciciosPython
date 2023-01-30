
nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))

if nome == 'Luciana':
    print('Olá Luciana!')
elif idade < 18:
    print('Você não é Luciana! E é menor de idade!')
elif idade > 100:
    print('Diferente de você, Luciana não é imortal!')
elif nome != 'Luciana':
    print('você é {}, você tem: {} anos'.format(nome, idade))



