# instale: pip install requests


import requests

def buscar_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        nome = dados['name'].capitalize()
        altura = dados['height']
        peso = dados['weight']
        tipos = [tipo['type']['name'] for tipo in dados['types']]
        
        print(f"Nome: {nome}")
        print(f"Altura: {altura / 10} m")  # altura em metros
        print(f"Peso: {peso / 10} kg")      # peso em kg
        print(f"Tipos: {', '.join(tipos)}")
    else:
        print("Pokémon não encontrado. Verifique o nome e tente novamente.")

def main():
    print("Bem-vindo à Pokédex!")
    while True:
        nome_pokemon = input("Digite o nome do Pokémon (ou 'sair' para encerrar): ")
        if nome_pokemon.lower() == 'sair':
            break
        buscar_pokemon(nome_pokemon)

if __name__ == "__main__":
    main()