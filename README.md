#  Spotify Data Analysis

Projeto de Engenharia de Dados com foco em análise de tendências musicais e sistema de recomendação personalizada usando a API do Spotify.

##  Objetivo

Extrair, transformar e analisar dados do Spotify para entender tendências musicais globais e sugerir músicas com base no gosto pessoal do usuário.

##  Tecnologias

- Python + Spotipy
- Pandas
- PostgreSQL (Docker)
- Power BI
- Docker Compose

##  Estrutura do Projeto

- Coleta de dados via Spotify Web API
- Armazenamento em banco PostgreSQL
- Visualizações com Power BI
- Sistema de recomendação com base nos artistas favoritos

##  Exemplo de Dashboard

*(inserir print do Power BI aqui depois)*

##  Como rodar localmente


### Clone o repositório
```bash
git clone https://github.com/AlanBReis/spotify-data-analysis.git
```
### Suba o banco de dados
```bash
docker-compose up -d
```
### Configure o arquivo .env com suas credenciais da API do Spotify

Para que o script de coleta de dados possa interagir com a API do Spotify, você precisará criar um aplicativo no [Painel de Desenvolvedores Spotify](https://developer.spotify.com/dashboard). Após criar o aplicativo, você receberá um **Client ID** e um **Client Secret**.

Siga estas etapas para configurar o arquivo `.env` localmente:

1.  **Copie o arquivo de exemplo:** Execute o seguinte comando no terminal, na raiz do seu projeto:
    ```bash
    cp .env.example .env
    ```
    Este comando criará uma cópia do arquivo `.env.example` chamada `.env`. O arquivo `.env.example` já deve conter as variáveis esperadas (por exemplo, `SPOTIPY_CLIENT_ID=` e `SPOTIPY_CLIENT_SECRET=`).

2.  **Edite o arquivo `.env`:** Abra o arquivo `.env` com um editor de texto. Você precisará preencher os valores corretos para as seguintes variáveis, **substituindo o texto `SEU_CLIENT_ID` e `SEU_CLIENT_SECRET` pelos seus valores reais** obtidos no Painel de Desenvolvedores Spotify:

    ```
    SPOTIPY_CLIENT_ID=SEU_CLIENT_ID
    SPOTIPY_CLIENT_SECRET=SEU_CLIENT_SECRET
    SPOTIPY_REDIRECT_URI=http://localhost:8888/callback  # Ou a URI de redirecionamento que você configurou no painel
    ```

    **Importante:**

    * **Não compartilhe seu arquivo `.env` ou suas credenciais diretamente com outras pessoas.**
    * Certifique-se de que o arquivo `.env` esteja listado no seu arquivo `.gitignore` para evitar que suas informações confidenciais sejam enviadas para o repositório Git.

3.  **URI de Redirecionamento:** A `SPOTIPY_REDIRECT_URI` é a URI para a qual o Spotify redirecionará o usuário após a autenticação. Para desenvolvimento local, `http://localhost:8888/callback`


### Instale as dependências
```bash
pip install -r requirements.txt
```
### Execute o ETL
```bash
python src/etl/fetch_trends.py
```


![thumbnail](images/thumbnail-spotify-data-analysis.png)

_“Tendências musicais e recomendações personalizadas em um só projeto”_


Desenvolvido por - [Alan Reis](https://www.linkedin.com/in/alanbrreis/) 

## Licença

[MIT](https://choosealicense.com/licenses/mit/)


