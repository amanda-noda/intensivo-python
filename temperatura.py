#Acesse OpenWeatherMap e crie uma conta.
#Após a criação da conta, obtenha uma chave de API (API key).
#instale pip install requests
#Substitua "SUA_CHAVE_DE_API_AQUI" pela sua chave de API obtida no OpenWeatherMap.
#Execute o código em um ambiente Python.
#Digite o nome da cidade quando solicitado.


import requests

def obter_temperatura(cidade, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric"
    
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        temperatura = dados['main']['temp']
        descricao = dados['weather'][0]['description']
        print(f"A temperatura atual em {cidade} é {temperatura}°C com {descricao}.")
    else:
        print("Erro ao obter os dados da temperatura. Verifique o nome da cidade ou a chave da API.")

def main():
    cidade = input("Digite o nome da cidade: ")
    api_key = "SUA_CHAVE_DE_API_AQUI"  # Substitua pela sua chave de API
    obter_temperatura(cidade, api_key)

if __name__ == "__main__":
    main()