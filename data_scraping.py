import bs4
import pandas as pd
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import itertools


# Função para extrair dados do imdb.com para as respectivas colunas de acordo com o gênero
def scrape(links, ranking, names, release_year, duration, subgenres, user_rating, directors_and_actors, votes):
    for x in links:  # Ler todos os links disponíveis de um arquivo de gênero específico
        url = x
        if url == '':
            exit()
        else:
            uClient = uReq(url)
            page_html = uClient.read()  
            uClient.close()
            page_soup = soup(page_html, "html.parser")  
            movie_info = page_soup.findAll("div", {
                "class": "lister-item-content"})  # Encontre tags específicas relacionadas à classificação e ao título do filme
            for container in movie_info:
                ranking.append(container.span.getText())  # Estabelecer ranking de filmes
                names.append(container.a.getText())  # Estabelecer titulo de filmes

            release_year_info = page_soup.findAll('span',
                                                  class_='lister-item-year text-muted unbold')  # Busca tags de acordo com o ano de lancamento
            for container in release_year_info:
                release_year.append(container.getText())  # Estabelecer ano de lancamento do filme

            """
            movie_certificate = page_soup.findAll('span', class_='certificate') 
            for container in movie_certificate:
                action_movie_certificate.append(container.getText())
            """
            movie_duration = page_soup.findAll('span',
                                               class_='runtime')  
            for container in movie_duration:
                duration.append(container.getText())  

            movie_subgenre = page_soup.findAll('span',
                                               class_='genre')  
            for container in movie_subgenre:
                subgenres.append(container.getText())  

            movie_rating = page_soup.findAll('div',
                                             class_='inline-block ratings-imdb-rating') 
            for container in movie_rating:
                user_rating.append(container['data-value']) 

            """
            movie_metascore = page_soup.findAll('span', class_='metascore favorable')
            for container in movie_metascore:
                action_movie_meta_score.append(container.getText())

            movie_synopsis = page_soup.findAll('p', class_='text-muted')
            for container in movie_synopsis:
                action_movie_synopsis.append(container.getText())
            """

            movie_directors_and_actors = page_soup.findAll('p',
                                                           class_="") 
            for container in movie_directors_and_actors:
                directors_and_actors.append(container.getText())  

            movie_votes = page_soup.find_all('span', attrs={
                'name': 'nv'})
            for i in range(0, len(movie_votes)):
                vote = movie_votes[i].getText()
                if vote != '':
                    votes.append(vote)  
                else:
                    votes.append('Not available')

                for i in range(0, len(votes)):
                    if votes[i].startswith('$'):
                        votes.pop(i)  

