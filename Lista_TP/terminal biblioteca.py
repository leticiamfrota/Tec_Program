from sisbiblioteca import *

def terminal():
    biblioteca = Biblioteca()
    while True:
        print("\n:: Sistema de Biblioteca ::")
        print("1 - Cadastrar Livro")
        print("2 - Remover Livro")
        print("3 - Cadastrar Usuário")
        print("4 - Emprestar Livro")
        print("5 - Devolver Livro")
        print("6 - Listar Livros")
        print("7 - Listar Usuários")
        print("8 - Sair")
        opcao = input("Digite sua escolha: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("Isbn: ")
            livro = Livro(titulo, autor, isbn)
            biblioteca.adicionar_livros(livro)
        
        elif opcao == "2":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("Isbn: ")
            livro = Livro(titulo, autor, isbn)
            biblioteca.remover_livros(livro)
        
        elif opcao == "3":
            nome = input("Nome: ")
            cpf = input("Cpf: ")
            usuario = Usuario(nome, cpf)
            biblioteca.cadastrar_usuario(usuario)

        elif opcao == "4":
            isbn = input("Isbn: ")
            cpf = input("CPF: ")
            biblioteca.emprestrar_livro(cpf, isbn)
          
        elif opcao == "5":
            isbn = input("Isbn: ")
            cpf = input("CPF: ")
            biblioteca.devolver_livro(cpf, isbn)

        elif opcao == "6":
            for livro in biblioteca.livros:
                print(f"Título: {livro.titulo} e Quantidade: {livro.quantidade}")

        elif opcao == "7":
            for usuario in biblioteca.usuario:
                print(f"Usuário: {usuario.nome} e Empréstimos: {usuario.listar_emprestimos()}")

        elif opcao == "8":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    terminal()