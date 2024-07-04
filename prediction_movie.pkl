
import os
from joblib import dump

# Criar diretório
os.makedirs('model', exist_ok=True)

# Salvar o modelo treinado
model_path = 'model/imdb_model.joblib'
dump(model, model_path)

# Salvar as colunas do conjunto de treinamento
X_columns_path = 'model/X_columns.joblib'
dump(X.columns, X_columns_path)

import pandas as pd
from joblib import load

# Função para carregar o modelo
def load_model(model_path):
    return load(model_path)

# Função para pré-processar os dados do novo filme
def preprocess_new_movie(new_movie):
    # Convertendo para DataFrame
    new_movie_df = pd.DataFrame([new_movie])

    # Removendo colunas desnecessárias
    new_movie_df = new_movie_df.drop(['Series_Title', 'Overview'], axis=1)

    # Convertendo 'Gross' para numérico
    new_movie_df['Gross'] = new_movie_df['Gross'].str.replace(',', '').astype(float)

    # Convertendo 'Runtime' para minutos inteiros
    new_movie_df['Runtime'] = new_movie_df['Runtime'].str.replace(' min', '').astype(int)

    # Codificar colunas categóricas usando get_dummies
    new_movie_df = pd.get_dummies(new_movie_df, columns=['Genre', 'Certificate', 'Director', 'Star1', 'Star2', 'Star3', 'Star4'])

    return new_movie_df

# Função para assegurar que todas as colunas presentes no conjunto de treinamento estão presentes no novo filme
def align_columns(new_movie_df, X_columns):
    missing_cols = set(X_columns) - set(new_movie_df.columns)
    for col in missing_cols:
        new_movie_df[col] = 0

    # Reordenando as colunas para garantir que a ordem seja a mesma
    new_movie_df = new_movie_df[X_columns]
    
    return new_movie_df

# Função para fazer a previsão
def predict_imdb(model, new_movie_df):
    return model.predict(new_movie_df)

# Carregar o modelo
model_path = 'model/imdb_model.joblib'
model = load_model(model_path)

# Dados do novo filme
new_movie = {
    'Series_Title': 'The Shawshank Redemption',
    'Released_Year': '1994',
    'Certificate': 'A',
    'Runtime': '142 min',
    'Genre': 'Drama',
    'Meta_score': 80.0,
    'Director': 'Frank Darabont',
    'Star1': 'Tim Robbins',
    'Star2': 'Morgan Freeman',
    'Star3': 'Bob Gunton',
    'Star4': 'William Sadler',
    'No_of_Votes': 2343110,
    'Gross': '28,341,469'
}

# Pré-processar os dados do novo filme
new_movie_df = preprocess_new_movie(new_movie)

# Carregar as colunas do conjunto de treinamento
X_columns = load('model/X_columns.joblib')

# Alinhar as colunas do novo filme com as do conjunto de treinamento
new_movie_df = align_columns(new_movie_df, X_columns)

# Fazer a previsão
imdb_prediction = predict_imdb(model, new_movie_df)

# Exibir a previsão
print(f"A previsão da nota do IMDb para 'The Shawshank Redemption' é: {imdb_prediction[0]}")
