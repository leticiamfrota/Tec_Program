class Livro:
    def __init__(self, titulo: str, autor: str, isbn: str, quantidade: int = 1):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.quantidade = quantidade

    def adicionar_exemplar(self, quantidade: int):
        self.quantidade += quantidade
    
    def remove_exemplar(self, quantidade: int):
        if self.quantidade < quantidade:
            print("Não à exemplares suficientes")
        else:
            self.quantidade -= quantidade

    def __str__(self):
        return self.titulo, self.autor, self.isbn, self.quantidade

class Usuario:
    
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf
        self.livros_emprestados = []

    def emprestar_livros(self, livro: Livro):
        self.livros_emprestados.append(livro)
        livro.remove_exemplar(1)

    def devolver_livros(self, livro: Livro):
        self.livros_emprestados.remove(livro)
        livro.adicionar_exemplar(1)
    
    def listar_emprestimos(self):
        titulos = []
        for livro in self.livros_emprestados:
            titulos.append(livro.titulo)
        return titulos
    
class Biblioteca:

    def __init__(self):
        self.livros = []
        self.usuario = []

    def adicionar_livros(self, livro: Livro):
        for i in self.livros:
            if i.isbn == livro.isbn:
                i.adicionar_exemplar(1)
        else:
            self.livros.append(livro)
    
    def remover_livro(self, livro: Livro):
        for i in self.livros:
            if i.isbn == livro.isbn:
                self.livros.remove(i)
        else:
            print("Livro não existe")
        
    def cadastrar_usuario(self, usuario: Usuario):
        self.usuario.append(usuario)
    
    def emprestar_livro(self, cpf: str, isbn: str):
        for i in self.livro:
            if i.isbn == isbn:
                livro = i
                break
        for usuario in self.usuario:
            if usuario.cpf == cpf:
                usuario.emprestar_livros(livro)
    
    def devolver_livro(self, cpf: str, isbn: str):
        for i in self.livro:
            if i.isbn == isbn:
                livro = i
                break
        for usuario in self.usuario:
            if usuario.cpf == cpf:
                usuario.devolver_livros(livro)
