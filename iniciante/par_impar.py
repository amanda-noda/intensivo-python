# Função para verificar se o número é par ou ímpar
def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Entrada do usuário
numero = int(input("Digite um número: "))

# Verificação e exibição do resultado
resultado = verificar_par_impar(numero)
print(f"O número {numero} é {resultado}.")