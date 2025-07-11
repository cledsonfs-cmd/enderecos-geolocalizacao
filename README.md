# Geolocalização por Endereço com Google Maps API

Esta aplicação em Python permite buscar a latitude e longitude de um endereço utilizando a [Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding).

## 🚀 Funcionalidades

- Busca de coordenadas geográficas (latitude e longitude) a partir de um endereço.
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

endereco = "Av. Paulista, 1000, São Paulo, SP"
resultado = gmaps.geocode(endereco)

if resultado:
    localizacao = resultado[0]['geometry']['location']
    print("Latitude:", localizacao['lat'])
    print("Longitude:", localizacao['lng'])
else:
    print("Endereço não encontrado.")
```

### 🖥️ Saída esperada:

```
Latitude: -23.5648575
Longitude: -46.6524022
```

## 📄 Licença

Este projeto está licenciado sob a licença MIT.

## 🙋‍♂️ Autor

[Cledson Francisco Silva](https://github.com/seu-usuario)

---

### ✅ TODO

- [ ] Adicionar tratamento de erros
- [ ] Suporte a múltiplos resultados
- [ ] Interface via linha de comando (CLI)