# Calculadora Python

Este projeto é uma calculadora simples desenvolvida em Python.

## Como Executar

### Executar diretamente:
1. Certifique-se de que tem Python instalado na sua máquina.
2. No terminal, navegue até o diretório do script e execute:

```bash
python3 calculadora.py

# Certifique-se de que o arquivo .sh tenha permissão de execução.
Se ainda não fez isso, execute o seguinte comando no terminal:

chmod +x executar_calculadora.sh


# No terminal, navegue até o diretório onde o arquivo executar_calculadora.sh está localizado.
Por exemplo: 

cd /caminho/para/sua/calculadora


# Execute o script usando o seguinte comando:


./executar_calculadora.sh


#explicação do Código
O script calculadora.py contém funções básicas de operações matemáticas. Aqui está uma visão geral das principais funções:

#Função de Soma A função somar(a, b) recebe dois números a e b como parâmetros e retorna a soma deles.

def somar(a, b):
    return a + b

#Função de Subtração A função subtrair(a, b) recebe dois números a e b e retorna a diferença entre eles.

def subtrair(a, b):
    return a - b

#Função de Multiplicação A função multiplicar(a, b) recebe dois números e retorna o produto deles.

def multiplicar(a, b):
    return a * b

#Função de Divisão A função dividir(a, b) recebe dois números e retorna o quociente.
Inclui uma verificação para evitar divisão por zero.

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

#Exemplo de Uso O script pode ser executado em um loop para permitir que o usuário escolha uma operação e insira os números a serem utilizados.
Aqui está um exemplo simplificado:

while True:
    print("Escolha a operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

    escolha = input("Digite sua escolha (1/2/3/4/5): ")

    if escolha == '5':
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado:", somar(num1, num2))
    elif escolha == '2':
        print("Resultado:", subtrair(num1, num2))
    elif escolha == '3':
        print("Resultado:", multiplicar(num1, num2))
    elif escolha == '4':
        print("Resultado:", dividir(num1, num2))
    else:
        print("Opção inválida!")


