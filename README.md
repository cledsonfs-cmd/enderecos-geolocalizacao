# Geolocalização por Endereço com Google Maps API

Esta aplicação em Python permite buscar a latitude e longitude de um endereço utilizando a [Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding).

## 🚀 Funcionalidades

- Busca de coordenadas geográficas (latitude e longitude) a partir de uma lista de endereço em um arquivo csv.
- Uso simples por linha de comando.
- Estrutura leve com virtualenv.

## 🛠️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -U googlemaps
```

## 🔑 Chave de API

Você precisa de uma chave válida da Google Maps API. Crie a sua em:  
https://console.cloud.google.com/

Substitua no código a variável `API_KEY` pelo valor da sua chave:

```python
API_KEY = "SUA_CHAVE_AQUI"
```

> ⚠️ **Atenção**: Não exponha sua chave pública em repositórios. Use variáveis de ambiente ou arquivos `.env` com a biblioteca `python-dotenv`.

## 📦 Exemplo de uso

```python
import googlemaps

API_KEY = "SUA_CHAVE_AQUI"  # Substitua aqui pela sua chave
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
```

### 🖥️ Saída esperada:

```
Latitude: -23.5648575
Longitude: -46.6524022
```

## 📄 Licença

Este projeto está licenciado sob a licença MIT.

## 🙋‍♂️ Autor

[Cledson Francisco Silva](https://www.cledsonfs.com.br/)

---

### ✅ TODO

- [ ] Adicionar tratamento de erros
- [ ] Suporte a múltiplos resultados
- [ ] Interface via linha de comando (CLI)