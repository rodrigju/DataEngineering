"""
author = Julien RODRIGUES
"""

#   IMPORTATION DES MODULES NECESSAIRES POUR LE DASHBOARD
#################################################################################################################################################################################
from dash import Dash, html, dcc, Input, Output
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go 
import numpy as np 
from plotly.subplots import make_subplots
from pymongo import MongoClient


client = MongoClient("localhost")
print(client.list_database_names())

dict_nameTeam = {"steelers" :"10403900-8251-6892-d81c-4348525c2d47",
"broncos": "10401400-b89b-96e5-55d1-caa7e18de3d8",
"seahawks" :"10404600-adcd-28ac-5826-b4d95ec2a228",
"rams": "10402510-8931-0d5f-9815-79bb79649a65",
"falcons": "10400200-f401-4e53-5175-0974e4f16cf7",
"jets": "10403430-1bc3-42c4-c7d8-39f38aed5f12",
"lions": "10401540-f97c-2d19-6fcd-fac6490a48b7",
"vikings": "10403000-5851-f9d5-da45-78365a05b6b0",
"saints":"10403300-f235-cf9b-6d3a-2f182be48dd1",
"redskins":"10405110-ec3c-669e-2614-db3dc1736e95",
"football team": "10405110-ec3c-669e-2614-db3dc1736e95",
"commanders": "10405110-ec3c-669e-2614-db3dc1736e95",
"texans" :"10402120-b0bc-693d-098a-803014096eb0",
"patriots" :"10403200-69ab-9ea6-5af5-e240fbc08bea",
"browns":"10401050-5e38-b907-1be1-55b91b19c057",
"ravens":"10400325-48de-3d6a-be29-8f829437f4c8",
"buccaneers":"10404900-d59e-b449-ef75-961e09ca027e",
"panthers":"10400750-259b-33ac-eee3-a3852e83cd1f",
"bengals":"10400920-57c1-7656-e77e-1af3d900483e",
"cowboys":"10401200-a308-98ca-ad5f-95df2fefea68",
"giants":"10403410-997c-9c75-256b-3b012f468bd0",
"jaguars":"10402250-89fe-7b86-ef98-9062cd354256",
"colts":"10402200-2ea3-84c3-e627-6a6b3b39d56d",
"titans":"10402100-447f-396e-8149-0a434ffb2f23",
"packers":"10401800-ab22-323d-721a-cee4713c4c2d",
"raiders":"10402520-96bf-e9f2-4f68-8521ca896060",
"chargers":"10404400-3b35-073f-197e-194bb8240723",
"chiefs":"10402310-a47e-10ea-7442-16b633633637",
"49ers":"10404500-e7cb-7fce-3f10-4eeb269bd179",
"dolphins":"10402700-1662-d8ad-f45c-0b0ea460d045",
"bears":"10400810-db30-43d6-221c-620006f3ca19",
"cardinals":"10403800-517c-7b8c-65a3-c61b95d86123",
"eagles":"10403700-b939-3cbd-3d16-24d4d6742fa2",
"bills":"10400610-c40e-a673-1743-2ce2a5d5d731"}

dict_idTeam= { "10403900-8251-6892-d81c-4348525c2d47":"steelers",
"10401400-b89b-96e5-55d1-caa7e18de3d8":"broncos",
"10404600-adcd-28ac-5826-b4d95ec2a228":"seahawks",
"10402510-8931-0d5f-9815-79bb79649a65":"rams",
"10400200-f401-4e53-5175-0974e4f16cf7":"falcons",
"10403430-1bc3-42c4-c7d8-39f38aed5f12":"jets",
 "10401540-f97c-2d19-6fcd-fac6490a48b7":"lions",
"10403000-5851-f9d5-da45-78365a05b6b0":"vikings",
"10403300-f235-cf9b-6d3a-2f182be48dd1":"saints",
 "10405110-ec3c-669e-2614-db3dc1736e95":{"2017":"redskins",
                                         "2018":"redskins",
                                         "2019":"redskins",
                                         "2020":"football-team","2021":"football-team",
                                         "2022":"commanders"},
"10402120-b0bc-693d-098a-803014096eb0":"texans",
"10403200-69ab-9ea6-5af5-e240fbc08bea":"patriots",
"10401050-5e38-b907-1be1-55b91b19c057":"browns",
"10400325-48de-3d6a-be29-8f829437f4c8":"ravens",
"10404900-d59e-b449-ef75-961e09ca027e":"buccaneers",
"10400750-259b-33ac-eee3-a3852e83cd1f":"panthers",
"10400920-57c1-7656-e77e-1af3d900483e":"bengals",
"10401200-a308-98ca-ad5f-95df2fefea68":"cowboys",
"10403410-997c-9c75-256b-3b012f468bd0":"giants",
"10402250-89fe-7b86-ef98-9062cd354256":"jaguars",
"10402200-2ea3-84c3-e627-6a6b3b39d56d":"colts",
"10402100-447f-396e-8149-0a434ffb2f23":"titans",
"10401800-ab22-323d-721a-cee4713c4c2d":"packers",
"10402520-96bf-e9f2-4f68-8521ca896060":"raiders",
"10404400-3b35-073f-197e-194bb8240723":"chargers",
"10402310-a47e-10ea-7442-16b633633637":"chiefs",
"10404500-e7cb-7fce-3f10-4eeb269bd179":"49ers",
"10402700-1662-d8ad-f45c-0b0ea460d045":"dolphins",
"10400810-db30-43d6-221c-620006f3ca19":"bears",
"10403800-517c-7b8c-65a3-c61b95d86123":"cardinals",
"10403700-b939-3cbd-3d16-24d4d6742fa2":"eagles",
"10400610-c40e-a673-1743-2ce2a5d5d731":"bills"}

postSeason={1:"Wild Card Weekend",  2:"Divisional Playoffs" ,3:"Conference Championships" , 4:"Super Bowl"}

dict_postSeason = {"Wild Card Weekend":"post1", "Divisional Playoffs":"post2", "Conference Championships":"post3", "Super Bowl":"post4"}
dict_postSeasonKey = {"post1":"Wild Card Weekend", "post2":"Divisional Playoffs", "post3":"Conference Championships", "post4":"Super Bowl"}

