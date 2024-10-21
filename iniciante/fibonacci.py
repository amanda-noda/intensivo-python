Copiar
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Entrada do usuário
num_terms = int(input("Digite o número de termos da sequência de Fibonacci: "))

# Cálculo da sequência
resultado = fibonacci(num_terms)

# Exibição do resultado
print(f"A sequência de Fibonacci até {num_terms} termos é: {resultado}")