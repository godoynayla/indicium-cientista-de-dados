import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from joblib import dump

# Carregar dados
data = pd.read_csv('desafio_indicium_imdb.csv')

# Pré-processamento
data['Gross'] = data['Gross'].str.replace(',', '').astype(float)
data['Runtime'] = data['Runtime'].str.replace(' min', '').astype(int)

# Remover colunas desnecessárias
X = data.drop(['Series_Title', 'Overview', 'IMDB_Rating'], axis=1)
y = data['IMDB_Rating']

# Codificar colunas categóricas usando get_dummies
X = pd.get_dummies(X, columns=['Genre', 'Certificate', 'Director', 'Star1', 'Star2', 'Star3', 'Star4'])

# Divisão de Dados em Treino e Teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinamento do Modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Avaliação do Modelo
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Salvar o modelo treinado
model_path = 'model/imdb_model.joblib'
dump(model, model_path)

# Salvar as colunas do conjunto de treinamento
X_columns_path = 'model/X_columns.joblib'
dump(X.columns, X_columns_path)