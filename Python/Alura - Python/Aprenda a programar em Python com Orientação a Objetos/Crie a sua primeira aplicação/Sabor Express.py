# Importando biblioteca 'OS' que nesse caso vamos utilizar para curtomizar nosso def finalizar_app(): para limpar o terminal quando optarmos pela opção de finaliza o programa\sair mostrar somente 'Finalizando programa' .
import os

restaurantes =['Pizza', 'sushi'] # criando uma lista onde vamos armazenar os dados.

def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_opçoes(): # Criando menu do projeto:
    # Criando menu do projeto:
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair\n')


# Definindo uma função finalizar_app() para finalizar o programa na linha 34, e assim deixar o codigo mais limpo.
def finalizar_app():
    exibir_subtitulo('Finalizar App')

def voltar_ao_menu_principal():
        input('\nDigite uma tecla para voltar ao menu inicial ')
        main() #chamando função main 

def opcao_invalida(): #caso o usuario não digite uma das opções ja determinadas
    print('Opção invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto): # com essa função vamos otimizar o codigo ao exibir subtitulos nas outras funções.
    os.system('cls')
    print(texto)

def cadastrar_novo_restaurante(): #Função que ira cadastrar os restaurantes;
    exibir_subtitulo('Cadastro de novos restaurantes ')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)# adicionando string e dados na lista.
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()


def listar_restaurantes(): # função que ira listar os restaurantes
    exibir_subtitulo('Listando restaurantes')

    for restaurante in restaurantes: # significa 'Para cada restaurante em restaurentes'
        print(f'.{restaurante}')
    voltar_ao_menu_principal()

def escolher_opcao():# Deixando o menu funcional armarzenando o input em uma variavel e logo após mestramos o resultado com o print:
    try: # significa (tente) tente executar isso:
        # Adicionando o int na frete de input significa que estamos mostrando que vamos receber um número inteiro.
        opcao_escolhida = int(input('Escolha uma opção: ')) 

        # Agora utilizando o if, elif e else para colocarmos funcionalidades nas opções.
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except: # caso não consiga:
        opcao_invalida()


def main():# função para limpar ou voltar para o menu de interação;
    os.system('cls') #comando para limpar a tela/terminal
    exibir_nome_do_programa()
    exibir_opçoes()
    escolher_opcao()

if __name__ == '__main__':
    main()