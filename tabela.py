# Função para adicionar contatos e listar em ordem alfabética
def adicionar_contato(contatos):
    while True:
        nome = input("Digite o nome: ")
        telefone = input("Digite o número de telefone: ")
        endereco = input("Digite o endereço: ")
        email = input("Digite o e-mail: ")

        # Adiciona o contato a lista
        contatos.append({
            'nome': nome,
            'telefone': telefone,
            'endereco': endereco,
            'email': email
        })

        continuar = input("Deseja adicionar outro contato? (s/n): ")
        if continuar.lower() != 's':
            break

    # Ordena os contatos por nome
    contatos.sort(key=lambda x: x['nome'])

    # Exibe a tabela
    print("\nTabela de Contatos:")
    print(f"{'Nome':<20} {'Telefone':<15} {'Endereço':<30} {'Email':<25}")
    print("-" * 90)
    for contato in contatos:
        print(f"{contato['nome']:<20} {contato['telefone']:<15} {contato['endereco']:<30} {contato['email']:<25}")

# Lista para armazenar os contatos
contatos = []

# Chamada da função
adicionar_contato(contatos)