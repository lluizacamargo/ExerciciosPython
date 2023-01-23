print('Bem vindo ao comercio de contrução L&A!')
print('Selecione o produto desejado:')

print('1 = Areia')
print('2 = Cimento')
print('3 = Pedra')

prod = int(input('Digite o produto desejado: '))
quant = int(input('Digite a quantidade desejada do produto: '))

if (prod == 1):
    pagar = quant * 10.5
    print('Você comprou Areia {}. O total para o pagamento é: {} '.format(quant, pagar))
elif (prod == 2):
    pagar = quant * 15.9
    print('Você comprou Cimento {}. O Total à ser pago é: {} '.format(quant, pagar))
elif (prod == 3):
    pagar = quant * 2.95
    print('Você comprou Pedra {}. O Total à ser pago é: {} '.format(quant, pagar))

else:
    print('Produto inexistente!')