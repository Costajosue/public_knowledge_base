r1 = float(input('Primeiro segmento:'))
r2 = float(input('segundo segmento:'))
r3 = float(input('terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os valores acima PODEM FORMAR UM TRIANGULO')
else:
    print('Os segmentos acima NÃo PODEM FORMAR UMA TRIANGULO')