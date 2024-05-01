
# Utilizando o medoto de impotação do python
# Vamos importar os medelos restalrantes, bebidas e prato
from Modelos.Restaurante import Restaurante
from Modelos.cardapio.bebida import Bebida
from Modelos.cardapio.prato import Prato

# Criando instancias dos restalrantes;
restaurante_praca = Restaurante('praca', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', '5.0', 'grande')
prato_paozinho = Prato('Paozinho', '2.00', 'O Melhor pão da cidade')
restaurante_praca.adicionar_bebida_no_cardapio(bebida_suco)
restaurante_praca.adicionar_bebida_no_cardapio(prato_paozinho)

def main(): # Função onde pedimos para exibir todos os restaurantes;
    print(bebida_suco)
    print(prato_paozinho)


if __name__ == '__main__': # Definindo como nosso programa principal.
    main() 