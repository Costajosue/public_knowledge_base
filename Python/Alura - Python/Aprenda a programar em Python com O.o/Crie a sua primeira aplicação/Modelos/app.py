# Utilizando medoto de impotação do python
from Modelos.Restaurante import Restaurante

# Criando instancias dos restalrantes;
restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_praca.receber_avaliação('Gui', 10)
restaurante_praca.receber_avaliação('Lais', 8)
restaurante_praca.receber_avaliação('Emy', 5)


def main(): # Função onde pedimos para exibir todos os restaurantes;
    Restaurante.listar_restalrantes()

if __name__ == '__main__': # Definindo como nosso programa principal.
    main() 