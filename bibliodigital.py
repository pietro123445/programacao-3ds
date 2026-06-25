class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nNúmero de Páginas: {self.paginas}"

# Solicitação de dados ao usuário
print("--- Cadastro de Livro ---")
titulo_input = input("Digite o título do livro: ")
autor_input = input("Digite o autor do livro: ")
paginas_input = input("Digite a quantidade de páginas: ")

# Criação da instância e exibição do resultado
meu_livro = Livro(titulo_input, autor_input, paginas_input)

print("\n--- Descrição do Livro Cadastrado ---")
print(meu_livro)