week_label = {
'REG1' :'Semaine 1',
'REG2' :'Semaine 2',
'REG3' :'Semaine 3',
'REG4' :'Semaine 4',
'REG5' :'Semaine 5',
'REG6' :'Semaine 6',
'REG7' :'Semaine 7',
'REG8' :'Semaine 8',
'REG9':'Semaine 9',
'REG10':'Semaine 10',
'REG11' :'Semaine 11',
'REG12' :'Semaine 12',
'REG13' :'Semaine 13',
'REG14':'Semaine 14',
'REG15':'Semaine 15',
'REG16' :'Semaine 16',
'REG17':'Semaine 17',
'REG18':'Semaine 18',
'Wild Card Weekend' :'Wild Card Weekend',
'Divisional Playoffs' :'Divisional Playoffs',
'Conference Championships':'Conference Championships',
'Super Bowl' : 'Super Bowl' } 
    
    
team_label_value = [('Baltimore Ravens','Ravens'),
('Cincinnati Bengals','Bengals'),
('Cleveland Browns','Browns'),
('Pittsburgh Steelers','Steelers'),
('Buffalo Bills','Bills'),
('Miami Dolphins','Dolphins'),
('New England Patriots','Patriots'),
('New York Jets','Jets'),
('Houston Texans','Texans'),
('Indianapolis Colts','Colts'),
('Jacksonville Jaguars','Jaguars'),
('Tennessee Titans','Titans'),
('Denver Broncos','Broncos'),
('Kansas City Chiefs','Chiefs'),
('Las Vegas Raiders','Raiders'),
('Los Angeles Chargers','Chargers'),
('Chicago Bears','Bears'),
('Detroit Lions','Lions'),
('Green Bay Packers','Packers'),
('Minnesota Vikings','Vikings'),
('Dallas Cowboys','Cowboys'),
('New York Giants','Giants'),
('Philadelphia Eagles','Eagles'),
('Washington Commanders','Commanders'),
('Atlanta Falcons','Falcons'),
('Carolina Panthers','Panthers'),
('New Orleans Saints','Saints'),
('Tampa Bay Buccaneers','Buccaneers'),
('Arizona Cardinals','Cardinals'),
('Los Angeles Rams','Rams'),
('San Francisco 49ers','49ers'),
('Seattle Seahawks','Seahawks')]                   

colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}

#   CREATION D'UNE INSTANCE DE DASH
app = Dash(__name__)

#   PARTIE FRONT END DU DASHBOARD
app.layout = html.Div([ 

    html.Div([ 
        html.H1(id='title-dash',
                children= 'Dashboard NFL',
                style={
                'textAlign': 'center',
                'color': colors['text']
                }
                ),
        dcc.Markdown('''
            * Présentation
            
            A travers ce dashboard, vous allez faire un voyage initiatique dans le monde de la NFL, de la National Football League.
        
            Le football américain est un sport collectif opposant deux équipes de onze joueurs qui alternent entre la défense et l'attaque.
        
            Le but du jeu est de marquer des points en portant ou lançant le ballon jusqu'à la zone d'en-but adverse. Pour conserver la possession, l'équipe attaquante doit parcourir au moins 10 yards en 4 tentatives (appelées « down »).
        
            Dans le même temps, l'équipe en défense doit empêcher l'attaque d'atteindre cet objectif, dans le but de reprendre la possession de la balle.
        
            Les points peuvent être marqués de différentes façons : en franchissant la ligne de but avec le ballon, en lançant la balle à un autre joueur situé de l'autre côté de la ligne de but, en plaquant le porteur du ballon de l'équipe adverse dans sa propre zone d'en-but (safety) ou en tirant au pied le ballon entre les poteaux du but adverse.
        
            Le vainqueur est l'équipe ayant marqué le plus de points à la fin du match.  
                            
        ''',
            style={
                'textAlign': 'left',
                'color': colors['text']
                }
            ),      
        dcc.Markdown('''
            * Répartition des équipes
            
            La NFL est divisé en 2 conférences, la NFC (National Football Conference) et l'AFC (American Football Conference), qui disposent de 16 équipes chacune. A la base, ces deux groupes étaient distincts (NFL et AFL), qui ont fusionné en 1970. Les champions de chaque conférence se rencontrent pour le match final qu’est le Super Bowl.
            
            Ces deux conférences sont subdivisées en quatre divisions chacune (Nord, Sud, Est, Ouest) et chaque division est composée de 4 équipes. Remporter le titre de sa division est le premier objectif d’une saison, car il qualifie automatiquement une équipe pour les playoffs, la seconde partie de la saison.               
        ''',
            style={
                'textAlign': 'left',
                'color': colors['text']
                }
            ),        
        dcc.Markdown('''
            * Saison régulière
            
            Après les camps d’entrainement et les 4 matchs de présaison, vient le moment de la saison régulière.
            
            La saison régulière dure 18 semaines. Chaque équipe a 17 matchs et une semaine de repos.
            
            Au cours d'une saison, une équipe affronte deux fois les équipes de sa division. Elle rencontre aussi une fois les équipes d'une division de sa conférence et une fois les équipes d'une division de la conférence opposée. Deux autres matchs opposent l’équipe aux clubs de la même conférence ayant terminé à la même place la saison précédente dans leur division (1er contre 1er, 2e contre 2e etc). Enfin, un dernier match oppose l’équipe à une équipe de la conférence opposée, qui a terminé à la même place la saison précédente et qui ne figure pas dans ses autres adversaires, cette 17e rencontre a été ajoutée à partir de la saison 2021.              
        ''',
            style={
                'textAlign': 'left',
                'color': colors['text']
                }
            ),
        dcc.Markdown('''
            * Playoffs
            
            À la fin de la saison régulière, quatorze équipes (7 par conférence) sont qualifiées pour les playoffs, tournoi final à élimination directe. Dans chaque conférence, il s’agit des 4 champions de division, plus les trois autres meilleures équipes en terme de bilan.

            Dans chaque conférence, le premier tour s’appelle wild card. Les vainqueurs passent au second tour (divisional round), notamment pour retrouver la tête de série numéro 1, qui a bénéficié d’une semaine de repos.

            Les gagnants se rencontrent lors des finales de Conférence. Enfin, les champions de Conférence se rencontrent, en terrain neutre, pour le Super Bowl.
            ''',
            style={
                'textAlign': 'left',
                'color': colors['text']
                }
            ),
            html.Br(),      
    ], id = 'presentation-section'),
    
    html.Div([
        html.H3("Teams stadium",
                style={
                'textAlign': 'center',
                'color': colors['text']
                },),
        dcc.Markdown('''
                     Vous pouvez voir sur la map, la localisation des stades des différentes équipes.
                     ''',
            style={
                'textAlign': 'left',
                'color': colors['text']
                },
        ),
        html.Iframe(id='team-stadium-map', srcDoc = open('map_nfl.html', mode='r').read(), width='100%', height='400')
        ],
             id='teams-stadium'),
    
    html.Br(),
    html.Div([
        html.Div([
            html.H2(id='title-teams',
                children= 'Teams',
                style={
                'textAlign': 'center',
                'color': colors['text']
                }),        
            dcc.Dropdown(id='team-dropdown',
            options = [
            {
                "label": html.Div(
                    [
                        html.Div(_[0], style={'font-size': 15, 'padding-left': 10}),
                    ], style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}
                ),
                "value": _[1],
            }
            for _ in team_label_value
            ],
            value=team_label_value[0][1],
            multi=False,
            clearable=False,
            style={'width':'40%', } 
            ),   
        ]),
        
        html.Br(),
        html.Div([
            dcc.Markdown(id='output-team-information'),
            ]),
        
        html.Br(),
        html.Div([
        html.H2("Offense",
                style={
                'textAlign': 'center',
                'color': colors['text']
                }),
        dcc.Markdown('''
                    Une équipe de football américain est composée de 4 équipes; il y a l'offense et la defense, mais aussi les teams spéciales (Punt et Kick)
                    Si l'offense offre les moments les plus mémorables lors des matchs, pas tous les postes sucitent le même intêret du public.
                    
                    Les postes de linemen (le Centre, les Guards et Tackles) sont joués par des joueurs grands et imposants ayant une grande mobilité. Leur but est de protéger le 
                    Quaterback, la vedette de l'équipe. Et à ce poste, un nom s'élève par rapport aux autres, celui de Tom Brady.
                    Considéré comme le G.O.A.T de la NFL, il a remporté 7 Super Bowls en 22 ans de carrière; il s'agit d'un record historique.
                    Sur les extrémités du terrain, on retrouve les Wide Receveur, ce sont eux qui sont chargés de receptionner les passes du Quaterback.
                    
                    En soutien du QB, on retrouve les Runing Backs et les Full Backs. Et enfin, il y a le poste de Tight End, c'est un mélange entre les Runing Backs et les Wide Receveurs.
                    
                    Nous avons séparé en trois catégories les données de l'offense. Une catégorie pour les passes, les courses, et les receptions.
                    ''',
                style={
                    'textAlign': 'left',
                    'color': colors['text']
                    }, id='team-info-text'
                ),
        html.Div([
            html.H3("Passing",
                style={
                'textAlign': 'center',
                'color': colors['text']
                }),
            dcc.Slider(2017,
                       2022,
                       value=2017,
                       step=None, 
                       marks={
                           2017:'2017',
                           2018:'2018',
                           2019:'2019',
                           2020:'2020',
                           2021:'2021',
                           2022:'2022',
                           },
                       id='slider-passing-year'),
            dcc.Graph(id='passing-completions-graph'),
            dcc.Graph(id='passing-yards-graph'),
            dcc.Graph(id='pass-td-int-graph'),
            ],id='passing-stats'),
        
        html.Br(),
        html.Br(),
        html.Div([
            html.H3("Rushing",
                style={
                'textAlign': 'center',
                'color': colors['text']
                }),
            dcc.Slider(2017,
                       2022,
                       value=2017,
                       step=None, 
                       marks={
                           2017:'2017',
                           2018:'2018',
                           2019:'2019',
                           2020:'2020',
                           2021:'2021',
                           2022:'2022',
                           },
                       id='slider-rushing-year'),
            dcc.Graph(id='rushing-yards-graph'),
            dcc.Graph(id='rushing-attempts-graph'),
            dcc.Graph(id='rushing-touchdowns-graph'),
            ],id='rushing-stats'),
        
        html.Br(),
        html.Br(),
        html.Div([
            html.H3("Receiving",
                style={
                'textAlign': 'center',
                'color': colors['text']
                }),
            dcc.Slider(2017,
                       2022,
                       2017,
                       step=None, 
                       marks={
                           2017:'2017',
                           2018:'2018',
                           2019:'2019',
                           2020:'2020',
                           2021:'2021',
                           2022:'2022',
                           },
                       id='slider-receiving-year'),
            dcc.Graph(id='receiving-receptions-graph'),
            dcc.Graph(id='receiving-attempts-graph'),
            dcc.Graph(id='receiving-touchdowns-graph'),
            ],id='receiving-stats'),           
    ],id='offense-stats'),
    
    html.Div([
        
        html.H2("Defense",
                style={
                'textAlign': 'center',
                'color': colors['text']
                }),
        dcc.Markdown('''
                     Cette section est en cours de maintenance, elle arrivera très bientôt
                     ''',
                style={
                'textAlign': 'left',
                'color': colors['text']
                }),
        
        ],id='defense-stats')
    
    ],id="teams-players-section"),   
    html.Br(),
    #Fermeture de Div principal
    ],
    style={'background' : colors['background']}
    
    )

