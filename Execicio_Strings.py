# Execulte as seguintes atribuições: s1 = 'ant' s2 = 'bat' e s3 = 'cod'

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

# Agora, utilizando operadores + e *, crie as saídas a seguir:
# a) 'ant bat cod'
# b) 'ant ant ant ant ant ant ant ant ant ant'
# c) 'ant bat bat cod cod cod'
# d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
# e) batbatcod batbatcod batbatcod batbatcod batbatcod'

print(s1 +  ' ' + s2 + ' ' + s3)

print(10 * (s1 + ' '))

print(s1 + ' ' + 2 * (s2 + ' ') + ' ' + 3 * (s3 + ' ') )

print(7 * (s1 + ' ' + s2 + ' '))

print(5 * (s2 + s2 + s3 + ' '))