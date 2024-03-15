
class Restaurante:# Criando uma classe no python , ' Objeto é a instancia de uma classe '
    restaurantes = []


    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restalrantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restalrantes() 