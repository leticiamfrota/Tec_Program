from sisbanco import *
from excecoes import *

def terminal():
   sisbanco = Banco()
   while(True):
      print("SisBanco::Bem-Vindo!")
      print(".::Opcoes::.")
      print("[0] Cadastrar Conta")
      print("[1] Creditar")
      print("[2] Debitar")
      print("[3] Transferir")
      print("[4] Consultar Saldo")
      print("[5] Render Juros")
      print("[6] Render Bonus")
      print("[7] Alterar Taxa_Juros")      
      print("[8] Alterar Taxa_Imposto")
      print("[9] Sair")
      opcao = int(input("Digite:"))
      
      if opcao == 0:
         num_conta = input("Num: ")
         print ("S-Simples")
         print ("P-Poupança")
         print ("E-Especial")
         print ("I-Imposto")
         tipo = input("Tipo:")
         if tipo == 'S':
            conta = Conta(num_conta)
         elif tipo == 'P':
            conta = ContaPoupanca(num_conta)
         elif tipo == 'E': 
            conta = ContaEspecial(num_conta)
         elif tipo == 'I':
            conta = ContaImposto(num_conta)
         #cadastre a conta no sis banco
         try:
            sisbanco.cadastrar(conta)
         except VIException as vie:
            vie.print_mensagem_erro()
         except CEException as ce:
            ce.print_mensagem_erro()
         else:
            print("Cadastro realizado com sucesso!")
         finally:
            print("Obrigado pro utilizar nossos serviços")   

      elif opcao == 1:
         #solicite o numero da conta alvo
         conta_alvo_cred = input("Num: ")
         #solicite o valor a ser creditado
         valor_cred = float(input("Valor: "))
         #realize a operacao de credito no sis banco
         try: 
            sisbanco.creditar(conta_alvo_cred, valor_cred)
         except VIException as vie:
            vie.print_mensagem_erro()
         except CIException as ci:
            ci.print_mensagem_erro()
         else:
            print("Crédito realizado com sucesso!")
         finally:
            print("Obrigado pro utilizar nossos serviços")
            

      elif opcao == 2:
         #solicite o numero da conta alvo
         conta_alvo_deb = input("Num: ")
         #solicite o valor a ser debitado
         valor_deb = float(input("Valor: "))   
         #realize a operacao de debito no sis banco
         try:
            sisbanco.debitar(conta_alvo_deb, valor_deb)
         except VIException as vie:
            vie.print_mensagem_erro()
         except SIException as sie:
            sie.print_mensagem_erro()
         except CIException as ci:
            ci.print_mensagem_erro()
         else:
            print("Débito realizado com sucesso!")
         finally:
            print("Obrigado pro utilizar nossos serviços")

      elif opcao == 3:
         #solicite o numero da conta origem
         conta_origem = input("Num_origem: ")
         #solicite o numero da conta destino
         conta_destino = input("Num_destino: ")
         #solicite o valor a ser transferido
         valor_transf = float(input("Valor: "))
         #realize a operacao de transferencia no sis banco
         try:
            sisbanco.transferir(conta_origem, conta_destino, valor_transf)
         except VIException as vie:
            vie.print_mensagem_erro()
         except SIException as sie:
            sie.print_mensagem_erro()
         except CIException as cie:
            cie.print_mensagem_erro()
         else:
            print("Transferência realizado com sucesso!")
         finally:
            print("Obrigado pro utilizar nossos serviços")
         

      elif opcao == 4:
         conta_alvo = input("Num: ")
         try:
            saldo = sisbanco.saldo(conta_alvo)
         except CIException as cie:
            cie.print_mensagem_erro()
         else:
            print(f"Seu saldo é de {saldo}")
         finally:
            print("Obrigado pro utilizar nossos serviços")
      
      elif opcao == 5:
         conta_alvo = input("Num: ")
         try:
            sisbanco.render_juros(conta_alvo)
         except CIException as cie:
            cie.print_mensagem_erro()
         except TJIException as tji:
            tji.print_mensagem_erro()
         else:
            print("Render Juros realizado com sucesso!")
         finally:
            print("Obrigado pro utilizar nossos serviços")

      elif opcao == 6:
         conta_alvo = input("Num: ")
         try:
            sisbanco.render_bonus(conta_alvo)
         except CIException as cie:
            cie.print_mensagem_erro()
         else:
            print("Render Bônus realizado com sucesso!")
         finally:
            print("Obrigado pro utilizar nossos serviços")
      
      elif opcao == 7:
         taxa = float(input('Taxa: '))
         sisbanco.set_taxa_poupanca(taxa)

      elif opcao == 8:
         taxa = float(input('Taxa: '))
         sisbanco.set_taxa_imposto(taxa)
         
      elif opcao == 9:
         print("SisBanco::Bye!")
         break

if __name__ == "__main__":
   terminal()