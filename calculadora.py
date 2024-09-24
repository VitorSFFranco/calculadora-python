#!/usr/bin/env python3

# Função para exibir o menu de operações
def exibir_menu():
    print("\nEscolha a operação que deseja realizar:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

# Loop principal
while True:
    # Recebendo os números do usuário e convertendo para float
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Exibindo o menu e solicitando a escolha
    exibir_menu()
    escolha = input("Digite o número da operação: ")

    # Condicional para realizar a operação escolhida
    if escolha == '1':
        resultado = num1 + num2
        print(f"\nResultado da adição: {resultado}")

    elif escolha == '2':
        resultado = num1 - num2
        print(f"\nResultado da subtração: {resultado}")

    elif escolha == '3':
        resultado = num1 * num2
        print(f"\nResultado da multiplicação: {resultado}")

    elif escolha == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"\nResultado da divisão: {resultado}")
        else:
            print("\nErro: divisão por zero não é permitida.")

    elif escolha == '5':
        print("\nEncerrando o programa. Até logo!")
        break

    else:
        print("\nOpção inválida, tente novamente.")

    # Perguntando se o usuário quer continuar
    continuar = input("\nDeseja realizar outra operação? (s/n): ")
    if continuar.lower() != 's':
        print("\nEncerrando o programa. Até logo!")
        break
