menu = """
[d] = Depósito
[s] = Saque
[e] = Extrato
[q] = Quit

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQES = 3

while True:

    opcao = input(menu)

    if opcao == "q":
        break

    elif opcao == "d":
        val = float(input("Digite o valor do depósito."))
        if val >= 0.01:
            saldo += val
            extrato += f"Depósito: R$ {val:.2f}.\n"
            print(f"valor de R$ {val:.2f} depositado com sucesso.")
        else:
            print("O valor do depósito deve ser maior do que 0.")

    elif opcao == "s":
        numero_saques += 1
        if numero_saques < LIMITE_SAQES:
            saque_val = float(input("Digite o valor do saque."))
            if saque_val < saldo:
                if saque_val > limite:
                    print(f"Limite de {limite:.2f} ultrapassado, tente realizar um saque com um valor abaixo do limite.")
                else:
                    saldo -= saque_val
                    extrato += f"Saque: (-) R$ {val:.2f}.\n"
                    print(f"Saque de R$ {saque_val:.2f} realizado com sucesso.")
            else:
                print(f"Saldo insuficiente.")
        else:
                print(f"O limite de saque foi atendido, tente novamente quando o limite for zerado.")
            
    elif opcao == "e":
        print(f"extrato:\n{extrato}")
        
    else:
        print("Opção inválida, por favor, digitar alguma das opções presentes no menu.")
