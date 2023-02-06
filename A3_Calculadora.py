print('CALCULADORA')
print(' + Adição')
print(' - Subtração')
print(' * Multiplicação')
print(' / Divisão')
print('Precisone outra tecla para Sair')

op = input ('Qual operação deseja fazer? ')
if op == '+' or op == '-' or op == '*' or op == '/':
    x = int(input('Digite o primeiro valor: '))
    y = int(input ('Digite o segundo valor: '))

if (op == '+'):
    res = x + y
    print('Resultado: {} + {} = {}'.format(x, y, res))
elif (op == '-'):
    res = x - y
    print('Resultado: {} - {} = {}'.format(x, y, res))
elif (op == '*'):
    res = x * y
    print('Resultado: {} * {} = {}'.format(x, y, res))
elif (op == '/'):
    res = x / y
    print('Resultado: {} / {} = {}'.format(x, y, res))

else: #Vai entrar nessa condição para o caso do usuario não escolher nenhuma opção acima.
    print('Operação invalida!')

print('Encerrando o programa...')
