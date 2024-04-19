# Uma classe tambem pode importar outras classes:
from Modelos.avaliacão  import Avaliacão


class Restaurante:# Criando uma classe no python , ' Objeto é a instancia de uma classe '
    restaurantes = []


    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacão = []
        Restaurante.restaurantes.append(self)
    

    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restalrantes(cls):
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    # Criando metodo para alternar estado de "ATIVO\DESATIVADO"
    def alternar_estado(self):
        self._ativo = not self._ativo

    
    #criando um metodo que ira passar as imformções e receber as avaliações:
    def receber_avaliação(self, cliente, nota):
        avaliacão = Avaliacão(cliente, nota)
        self._avaliacão.append(avaliacão)