import csv
import googlemaps
import time
from datetime import datetime


API_KEY = 'AIzaSyDR6HcEZLFikds2BANapGEAsCdg2MKQMVM'
gmaps = googlemaps.Client(key=API_KEY)


enderecos = []


with open('enderecos.csv', 'r', encoding='utf-8') as infile:
    leitor = csv.DictReader(infile)
    total = 0
    for linha in leitor:
        total += 1
        print(f"Processando linha {total}: {linha.get('endereco', 'sem endereço')}")
        endereco = linha.get('endereco')
        if not endereco:
            print(f"Endereço ausente na linha: {linha}")
            continue

        try:
            resultado = gmaps.geocode(endereco)
            if resultado:
                localizacao = resultado[0]['geometry']['location']
                latitude = localizacao['lat']
                longitude = localizacao['lng']
            else:
                latitude = longitude = None
        except Exception as e:
            print(f"Erro ao processar '{endereco}': {e}")
            latitude = longitude = None

        linha['latitude'] = latitude
        linha['longitude'] = longitude
        enderecos.append(linha)
        
        time.sleep(0.1)


campos = ['id', 'endereco', 'latitude', 'longitude']

# Gera timestamp no formato: 2025-07-08_10-42-30
agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nome_arquivo = f"enderecos_com_coordenadas_{agora}.csv"

with open(nome_arquivo, 'w', newline='', encoding='utf-8') as outfile:
    escritor = csv.DictWriter(outfile, fieldnames=campos)
    escritor.writeheader()
    for linha in enderecos:
        linha_filtrada = {k: linha.get(k, '') for k in campos}
        escritor.writerow(linha_filtrada)

print(f"Arquivo '{nome_arquivo}' criado com sucesso.")
