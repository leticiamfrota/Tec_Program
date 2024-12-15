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
            raise ValueError("Quantidade a remover maior do que a disponível.")
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
        if livro.quantidade > 0:
            self.livros_emprestados.append(livro)
            livro.remove_exemplar(1)
        else:
            raise ValueError("Não há exemplares disponíveis")

    def devolver_livros(self, livro: Livro):
        for i in self.livros_emprestados:
            if i.isbn == livro.isbn:
                self.livros_emprestados.remove(livro)
                livro.adicionar_exemplar(1)
                return
        else:
            raise ValueError("Este livro não está emprestado por este usuário.")
    
    def listar_emprestimos(self):
        return [livro.titulo for livro in self.livros_emprestados]
    
class Biblioteca:

    def __init__(self):
        self.livros = []
        self.usuario = []

    def adicionar_livros(self, livro: Livro):
        for i in self.livros:
            if i.isbn == livro.isbn:
                i.adicionar_exemplar(1)
                return
        else:
            self.livros.append(livro)
    
    def remover_livro(self, isbn: str):
        for livro in self.livros:
            if livro.isbn == isbn:
                self.livros.remove(livro)
                return
        else:
            raise KeyError("Livro não existe")
        
    def cadastrar_usuario(self, usuario: Usuario):
        for i in self.usuario:
            if i.cpf == usuario.cpf:
                raise ValueError("Usuário já cadastrado")
        else:
           self.usuario.append(usuario)
    
    def emprestar_livro(self, cpf: str, isbn: str):
        for usuario in self.usuario:
            if usuario.cpf == cpf:
                for livro in self.livros:
                    if livro.isbn == isbn:
                        usuario.emprestar_livros(livro)
                        return
                else:
                    raise ValueError("Livro Não Cadastrado")
        else:
            raise ValueError("Usuário Não Cadastrado")
                
    
    def devolver_livro(self, cpf: str, isbn: str):
        for usuario in self.usuario:
            if usuario.cpf == cpf:
                for livro in usuario.livros_emprestados:
                    if livro.isbn == isbn:
                        usuario.devolver_livros(livro)
                        return
        else:
            raise ValueError("Usuário Não Cadastrado")
                
                