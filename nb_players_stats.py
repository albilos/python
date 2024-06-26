# -*- coding: utf-8 -*-
"""NB_players_stats.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_HiVAWOp8dUN3m2cDBQxIlVl9goMqI_b
"""

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px
import plotly

r = requests.get('http://www.basketball-reference.com/leagues/NBA_2022_per_game.html') # collecter le contenu de l'url 
soup = BeautifulSoup(r.content,'html.parser')
soup.prettify

tableau = soup.find_all('tr',attrs={'class':'full_table'})
tableau

joueurs = []
for i in range(len(tableau)):
  joueur = []
  for j in tableau[i].find_all('td'):
    joueur.append(j.text)
  joueurs.append(joueur)

joueurs

titre = soup.find(class_='thead')
titre.text
Nom = [titre.text for item in titre][0]
Nom

Nom_clean = Nom.split('\n')[2:-1]
Nom_clean

df = pd.DataFrame(joueurs,columns=Nom_clean)

"""# Nouvelle section

# statistique des joueurs de NBA FRANCHISE
"""

df.head(10)

df.info()

df.isnull().sum()

df.tail(10)

df['3P'].astype(float)

df.shape

df.iloc[4:10,[0,1,2,3]]

df.columns

df.loc[100:200,['Player','Pos','Age','Tm','G','GS','MP']]

tab = (df['3P']>='10.0')
tab_1 = df.loc[tab,['Player','Tm','3P','PTS','BLK','AST']].head(30)
tab_1.sort_values(['3P','PTS','AST'],ascending=False)

df.isnull().sum()

df[['MP','TRB','STL','BLK','PTS','3P']].astype(float)

data = df[['Player','Tm','Pos','G','GS','MP','FG','3P','TRB','AST','STL','BLK','PTS']]
data

data[['G','GS','3P','BLK','PTS']] = data[['G','GS','3P','BLK','PTS']].astype(float)

data

pip install dash

pip install jupyter-dash

pip install matplotlib-venn

!apt-get -qq install -y libfluidsynth1

# https://pypi.python.org/pypi/libarchive
!apt-get -qq install -y libarchive-dev && pip install -U libarchive
import libarchive

# https://pypi.python.org/pypi/pydot
!apt-get -qq install -y graphviz && pip install pydot
import pydot

!pip install cartopy
import cartopy

pip install dash-html-components