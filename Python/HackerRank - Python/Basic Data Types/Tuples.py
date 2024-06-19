if __name__ == "__main__":
    n = int(input().strip())  # Ler o número de elementos na tupla
    elementos = input().strip().split()  # Ler os inteiros separados por espaços
    
    # Converter os elementos para inteiros e criar a tupla
    t = tuple(map(int, elementos))
    
    # Calcular o valor hash da tupla
    resultado = hash(t)
    
    # Imprimir o resultado do hash
    print(resultado)
