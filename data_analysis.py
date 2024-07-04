import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def data_analysis():
    k = pd.read_csv('Data_Files/desafio_indicium_imdb.csv')

    # Quantidade de títulos por letra inicial
    alphabet_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alphabet_count = [k[k['Title'].str.startswith(letter)].shape[0] for letter in alphabet_list]
    starting_with_numbers = k.shape[0] - sum(alphabet_count)
    alphabet_count.append(starting_with_numbers)
    alphabet_list.append('Numerals')
    
    title_and_count = pd.DataFrame({'Alphabet': alphabet_list, 'Count': alphabet_count})
    title_and_count['Proportion'] = title_and_count['Count'] / title_and_count['Count'].sum() * 100
    
    # Gráfico de barras para quantidade de títulos por letra inicial
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.bar(title_and_count['Alphabet'], title_and_count['Count'])
    ax.grid(True, color='grey', linestyle='-', linewidth=0.3)
    ax.set_title('Count of Movies by Initial Character')
    plt.xlabel('Initial Character of Movie Title')
    plt.ylabel('Frequency of Usage')
    plt.show()
    
    # Filmes com mais de 7500 votos e classificação acima de 6
    movies_with_more_than_10k_votes = k[(k['Votes'] > 7500) & (k['User Rating'] > 6)]
    
    # Contagem de filmes por ano
    year_wise_movie_count = movies_with_more_than_10k_votes.groupby('Release Year').size().reset_index(name='Count')
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.bar(year_wise_movie_count['Release Year'], year_wise_movie_count['Count'])
    ax.grid(True, color='grey', linestyle='-', linewidth=0.3)
    ax.set_title('Count of Movies by Release Year')
    plt.xlabel('Year')
    plt.ylabel('Movie Count')
    plt.show()
    
    # Duração média dos filmes por ano
    year_wise_runtime = movies_with_more_than_10k_votes.groupby('Release Year')['Duration(Min.)'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.bar(year_wise_runtime['Release Year'], year_wise_runtime['Duration(Min.)'])
    ax.grid(True, color='grey', linestyle='-', linewidth=0.3)
    ax.set_title('Average Runtime of Movies by Year')
    plt.xlabel('Year')
    plt.ylabel('Average Runtime (minutes)')
    plt.show()
    
    # Proporção de filmes por gênero e ano
    year_genre_count = movies_with_more_than_10k_votes.groupby(['Release Year', 'Genre']).size().unstack().fillna(0)
    year_genre_count.plot(kind='bar', stacked=True, figsize=(10, 10))
    plt.title('Proportion of Movies by Genre and Year')
    plt.xlabel('Year')
    plt.ylabel('Movie Count')
    plt.show()
    
    # Votos por ano
    year_wise_votes = movies_with_more_than_10k_votes.groupby('Release Year')['Votes'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.bar(year_wise_votes['Release Year'], year_wise_votes['Votes'])
    ax.grid(True, color='grey', linestyle='-', linewidth=0.3)
    ax.set_title('User Votes by Release Year')
    plt.xlabel('Year')
    plt.ylabel('Total User Votes')
    plt.show()
    
    # Filme mais bem avaliado por ano
    year_top_movies = movies_with_more_than_10k_votes.sort_values(by=['Release Year', 'User Rating'], ascending=[True, False]).drop_duplicates('Release Year')
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.bar(year_top_movies['Release Year'], year_top_movies['User Rating'])
    ax.grid(True, color='grey', linestyle='-', linewidth=0.3)
    ax.set_title('Highest Rated Movie by Year')
    plt.xlabel('Year')
    plt.ylabel('User Rating')
    plt.show()
    
    # Proporção de filmes por gênero
    genre_counts = movies_with_more_than_10k_votes['Genre'].value_counts(normalize=True) * 100
    fig, ax = plt.subplots()
    ax.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Proportion of Movies by Genre')
    plt.show()
    
    # Ator principal mais bem sucedido (pelo menos 30 filmes)
    actor1_movies = k['Actor #1'].value_counts()
    top_actors = actor1_movies[actor1_movies > 30].index
    top_actors_ratings = k[k['Actor #1'].isin(top_actors)].groupby('Actor #1')['User Rating'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.barh(top_actors_ratings.index, top_actors_ratings.values, color='crimson')
    ax.invert_yaxis()
    ax.grid(True, color='grey', linestyle='-', linewidth=0.3)
    ax.set_title('Most Successful Actor (at least 30 movies)')
    plt.xlabel('Average User Rating')
    plt.show()
    
    # Adicionar coluna de década
    movies_with_more_than_10k_votes['Decade'] = (movies_with_more_than_10k_votes['Release Year'] // 10 * 10).astype(str) + 's'
    
    # Contagem de filmes por década
    decade_counts = movies_with_more_than_10k_votes['Decade'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.bar(decade_counts.index, decade_counts.values)
    ax.grid(True, color='grey', linestyle='-', linewidth=0.3)
    ax.set_title('Count of Movies by Decade')
    plt.xlabel('Decade')
    plt.ylabel('Movie Count')
    plt.show()
    
    # Ator coadjuvante mais bem sucedido (pelo menos 15 filmes)
    actor2_movies = k['Actor #2'].value_counts()
    top_supporting_actors = actor2_movies[actor2_movies > 15].index
    top_supporting_actors_ratings = k[k['Actor #2'].isin(top_supporting_actors)].groupby('Actor #2')['User Rating'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.barh(top_supporting_actors_ratings.index, top_supporting_actors_ratings.values, color='crimson')
    ax.invert_yaxis()
    ax.grid(True, color='grey', linestyle='-', linewidth=0.3)
    ax.set_title('Most Successful Supporting Actor (at least 15 movies)')
    plt.xlabel('Average User Rating')
    plt.show()
    
    # Diretor mais bem sucedido (pelo menos 20 filmes)
    director_movies = k['Director'].value_counts()
    top_directors = director_movies[director_movies > 20].index
    top_directors_ratings = k[k['Director'].isin(top_directors)].groupby('Director')['User Rating'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.barh(top_directors_ratings.index, top_directors_ratings.values, color='crimson')
    ax.invert_yaxis()
    ax.grid(True, color='grey', linestyle='-', linewidth=0.3)
    ax.set_title('Most Successful Director (at least 20 movies)')
    plt.xlabel('Average User Rating')
    plt.show()
    
    # Popularidade dos gêneros ao longo do tempo
    genre_year_counts = k.groupby(['Genre', 'Release Year']).size().unstack().fillna(0)
    fig, axs = plt.subplots(3, 4, figsize=(15, 15))
    fig.suptitle('Popularity of Different Genres from 1915 to 2020')
    genres = genre_year_counts.index
    for i, genre in enumerate(genres):
        row, col = divmod(i, 4)
        axs[row, col].stem(genre_year_counts.columns, genre_year_counts.loc[genre])
        axs[row, col].set_title(genre + ' Genre')
    plt.tight_layout()
    plt.show()

# Executar a análise de dados
data_analysis()