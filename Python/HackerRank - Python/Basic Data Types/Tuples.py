if __name__ == "__main__":

    n = int(input())  # Ler o número de elementos na tupla
    numeros = (input().split())  # Ler os inteiros separados por espaços utilizando o split() para separalos
    
    # criar a tupla, como queremos umatupla de inteiros, vou utilizar o função map para percorre a lista e transformar possiveis numeros em inteiros
    t = tuple(map(numeros))

print(t)