def links_reading_and_dataframe_setup():

    action_url = open("Links\\Action.txt", "r")
    action_links = action_url.readlines()

    animation_url = open("Links\\Animation(503).txt", "r")
    animation_links = animation_url.readlines()

    biography_url = open("Links\\Biography(775).txt", "r")
    biography_links = biography_url.readlines()

    comedy_url = open("Links\\Comedy.txt", "r")
    comedy_links = comedy_url.readlines()

    crime_url = open("Links\\Crime.txt", "r")
    crime_links = crime_url.readlines()

    drama_url = open("Links\\Drama.txt", "r")
    drama_links = drama_url.readlines()

    fantasy_url = open("Links\\Fantasy.txt", "r")
    fantasy_links = fantasy_url.readlines()

    horror_url = open("Links\\Horror.txt", "r")
    horror_links = horror_url.readlines()

    mystery_url = open("Links\\Mystery.txt", "r")
    mystery_links = mystery_url.readlines()

    romance_url = open("Links\\Romance.txt", "r")
    romance_links = romance_url.readlines()

    scifi_url = open("Links\\Sci-fi.txt", "r")
    scifi_links = scifi_url.readlines()

    thriller_url = open("Links\\Thriller.txt", "r")
    thriller_links = thriller_url.readlines()

    war_url = open("Links\\War (640+).txt", "r")
    war_links = war_url.readlines()

    # Action
    url = ''
    action_movie_ranking = list()
    action_movie_names = list()
    action_movie_release_year = list()
    # action_movie_certificate=list()
    action_movie_duration = list()
    action_movie_subgenres = list()
    action_movie_user_rating = list()
    # action_movie_meta_score=list()
    # action_movie_synopsis=list()
    action_movie_directors_and_actors = list()
    action_movie_votes = list()

    # Animation
    animation_movie_ranking = list()
    animation_movie_names = list()
    animation_movie_release_year = list()
    # animation_movie_certificate=list()
    animation_movie_duration = list()
    animation_movie_subgenres = list()
    animation_movie_user_rating = list()
    # animation_movie_meta_score=list()
    # animation_movie_synopsis=list()
    animation_movie_directors_and_actors = list()
    animation_movie_votes = list()

    # Biography
    biography_movie_ranking = list()
    biography_movie_names = list()
    biography_movie_release_year = list()
    # biography_movie_certificate=list()
    biography_movie_duration = list()
    biography_movie_subgenres = list()
    biography_movie_user_rating = list()
    # biography_movie_meta_score=list()
    # biography_movie_synopsis=list()
    biography_movie_directors_and_actors = list()
    biography_movie_votes = list()

    # Comedy
    comedy_movie_ranking = list()
    comedy_movie_names = list()
    comedy_movie_release_year = list()
    # comedy_movie_certificate=list()
    comedy_movie_duration = list()
    comedy_movie_subgenres = list()
    comedy_movie_user_rating = list()
    # comedy_movie_meta_score=list()
    # comedy_movie_synopsis=list()
    comedy_movie_directors_and_actors = list()
    comedy_movie_votes = list()

    # Crime
    crime_movie_ranking = list()
    crime_movie_names = list()
    crime_movie_release_year = list()
    # crime_movie_certificate=list()
    crime_movie_duration = list()
    crime_movie_subgenres = list()
    crime_movie_user_rating = list()
    # crime_movie_meta_score=list()
    # crime_movie_synopsis=list()
    crime_movie_directors_and_actors = list()
    crime_movie_votes = list()

    # Drama
    drama_movie_ranking = list()
    drama_movie_names = list()
    drama_movie_release_year = list()
    # drama_movie_certificate=list()
    drama_movie_duration = list()
    drama_movie_subgenres = list()
    drama_movie_user_rating = list()
    # drama_movie_meta_score=list()
    # drama_movie_synopsis=list()
    drama_movie_directors_and_actors = list()
    drama_movie_votes = list()

    # Fantasy
    fantasy_movie_ranking = list()
    fantasy_movie_names = list()
    fantasy_movie_release_year = list()
    # fantasy_movie_certificate=list()
    fantasy_movie_duration = list()
    fantasy_movie_subgenres = list()
    fantasy_movie_user_rating = list()
    # fantasy_movie_meta_score=list()
    # fantasy_movie_synopsis=list()
    fantasy_movie_directors_and_actors = list()
    fantasy_movie_votes = list()

    # Horror
    horror_movie_ranking = list()
    horror_movie_names = list()
    horror_movie_release_year = list()
    # horror_movie_certificate=list()
    horror_movie_duration = list()
    horror_movie_subgenres = list()
    horror_movie_user_rating = list()
    # horror_movie_meta_score=list()
    # horror_movie_synopsis=list()
    horror_movie_directors_and_actors = list()
    horror_movie_votes = list()

    # Mystery
    mystery_movie_ranking = list()
    mystery_movie_names = list()
    mystery_movie_release_year = list()
    # mystery_movie_certificate=list()
    mystery_movie_duration = list()
    mystery_movie_subgenres = list()
    mystery_movie_user_rating = list()
    # mystery_movie_meta_score=list()
    # mystery_movie_synopsis=list()
    mystery_movie_directors_and_actors = list()
    mystery_movie_votes = list()

    # Romance
    romance_movie_ranking = list()
    romance_movie_names = list()
    romance_movie_release_year = list()
    # romance_movie_certificate=list()
    romance_movie_duration = list()
    romance_movie_subgenres = list()
    romance_movie_user_rating = list()
    # romance_movie_meta_score=list()
    # romance_movie_synopsis=list()
    romance_movie_directors_and_actors = list()
    romance_movie_votes = list()

    # Sci-fi
    scifi_movie_ranking = list()
    scifi_movie_names = list()
    scifi_movie_release_year = list()
    # scifi_movie_certificate=list()
    scifi_movie_duration = list()
    scifi_movie_subgenres = list()
    scifi_movie_user_rating = list()
    # scifi_movie_meta_score=list()
    # scifi_movie_synopsis=list()
    scifi_movie_directors_and_actors = list()
    scifi_movie_votes = list()

    # Thriller
    thriller_movie_ranking = list()
    thriller_movie_names = list()
    thriller_movie_release_year = list()
    # thriller_movie_certificate=list()
    thriller_movie_duration = list()
    thriller_movie_subgenres = list()
    thriller_movie_user_rating = list()
    # thriller_movie_meta_score=list()
    # thriller_movie_synopsis=list()
    thriller_movie_directors_and_actors = list()
    thriller_movie_votes = list()

    # War genre column headings
    war_movie_ranking = list()
    war_movie_names = list()
    war_movie_release_year = list()
    # war_movie_certificate=list()
    war_movie_duration = list()
    war_movie_subgenres = list()
    war_movie_user_rating = list()
    # war_movie_meta_score=list()
    # war_movie_synopsis=list()
    war_movie_directors_and_actors = list()
    war_movie_votes = list()


    # Chama funcao scrape
    scrape(action_links, action_movie_ranking, action_movie_names, action_movie_release_year, action_movie_duration,
           action_movie_subgenres, action_movie_user_rating, action_movie_directors_and_actors, action_movie_votes)
    scrape(animation_links, animation_movie_ranking, animation_movie_names, animation_movie_release_year,
           animation_movie_duration, animation_movie_subgenres, animation_movie_user_rating,
           animation_movie_directors_and_actors, animation_movie_votes)
    scrape(biography_links, biography_movie_ranking, biography_movie_names, biography_movie_release_year,
           biography_movie_duration, biography_movie_subgenres, biography_movie_user_rating,
           biography_movie_directors_and_actors, biography_movie_votes)
    scrape(comedy_links, comedy_movie_ranking, comedy_movie_names, comedy_movie_release_year, comedy_movie_duration,
           comedy_movie_subgenres, comedy_movie_user_rating, comedy_movie_directors_and_actors, comedy_movie_votes)
    scrape(crime_links, crime_movie_ranking, crime_movie_names, crime_movie_release_year, crime_movie_duration,
           crime_movie_subgenres, crime_movie_user_rating, crime_movie_directors_and_actors, crime_movie_votes)
    scrape(drama_links, drama_movie_ranking, drama_movie_names, drama_movie_release_year, drama_movie_duration,
           drama_movie_subgenres, drama_movie_user_rating, drama_movie_directors_and_actors, drama_movie_votes)
    scrape(fantasy_links, fantasy_movie_ranking, fantasy_movie_names, fantasy_movie_release_year, fantasy_movie_duration,
           fantasy_movie_subgenres, fantasy_movie_user_rating, fantasy_movie_directors_and_actors, fantasy_movie_votes)
    scrape(horror_links, horror_movie_ranking, horror_movie_names, horror_movie_release_year, horror_movie_duration,
           horror_movie_subgenres, horror_movie_user_rating, horror_movie_directors_and_actors, horror_movie_votes)
    scrape(mystery_links, mystery_movie_ranking, mystery_movie_names, mystery_movie_release_year, mystery_movie_duration,
           mystery_movie_subgenres, mystery_movie_user_rating, mystery_movie_directors_and_actors, mystery_movie_votes)
    scrape(romance_links, romance_movie_ranking, romance_movie_names, romance_movie_release_year, romance_movie_duration,
           romance_movie_subgenres, romance_movie_user_rating, romance_movie_directors_and_actors, romance_movie_votes)
    scrape(scifi_links, scifi_movie_ranking, scifi_movie_names, scifi_movie_release_year, scifi_movie_duration,
           scifi_movie_subgenres, scifi_movie_user_rating, scifi_movie_directors_and_actors, scifi_movie_votes)
    scrape(thriller_links, thriller_movie_ranking, thriller_movie_names, thriller_movie_release_year,
           thriller_movie_duration, thriller_movie_subgenres, thriller_movie_user_rating,
           thriller_movie_directors_and_actors, thriller_movie_votes)
    scrape(war_links, war_movie_ranking, war_movie_names, war_movie_release_year, war_movie_duration, war_movie_subgenres,
           war_movie_user_rating, war_movie_directors_and_actors, war_movie_votes)

    # Adicionar uma coluna a todos os respectivos quadros de dados de subgêneros e genero principal
    action_movie_genre = list(itertools.repeat("Action", len(action_movie_ranking)))
    animation_movie_genre = list(itertools.repeat("Animation", len(animation_movie_ranking)))
    biography_movie_genre = list(itertools.repeat("Biography", len(biography_movie_ranking)))
    comedy_movie_genre = list(itertools.repeat("Comedy", len(comedy_movie_ranking)))
    crime_movie_genre = list(itertools.repeat("Crime", len(crime_movie_ranking)))
    drama_movie_genre = list(itertools.repeat("Drama", len(drama_movie_ranking)))
    fantasy_movie_genre = list(itertools.repeat("Fantasy", len(fantasy_movie_ranking)))
    horror_movie_genre = list(itertools.repeat("Horror", len(horror_movie_ranking)))
    mystery_movie_genre = list(itertools.repeat("Mystery", len(mystery_movie_ranking)))
    romance_movie_genre = list(itertools.repeat("Action", len(romance_movie_ranking)))
    scifi_movie_genre = list(itertools.repeat("Sci-fi", len(scifi_movie_ranking)))
    thriller_movie_genre = list(itertools.repeat("Thriller", len(thriller_movie_ranking)))
    war_movie_genre = list(itertools.repeat("War", len(war_movie_ranking)))

    # Criar dataframe para cada genero de filme
    action_df = pd.DataFrame(list(
        zip(action_movie_ranking, action_movie_names, action_movie_release_year, action_movie_duration, action_movie_genre,
            action_movie_subgenres, action_movie_user_rating, action_movie_directors_and_actors, action_movie_votes)),
                             columns=['Ranking', 'Title', 'Release Year', 'Duration(Min.)', 'Genre', 'Sub Genres',
                                      'User Rating', 'Directors & Actors', 'Votes'])
    animation_df = pd.DataFrame(list(
        zip(animation_movie_ranking, animation_movie_names, animation_movie_release_year, animation_movie_duration,
            animation_movie_genre, animation_movie_subgenres, animation_movie_user_rating,
            animation_movie_directors_and_actors, animation_movie_votes)),
                                columns=['Ranking', 'Title', 'Release Year', 'Duration(Min.)', 'Genre', 'Sub Genres',
                                         'User Rating', 'Directors & Actors', 'Votes'])
    biography_df = pd.DataFrame(list(
        zip(biography_movie_ranking, biography_movie_names, biography_movie_release_year, biography_movie_duration,
            biography_movie_genre, biography_movie_subgenres, biography_movie_user_rating,
            biography_movie_directors_and_actors, biography_movie_votes)),
                                columns=['Ranking', 'Title', 'Release Year', 'Duration(Min.)', 'Genre', 'Sub Genres',
                                         'User Rating', 'Directors & Actors', 'Votes'])
    comedy_df = pd.DataFrame(list(
        zip(comedy_movie_ranking, comedy_movie_names, comedy_movie_release_year, comedy_movie_duration, comedy_movie_genre,
            comedy_movie_subgenres, comedy_movie_user_rating, comedy_movie_directors_and_actors, comedy_movie_votes)),
                             columns=['Ranking', 'Title', 'Release Year', 'Duration(Min.)', 'Genre', 'Sub Genres',
                                      'User Rating', 'Directors & Actors', 'Votes'])
    crime_df = pd.DataFrame(list(
        zip(crime_movie_ranking, crime_movie_names, crime_movie_release_year, crime_movie_duration, crime_movie_genre,
            crime_movie_subgenres, crime_movie_user_rating, crime_movie_directors_and_actors, crime_movie_votes)),
                            columns=['Ranking', 'Title', 'Release Year', 'Duration(Min.)', 'Genre', 'Sub Genres',
                                     'User Rating', 'Directors & Actors', 'Votes'])
    drama_df = pd.DataFrame(list(
        zip(drama_movie_ranking, drama_movie_names, drama_movie_release_year, drama_movie_duration, drama_movie_genre,
            drama_movie_subgenres, drama_movie_user_rating, drama_movie_directors_and_actors, drama_movie_votes)),
                            columns=['Ranking', 'Title', 'Release Year', 'Duration(Min.)', 'Genre', 'Sub Genres',
                                     'User Rating', 'Directors & Actors', 'Votes'])
    fantasy_df = pd.DataFrame(list(
        zip(fantasy_movie_ranking, fantasy_movie_names, fantasy_movie_release_year, fantasy_movie_duration,
            fantasy_movie_genre, fantasy_movie_subgenres, fantasy_movie_user_rating, fantasy_movie_directors_and_actors,
            fantasy_movie_votes)), columns=['Ranking', 'Title', 'Release Year', 'Duration(Min.)', 'Genre', 'Sub Genres',
                                            'User Rating', 'Directors & Actors', 'Votes'])
    horror_df = pd.DataFrame(list(
        zip(horror_movie_ranking, horror_movie_names, horror_movie_release_year, horror_movie_duration, horror_movie_genre,
            horror_movie_subgenres, horror_movie_user_rating, horror_movie_directors_and_actors, horror_movie_votes)),
                             columns=['Ranking', 'Title', 'Release Year', 'Duration(Min.)', 'Genre', 'Sub Genres',
                                      'User Rating', 'Directors & Actors', 'Votes'])
    mystery_df = pd.DataFrame(list(
        zip(mystery_movie_ranking, mystery_movie_names, mystery_movie_release_year, mystery_movie_duration,
            mystery_movie_genre, mystery_movie_subgenres, mystery_movie_user_rating, mystery_movie_directors_and_actors,
            mystery_movie_votes)), columns=['Ranking', 'Title', 'Release Year', 'Duration(Min.)', 'Genre', 'Sub Genres',
                                            'User Rating', 'Directors & Actors', 'Votes'])
    romance_df = pd.DataFrame(list(
        zip(romance_movie_ranking, romance_movie_names, romance_movie_release_year, romance_movie_duration,
            romance_movie_genre, romance_movie_subgenres, romance_movie_user_rating, romance_movie_directors_and_actors,
            romance_movie_votes)), columns=['Ranking', 'Title', 'Release Year', 'Duration(Min.)', 'Genre', 'Sub Genres',
                                            'User Rating', 'Directors & Actors', 'Votes'])
    scifi_df = pd.DataFrame(list(
        zip(scifi_movie_ranking, scifi_movie_names, scifi_movie_release_year, scifi_movie_duration, scifi_movie_genre,
            scifi_movie_subgenres, scifi_movie_user_rating, scifi_movie_directors_and_actors, scifi_movie_votes)),
                            columns=['Ranking', 'Title', 'Release Year', 'Duration(Min.)', 'Genre', 'Sub Genres',
                                     'User Rating', 'Directors & Actors', 'Votes'])
    thriller_df = pd.DataFrame(list(
        zip(thriller_movie_ranking, thriller_movie_names, thriller_movie_release_year, thriller_movie_duration,
            thriller_movie_genre, thriller_movie_subgenres, thriller_movie_user_rating, thriller_movie_directors_and_actors,
            thriller_movie_votes)), columns=['Ranking', 'Title', 'Release Year', 'Duration(Min.)', 'Genre', 'Sub Genres',
                                             'User Rating', 'Directors & Actors', 'Votes'])
    war_df = pd.DataFrame(list(
        zip(war_movie_ranking, war_movie_names, war_movie_release_year, war_movie_duration, war_movie_genre,
            war_movie_subgenres, war_movie_user_rating, war_movie_directors_and_actors, war_movie_votes)),
                          columns=['Ranking', 'Title', 'Release Year', 'Duration(Min.)', 'Genre', 'Sub Genres',
                                   'User Rating', 'Directors & Actors', 'Votes'])

    # Mesclar dataframes
    complete = [action_df, animation_df, biography_df, comedy_df, crime_df, drama_df, fantasy_df, horror_df, mystery_df,
                romance_df, scifi_df, thriller_df, war_df]
    final = pd.concat(complete)
    # Salve o arquivo finalizado como csv no diretório local para processamento posterior
    final.to_csv('Data_Files/desafio_indicium_limpo.csv')