#   PARTIE BACK END DU DASHBOARD
#   DEBUT PARTIE CALLBACK FUNCTIONS PERMETTANT DE GERER L'AFFICHAGE DYNAMIQUE DE LA PAGE 
###################################################################################################################################################
'''
Nous avons plusieurs parties qui doivent appeler des callback functions.
Nous allons séparer les callbacks pour les différents appels et affichages.
'''

'''
Le premier app.callback doit permettre de mofifier les options disponibles dans le selecteur de semaines, il n'y a pas le même nombre de semaines pour toutes les années.
On récupère la valeur du selecteur d'année et nous renvoyons les options de selections qui lui sont associées.
'''
@app.callback(
    Output('week-dropdown','options') ,
    Input(component_id='year-dropdown', component_property='value')
)
def set_weeks_options(selected_year):
    """
    Retourne les options de sélection des semaines de la saison régulière et des playoffs en fonction de l'année sélectionnée

    Args:
        selected_year (int): année choisie dans le dropdown

    Returns:
        options: liste de dictionnaires avec les lables affichés et les valeurs qui correspondent aux options du dropdown
    """
    if selected_year in [2017,2018,2019,2020]:
        options=[
            {'label': 'Week 1', 'value': 'reg1'},
            {'label': 'Week 2', 'value': 'reg2'},
            {'label': 'Week 3', 'value': 'reg3'},
            {'label': 'Week 4', 'value': 'reg4'},
            {'label': 'Week 5', 'value': 'reg5'},
            {'label': 'Week 6', 'value': 'reg6'},
            {'label': 'Week 7', 'value': 'reg7'},
            {'label': 'Week 8', 'value': 'reg8'},
            {'label': 'Week 9', 'value': 'reg9'},
            {'label': 'Week 10', 'value': 'reg10'},
            {'label': 'Week 11', 'value': 'reg11'},
            {'label': 'Week 12', 'value': 'reg12'},
            {'label': 'Week 13', 'value': 'reg13'},
            {'label': 'Week 14', 'value': 'reg14'},
            {'label': 'Week 15', 'value': 'reg15'},
            {'label': 'Week 16', 'value': 'reg16'},
            {'label': 'Week 17', 'value': 'reg17'},
            {'label': 'Wild Card Weekend', 'value': 'Wild Card Weekend'},
            {'label': 'Divisional Playoffs', 'value': 'Divisional Playoffs'},
            {'label': 'Conference Championships', 'value': 'Conference Championships'},
            {'label': 'Super Bowl', 'value': 'Super Bowl'},
        ]
    elif selected_year in [2021,2022]:
        options=[
            {'label': 'Week 1', 'value': 'reg1'},
            {'label': 'Week 2', 'value': 'reg2'},
            {'label': 'Week 3', 'value': 'reg3'},
            {'label': 'Week 4', 'value': 'reg4'},
            {'label': 'Week 5', 'value': 'reg5'},
            {'label': 'Week 6', 'value': 'reg6'},
            {'label': 'Week 7', 'value': 'reg7'},
            {'label': 'Week 8', 'value': 'reg8'},
            {'label': 'Week 9', 'value': 'reg9'},
            {'label': 'Week 10', 'value': 'reg10'},
            {'label': 'Week 11', 'value': 'reg11'},
            {'label': 'Week 12', 'value': 'reg12'},
            {'label': 'Week 13', 'value': 'reg13'},
            {'label': 'Week 14', 'value': 'reg14'},
            {'label': 'Week 15', 'value': 'reg15'},
            {'label': 'Week 16', 'value': 'reg16'},
            {'label': 'Week 17', 'value': 'reg17'},
            {'label': 'Week 18', 'value': 'reg18'},
            {'label': 'Wild Card Weekend', 'value': 'Wild Card Weekend'},
            {'label': 'Divisional Playoffs', 'value': 'Divisional Playoffs'},
            {'label': 'Conference Championships', 'value': 'Conference Championships'},
            {'label': 'Super Bowl', 'value': 'Super Bowl'},
        ]
    return options 


