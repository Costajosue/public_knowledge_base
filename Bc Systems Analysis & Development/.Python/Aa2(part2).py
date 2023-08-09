# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a
# multiplicação e os números.

vetor = []
num = 0 
soma = 0 
mul = 1
for c in range(0, 5):
    num = int(input('Digite um numero: '))
    vetor.append(num)
for num in vetor:
    soma += vetor
    mul *= vetor
print(f'A soma dos numeros são: {soma}')
print(f'A multiplicação dos numeros é: {mul}')