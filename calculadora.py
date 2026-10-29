# =========================================================
# CALCULADORA BÁSICA EM PYTHON
# Operações: Adição, Subtração, Multiplicação e Divisão
# =========================================================

# 1. Definição das Funções Matemáticas
def adicao(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtracao(a, b):
    """Retorna a subtração entre dois números."""
    return a - b

def multiplicacao(a, b):
    """Retorna o produto de dois números."""
    return a * b

def divisao(a, b):
    """Retorna o quociente ou mensagem se dividir por zero."""
    if b == 0:
        return "Erro: Não é possível dividir por zero!"
    return a / b

# 2. Exibição do Menu para o Usuário
print("=" * 35) #repete o caractere "=" 35 vezes para criar uma linha de separação
print("     CALCULADORA EM PYTHON")
print("=" * 35)
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
print("=" * 35)

# 3. Leitura da Operação Desejada
opcao = input("Escolha a operação (1/2/3/4): ")

# 4. Verificação da Opção e Execução
if opcao in ['1', '2', '3', '4']:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == '1':
        resultado = adicao(num1, num2)
        print(f"\nResultado: {num1} + {num2} = {resultado}")
    elif opcao == '2':
        resultado = subtracao(num1, num2)
        print(f"\nResultado: {num1} - {num2} = {resultado}")
    elif opcao == '3':
        resultado = multiplicacao(num1, num2)
        print(f"\nResultado: {num1} * {num2} = {resultado}")
    elif opcao == '4':
        resultado = divisao(num1, num2)
        print(f"\nResultado: {num1} / {num2} = {resultado}")
else:
    print("\nOpção inválida! Escolha um número de 1 a 4.")