'''
Deuxième callback
'''
@app.callback(
    Output('week-dropdown', 'value'),
    Input('week-dropdown', 'options'))
def set_weeks_value(available_options):
    
    """fonction callback qui initialise la valeur par défaut du week-dropdown à REG1
    Args:
        available_options : les options disponibles dans le week-dropdown
    
    Returns:
        value: value du premier dictionnaire de la liste de dictionnaires des options disponibles
    """
    return available_options[0]['value']

'''
Troisième callback
'''
@app.callback(
    [Output(component_id='output-team-information',component_property='children'),],
    [Input(component_id='team-dropdown',component_property='value'),]    
)
def update_informations(selected_team):
    """fonction d'actualisation du texte affiché avec les informations sur l'équipe choisie

    Args:
        selected_team (factor): value sélectionnée par le dropdown avec les différentes équipes de la NFL.

    Returns:
        list: liste avec les informations sur l'équipe
    """
    if selected_team == "Ravens":
        return ['''
                *** BALTIMORE RAVENS *** \n                
                Tout savoir sur les BALTIMORE RAVENS \n

                L'équipe voir le jour en 1996 suite à une volonté du propriétaire des Cleveland Browns de l'époque, Art MODDEL, de quitter Cleveland.\n
                Ce départ fut accepté par la ligue à la condition que l'histoire, le nom, les couleurs et le bilan des Browns restent à Cleveland.\n
                Les Ravens sont donc une nouvelle franchise et non pas une franchise qui déménage lors de leur apparition en 1996.\n

                    fun fact : les Ravens tiennent leur nom du célèbre auteur de baltimore : Edgar Allan Poe. La mascotte de l'équipe qui représente un corbeau s'appelle d'ailleurs "Poe" en hommage à l'auteur.\n

                Situés à Baltimore dans le Maryland, les Ravens jouent au M&T Bank Stadium devant 70.745 spectacteurs. Les couleurs de l'équipe sont le violet le doré ainsi que le noir. \n   
                13 apparitions en playoffs\n
                2x AFC Champions >  2 SUPER BOWLS\n
                ''']

    elif selected_team == "Bengals":
        return ['''
                *** CINCINNATI BENGALS ***\n
                En apprendre plus sur les CINCINNATI BENGALS\n
                En 1965, l'ancien Head Coach des Cleveland Borwns, Paul Brown, commence à planifier la création d'une nouvelle équipe de football.\n
                Souhaitant rester dans l'Ohio, c'est en 1966, que la ville de Cincinnati accepte d'acceuillir cette nouvelle équipe et c'est ainsi 
                qu'en 1967 les Bengals voient le jour.\n
                Originalement une équipe de l'American Football League, c'est en 1970 que les Bengals rejoignent la NFL lors de la fusion des deux ligues.\n
                Paul Brown, le fondateur de la franchise tiendra également le rôle de Head Coach jusqu'en 1975.\n
                Les Bengals ont été très irréguliers dans leur histoire, avec de nombreuses périodes de creux, notamment dans les années 90 avec 14 saisons 
                consécutives sans se qualifier en Playoffs.\n
                Ils n'ont jamais remporté de Super Bowl malgré avoir participé à 3 Super Bowls, dont la dernière défaite remontant à la saison passée.\n
                Les Bengalsjouent au Paycor Stadium aussi surnommé "The Jungle" en référence à l'habitat naturel des titres du bengal dont l'équipe tient son nom.\n
                Inauguré en 2000, le stade s'appelait jusqu'à cette saison le Paul Brown Stadium en hommage au fondateur de la franchise.\n
                Le paycor Stadium a une capacité de 65.515 spectacteurs ce qui en fait l'un des plus petits stades de la ligue.\n
                Les couleurs des Cincinnati Bengals sont le orange, le noir et le blanc.                         
                ''']

    elif selected_team == "Browns":
        return ['''
                *** CLEVELAND BROWNS ***                
                ''']

    elif selected_team == "Steelers":
        return ['''
                *** PITTSBURGH STEELERS ***\n
                Ce qu'il faut savoir sur les PITTSBURGH STEELERS\n
                Fondés en 1933, les Steelers sont l'une des plus vieilles équipes de la ligue. Ils ont toujours fait partie de la NFL.\n
                Originalement appelés PITTSBURGH PIRATES, c'est en 1939 qu'ils adoptent le nom de Steelers que nous connaissons aujourd'hui.\n
                Lors de la seconde guerre mondiale, l'équipe a également connu 2 fusions temporaires avec d'autres équipes de la ligue : en 1943 avec les 
                Eagles ce qui a donné les "Phil-Pitt Steagles" et en 1944 avec les Cardinals ce qui a donné les "Card-Pitt.\n
                Ce n'est que 40 ans après leur apparition que les Steelers nouent enfin avec le succès. C'est dans les 1970 que la dynastie des Steelers
                apparaît en remportant 4 super bowls en 6 ans.\n
                Depuis l'équipe a su rester sur les devants de la scène, et a gagné 2 autres Super Bowls dans les années 2000 avec Ben Roethlisberger.\n
                Avec 6 super bowls remportés, les Steelers sont l'équipe la plus titrée de la ligue à égalité avec les patriots. \n
                Les couleurs de l'équipe sont le jaune, le noir et le blanc.\n
                Particularité de l'équipement des steelers, le logo n'est présent que sur un seul côté du casque.\n
                Inauguré en 2001, l'équipe joue au Acrisure Stadium, stade de 68.400 places.\n
                    fun fact : le stade des steelers est celui qui a été choisi et utilisé dans le film Batman The Dark Knight Rises de Cristopher Nolan
                ''']
    elif selected_team == "Jaguars":
        return ['''
                *** JACKSONVILLE JAGUARS ***\n

                En apprendre plus sur les JAGUARS\n
                Tout savoir sur la jeune équipe de Jacksonville\n
                Fondés en 1995, les Jaguars font partie d'un plan d'expansion de a ligue qui donnera égaleent vie aux Carolina Panthers.\n
                Malgré des bons débuts dans la ligue avec 4 apparitions en playoffs lors de leurs 6 premières années d'éxistence, les jaguars font partie des 4 équipes qui n'ont jamais participé à un SUPER BOWL.\n

                7 apparitions en playoffs \n
                3x Champions de division\n

                Situés à Jacksonville en Floride, les Jaguars jouent au TIAA Bank Field devant 67.814 spectacteurs. Ce stade a également la particularité d'avoir une piscine dans son enceinte. Les couleurs de l'équipe sont le teal, le blanc, le doré et le noir.\n
                Pour la seconde saison consécutive, les Jaguars ont fini avec le plus mauvais bilan de la ligue et ont donc obtenu le premier choix de la draft.\n
                Cependant, les Jaguars ont été très actfis lors de cette intersaison et ont signé de nombreux vétérans afin de renforcer leur effectif aussi bien en attaque qu'en défense.\n
                ''']
    elif selected_team == "Buccaneers":
        return ['''
                *** TAMPA BAY BUCCANEERS ***\n

                Devenir incollable sur les TAMPA BAY BUCCANEERS\n
                Situés à Tampa Bay à l'ouest de la floride, les buccanners ont été fondés en 1976 en même temps que les Seattle Seahawks\n
                Les débuts dans la ligue ont été très compliqués pour l'équipe avec notamment 14 saisons consécutives avec un bilan négatif entre 1983 et 1996.\n
                Les Buccaneers jouent au Raymond James Stadium devant 65.618 places.\n
                
                Les couleurs des Buccaneers sont le rouge, la couleur étain, le orange ainsi que le blanc et le noir.\n

                12 apparitions en playoffs\n
                7x Champions de division\n
                2x NFC Chamions\n
                2 SUPER BOWLS\n                  
                ''']
    elif selected_team == "Raiders":
        return ['''
                *** LAS VEGAS RAIDERS ***\n
                Les chroniques LAS VEGAS RAIDERS\n

                Fondés en 1960, les Raiders sont l'une des plus vieilles franchises présentes en NFL.\n
                
                Les Raiders ont d'abord évolué à Oakland en Californie , avant de déménager à Los Angeles entre 1982 et 1994. Dès 1995 ils font leur retour à Oakland jusqu'en 2020 et leur relocalisation à Las Vegas.\n
                
                Dans les années 70 et 80, menés par la légende du football John MADDEN, les Raiders ont dominé la ligue en remportant les 3 seuls SUPER BOWLS de leur histoire en l'espace de 7 ans.\n
                
                Dès le début, les "SILVER & BLACK" paraissent plus cools et plus forts que tout le monde. \n

                Leur logo avec la tête de pirate portant un casque de football et les 2 sabres croisés dans le fond, l'imagerie du bandit et leurs couleurs argent et noir font de la franchise de Las Vegas l'une des plus iconiques de la ligue.\n

                L'arrivée à Las Vegas est synonime de nouveau départ pour les Raiders. \n

                En 2020 ils ont inauguré leur nouveau stade ultra-moderne l'Allegiant Stadium.\n

                Surnomé "The Death Star" cette merveille d'architecture a une capacité de 65.000 places.\n                 
                ''']
    elif selected_team == "Giants":
        return ['''
                *** NEW YORK GIANTS ***\n
                Tout savoir sur les NEW YORK GIANTS \n

                Les Giants sont l'une des franchises historiques de la ligue.\n
                
                Fondée en 1925 en même temps que 5 autres franchises, l'équipe de New York est l'une des premières à avoir rejoint la ligue et
                est aujourd'hui la seule de ces 5 équipes qui éxiste toujours.\n
                Les "Big Blue" sont l'une des équipes les plus populaires de la NFL.\n
                Ils ont su traverser les époques en étant notamment 4 fois champions NFL entre 1927 et 1956 et de retrouver le succès à partir des années
                80 en gagnant un Super Bowl dans chaque décennie depuis.\n    
                Les Giants jouent au Metlife Stadium dans le New Jersey, stade qu'ils partagent avec l'autre équipe de New York, les Jets.\n
                Inauguré en 2010, le Metlife est l'un des plus grands satdes de la ligue et l'un des plus célèbres.\n
                Avec une capacité de 82.500 spectacteurs, il est le stade avec la plus grande capacité.\n
                Les Giants jouent en bleu, rouge et blanc.\n
                32 apparitions en Playoffs\n
                11 champions NFC\n
                4 champions NFL\n
                4 Super Bowls\n 
                Les Giants sortent d'une très mauvaise saison, avec un bilan de 4-13 ils étaient l'une des 5 plus mauvaises équipes la saison passée.\n
                Dès la fin de saison, les Giants ont entamé de grands changements internes en remplaçant leur Head Coach et leur General Manager.\n
                L'équipe de New York a eu l'occasion de se renforcer pendant la Draft, avec l'arrivée de Edge Rusher, Kayvon Thibodeaux et du lineman offensif Evan Neal.\n
                Il semble évident que les Giants seront cette saison encore dans une période de reconstruction mais les nombreuses stars de l'équipe et l'arrivée du nouveau Head Coach, font des Giants une équipe qu'il faudra suivre dans une division NFC East où tout est toujours possible.             
                ''']
    elif selected_team=="Lions" : 
        return ['''
                *** DETROIT LIONS ***\n
                Apprenez-en plus sur les DETROIT LIONS\n
                Fondés en 1930, les Lions sont l'une des plus veilles équipes de la ligue.\n
                Originalement appelée Spartans et installée à Portsmouth dans l'Ohio, l'équipe changera de nom en 1934 en même temps que son 
                arrivée à Detroit dans le Michigan.\n 
                Les débuts de la franchise à Detroit sont plutôt fructueux en étant 4 fois champions entre 1935 et 1957.\n
                Malheureusement, depuis les Lions ont du mal à renouer avec le succès avec une seule victoire en playoffs depuis et en étant la
                seule équipe existante depuis le début de l'ère Super Bowl à ne pas avoir participé à un Super Bowl.\n
                Les Lions jouent au Ford Field dans le centre ville de Detroit. Le stade a une capacité de 65.000 places.\n
                Les couleurs de l'équipe sont le bleu ciel, le gris et le blanc.
                ''']
    elif selected_team=="49ers" : 
        return ['''
                *** San Francisco 49ers ***\n
                Les 49ers un favori en NFC\n
                Tout ce que vous devez savoir sur l'équipe de San Francisco\n
                
                Fondés en 1946, et originalement membres de la ligue "All-America Football Conference", les Niners rejoignent la NFL en 1949 quand
                les deux ligues fusionnent.\n
                Les 49ers sont la 10ème plus vieille équipe de la ligue et la première équipe sportive de l'histoire à s'installer à San Francisco.\n
                Ils tiennent leur nom des chercheurs d'or qui s'étaient installés dans la région lors de la ruée vers l'or en 1849.\n
                Une longétivité qui a été pleine de succès, les 49ers ayant de nombreux records à leur actif, tels que le plus de participation
                à une finale NFC, le plus de points inscrits lors d'une saison en Playoffs.\n
                L'équipe de San Francisco a également remporté 5 super bowls dans son histoire, tous gagnés entre 1981 et 1994, ce qui en fait la deuxième
                équipe la plus titrée de la ligue à égalité avec les Dallas Cowboys et juste derrière les Pittsburgh Steelers et les New England Patriots (6 super bowls chacun).
                Depuis 2014, les Niners jouent au Levi's Stadium situé à Santa Clara à quelques kilomètres au sud de San Francisco.\n
                Le stade a une capacité de 68.500 places.\n
                Les couleurs de la franchise de San Francisco sont le rouge, le doré, le blanc ainsi que le noir.
                ''']    
    elif selected_team=="Bills" : 
        return ['''
                *** BUFFALO BILLS ***\n
                Tout ce qu'il y a à savoir sur les BUFFALO BILLS\n
                Les Buffalo Bills ont été fondés en 1960, originalement membres de l'American Football League les bills ont rejoint la NFL en 1970
                lors de la fusion des deux ligues.\n
                L'équipe tient son nom d'une figure historique des états-unis, William Frederick Cody connu sous le surnom de Buffalo Bill.\n
                Avant de rejoindre la NFL, les Bills ont été Champions AFL à deux reprises, en 1964 puis en 1965. Depuis les Bills, n'ont pas été 
                capables de renouer avec le même succès, malgré un sursaut au tout début des années 90 avec un record de 4 participations consécutives
                au Super Bowl, tous perdus.\n
                Cependant, les Bills sont revenus au premier plan ces dernières années et vont entamer cette saison en tant que grand favoris pour le titre.\n
                Les Bills jouent au Highmark Stadium, à Orchard Park à l'est de New York. L'équipe de Buffalo est la seule des trois équipes de
                l'état de New York à y jouer.\n
                Inauguré en 1973, c'est l'un des plus vieux stades encore en activité aujourdh'ui.\n
                Les couleurs de l'équipe sont le bleu, le blanc et le rouge.\n
                Les bills sont également réputés pour leurs fans totalement fous, qui ont pour rituel de casser des tables en sautant dessus.
                ''']    
    elif selected_team=="Colts" : 
        return ['''
                *** INDIANAPOLIS COLTS ***\n
                De Baltimore à Indianapolis, tout savoir sur les COLTS\n
                Fondés en 1953, les Colts ont toujours fait partie de la NFL.\n
                Les débuts de la franchise se font à Baltimore où les Colts joueront et seront champions NFL à 3 reprises et gagneront 1 Super Bowl.
                Avant de rejoindre la ville d'Indianapolis en 1984.\n
                Les débuts dans L'Indiana des Colts furent compliqués, avec une seule apparition en playoffs entre 1984 et 1995.\n
                Mais les années 2000 ont été synonime de renouveau pour l'équipe d'Indianapolis notamment grâce à Peyton Manning qui emmena les 
                Colts à 2 Super Bowls dont 1 gangé.\n
                Inauguré en 2008, les Colts jouent au Lucas Oil Stadium devant 67.000 spectacteurs.\n
                Célèbre notamment pour ses grandes baies vitrées et son toit rétractable, le stade acceuille chaque année le NFL Souting Combine.\n
                Les couleurs des Colts sont le bleu et le blanc.\n
                La mascotte des Colts, un cheval bleu appelé "Blue" est également très connu pour être l'une des plus drôles de la ligue.
                '''] 
    else:
        return ['''''']
    
