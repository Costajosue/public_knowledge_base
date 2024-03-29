# Utilizando medoto de impotação do python
from Modelos.Restaurante import Restaurante

# Criando instancias dos restalrantes;
restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternar_estado() # utilizando função que importamos para ativar restalrante; 

def main(): # Função onde pedimos para exibir todos os restaurantes;
    Restaurante.listar_restalrantes()

if __name__ == '__main__': # Definindo como nosso programa principal.
    main()