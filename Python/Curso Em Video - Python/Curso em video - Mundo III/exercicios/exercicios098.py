# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), 
# que receba três parâmetros: início, fim e passo. Seu programa tem que realizar 
# três contagens através da função criada: 
# a) de 1 até 10, de 1 em 1 
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep

def contador(i, f, p): # inicio, fim e passo.
    if p < 0:
        p *= -1
    if p ==0:
        p = 1
    print(f'contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')

# Programa principal.
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez e presonalizar a contagem!')
ini = int(input('inicio:   '))
fim = int(input('fim:      '))
pas = int(input('passo:    '))
contador(ini, fim, pas)