@app.callback(
    [Output(component_id='passing-completions-graph',component_property='figure'),
     Output(component_id='passing-yards-graph',component_property='figure'),
     Output(component_id='pass-td-int-graph',component_property='figure')],
    [Input(component_id='team-dropdown',component_property='value'),
     Input(component_id='slider-passing-year',component_property='value')]
)
   
def update_figures(selected_team, selected_year):
    
    """Fonction pour actualiser les trois graphiques affichés pour les stats de passe des joueurs Quaterbacks (QBs) de l'équipe choisie et par rappport à l'année choisie 

    Args :
        selected_team (factor) : selected_team est l'option sélectionnée par le team-dropdown, elle permet de trier les données de la dataframe à afficher 
        selected_year (int) : selected_team est l'option sélectionnée par le slider des années, elle permet de trier les données avec l'année choisie. 
    Returns:
        fig1,fig2,fig3 : les trois graphiques qui vont être afficher dans les composants graphiques du module dcc
        fig1 est un line plot des passes tentées et complétées des quaterbacks en fonction des semaines de la saison 
        fig2 est un line plot du nombre de yards à la passe des quaterbacks en fonction des semaines de la saison
        fig3 est un bar plot des passes touchdowns et des passes interceptées des quaterbacks en fonction des semaines de la saison 
    """
    # création de la dataframe des données de passes pour l'équipe choisie       
    dfs = []
    for _ in range(1,18):
        df = pd.DataFrame(list(client['nfl']['projet']['players'][f'year{selected_year}'][f"reg{_}"].find({"$and":[{"position":"QB"},{"teamName":f"{selected_team}"}]})))
        df["week"] = f"reg{_}"

        dfs.append(df)
        
    for _ in range(1,5):
        df = pd.DataFrame(list(client['nfl']['projet']['players'][f'year{selected_year}'][f"post{_}"].find({"$and":[{"position":"QB"},{"teamName":f"{selected_team}"}]})))
        df["week"] = dict_postSeasonKey[f"post{_}"]
        
        dfs.append(df)
        
    dataFrame = pd.concat(dfs)
    # print(dataFrame)
    
    ordered_weeks=["reg1","reg2","reg3","reg4","reg5","reg6","reg7","reg8","reg9","reg10","reg11","reg12","reg13","reg14","reg15","reg16","reg17","reg18","Wild Card Weekend","Divisional Playoffs" ,"Conference Championships","Super Bowl"]
    passing_stats = ['passingAttempts', 'passingCompletions', 'passingTouchdowns', 'passingYards','passingInterceptions']
    
    # première figure affichée 
    fig1 = px.line(dataFrame, x= 'week', y =[passing_stats[0],passing_stats[1]], color='displayName', markers=True, category_orders={"week" :ordered_weeks })
    fig1.update_traces(mode="markers+lines", hovertemplate=None)
    fig1.update_layout(hovermode="x")
    fig1.update_layout(
        title='Passing rates from Pittsburgh Steelers players',
        xaxis_tickfont_size=14,
        xaxis_title='Weeks',
        yaxis=dict(
            title='Passing completions function of passing attempts',
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
    )
    
    # deuxième figure affichée 
    fig2 = px.line(dataFrame, x= 'week', y =passing_stats[3], labels={'x':'Weeks', 'y':'Total Yards'}, color='displayName', markers=True, category_orders={"week" :ordered_weeks } )
    fig2.update_traces(mode="markers+lines", hovertemplate=None)
    fig2.update_layout(hovermode="x")
    fig2.update_layout(
        title='Passing yards Pittsburgh Steelers players',
        xaxis_tickfont_size=14,
        xaxis_title='Weeks',
        yaxis=dict(
            title='Passing yards',
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
    )

    # troisième figure affichée 
    fig3 = go.Figure()
    fig3.add_trace(go.Bar(
        x=dataFrame["week"],
        y=dataFrame[passing_stats[2]],
        name='Total touchdown passes',
        marker_color='rgb(55, 83, 109)',
        text=dataFrame["displayName"],
        hovertemplate="<br>".join([
                "passing touchdowns: %{y}",
            ])
        
    ))
    fig3.add_trace(go.Bar(
        x=dataFrame["week"],
        y=dataFrame[passing_stats[4]],
        name='Total intercepted passes',
        marker_color='rgb(26, 118, 255)',
        text=dataFrame["displayName"],
        hovertemplate="<br>".join([
                "passing attempts: %{y}",
            ])
    ))

    # Here we modify the tickangle of the xaxis, resulting in rotated labels.
    fig3.update_layout(barmode='group', xaxis_tickangle=90, hovermode="x")
    fig3.update_layout(
        title='Pass Touchdowns and pass interceptions of QB players from Pittsburgh Steelers',
        xaxis_tickfont_size=14,
        yaxis=dict(
            title='Pass touchdown and pass interception',
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.15, # gap between bars of adjacent location coordinates.
        bargroupgap=0.1, # gap between bars of the same location coordinate.
    )
    return fig1, fig2, fig3

@app.callback(
    [Output(component_id='rushing-yards-graph',component_property='figure'),
     Output(component_id='rushing-attempts-graph',component_property='figure'),
     Output(component_id='rushing-touchdowns-graph',component_property='figure')],
    [Input(component_id='team-dropdown',component_property='value'),
     Input(component_id='slider-rushing-year',component_property='value')]
)
def update_figure(selected_team, selected_year):

    """Fonction pour actualiser les trois graphiques affichés pour les stats de courses des joueurs offensifs de l'équipe choisie et par rappport à l'année choisie 

    Args :
        selected_team (factor) : selected_team est l'option sélectionnée par le team-dropdown, elle permet de trier les données de la dataframe à afficher 
        selected_year (int) : selected_team est l'option sélectionnée par le slider des années, elle permet de trier les données avec l'année choisie. 
    Returns:
        fig1,fig2,fig3 : les trois graphiques qui vont être afficher dans les composants graphiques du module dcc
        fig1 est un scatter plot du nombre de Yards gagnés à la course des joueurs offensifs en fonction des semaines de la saison, la taille des points
        dépend du nombre moyen de yards gagnés
        fig2 est un scatter plot du nombre de courses tentées en fonction des semaines de la saison, la taille du point dépend de ce nombre
        fig3 est un bar plot des touchdowns marqués à la course en fonction des semaines de la saison 
    """
    # sélection des données de la dataframe qui nous intéressent, on s'intéresse à certains postes de l'offense spécifique
    dfs = []
    for _ in range(1,18):
        df = pd.DataFrame(list(client['nfl']['projet']['players'][f'year{selected_year}'][f"reg{_}"].find({"$and":[{"$or":[{"position":"RB"},{"position":"FB"}]},{"teamName":f"{selected_team}"}]})))
        df["week"] = f"reg{_}"

        dfs.append(df)

    for _ in range(1,5):
        df = pd.DataFrame(list(client['nfl']['projet']['players']['year2017'][f"post{_}"].find({"$and":[{"$or":[{"position":"RB"},{"position":"FB"}]},{"teamName":"Steelers"}]})))
        df["week"] = dict_postSeasonKey[f"post{_}"]
        
        dfs.append(df)
    
    dataFrame = pd.concat(dfs)
    
    # print(dataFrame)
    
    rushing_stats =['rushingAttempts', 'rushingAverageYards', 'rushingTouchdowns', 'rushingYards']
    ordered_weeks=["reg1","reg2","reg3","reg4","reg5","reg6","reg7","reg8","reg9","reg10","reg11","reg12","reg13","reg14","reg15","reg16","reg17","reg18","Wild Card Weekend","Divisional Playoffs" ,"Conference Championships","Super Bowl"]

    dataFrame['abs_rushAverage'] = np.abs(dataFrame['rushingAverageYards'])

    #scatter plot des yards à la course dont la taile du point dépend du nombre de yards moyen à la course.
    #plus le point est gros, plus le joeur associé a un grand nombre de yards moyen gagné par course 
    fig1 = px.scatter(dataFrame, x = "week", y = "rushingYards", size = "abs_rushAverage", color = "displayName", category_orders={"week" :ordered_weeks } )
    fig1.update_traces(hovertemplate =None)
    fig1.update_layout(hovermode="x", xaxis_tickangle=90)
    fig1.update_layout(
        title='Rushing yards Pittsburgh Steelers players',
        xaxis_tickfont_size=14,
        xaxis_title='Weeks',
        yaxis=dict(
            title='Rushing yards',
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
    )
    
    #scatter plot des tentatives de courses par semaine  dont la taille du point est corrélée au nombre de tentaives de courses par semaine
    fig2 = px.scatter(dataFrame, x="week", y="rushingAttempts", size= 'rushingAttempts', color = "displayName", category_orders={"week" :ordered_weeks })
    fig2.update_traces( hovertemplate=None)
    fig2.update_layout(hovermode="x", xaxis_tickangle=90)
    fig2.update_layout(
        title='Rushing attempts Pittsburgh Steelers players',

        xaxis_title='Weeks',
        yaxis=dict(
            title='Rushing attempts',
            titlefont_size=16,
        ),
        legend=dict(
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
    )
    
    #bar plot des touchdowns à la course 
    fig3 = px.bar(dataFrame.query('rushingTouchdowns != 0'), x="week", y="rushingTouchdowns", color='lastName', category_orders={"week" :ordered_weeks })
    fig3.update_traces( hovertemplate=None)
    fig3.update_layout(barmode='group', hovermode="x unified", xaxis_tickangle=90)
    fig3.update_layout(
        title='Bar plot of touchdowns by rushing from Steelers players',
        xaxis_title='Weeks',
        xaxis_showgrid=False,   #désactivation des lignes des axes
        xaxis_linecolor="#BCCCDC",
        plot_bgcolor="#FFF", 
        yaxis=dict(
            title='Rushing touchdowns',
            titlefont_size=16,
            showgrid=False, #désactivation des lignes des axes
            linecolor="#BCCCDC",
            visible=False
        ),
        legend=dict(
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
    )
    
    return fig1, fig2, fig3  

@app.callback(
    [Output(component_id='receiving-receptions-graph',component_property='figure'),
     Output(component_id='receiving-attempts-graph',component_property='figure'),
     Output(component_id='receiving-touchdowns-graph',component_property='figure')],
    [Input(component_id='team-dropdown',component_property='value'),
     Input(component_id='slider-receiving-year',component_property='value')]
)
    
def update_figure(selected_team,selected_year):
    
    """Fonction pour actualiser les trois graphiques affichés pour les stats de receptions des joueurs offensifs de l'équipe choisie et par rappport à l'année choisie 

    Args :
        selected_team (factor) : selected_team est l'option sélectionnée par le team-dropdown, elle permet de trier les données de la dataframe à afficher 
        selected_year (int) : selected_team est l'option sélectionnée par le slider des années, elle permet de trier les données avec l'année choisie. 
    Returns:
        fig1,fig2,fig3 : les trois graphiques qui vont être afficher dans les composants graphiques du module dcc
        fig1 est un line plot du nombre de passes lancées et les passes receptionnées en fonction des semaines de la saison 
        fig2 est un scatter plot du nombre de yards à la réception en fonction des semaines de la saison
        fig3 est un bar plot des touchdowns marqués à la réception en fonction des semaines de la saison 
    """
    # sélection des données de la dataframe qui nous intéressent, on s'intéresse à certains postes de l'offense spécifique
    dfs = []
    for _ in range(1,18):
        df = pd.DataFrame(list(client['nfl']['projet']['players'][f'year{selected_year}'][f"reg{_}"].find({"$and":[{"$or":[{"position":"RB"},{"position":"WR"},{"position":"TE"}]},{"teamName":f"{selected_team}"}]})))
        df["week"] = f"reg{_}"

        dfs.append(df)
        
    for _ in range(1,5):
        df = pd.DataFrame(list(client['nfl']['projet']['players'][f'year{selected_year}'][f"post{_}"].find({"$and":[{"$or":[{"position":"RB"},{"position":"WR"},{"position":"TE"}]},{"teamName":f"{selected_team}"}]})))
        df["week"] = dict_postSeasonKey[f"post{_}"]
        
        dfs.append(df)

    dataFrame = pd.concat(dfs)
# print(dataFrame)
    
    #ajout d'une nouvelle colonne 'receivingFail' comme la différence de la colonne 'receivingTarget' et de la colonne 'receivingReceptions'
    receiving_stats = ['receivingReceptions', 'receivingTarget', 'receivingTouchdowns', 'receivingYards']
    ordered_weeks=["reg1","reg2","reg3","reg4","reg5","reg6","reg7","reg8","reg9","reg10","reg11","reg12","reg13","reg14","reg15","reg16","reg17","reg18","Wild Card Weekend","Divisional Playoffs" ,"Conference Championships","Super Bowl"]

    dataFrame["inv_receivingFail"] = np.abs(dataFrame["receivingTarget"] - dataFrame["receivingReceptions"])

    # Premier graphe à afficher
    fig1 = px.scatter(dataFrame.query('receivingReceptions!=0'), x="week", y='receivingReceptions',size='inv_receivingFail', color='displayName', category_orders={"week" :ordered_weeks })
    fig1.update_traces( hovertemplate=None)
    fig1.update_layout(hovermode="x", xaxis_tickangle=90)
    fig1.update_layout(
        title='Nombre de passes réceptionnées par les joueurs des Steelers dont la taille dépend du nombre de passes non réceptionnées',

        xaxis_title='Weeks',
        yaxis=dict(
            title='Receiving receptions',
            titlefont_size=16,

        ),
        legend=dict(

            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
    )

    # Deuxième graphe à afficher 
    fig2 = px.scatter(dataFrame, x="week", y="rushingAttempts", size= 'rushingAttempts', color = "displayName", category_orders={"week" :ordered_weeks })
    fig2.update_traces( hovertemplate=None)
    fig2.update_layout(hovermode="x", xaxis_tickangle=90)
    fig2.update_layout(
        title='Rushing attempts Pittsburgh Steelers players',

        xaxis_title='Weeks',
        yaxis=dict(
            title='Rushing attempts',
            titlefont_size=16,
        ),
        legend=dict(
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
    )

    # Troisième graphe à afficher
    #bar plot des touchdowns à la course 
    fig3 = px.bar(dataFrame.query('rushingTouchdowns != 0'), x="week", y="rushingTouchdowns", color='lastName', category_orders={"week" :ordered_weeks })
    fig3.update_traces( hovertemplate=None)
    fig3.update_layout(barmode='group', hovermode="x unified", xaxis_tickangle=90)
    fig3.update_layout(
        title='Bar plot of touchdowns by rushing from Steelers players',
        xaxis_title='Weeks',
        xaxis_showgrid=False,   #désactivation des lignes des axes
        xaxis_linecolor="#BCCCDC",
        plot_bgcolor="#FFF", 
        yaxis=dict(
            title='Rushing touchdowns',
            titlefont_size=16,
            showgrid=False, #désactivation des lignes des axes
            linecolor="#BCCCDC",
            visible=False
        ),
        legend=dict(
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
    )
    
    return fig1, fig2, fig3

#   FIN DE LA PARTIE CALLBACKS FUNCTIONS DU DASHBOARD
###################################################################################################################################################
  
if __name__ == '__main__':
    app.run_server(debug=True)