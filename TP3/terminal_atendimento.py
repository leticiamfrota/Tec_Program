from sisbanco import *

def terminal():
    sisbanco = Banco()
    while (True):
        print ("SisBanco::Bem-Vindo!")
        print (".::Opcoes::.")
        print ("[0]-CriarConta")
        print ("[1]-Creditar")
        print ("[2]-Debitar")
        print ("[3]-Transferir")
        print ("[4]-Saldo")
        print ("[5]-Render_Juros")
        print ("[6]-Render_Bonus")
        print ("[7]-Alterar_Taxa_Juros")
        print ("[8]-Sair")
        opcao = int(input("Digite:"))

        if opcao == 0:
            #solicite o numero da conta a ser criada
            num_conta = input("Num: ")
            print ("[0]-Conta")
            print ("[1]-Conta Poupança")
            print ("[2]-Conta Especial")
            tipo = int(input("Tipo:"))
            if tipo == 0:
                conta = Conta(num_conta)
            elif tipo == 1:
                conta = ContaPoupanca(num_conta)
            elif tipo == 2: 
                conta = ContaEspecial(num_conta)
            #cadastre a conta no sis banco
            sisbanco.cadastrar(conta)

        elif opcao == 1:
            #solicite o numero da conta alvo
            conta_alvo_cred = input("Num: ")
            #solicite o valor a ser creditado
            valor_cred = float(input("Valor: "))
            #realize a operacao de credito no sis banco
            sisbanco.creditar(conta_alvo_cred, valor_cred)
        elif opcao == 2:
            #solicite o numero da conta alvo
            conta_alvo_deb = input("Num: ")
            #solicite o valor a ser debitado
            valor_deb = float(input("Valor: "))
            #realize a operacao de debito no sis banco
            sisbanco.debitar(conta_alvo_deb, valor_deb)
        elif opcao == 3:
            #solicite o numero da conta origem
            conta_origem = input("Num_origem: ")
            #solicite o numero da conta destino
            conta_destino = input("Num_destino: ")
            #solicite o valor a ser transferido
            valor_transf = float(input("Valor: "))
            #realize a operacao de transferencia no sis banco
            sisbanco.transferir(conta_origem, conta_destino, valor_transf)
        elif opcao == 4:
            #solicite o numero da conta alvo
            conta_alvo = input("Num: ")
            #realize a operacao de obtencao de saldo no sis banco
            saldo = sisbanco.saldo(conta_alvo)
            #exiba o saldo na tela
            print(saldo)
        elif opcao == 5 :
            conta_alvo = input("Num: ")
            sisbanco.render_juros(conta_alvo)
        elif opcao == 6 :
            conta_alvo = input("Num: ")
            sisbanco.render_bonus(conta_alvo)
        elif opcao == 7 :
            taxa = float(input('Taxa: '))
            sisbanco.set_taxa(taxa)
        elif opcao == 8 :
            print ("SisBanco ::Bye!")
            break

        
terminal()