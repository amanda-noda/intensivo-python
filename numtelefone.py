import random

def gerar_telefone():
    # Lista de DDDs e operadoras
    ddds = [11, 21, 31, 41, 51, 61, 71, 81, 91]  # Exemplos de DDDs
    operadoras = ['Vivo', 'Claro', 'TIM', 'Oi', 'Nextel']

    # Escolhe um DDD aleatório
    ddd = random.choice(ddds)
    
    # Gera um número de telefone no formato (DDD) 9XXXX-XXXX
    numero = f"({ddd}) 9{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
    
    # Escolhe uma operadora aleatória
    operadora = random.choice(operadoras)

    return numero, operadora

# Gera e imprime 5 números de telefone
for _ in range(5):
    telefone, operadora = gerar_telefone()
    print(f"Número: {telefone}, Operadora: {operadora}")
