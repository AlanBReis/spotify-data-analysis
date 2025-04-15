import pandas as pd
import os

# Define o caminho para a raiz do projeto (sobe 2 níveis)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
INPUT_PATH = os.path.join(ROOT_DIR, "data", "processed", "playlist.csv")
OUTPUT_PATH = os.path.join(ROOT_DIR, "data", "processed", "playlist_transformed.csv")

def transformar_playlist(df):
    # Converte duração de ms para string no formato min:seg
    df['duration_min'] = df['duration_ms'].apply(lambda x: f"{x // 60000}:{(x % 60000) // 1000:02}")
    
    # Seleciona e reordena colunas
    df_transformado = df[['name', 'artist', 'album', 'popularity', 'duration_min', 'id']]

    return df_transformado

def main():
    try:
        df = pd.read_csv(INPUT_PATH)
        print(f"Lido com sucesso: {INPUT_PATH}")

        df_transformado = transformar_playlist(df)

        df_transformado.to_csv(OUTPUT_PATH, index=False)
        print(f"Transformação concluída. Arquivo salvo em: {OUTPUT_PATH}")

    except Exception as e:
        print(f"Erro na transformação: {e}")

if __name__ == "__main__":
    main()
