# Importando biblioteca 'OS' que nesse caso vamos utilizar para curtomizar nosso def finalizar_app(): para limpar o terminal quando optarmos pela opção de finaliza o programa\sair mostrar somente 'Finalizando programa' .
import os

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
    os.system('cls') # Utilizando biblioteca os para limpar terminal e mostrar somente 'Finalizando programa'
    print('Finalizando o App\n')

def escolher_opcao():
    # Deixando o menu funcional armarzenando o input em uma variavel e logo após mestramos o resultado com o print:
    # Adicionando o int na frete de input significa que estamos mostrando que vamos receber um número inteiro.
    opcao_escolhida = int(input('Escolha uma opção: '))

    # Agora utilizando o if, elif e else para colocarmos funcionalidades nas opções.
    if opcao_escolhida == 1:
        print('Cadastrar restaurantes')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurantes')
    else:
        finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opçoes()
    escolher_opcao()

if __name__ == '__main__':
    main()