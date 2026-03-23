
def adicionar(x, y):
    """Realiza a adição"""
    return x + y

def subtrair(x, y):
    """Realiza a subtração"""
    return x - y

def multiplicar(x, y):
    """Realiza a multiplicação"""
    return x * y

def dividir(x, y):
    """Realiza a divisão"""
    if y == 0:
        return "Erro: Não é possível dividir por zero!"
    return x / y

def calculadora():
    """Função principal da calculadora"""
    print("=" * 40)
    print("         CALCULADORA SIMPLES")
    print("=" * 40)
    
    while True:
        print("\nSelecione a operação:")
        print("1. Adição (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Sair")
        
        escolha = input("\nDigite sua escolha (1/2/3/4/5): ")
        
        if escolha == '5':
            print("\nObrigado por usar a calculadora!")
            break
        
        if escolha in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if escolha == '1':
                    print(f"\n{num1} + {num2} = {adicionar(num1, num2)}")
                elif escolha == '2':
                    print(f"\n{num1} - {num2} = {subtrair(num1, num2)}")
                elif escolha == '3':
                    print(f"\n{num1} * {num2} = {multiplicar(num1, num2)}")
                elif escolha == '4':
                    resultado = dividir(num1, num2)
                    print(f"\n{num1} / {num2} = {resultado}")
            except ValueError:
                print("\nErro: Digite um número válido!")
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    calculadora()
