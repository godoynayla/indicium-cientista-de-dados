
# Análise de Filmes: Predição de Avaliação IMDb e Faturamento

Este projeto visa explorar e prever a avaliação IMDb e o faturamento de filmes com base em diversas variáveis. Utilizamos técnicas de análise de dados e machine learning para extrair insights e construir modelos preditivos.

## Visão Geral

O objetivo deste projeto é entender os fatores que contribuem para o sucesso de um filme em termos de avaliação crítica (IMDb) e faturamento. Vamos explorar os dados disponíveis, realizar uma análise exploratória (EDA) e desenvolver modelos de machine learning para prever a pontuação IMDb de filmes com base em características como diretor, elenco, gênero, pontuação crítica, entre outros.

## Pré-requisitos

Certifique-se de ter Python 3 instalado, juntamente com as bibliotecas necessárias listadas no `requirements.txt`. Você pode instalá-las executando:

```
pip install -r requirements.txt
```

## Como instalar e executar o projeto

Passo 1: Crie um diretório local em sua máquina onde você deseja baixar o projeto Git e clone o projeto executando o comando abaixo no terminal (Certifique-se de estar no diretório recém-criado antes!):

```
git clone https://github.com/godoynayla/indicium-cientista-de-dados.git
```

Passo 2: No terminal, navegue até a pasta principal do projeto clonado:

```
cd IMDB_Data_Science_Project_Python
```

Passo 3: Execute os comandos abaixo para atender aos pré-requisitos para executar o código:

- Unix/macOS
  ```
  python -m pip install -r requirements.txt
  ```

- Windows
  ```
  py -m pip install -r requirements.txt
  ```

Passo 4: Execute os comandos abaixo para rodar o código a partir do terminal:

- Unix/macOS
  ```
  python main.py
  ```

- Windows
  ```
  %run main.py
  ```

Isso deve configurar o ambiente necessário e executar o código do projeto corretamente.

## Estrutura do Projeto

- `Data.Files/`: Pasta contendo os dados do projeto.
- `README.md`: Documentação do projeto.

## Execução

Para executar a análise de dados e os modelos:

1. **Análise Exploratória de Dados (EDA)**:
   - Execute os notebooks em `notebooks/` para explorar os dados e identificar insights preliminares.

2. **Treinamento do Modelo**:
   - Utilize o script `train_model.py` para treinar modelos de regressão para prever a pontuação IMDb.

3. **Avaliação do Modelo**:
   - Avalie o desempenho do modelo utilizando métricas como MSE (Mean Squared Error) ou RMSE (Root Mean Squared Error).

4. **Previsão**:
   - Use o modelo treinado para prever a pontuação IMDb de novos filmes com base em suas características.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) e enviar pull requests com melhorias ou novas funcionalidades.

## Autores

- Nayla Maria Silva de Godoy

## Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
