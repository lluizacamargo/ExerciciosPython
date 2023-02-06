# Ler o código de uma peça 1, o número de peça 1, o valor unitário de cada peça 1
# o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2.
# Após, calcule e mostre o valor a ser pago.
# O arquivo de entreda contém duas linhas de dados. Em cada linha haverá 3 valores,
# respectivamente dois interiros e um valor com 2 casas decimais.
# A saída deverá ser uma mensagem conforme o exemplo, lembrando de deixar um espaço após os dois pontos e um espaço após "R$"
# O valor deverá ser apresentado com 2 casas após o ponto.


linha = input().split()
peca1 = int(linha[0])
qt1 = int(linha[1])
valor1 = float(linha[2])

linha2 = input().split()
peca2 = int(linha[0])
qt2 = int(linha2[1])
valor2 = float(linha2[2])

pagamento = (qt1 * valor1) + (qt2 * valor2)
print("VALOR A PAGAR: R$ %.2f" % pagamento)
