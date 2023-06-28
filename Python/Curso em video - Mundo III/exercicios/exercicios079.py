#  Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
#  Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, 
#  em ordem crescente.

números = list()
while True:
    n = int(input('Digite um número:'))
    if n not in números:
        números.append(n)
        print('registrado')
    else:
        print('Não registrado')
    r = str(input('quer continuar? [N\S]'))
    if r in 'Nn':
        break
números.sort()
print(f'Vc digitou {números}')
