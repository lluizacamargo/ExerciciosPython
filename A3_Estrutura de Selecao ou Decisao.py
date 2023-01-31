
A = int(input(' Digite o 1 lado do triângulo: '))
B = int(input(' Digite o 2 lado do triângulo: '))
C = int(input(' Digite o 3 lado do triângulo: '))

if (A > 0) and (B > 0) and (C > 0):
    if (A + B > C) and (A + C > B) and (B + C > A):
        if (A != B) and (A != C) and (B != C):
            print ('Triâgulo Escaleno!')
        else:
            if (A == B) and (A == C) and (B == C):
                print ('Triângulo Equilátero!')
            else:
                print('Triangulo Isóceles!')

    else:
        print ('Ao menos um dos valores indicados não servem para formar um triângulo!')

else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo!')