# Uma classe tambem pode importar outras classes:
from Modelos.avaliacão import Avaliacão


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
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} |{str(restaurante.media_avaliacões).ljust(25)}| {restaurante.ativo}')

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


    @property
    # Criando um metodo para calcular a media da avaliação:
    # Nele estou utilizando algumas funcionalidades como:
    # sum = soma 
    # len = tamanho
    # / = dividido
    # round = aredondar os numeros e manter a ordem decimal
    def media_avaliacões(self):
        if not self._avaliacão:
            return 0
        # Calculo das medias:
        soma_das_notas = sum(Avaliacão._nota for Avaliacão in self._avaliacão)
        quantidade_de_notas = len(self._avaliacão)
        media = round (soma_das_notas / quantidade_de_notas, 1)
        return media
    