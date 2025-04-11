# 🎧 Spotify Data Analysis

Projeto de Engenharia de Dados com foco em análise de tendências musicais e sistema de recomendação personalizada usando a API do Spotify.

## 🔍 Objetivo

Extrair, transformar e analisar dados do Spotify para entender tendências musicais globais e sugerir músicas com base no gosto pessoal do usuário.

## 🚀 Tecnologias

- Python + Spotipy
- Pandas
- PostgreSQL (Docker)
- Power BI
- Docker Compose

## 🧱 Estrutura do Projeto

- Coleta de dados via Spotify Web API
- Armazenamento em banco PostgreSQL
- Visualizações com Power BI
- Sistema de recomendação com base nos artistas favoritos

## 🖼️ Exemplo de Dashboard

*(inserir print do Power BI aqui depois)*

## 📦 Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/AlanBReis/spotify-data-analysis.git

# Suba o banco de dados
docker-compose up -d

# Configure o .env com suas credenciais da API do Spotify
cp .env.example .env

# Instale as dependências
pip install -r requirements.txt

# Execute o ETL
python src/etl/fetch_trends.py
```

## 📊 Próximos passos
Adicionar clusterização por gênero

Melhorar motor de recomendação com features de áudio


Desenvolvido por Alan Reis 

