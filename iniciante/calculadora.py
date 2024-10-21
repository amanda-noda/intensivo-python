import sympy as sp

def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Fatorial")
        print("6. Derivada")
        print("7. Limite")
        print("8. Integral")
        print("9. Sair")

        escolha = input("Digite a opção (1-9): ")

        if escolha == '1':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print(f"{a} + {b} = {a + b}")

        elif escolha == '2':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print(f"{a} - {b} = {a - b}")

        elif escolha == '3':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print(f"{a} * {b} = {a * b}")

        elif escolha == '4':
            a = float(input("Digite o numerador: "))
            b = float(input("Digite o denominador: "))
            if b != 0:
                print(f"{a} / {b} = {a / b}")
            else:
                print("Erro: Divisão por zero.")

        elif escolha == '5':
            n = int(input("Digite um número inteiro: "))
            if n >= 0:
                print(f"{n}! = {sp.factorial(n)}")
            else:
                print("Erro: Fatorial somente para números inteiros não negativos.")

        elif escolha == '6':
            x = sp.symbols('x')
            funcao = input("Digite a função (ex: x**2 + 3*x + 2): ")
            derivada = sp.diff(funcao, x)
            print(f"A derivada de {funcao} é: {derivada}")

        elif escolha == '7':
            x = sp.symbols('x')
            funcao = input("Digite a função (ex: x**2 + 3*x + 2): ")
            ponto = float(input("Digite o ponto para calcular o limite: "))
            limite = sp.limit(funcao, x, ponto)
            print(f"O limite de {funcao} quando x se aproxima de {ponto} é: {limite}")

        elif escolha == '8':
            x = sp.symbols('x')
            funcao = input("Digite a função (ex: x**2 + 3*x + 2): ")
            integral = sp.integrate(funcao, x)
            print(f"A integral de {funcao} é: {integral}")

        elif escolha == '9':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Chamada da função da calculadora
calculadora()