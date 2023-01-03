# Desenvolva um algoritimo que solicite a ao usuário o preço de um produto
# e um percentual de desconto a ser aplicado a ele.
# Calcule e exiba o valor do desconto e o preço final do produto.

preco = float(input(' Digite o preço do produto: ')) #O resultado da saída do input é sempre uma string como o preço é um valor com virgula ou seja valor com ponto flutuante é necessario convertar a string com ponto flutuante usando o float.
p = float(input(' Digite o percentual de desconto (0-100)%: '))

desconto = preco * (p / 100)
final = preco - desconto

print(' O preço do produto é {} . Desconto de {}. '.format(preco, p))
#print(' o preco do produto' + preco + 'desconto de ' + p ) metodo antigo.
print(' O Valor calculado de desconto: {}. Valor final do produto: {}'.format(desconto, final))

