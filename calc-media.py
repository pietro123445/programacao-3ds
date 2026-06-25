def calcular_media(numeros):
    # sum() soma os elementos e len() obtém o tamanho da lista
    if not numeros:  # Evita divisão por zero se a lista estiver vazia
        return 0.0
    return sum(numeros) / len(numeros)

# Bloco principal
if __name__ == "__main__":
    numeros = [10, 20, 30, 40, 50]
    
    media = calcular_media(numeros)
    
    # f-string formatada para mostrar 2 casas decimais (: .2f)
    print(f"A média é: {media:.2f}")
