
class Restaurante: # Criando uma classe no python , ' Objeto é a instancia de uma classe '
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'


restaurante_pizza = Restaurante()

Restaurantes = [ restaurante_pizza, restaurante_praca ]

print(vars(restaurante_praca))