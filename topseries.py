# instale: pip install IMDbPY


from imdb import IMDb

def obter_series_mais_assistidas():
    ia = IMDb()
    
    # Obtendo as séries mais assistidas
    series = ia.get_top250_tv()
    
    print("As 10 séries mais assistidas de todos os tempos:")
    print(f"{'Rank':<5} {'Título':<50} {'Ano':<5} {'Nota':<5}")
    print("-" * 70)
    
    for rank, serie in enumerate(series[:10], start=1):
        titulo = serie['title']
        ano = serie['year']
        nota = serie['rating']
        print(f"{rank:<5} {titulo:<50} {ano:<5} {nota:<5}")

def main():
    obter_series_mais_assistidas()

if __name__ == "__main__":
    main()
