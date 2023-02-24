{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "bab90583",
   "metadata": {},
   "source": [
    "# 1. Importation des librairies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "a677d2d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import pandas as pd \n",
    "from urllib.request import urlopen\n",
    "import json\n",
    "import time\n",
    "\n",
    "import pandas as pd \n",
    "import plotly.graph_objects as go\n",
    "import plotly.express as px \n",
    "import numpy as np \n",
    "from plotly.subplots import make_subplots"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "83923069",
   "metadata": {},
   "source": [
    "Dictionnaire des clés des équipes associés aux équipes. Les clés servent pour l'identification des équipes sur la page officielle de la NFL.\n",
    "Le premier dictionnaire associe le nom des équipes à leure clé respective et le deuxième dictionnaire associe les clés aux noms des équipes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "ece15c3c",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict_nameTeam = {\"steelers\" :\"10403900-8251-6892-d81c-4348525c2d47\",\n",
    "\"broncos\": \"10401400-b89b-96e5-55d1-caa7e18de3d8\",\n",
    "\"seahawks\" :\"10404600-adcd-28ac-5826-b4d95ec2a228\",\n",
    "\"rams\": \"10402510-8931-0d5f-9815-79bb79649a65\",\n",
    "\"falcons\": \"10400200-f401-4e53-5175-0974e4f16cf7\",\n",
    "\"jets\": \"10403430-1bc3-42c4-c7d8-39f38aed5f12\",\n",
    "\"lions\": \"10401540-f97c-2d19-6fcd-fac6490a48b7\",\n",
    "\"vikings\": \"10403000-5851-f9d5-da45-78365a05b6b0\",\n",
    "\"saints\":\"10403300-f235-cf9b-6d3a-2f182be48dd1\",\n",
    "\"redskins\":\"10405110-ec3c-669e-2614-db3dc1736e95\",\n",
    "\"football team\": \"10405110-ec3c-669e-2614-db3dc1736e95\",\n",
    "\"commanders\": \"10405110-ec3c-669e-2614-db3dc1736e95\",\n",
    "\"texans\" :\"10402120-b0bc-693d-098a-803014096eb0\",\n",
    "\"patriots\" :\"10403200-69ab-9ea6-5af5-e240fbc08bea\",\n",
    "\"browns\":\"10401050-5e38-b907-1be1-55b91b19c057\",\n",
    "\"ravens\":\"10400325-48de-3d6a-be29-8f829437f4c8\",\n",
    "\"buccaneers\":\"10404900-d59e-b449-ef75-961e09ca027e\",\n",
    "\"panthers\":\"10400750-259b-33ac-eee3-a3852e83cd1f\",\n",
    "\"bengals\":\"10400920-57c1-7656-e77e-1af3d900483e\",\n",
    "\"cowboys\":\"10401200-a308-98ca-ad5f-95df2fefea68\",\n",
    "\"giants\":\"10403410-997c-9c75-256b-3b012f468bd0\",\n",
    "\"jaguars\":\"10402250-89fe-7b86-ef98-9062cd354256\",\n",
    "\"colts\":\"10402200-2ea3-84c3-e627-6a6b3b39d56d\",\n",
    "\"titans\":\"10402100-447f-396e-8149-0a434ffb2f23\",\n",
    "\"packers\":\"10401800-ab22-323d-721a-cee4713c4c2d\",\n",
    "\"raiders\":\"10402520-96bf-e9f2-4f68-8521ca896060\",\n",
    "\"chargers\":\"10404400-3b35-073f-197e-194bb8240723\",\n",
    "\"chiefs\":\"10402310-a47e-10ea-7442-16b633633637\",\n",
    "\"49ers\":\"10404500-e7cb-7fce-3f10-4eeb269bd179\",\n",
    "\"dolphins\":\"10402700-1662-d8ad-f45c-0b0ea460d045\",\n",
    "\"bears\":\"10400810-db30-43d6-221c-620006f3ca19\",\n",
    "\"cardinals\":\"10403800-517c-7b8c-65a3-c61b95d86123\",\n",
    "\"eagles\":\"10403700-b939-3cbd-3d16-24d4d6742fa2\",\n",
    "\"bills\":\"10400610-c40e-a673-1743-2ce2a5d5d731\"}\n",
    "\n",
    "dict_idTeam= { \"10403900-8251-6892-d81c-4348525c2d47\":\"steelers\",\n",
    "\"10401400-b89b-96e5-55d1-caa7e18de3d8\":\"broncos\",\n",
    "\"10404600-adcd-28ac-5826-b4d95ec2a228\":\"seahawks\",\n",
    "\"10402510-8931-0d5f-9815-79bb79649a65\":\"rams\",\n",
    "\"10400200-f401-4e53-5175-0974e4f16cf7\":\"falcons\",\n",
    "\"10403430-1bc3-42c4-c7d8-39f38aed5f12\":\"jets\",\n",
    " \"10401540-f97c-2d19-6fcd-fac6490a48b7\":\"lions\",\n",
    "\"10403000-5851-f9d5-da45-78365a05b6b0\":\"vikings\",\n",
    "\"10403300-f235-cf9b-6d3a-2f182be48dd1\":\"saints\",\n",
    " \"10405110-ec3c-669e-2614-db3dc1736e95\":{\"2017\":\"redskins\",\n",
    "                                         \"2018\":\"redskins\",\n",
    "                                         \"2019\":\"redskins\",\n",
    "                                         \"2020\":\"football-team\",\"2021\":\"football-team\",\n",
    "                                         \"2022\":\"commanders\"},\n",
    "\"10402120-b0bc-693d-098a-803014096eb0\":\"texans\",\n",
    "\"10403200-69ab-9ea6-5af5-e240fbc08bea\":\"patriots\",\n",
    "\"10401050-5e38-b907-1be1-55b91b19c057\":\"browns\",\n",
    "\"10400325-48de-3d6a-be29-8f829437f4c8\":\"ravens\",\n",
    "\"10404900-d59e-b449-ef75-961e09ca027e\":\"buccaneers\",\n",
    "\"10400750-259b-33ac-eee3-a3852e83cd1f\":\"panthers\",\n",
    "\"10400920-57c1-7656-e77e-1af3d900483e\":\"bengals\",\n",
    "\"10401200-a308-98ca-ad5f-95df2fefea68\":\"cowboys\",\n",
    "\"10403410-997c-9c75-256b-3b012f468bd0\":\"giants\",\n",
    "\"10402250-89fe-7b86-ef98-9062cd354256\":\"jaguars\",\n",
    "\"10402200-2ea3-84c3-e627-6a6b3b39d56d\":\"colts\",\n",
    "\"10402100-447f-396e-8149-0a434ffb2f23\":\"titans\",\n",
    "\"10401800-ab22-323d-721a-cee4713c4c2d\":\"packers\",\n",
    "\"10402520-96bf-e9f2-4f68-8521ca896060\":\"raiders\",\n",
    "\"10404400-3b35-073f-197e-194bb8240723\":\"chargers\",\n",
    "\"10402310-a47e-10ea-7442-16b633633637\":\"chiefs\",\n",
    "\"10404500-e7cb-7fce-3f10-4eeb269bd179\":\"49ers\",\n",
    "\"10402700-1662-d8ad-f45c-0b0ea460d045\":\"dolphins\",\n",
    "\"10400810-db30-43d6-221c-620006f3ca19\":\"bears\",\n",
    "\"10403800-517c-7b8c-65a3-c61b95d86123\":\"cardinals\",\n",
    "\"10403700-b939-3cbd-3d16-24d4d6742fa2\":\"eagles\",\n",
    "\"10400610-c40e-a673-1743-2ce2a5d5d731\":\"bills\"}\n",
    "\n",
    "postSeason={1:\"Wild Card Weekend\",  2:\"Divisional Playoffs\" ,3:\"Conference Championships\" , 4:\"Super Bowl\"}\n",
    "\n",
    "dict_postSeason = {\"Wild Card Weekend\":\"post1\", \"Divisional Playoffs\":\"post2\", \"Conference Championships\":\"post3\", \"Super Bowl\":\"post4\"}\n",
    "dict_postSeasonKey = {\"post1\":\"Wild Card Weekend\", \"post2\":\"Divisional Playoffs\", \"post3\":\"Conference Championships\", \"post4\":\"Super Bowl\"}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cf77ad23",
   "metadata": {},
   "source": [
    "# 2. Partie Web Scrapping\n",
    "\n",
    "La partie Web Scrapping est décomposée en 2 parties, une première partie qui s'occupe de récupérer les données de saison régulière et une deuxième partie qui s'occupe de récupérer les données de post saison.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "45763d9e",
   "metadata": {},
   "source": [
    "## La cellule suivante contient le headers utilisé pour toute la partie web scraping, avant de lancer le scraping sur votre machine veuillez suivre le tutoriel sur comment récupérer la valeur de l'authorization depuis le site NFL"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "fb59afd9",
   "metadata": {},
   "outputs": [],
   "source": [
    "headers = {'User-Agent':\n",
    "           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',\n",
    "           'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJZCI6ImU1MzVjN2MwLTgxN2YtNDc3Ni04OTkwLTU2NTU2ZjhiMTkyOCIsImNsaWVudEtleSI6IjRjRlVXNkRtd0pwelQ5TDdMckczcVJBY0FCRzVzMDRnIiwiaXNzIjoiTkZMIiwiZGV2aWNlSWQiOiIxNTBlOGQ5OS04ZTk5LTQxNjgtYmUyZS1lNDBhYTNjMGZiYzMiLCJwbGFucyI6W3sicGxhbiI6ImZyZWUiLCJleHBpcmF0aW9uRGF0ZSI6IjIwMjQtMDItMjQiLCJzb3VyY2UiOiJORkwiLCJzdGFydERhdGUiOiIyMDIzLTAyLTI0Iiwic3RhdHVzIjoiQUNUSVZFIiwidHJpYWwiOmZhbHNlfV0sIkRpc3BsYXlOYW1lIjoiV0VCX0RFU0tUT1BfREVTS1RPUCIsIk5vdGVzIjoiIiwiZm9ybUZhY3RvciI6IkRFU0tUT1AiLCJsdXJhQXBwS2V5IjoiU1pzNTdkQkdSeGJMNzI4bFZwN0RZUSIsInBsYXRmb3JtIjoiREVTS1RPUCIsInByb2R1Y3ROYW1lIjoiV0VCIiwiY291bnRyeUNvZGUiOiJGUiIsImRtYUNvZGUiOiIyNTAwNzUiLCJobWFUZWFtcyI6W10sImJyb3dzZXIiOiJDaHJvbWUiLCJjZWxsdWxhciI6ZmFsc2UsImVudmlyb25tZW50IjoicHJvZHVjdGlvbiIsInJvbGVzIjpbImZyZWUiXSwiZXhwIjoxNjc3MjU1MjA5fQ.9iCvdaT3e_S2_vVBYKT3w0QfqSb2-81gc-OlBgb0yx0'\n",
    "          }"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4f21352e",
   "metadata": {},
   "source": [
    "### 1. Saison régulière \n",
    "\n",
    "#### Récupération des couples de nom des équipes jouant les matchs\n",
    "\n",
    "Tout d'abord, je dois récupérer le nom des équipes qui s'affrontent toutes les semaines pour construire les urls associées. Les urls des matchs sont toutes construites selon le même schéma suivant : \n",
    "1. le protocole, le sous-domaine, le nom de domaine (ici NFL), le sous-domaine et du répertoire principal (ici \"/games/\") :\n",
    "    \"https://www.nfl.com/games/\"\n",
    "\n",
    "2. l'url du match : \n",
    "    \"equipe1-at-equipe2-annee-reg-semaine\" , equipe 1 est l'équipe jouant à l'extérieur et equipe 2 l'équipe à domicile, annee et semaine correspondent respectivement à la saison et à la semaine de jeu.\n",
    "\n",
    "3. pour finir la fin de l'url : \n",
    "    \"?active-tab=watch\"\n",
    "\n",
    "\n",
    "La première ligne avec la variable gameTeams contient toutes tuples des équipes que j'ai récupéré en scrapant, ça me permet de lancer directement les codes qui vont suivre. \n",
    "Vous pouvez essayer de lancer le scraping en décommentant les deux cellules de code qui suivent, mais ATTENTION pensez bien à récupérer une autorisation sur le site NFL et de la mettre à jour dans le headers pour pouvoir le lancer.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba088907",
   "metadata": {},
   "source": [
    "### J'ai créé le dictionnaire gameTeams avec tous les tuples des équipes qui s'affrontent pour des raisons de facilité. Pour récupérer vous-même, vous pouvez décommenter les deux cellules qui suivent et les lancer pour récupérer le dictionnaire.\n",
    "\n",
    "### Attention! Il faut que la valeur du headers soit bien mis à jour pour lancer les codes suivants sinon vous rencontrerez une erreur."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c78650c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "gameTeams = {'2017': {'reg1': [('chiefs', 'patriots'), ('jets', 'bills'), ('falcons', 'bears'), ('ravens', 'bengals'), ('steelers', 'browns'), ('cardinals', 'lions'), ('jaguars', 'texans'), ('raiders', 'titans'), ('eagles', 'redskins'), ('colts', 'rams'), ('seahawks', 'packers'), ('panthers', '49ers'), ('giants', 'cowboys'), ('saints', 'vikings'), ('chargers', 'broncos')], 'reg2': [('texans', 'bengals'), ('browns', 'ravens'), ('bills', 'panthers'), ('cardinals', 'colts'), ('titans', 'jaguars'), ('eagles', 'chiefs'), ('patriots', 'saints'), ('vikings', 'steelers'), ('bears', 'buccaneers'), ('dolphins', 'chargers'), ('jets', 'raiders'), ('cowboys', 'broncos'), ('redskins', 'rams'), ('49ers', 'seahawks'), ('packers', 'falcons'), ('lions', 'giants')], 'reg3': [('rams', '49ers'), ('ravens', 'jaguars'), ('broncos', 'bills'), ('saints', 'panthers'), ('steelers', 'bears'), ('falcons', 'lions'), ('browns', 'colts'), ('buccaneers', 'vikings'), ('texans', 'patriots'), ('dolphins', 'jets'), ('giants', 'eagles'), ('seahawks', 'titans'), ('bengals', 'packers'), ('chiefs', 'chargers'), ('raiders', 'redskins'), ('cowboys', 'cardinals')], 'reg4': [('bears', 'packers'), ('saints', 'dolphins'), ('bills', 'falcons'), ('steelers', 'ravens'), ('bengals', 'browns'), ('rams', 'cowboys'), ('titans', 'texans'), ('lions', 'vikings'), ('panthers', 'patriots'), ('jaguars', 'jets'), ('49ers', 'cardinals'), ('eagles', 'chargers'), ('giants', 'buccaneers'), ('raiders', 'broncos'), ('colts', 'seahawks'), ('redskins', 'chiefs')], 'reg5': [('patriots', 'buccaneers'), ('bills', 'bengals'), ('jets', 'browns'), ('panthers', 'lions'), ('49ers', 'colts'), ('titans', 'dolphins'), ('chargers', 'giants'), ('cardinals', 'eagles'), ('jaguars', 'steelers'), ('seahawks', 'rams'), ('ravens', 'raiders'), ('packers', 'cowboys'), ('chiefs', 'texans'), ('vikings', 'bears')], 'reg6': [('eagles', 'panthers'), ('dolphins', 'falcons'), ('bears', 'ravens'), ('browns', 'texans'), ('packers', 'vikings'), ('lions', 'saints'), ('patriots', 'jets'), ('49ers', 'redskins'), ('buccaneers', 'cardinals'), ('rams', 'jaguars'), ('steelers', 'chiefs'), ('chargers', 'raiders'), ('giants', 'broncos'), ('colts', 'titans')], 'reg7': [('chiefs', 'raiders'), ('buccaneers', 'bills'), ('panthers', 'bears'), ('titans', 'browns'), ('saints', 'packers'), ('jaguars', 'colts'), ('cardinals', 'rams'), ('jets', 'dolphins'), ('ravens', 'vikings'), ('cowboys', '49ers'), ('bengals', 'steelers'), ('broncos', 'chargers'), ('seahawks', 'giants'), ('falcons', 'patriots'), ('redskins', 'eagles')], 'reg8': [('dolphins', 'ravens'), ('vikings', 'browns'), ('raiders', 'bills'), ('colts', 'bengals'), ('chargers', 'patriots'), ('bears', 'saints'), ('falcons', 'jets'), ('49ers', 'eagles'), ('panthers', 'buccaneers'), ('texans', 'seahawks'), ('cowboys', 'redskins'), ('steelers', 'lions'), ('broncos', 'chiefs')], 'reg9': [('bills', 'jets'), ('falcons', 'panthers'), ('colts', 'texans'), ('bengals', 'jaguars'), ('buccaneers', 'saints'), ('rams', 'giants'), ('broncos', 'eagles'), ('ravens', 'titans'), ('cardinals', '49ers'), ('redskins', 'seahawks'), ('chiefs', 'cowboys'), ('raiders', 'dolphins'), ('lions', 'packers')], 'reg10': [('seahawks', 'cardinals'), ('saints', 'bills'), ('packers', 'bears'), ('browns', 'lions'), ('steelers', 'colts'), ('chargers', 'jaguars'), ('jets', 'buccaneers'), ('bengals', 'titans'), ('vikings', 'redskins'), ('texans', 'rams'), ('cowboys', 'falcons'), ('giants', '49ers'), ('patriots', 'broncos'), ('dolphins', 'panthers')], 'reg11': [('titans', 'steelers'), ('lions', 'bears'), ('jaguars', 'browns'), ('ravens', 'packers'), ('cardinals', 'texans'), ('rams', 'vikings'), ('redskins', 'saints'), ('chiefs', 'giants'), ('buccaneers', 'dolphins'), ('bills', 'chargers'), ('bengals', 'broncos'), ('patriots', 'raiders'), ('eagles', 'cowboys'), ('falcons', 'seahawks')], 'reg12': [('vikings', 'lions'), ('chargers', 'cowboys'), ('giants', 'redskins'), ('buccaneers', 'falcons'), ('browns', 'bengals'), ('titans', 'colts'), ('bills', 'chiefs'), ('dolphins', 'patriots'), ('panthers', 'jets'), ('bears', 'eagles'), ('seahawks', '49ers'), ('saints', 'rams'), ('jaguars', 'cardinals'), ('broncos', 'raiders'), ('packers', 'steelers'), ('texans', 'ravens')], 'reg13': [('redskins', 'cowboys'), ('vikings', 'falcons'), ('lions', 'ravens'), ('patriots', 'bills'), ('49ers', 'bears'), ('buccaneers', 'packers'), ('colts', 'jaguars'), ('broncos', 'dolphins'), ('chiefs', 'jets'), ('texans', 'titans'), ('browns', 'chargers'), ('panthers', 'saints'), ('rams', 'cardinals'), ('giants', 'raiders'), ('eagles', 'seahawks'), ('steelers', 'bengals')], 'reg14': [('saints', 'falcons'), ('colts', 'bills'), ('vikings', 'panthers'), ('bears', 'bengals'), ('packers', 'browns'), ('49ers', 'texans'), ('raiders', 'chiefs'), ('lions', 'buccaneers'), ('cowboys', 'giants'), ('titans', 'cardinals'), ('jets', 'broncos'), ('redskins', 'chargers'), ('seahawks', 'jaguars'), ('eagles', 'rams'), ('ravens', 'steelers'), ('patriots', 'dolphins')], 'reg15': [('broncos', 'colts'), ('bears', 'lions'), ('chargers', 'chiefs'), ('dolphins', 'bills'), ('packers', 'panthers'), ('ravens', 'browns'), ('texans', 'jaguars'), ('bengals', 'vikings'), ('jets', 'saints'), ('eagles', 'giants'), ('cardinals', 'redskins'), ('rams', 'seahawks'), ('patriots', 'steelers'), ('titans', '49ers'), ('cowboys', 'raiders'), ('falcons', 'buccaneers')], 'reg16': [('colts', 'ravens'), ('vikings', 'packers'), ('buccaneers', 'panthers'), ('browns', 'bears'), ('lions', 'bengals'), ('dolphins', 'chiefs'), ('bills', 'patriots'), ('falcons', 'saints'), ('chargers', 'jets'), ('rams', 'titans'), ('broncos', 'redskins'), ('jaguars', '49ers'), ('giants', 'cardinals'), ('seahawks', 'cowboys'), ('steelers', 'texans'), ('raiders', 'eagles')], 'reg17': [('packers', 'lions'), ('texans', 'colts'), ('bears', 'vikings'), ('jets', 'patriots'), ('redskins', 'giants'), ('cowboys', 'eagles'), ('browns', 'steelers'), ('panthers', 'falcons'), ('bengals', 'ravens'), ('bills', 'dolphins'), ('saints', 'buccaneers'), ('jaguars', 'titans'), ('chiefs', 'broncos'), ('raiders', 'chargers'), ('49ers', 'rams'), ('cardinals', 'seahawks')]}, '2018': {'reg1': [('falcons', 'eagles'), ('bills', 'ravens'), ('steelers', 'browns'), ('bengals', 'colts'), ('titans', 'dolphins'), ('49ers', 'vikings'), ('texans', 'patriots'), ('buccaneers', 'saints'), ('jaguars', 'giants'), ('chiefs', 'chargers'), ('redskins', 'cardinals'), ('cowboys', 'panthers'), ('seahawks', 'broncos'), ('bears', 'packers'), ('jets', 'lions'), ('rams', 'raiders')], 'reg2': [('ravens', 'bengals'), ('panthers', 'falcons'), ('chargers', 'bills'), ('vikings', 'packers'), ('browns', 'saints'), ('dolphins', 'jets'), ('chiefs', 'steelers'), ('eagles', 'buccaneers'), ('texans', 'titans'), ('colts', 'redskins'), ('cardinals', 'rams'), ('lions', '49ers'), ('raiders', 'broncos'), ('patriots', 'jaguars'), ('giants', 'cowboys'), ('seahawks', 'bears')], 'reg3': [('jets', 'browns'), ('saints', 'falcons'), ('broncos', 'ravens'), ('bengals', 'panthers'), ('giants', 'texans'), ('titans', 'jaguars'), ('49ers', 'chiefs'), ('raiders', 'dolphins'), ('bills', 'vikings'), ('colts', 'eagles'), ('packers', 'redskins'), ('chargers', 'rams'), ('bears', 'cardinals'), ('cowboys', 'seahawks'), ('patriots', 'lions'), ('steelers', 'buccaneers')], 'reg4': [('vikings', 'rams'), ('bengals', 'falcons'), ('buccaneers', 'bears'), ('lions', 'cowboys'), ('bills', 'packers'), ('texans', 'colts'), ('jets', 'jaguars'), ('dolphins', 'patriots'), ('eagles', 'titans'), ('seahawks', 'cardinals'), ('browns', 'raiders'), ('49ers', 'chargers'), ('saints', 'giants'), ('ravens', 'steelers'), ('chiefs', 'broncos')], 'reg5': [('colts', 'patriots'), ('titans', 'bills'), ('giants', 'panthers'), ('dolphins', 'bengals'), ('ravens', 'browns'), ('packers', 'lions'), ('jaguars', 'chiefs'), ('broncos', 'jets'), ('falcons', 'steelers'), ('raiders', 'chargers'), ('vikings', 'eagles'), ('cardinals', '49ers'), ('rams', 'seahawks'), ('cowboys', 'texans'), ('redskins', 'saints')], 'reg6': [('eagles', 'giants'), ('buccaneers', 'falcons'), ('steelers', 'bengals'), ('chargers', 'browns'), ('bills', 'texans'), ('bears', 'dolphins'), ('cardinals', 'vikings'), ('colts', 'jets'), ('seahawks', 'raiders'), ('panthers', 'redskins'), ('rams', 'broncos'), ('jaguars', 'cowboys'), ('ravens', 'titans'), ('chiefs', 'patriots'), ('49ers', 'packers')], 'reg7': [('broncos', 'cardinals'), ('titans', 'chargers'), ('patriots', 'bears'), ('bills', 'colts'), ('texans', 'jaguars'), ('lions', 'dolphins'), ('vikings', 'jets'), ('panthers', 'eagles'), ('browns', 'buccaneers'), ('saints', 'ravens'), ('cowboys', 'redskins'), ('rams', '49ers'), ('bengals', 'chiefs'), ('giants', 'falcons')], 'reg8': [('dolphins', 'texans'), ('eagles', 'jaguars'), ('ravens', 'panthers'), ('jets', 'bears'), ('buccaneers', 'bengals'), ('seahawks', 'lions'), ('broncos', 'chiefs'), ('redskins', 'giants'), ('browns', 'steelers'), ('colts', 'raiders'), ('49ers', 'cardinals'), ('packers', 'rams'), ('saints', 'vikings'), ('patriots', 'bills')], 'reg9': [('raiders', '49ers'), ('steelers', 'ravens'), ('bears', 'bills'), ('buccaneers', 'panthers'), ('chiefs', 'browns'), ('jets', 'dolphins'), ('lions', 'vikings'), ('falcons', 'redskins'), ('texans', 'broncos'), ('chargers', 'seahawks'), ('rams', 'saints'), ('packers', 'patriots'), ('titans', 'cowboys')], 'reg10': [('panthers', 'steelers'), ('lions', 'bears'), ('saints', 'bengals'), ('falcons', 'browns'), ('jaguars', 'colts'), ('cardinals', 'chiefs'), ('bills', 'jets'), ('redskins', 'buccaneers'), ('patriots', 'titans'), ('chargers', 'raiders'), ('dolphins', 'packers'), ('seahawks', 'rams'), ('cowboys', 'eagles'), ('giants', '49ers')], 'reg11': [('packers', 'seahawks'), ('cowboys', 'falcons'), ('bengals', 'ravens'), ('panthers', 'lions'), ('titans', 'colts'), ('buccaneers', 'giants'), ('texans', 'redskins'), ('steelers', 'jaguars'), ('raiders', 'cardinals'), ('broncos', 'chargers'), ('eagles', 'saints'), ('vikings', 'bears'), ('chiefs', 'rams')], 'reg12': [('bears', 'lions'), ('redskins', 'cowboys'), ('falcons', 'saints'), ('raiders', 'ravens'), ('jaguars', 'bills'), ('seahawks', 'panthers'), ('browns', 'bengals'), ('patriots', 'jets'), ('giants', 'eagles'), ('49ers', 'buccaneers'), ('cardinals', 'chargers'), ('dolphins', 'colts'), ('steelers', 'broncos'), ('packers', 'vikings'), ('titans', 'texans')], 'reg13': [('saints', 'cowboys'), ('ravens', 'falcons'), ('broncos', 'bengals'), ('rams', 'lions'), ('cardinals', 'packers'), ('browns', 'texans'), ('colts', 'jaguars'), ('bills', 'dolphins'), ('bears', 'giants'), ('panthers', 'buccaneers'), ('chiefs', 'raiders'), ('jets', 'titans'), ('vikings', 'patriots'), ('49ers', 'seahawks'), ('chargers', 'steelers'), ('redskins', 'eagles')], 'reg14': [('jaguars', 'titans'), ('jets', 'bills'), ('panthers', 'browns'), ('falcons', 'packers'), ('colts', 'texans'), ('ravens', 'chiefs'), ('patriots', 'dolphins'), ('saints', 'buccaneers'), ('giants', 'redskins'), ('bengals', 'chargers'), ('broncos', '49ers'), ('lions', 'cardinals'), ('eagles', 'cowboys'), ('steelers', 'raiders'), ('rams', 'bears'), ('vikings', 'seahawks')], 'reg15': [('chargers', 'chiefs'), ('texans', 'jets'), ('browns', 'broncos'), ('cardinals', 'falcons'), ('buccaneers', 'ravens'), ('lions', 'bills'), ('packers', 'bears'), ('raiders', 'bengals'), ('cowboys', 'colts'), ('redskins', 'jaguars'), ('dolphins', 'vikings'), ('titans', 'giants'), ('seahawks', '49ers'), ('patriots', 'steelers'), ('eagles', 'rams'), ('saints', 'panthers')], 'reg16': [('redskins', 'titans'), ('ravens', 'chargers'), ('giants', 'colts'), ('jaguars', 'dolphins'), ('falcons', 'panthers'), ('bengals', 'browns'), ('buccaneers', 'cowboys'), ('vikings', 'lions'), ('bills', 'patriots'), ('packers', 'jets'), ('texans', 'eagles'), ('rams', 'cardinals'), ('bears', '49ers'), ('steelers', 'saints'), ('chiefs', 'seahawks'), ('broncos', 'raiders')], 'reg17': [('dolphins', 'bills'), ('lions', 'packers'), ('jaguars', 'texans'), ('jets', 'patriots'), ('panthers', 'saints'), ('cowboys', 'giants'), ('falcons', 'buccaneers'), ('browns', 'ravens'), ('raiders', 'chiefs'), ('bears', 'vikings'), ('bengals', 'steelers'), ('eagles', 'redskins'), ('chargers', 'broncos'), ('49ers', 'rams'), ('cardinals', 'seahawks'), ('colts', 'titans')]}, '2019': {'reg1': [('packers', 'bears'), ('rams', 'panthers'), ('titans', 'browns'), ('chiefs', 'jaguars'), ('ravens', 'dolphins'), ('falcons', 'vikings'), ('bills', 'jets'), ('redskins', 'eagles'), ('colts', 'chargers'), ('bengals', 'seahawks'), ('lions', 'cardinals'), ('giants', 'cowboys'), ('49ers', 'buccaneers'), ('steelers', 'patriots'), ('texans', 'saints'), ('broncos', 'raiders')], 'reg2': [('buccaneers', 'panthers'), ('cardinals', 'ravens'), ('49ers', 'bengals'), ('chargers', 'lions'), ('vikings', 'packers'), ('jaguars', 'texans'), ('patriots', 'dolphins'), ('bills', 'giants'), ('seahawks', 'steelers'), ('colts', 'titans'), ('cowboys', 'redskins'), ('chiefs', 'raiders'), ('bears', 'broncos'), ('saints', 'rams'), ('eagles', 'falcons'), ('browns', 'jets')], 'reg3': [('titans', 'jaguars'), ('bengals', 'bills'), ('dolphins', 'cowboys'), ('broncos', 'packers'), ('falcons', 'colts'), ('ravens', 'chiefs'), ('raiders', 'vikings'), ('jets', 'patriots'), ('lions', 'eagles'), ('panthers', 'cardinals'), ('giants', 'buccaneers'), ('texans', 'chargers'), ('saints', 'seahawks'), ('steelers', '49ers'), ('rams', 'browns'), ('bears', 'redskins')], 'reg4': [('eagles', 'packers'), ('titans', 'falcons'), ('browns', 'ravens'), ('patriots', 'bills'), ('chiefs', 'lions'), ('panthers', 'texans'), ('raiders', 'colts'), ('chargers', 'dolphins'), ('redskins', 'giants'), ('seahawks', 'cardinals'), ('buccaneers', 'rams'), ('vikings', 'bears'), ('jaguars', 'broncos'), ('cowboys', 'saints'), ('bengals', 'steelers')], 'reg5': [('rams', 'seahawks'), ('jaguars', 'panthers'), ('cardinals', 'bengals'), ('falcons', 'texans'), ('buccaneers', 'saints'), ('vikings', 'giants'), ('bears', 'raiders'), ('jets', 'eagles'), ('ravens', 'steelers'), ('bills', 'titans'), ('patriots', 'redskins'), ('broncos', 'chargers'), ('packers', 'cowboys'), ('colts', 'chiefs'), ('browns', '49ers')], 'reg6': [('giants', 'patriots'), ('panthers', 'buccaneers'), ('bengals', 'ravens'), ('seahawks', 'browns'), ('saints', 'jaguars'), ('texans', 'chiefs'), ('redskins', 'dolphins'), ('eagles', 'vikings'), ('falcons', 'cardinals'), ('49ers', 'rams'), ('titans', 'broncos'), ('cowboys', 'jets'), ('steelers', 'chargers'), ('lions', 'packers')], 'reg7': [('chiefs', 'broncos'), ('rams', 'falcons'), ('dolphins', 'bills'), ('jaguars', 'bengals'), ('vikings', 'lions'), ('raiders', 'packers'), ('texans', 'colts'), ('cardinals', 'giants'), ('49ers', 'redskins'), ('chargers', 'titans'), ('saints', 'bears'), ('ravens', 'seahawks'), ('eagles', 'cowboys'), ('patriots', 'jets')], 'reg8': [('redskins', 'vikings'), ('seahawks', 'falcons'), ('eagles', 'bills'), ('chargers', 'bears'), ('giants', 'lions'), ('jets', 'jaguars'), ('bengals', 'rams'), ('cardinals', 'saints'), ('buccaneers', 'titans'), ('broncos', 'colts'), ('panthers', '49ers'), ('raiders', 'texans'), ('browns', 'patriots'), ('packers', 'chiefs'), ('dolphins', 'steelers')], 'reg9': [('49ers', 'cardinals'), ('texans', 'jaguars'), ('redskins', 'bills'), ('titans', 'panthers'), ('vikings', 'chiefs'), ('jets', 'dolphins'), ('bears', 'eagles'), ('colts', 'steelers'), ('lions', 'raiders'), ('buccaneers', 'seahawks'), ('browns', 'broncos'), ('packers', 'chargers'), ('patriots', 'ravens'), ('cowboys', 'giants')], 'reg10': [('chargers', 'raiders'), ('lions', 'bears'), ('ravens', 'bengals'), ('bills', 'browns'), ('falcons', 'saints'), ('giants', 'jets'), ('cardinals', 'buccaneers'), ('chiefs', 'titans'), ('dolphins', 'colts'), ('panthers', 'packers'), ('rams', 'steelers'), ('vikings', 'cowboys'), ('seahawks', '49ers')], 'reg11': [('steelers', 'browns'), ('texans', 'ravens'), ('falcons', 'panthers'), ('cowboys', 'lions'), ('jaguars', 'colts'), ('bills', 'dolphins'), ('broncos', 'vikings'), ('saints', 'buccaneers'), ('jets', 'redskins'), ('cardinals', '49ers'), ('bengals', 'raiders'), ('patriots', 'eagles'), ('bears', 'rams'), ('chiefs', 'chargers')], 'reg12': [('colts', 'texans'), ('buccaneers', 'falcons'), ('broncos', 'bills'), ('giants', 'bears'), ('steelers', 'bengals'), ('dolphins', 'browns'), ('panthers', 'saints'), ('raiders', 'jets'), ('lions', 'redskins'), ('seahawks', 'eagles'), ('jaguars', 'titans'), ('cowboys', 'patriots'), ('packers', '49ers'), ('ravens', 'rams')], 'reg13': [('bears', 'lions'), ('bills', 'cowboys'), ('saints', 'falcons'), ('49ers', 'ravens'), ('redskins', 'panthers'), ('jets', 'bengals'), ('titans', 'colts'), ('buccaneers', 'jaguars'), ('eagles', 'dolphins'), ('packers', 'giants'), ('browns', 'steelers'), ('rams', 'cardinals'), ('raiders', 'chiefs'), ('chargers', 'broncos'), ('patriots', 'texans'), ('vikings', 'seahawks')], 'reg14': [('cowboys', 'bears'), ('panthers', 'falcons'), ('ravens', 'bills'), ('bengals', 'browns'), ('redskins', 'packers'), ('broncos', 'texans'), ('lions', 'vikings'), ('49ers', 'saints'), ('dolphins', 'jets'), ('colts', 'buccaneers'), ('chargers', 'jaguars'), ('steelers', 'cardinals'), ('chiefs', 'patriots'), ('titans', 'raiders'), ('seahawks', 'rams'), ('giants', 'eagles')], 'reg15': [('jets', 'ravens'), ('seahawks', 'panthers'), ('patriots', 'bengals'), ('buccaneers', 'lions'), ('bears', 'packers'), ('broncos', 'chiefs'), ('dolphins', 'giants'), ('texans', 'titans'), ('eagles', 'redskins'), ('browns', 'cardinals'), ('jaguars', 'raiders'), ('vikings', 'chargers'), ('rams', 'cowboys'), ('falcons', '49ers'), ('bills', 'steelers'), ('colts', 'saints')], 'reg16': [('texans', 'buccaneers'), ('bills', 'patriots'), ('rams', '49ers'), ('jaguars', 'falcons'), ('ravens', 'browns'), ('panthers', 'colts'), ('bengals', 'dolphins'), ('steelers', 'jets'), ('saints', 'titans'), ('giants', 'redskins'), ('lions', 'broncos'), ('raiders', 'chargers'), ('cowboys', 'eagles'), ('cardinals', 'seahawks'), ('chiefs', 'bears'), ('packers', 'vikings')], 'reg17': [('jets', 'bills'), ('saints', 'panthers'), ('browns', 'bengals'), ('packers', 'lions'), ('chargers', 'chiefs'), ('bears', 'vikings'), ('dolphins', 'patriots'), ('falcons', 'buccaneers'), ('steelers', 'ravens'), ('redskins', 'cowboys'), ('titans', 'texans'), ('colts', 'jaguars'), ('eagles', 'giants'), ('raiders', 'broncos'), ('cardinals', 'rams'), ('49ers', 'seahawks')]}, '2020': {'reg1': [('texans', 'chiefs'), ('seahawks', 'falcons'), ('browns', 'ravens'), ('jets', 'bills'), ('raiders', 'panthers'), ('bears', 'lions'), ('colts', 'jaguars'), ('packers', 'vikings'), ('dolphins', 'patriots'), ('eagles', 'football-team'), ('chargers', 'bengals'), ('buccaneers', 'saints'), ('cardinals', '49ers'), ('cowboys', 'rams'), ('steelers', 'giants'), ('titans', 'broncos')], 'reg2': [('bengals', 'browns'), ('giants', 'bears'), ('falcons', 'cowboys'), ('lions', 'packers'), ('vikings', 'colts'), ('bills', 'dolphins'), ('49ers', 'jets'), ('rams', 'eagles'), ('broncos', 'steelers'), ('panthers', 'buccaneers'), ('jaguars', 'titans'), ('football-team', 'cardinals'), ('ravens', 'texans'), ('chiefs', 'chargers'), ('patriots', 'seahawks'), ('saints', 'raiders')], 'reg3': [('dolphins', 'jaguars'), ('bears', 'falcons'), ('rams', 'bills'), ('football-team', 'browns'), ('titans', 'vikings'), ('raiders', 'patriots'), ('49ers', 'giants'), ('bengals', 'eagles'), ('texans', 'steelers'), ('jets', 'colts'), ('panthers', 'chargers'), ('lions', 'cardinals'), ('buccaneers', 'broncos'), ('cowboys', 'seahawks'), ('packers', 'saints'), ('chiefs', 'ravens')], 'reg4': [('broncos', 'jets'), ('cardinals', 'panthers'), ('jaguars', 'bengals'), ('browns', 'cowboys'), ('saints', 'lions'), ('vikings', 'texans'), ('seahawks', 'dolphins'), ('chargers', 'buccaneers'), ('ravens', 'football-team'), ('giants', 'rams'), ('colts', 'bears'), ('bills', 'raiders'), ('eagles', '49ers'), ('patriots', 'chiefs'), ('falcons', 'packers')], 'reg5': [('buccaneers', 'bears'), ('panthers', 'falcons'), ('bengals', 'ravens'), ('jaguars', 'texans'), ('raiders', 'chiefs'), ('cardinals', 'jets'), ('eagles', 'steelers'), ('rams', 'football-team'), ('dolphins', '49ers'), ('colts', 'browns'), ('giants', 'cowboys'), ('vikings', 'seahawks'), ('chargers', 'saints'), ('bills', 'titans')], 'reg6': [('bears', 'panthers'), ('bengals', 'colts'), ('lions', 'jaguars'), ('falcons', 'vikings'), ('football-team', 'giants'), ('ravens', 'eagles'), ('browns', 'steelers'), ('texans', 'titans'), ('broncos', 'patriots'), ('jets', 'dolphins'), ('packers', 'buccaneers'), ('rams', '49ers'), ('chiefs', 'bills'), ('cardinals', 'cowboys')], 'reg7': [('giants', 'eagles'), ('lions', 'falcons'), ('browns', 'bengals'), ('packers', 'texans'), ('panthers', 'saints'), ('bills', 'jets'), ('cowboys', 'football-team'), ('steelers', 'titans'), ('buccaneers', 'raiders'), ('chiefs', 'broncos'), ('49ers', 'patriots'), ('jaguars', 'chargers'), ('seahawks', 'cardinals'), ('bears', 'rams')], 'reg8': [('falcons', 'panthers'), ('patriots', 'bills'), ('titans', 'bengals'), ('raiders', 'browns'), ('colts', 'lions'), ('vikings', 'packers'), ('jets', 'chiefs'), ('rams', 'dolphins'), ('steelers', 'ravens'), ('chargers', 'broncos'), ('saints', 'bears'), ('49ers', 'seahawks'), ('cowboys', 'eagles'), ('buccaneers', 'giants')], 'reg9': [('packers', '49ers'), ('broncos', 'falcons'), ('seahawks', 'bills'), ('ravens', 'colts'), ('texans', 'jaguars'), ('panthers', 'chiefs'), ('lions', 'vikings'), ('bears', 'titans'), ('giants', 'football-team'), ('raiders', 'chargers'), ('dolphins', 'cardinals'), ('steelers', 'cowboys'), ('saints', 'buccaneers'), ('patriots', 'jets')], 'reg10': [('colts', 'titans'), ('buccaneers', 'panthers'), ('texans', 'browns'), ('football-team', 'lions'), ('jaguars', 'packers'), ('eagles', 'giants'), ('bills', 'cardinals'), ('broncos', 'raiders'), ('chargers', 'dolphins'), ('bengals', 'steelers'), ('seahawks', 'rams'), ('49ers', 'saints'), ('ravens', 'patriots'), ('vikings', 'bears')], 'reg11': [('cardinals', 'seahawks'), ('titans', 'ravens'), ('lions', 'panthers'), ('eagles', 'browns'), ('patriots', 'texans'), ('steelers', 'jaguars'), ('falcons', 'saints'), ('bengals', 'football-team'), ('dolphins', 'broncos'), ('jets', 'chargers'), ('packers', 'colts'), ('cowboys', 'vikings'), ('chiefs', 'raiders'), ('rams', 'buccaneers')], 'reg12': [('texans', 'lions'), ('football-team', 'cowboys'), ('raiders', 'falcons'), ('chargers', 'bills'), ('giants', 'bengals'), ('titans', 'colts'), ('browns', 'jaguars'), ('panthers', 'vikings'), ('cardinals', 'patriots'), ('dolphins', 'jets'), ('saints', 'broncos'), ('49ers', 'rams'), ('chiefs', 'buccaneers'), ('bears', 'packers'), ('seahawks', 'eagles'), ('ravens', 'steelers')], 'reg13': [('saints', 'falcons'), ('lions', 'bears'), ('colts', 'texans'), ('bengals', 'dolphins'), ('jaguars', 'vikings'), ('raiders', 'jets'), ('browns', 'titans'), ('rams', 'cardinals'), ('giants', 'seahawks'), ('eagles', 'packers'), ('patriots', 'chargers'), ('broncos', 'chiefs'), ('football-team', 'steelers'), ('bills', '49ers'), ('cowboys', 'ravens')], 'reg14': [('patriots', 'rams'), ('broncos', 'panthers'), ('texans', 'bears'), ('cowboys', 'bengals'), ('titans', 'jaguars'), ('chiefs', 'dolphins'), ('cardinals', 'giants'), ('vikings', 'buccaneers'), ('colts', 'raiders'), ('jets', 'seahawks'), ('packers', 'lions'), ('falcons', 'chargers'), ('saints', 'eagles'), ('football-team', '49ers'), ('steelers', 'bills'), ('ravens', 'browns')], 'reg15': [('chargers', 'raiders'), ('bills', 'broncos'), ('panthers', 'packers'), ('texans', 'colts'), ('lions', 'titans'), ('buccaneers', 'falcons'), ('jaguars', 'ravens'), ('patriots', 'dolphins'), ('bears', 'vikings'), ('seahawks', 'football-team'), ('49ers', 'cowboys'), ('jets', 'rams'), ('eagles', 'cardinals'), ('chiefs', 'saints'), ('browns', 'giants'), ('steelers', 'bengals')], 'reg16': [('vikings', 'saints'), ('buccaneers', 'lions'), ('49ers', 'cardinals'), ('dolphins', 'raiders'), ('browns', 'jets'), ('giants', 'ravens'), ('bengals', 'texans'), ('bears', 'jaguars'), ('falcons', 'chiefs'), ('colts', 'steelers'), ('broncos', 'chargers'), ('panthers', 'football-team'), ('rams', 'seahawks'), ('eagles', 'cowboys'), ('titans', 'packers'), ('bills', 'patriots')], 'reg17': [('dolphins', 'bills'), ('ravens', 'bengals'), ('steelers', 'browns'), ('vikings', 'lions'), ('jets', 'patriots'), ('cowboys', 'giants'), ('falcons', 'buccaneers'), ('saints', 'panthers'), ('packers', 'bears'), ('chargers', 'chiefs'), ('raiders', 'broncos'), ('titans', 'texans'), ('jaguars', 'colts'), ('cardinals', 'rams'), ('seahawks', '49ers'), ('football-team', 'eagles')]}, '2021': {'reg1': [('cowboys', 'buccaneers'), ('jaguars', 'texans'), ('chargers', 'football-team'), ('seahawks', 'colts'), ('jets', 'panthers'), ('vikings', 'bengals'), ('cardinals', 'titans'), ('49ers', 'lions'), ('steelers', 'bills'), ('eagles', 'falcons'), ('browns', 'chiefs'), ('packers', 'saints'), ('broncos', 'giants'), ('dolphins', 'patriots'), ('bears', 'rams'), ('ravens', 'raiders')], 'reg2': [('giants', 'football-team'), ('patriots', 'jets'), ('broncos', 'jaguars'), ('bills', 'dolphins'), ('49ers', 'eagles'), ('rams', 'colts'), ('raiders', 'steelers'), ('bengals', 'bears'), ('texans', 'browns'), ('saints', 'panthers'), ('vikings', 'cardinals'), ('falcons', 'buccaneers'), ('titans', 'seahawks'), ('cowboys', 'chargers'), ('chiefs', 'ravens'), ('lions', 'packers')], 'reg3': [('panthers', 'texans'), ('colts', 'titans'), ('falcons', 'giants'), ('chargers', 'chiefs'), ('bengals', 'steelers'), ('bears', 'browns'), ('ravens', 'lions'), ('saints', 'patriots'), ('cardinals', 'jaguars'), ('football-team', 'bills'), ('jets', 'broncos'), ('dolphins', 'raiders'), ('seahawks', 'vikings'), ('buccaneers', 'rams'), ('packers', '49ers'), ('eagles', 'cowboys')], 'reg4': [('jaguars', 'bengals'), ('titans', 'jets'), ('chiefs', 'eagles'), ('panthers', 'cowboys'), ('giants', 'saints'), ('browns', 'vikings'), ('lions', 'bears'), ('texans', 'bills'), ('colts', 'dolphins'), ('football-team', 'falcons'), ('seahawks', '49ers'), ('cardinals', 'rams'), ('steelers', 'packers'), ('ravens', 'broncos'), ('buccaneers', 'patriots'), ('raiders', 'chargers')], 'reg5': [('rams', 'seahawks'), ('jets', 'falcons'), ('lions', 'vikings'), ('saints', 'football-team'), ('patriots', 'texans'), ('dolphins', 'buccaneers'), ('packers', 'bengals'), ('broncos', 'steelers'), ('eagles', 'panthers'), ('titans', 'jaguars'), ('browns', 'chargers'), ('bears', 'raiders'), ('49ers', 'cardinals'), ('giants', 'cowboys'), ('bills', 'chiefs'), ('colts', 'ravens')], 'reg6': [('buccaneers', 'eagles'), ('dolphins', 'jaguars'), ('chiefs', 'football-team'), ('rams', 'giants'), ('texans', 'colts'), ('bengals', 'lions'), ('packers', 'bears'), ('chargers', 'ravens'), ('vikings', 'panthers'), ('cardinals', 'browns'), ('raiders', 'broncos'), ('cowboys', 'patriots'), ('seahawks', 'steelers'), ('bills', 'titans')], 'reg7': [('broncos', 'browns'), ('panthers', 'giants'), ('jets', 'patriots'), ('chiefs', 'titans'), ('football-team', 'packers'), ('falcons', 'dolphins'), ('bengals', 'ravens'), ('lions', 'rams'), ('eagles', 'raiders'), ('texans', 'cardinals'), ('bears', 'buccaneers'), ('colts', '49ers'), ('saints', 'seahawks')], 'reg8': [('packers', 'cardinals'), ('bengals', 'jets'), ('titans', 'colts'), ('rams', 'texans'), ('steelers', 'browns'), ('eagles', 'lions'), ('49ers', 'bears'), ('panthers', 'falcons'), ('dolphins', 'bills'), ('patriots', 'chargers'), ('jaguars', 'seahawks'), ('football-team', 'broncos'), ('buccaneers', 'saints'), ('cowboys', 'vikings'), ('giants', 'chiefs')], 'reg9': [('jets', 'colts'), ('falcons', 'saints'), ('broncos', 'cowboys'), ('patriots', 'panthers'), ('vikings', 'ravens'), ('browns', 'bengals'), ('bills', 'jaguars'), ('texans', 'dolphins'), ('raiders', 'giants'), ('chargers', 'eagles'), ('packers', 'chiefs'), ('cardinals', '49ers'), ('titans', 'rams'), ('bears', 'steelers')], 'reg10': [('ravens', 'dolphins'), ('bills', 'jets'), ('buccaneers', 'football-team'), ('falcons', 'cowboys'), ('saints', 'titans'), ('jaguars', 'colts'), ('lions', 'steelers'), ('browns', 'patriots'), ('vikings', 'chargers'), ('panthers', 'cardinals'), ('eagles', 'broncos'), ('seahawks', 'packers'), ('chiefs', 'raiders'), ('rams', '49ers')], 'reg11': [('patriots', 'falcons'), ('saints', 'eagles'), ('dolphins', 'jets'), ('football-team', 'panthers'), ('colts', 'bills'), ('lions', 'browns'), ('49ers', 'jaguars'), ('texans', 'titans'), ('packers', 'vikings'), ('ravens', 'bears'), ('bengals', 'raiders'), ('cardinals', 'seahawks'), ('cowboys', 'chiefs'), ('steelers', 'chargers'), ('giants', 'buccaneers')], 'reg12': [('bears', 'lions'), ('raiders', 'cowboys'), ('bills', 'saints'), ('buccaneers', 'colts'), ('jets', 'texans'), ('eagles', 'giants'), ('panthers', 'dolphins'), ('titans', 'patriots'), ('steelers', 'bengals'), ('falcons', 'jaguars'), ('chargers', 'broncos'), ('rams', 'packers'), ('vikings', '49ers'), ('browns', 'ravens'), ('seahawks', 'football-team')], 'reg13': [('cowboys', 'saints'), ('giants', 'dolphins'), ('colts', 'texans'), ('vikings', 'lions'), ('eagles', 'jets'), ('cardinals', 'bears'), ('chargers', 'bengals'), ('buccaneers', 'falcons'), ('jaguars', 'rams'), ('football-team', 'raiders'), ('ravens', 'steelers'), ('49ers', 'seahawks'), ('broncos', 'chiefs'), ('patriots', 'bills')], 'reg14': [('steelers', 'vikings'), ('cowboys', 'football-team'), ('jaguars', 'titans'), ('seahawks', 'texans'), ('raiders', 'chiefs'), ('saints', 'jets'), ('falcons', 'panthers'), ('ravens', 'browns'), ('giants', 'chargers'), ('lions', 'broncos'), ('49ers', 'bengals'), ('bills', 'buccaneers'), ('bears', 'packers'), ('rams', 'cardinals')], 'reg15': [('chiefs', 'chargers'), ('patriots', 'colts'), ('cowboys', 'giants'), ('texans', 'jaguars'), ('titans', 'steelers'), ('jets', 'dolphins'), ('cardinals', 'lions'), ('panthers', 'bills'), ('bengals', 'broncos'), ('falcons', '49ers'), ('packers', 'ravens'), ('saints', 'buccaneers'), ('raiders', 'browns'), ('vikings', 'bears'), ('seahawks', 'rams'), ('football-team', 'eagles')], 'reg16': [('49ers', 'titans'), ('browns', 'packers'), ('colts', 'cardinals'), ('giants', 'eagles'), ('rams', 'vikings'), ('bills', 'patriots'), ('buccaneers', 'panthers'), ('jaguars', 'jets'), ('lions', 'falcons'), ('chargers', 'texans'), ('ravens', 'bengals'), ('bears', 'seahawks'), ('steelers', 'chiefs'), ('broncos', 'raiders'), ('football-team', 'cowboys'), ('dolphins', 'saints')], 'reg17': [('eagles', 'football-team'), ('rams', 'ravens'), ('buccaneers', 'jets'), ('dolphins', 'titans'), ('jaguars', 'patriots'), ('raiders', 'colts'), ('chiefs', 'bengals'), ('giants', 'bears'), ('falcons', 'bills'), ('texans', '49ers'), ('broncos', 'chargers'), ('panthers', 'saints'), ('lions', 'seahawks'), ('cardinals', 'cowboys'), ('vikings', 'packers'), ('browns', 'steelers')], 'reg18': [('chiefs', 'broncos'), ('cowboys', 'eagles'), ('packers', 'lions'), ('colts', 'jaguars'), ('football-team', 'giants'), ('bears', 'vikings'), ('titans', 'texans'), ('steelers', 'ravens'), ('bengals', 'browns'), ('49ers', 'rams'), ('panthers', 'buccaneers'), ('seahawks', 'cardinals'), ('patriots', 'dolphins'), ('saints', 'falcons'), ('jets', 'bills'), ('chargers', 'raiders')]}, '2022': {'reg1': [('bills', 'rams'), ('saints', 'falcons'), ('browns', 'panthers'), ('49ers', 'bears'), ('steelers', 'bengals'), ('eagles', 'lions'), ('colts', 'texans'), ('patriots', 'dolphins'), ('ravens', 'jets'), ('jaguars', 'commanders'), ('giants', 'titans'), ('chiefs', 'cardinals'), ('raiders', 'chargers'), ('packers', 'vikings'), ('buccaneers', 'cowboys'), ('broncos', 'seahawks')], 'reg2': [('chargers', 'chiefs'), ('dolphins', 'ravens'), ('jets', 'browns'), ('commanders', 'lions'), ('colts', 'jaguars'), ('buccaneers', 'saints'), ('panthers', 'giants'), ('patriots', 'steelers'), ('falcons', 'rams'), ('seahawks', '49ers'), ('bengals', 'cowboys'), ('texans', 'broncos'), ('cardinals', 'raiders'), ('bears', 'packers'), ('titans', 'bills'), ('vikings', 'eagles')], 'reg3': [('steelers', 'browns'), ('saints', 'panthers'), ('texans', 'bears'), ('chiefs', 'colts'), ('bills', 'dolphins'), ('lions', 'vikings'), ('ravens', 'patriots'), ('bengals', 'jets'), ('raiders', 'titans'), ('eagles', 'commanders'), ('jaguars', 'chargers'), ('rams', 'cardinals'), ('falcons', 'seahawks'), ('packers', 'buccaneers'), ('49ers', 'broncos'), ('cowboys', 'giants')], 'reg4': [('dolphins', 'bengals'), ('vikings', 'saints'), ('browns', 'falcons'), ('bills', 'ravens'), ('commanders', 'cowboys'), ('seahawks', 'lions'), ('chargers', 'texans'), ('titans', 'colts'), ('bears', 'giants'), ('jaguars', 'eagles'), ('jets', 'steelers'), ('cardinals', 'panthers'), ('patriots', 'packers'), ('broncos', 'raiders'), ('chiefs', 'buccaneers'), ('rams', '49ers')], 'reg5': [('colts', 'broncos'), ('giants', 'packers'), ('steelers', 'bills'), ('chargers', 'browns'), ('texans', 'jaguars'), ('bears', 'vikings'), ('lions', 'patriots'), ('seahawks', 'saints'), ('dolphins', 'jets'), ('falcons', 'buccaneers'), ('titans', 'commanders'), ('49ers', 'panthers'), ('eagles', 'cardinals'), ('cowboys', 'rams'), ('bengals', 'ravens'), ('raiders', 'chiefs')], 'reg6': [('commanders', 'bears'), ('49ers', 'falcons'), ('patriots', 'browns'), ('jets', 'packers'), ('jaguars', 'colts'), ('vikings', 'dolphins'), ('bengals', 'saints'), ('ravens', 'giants'), ('buccaneers', 'steelers'), ('panthers', 'rams'), ('cardinals', 'seahawks'), ('bills', 'chiefs'), ('cowboys', 'eagles'), ('broncos', 'chargers')], 'reg7': [('saints', 'cardinals'), ('browns', 'ravens'), ('buccaneers', 'panthers'), ('falcons', 'bengals'), ('lions', 'cowboys'), ('giants', 'jaguars'), ('colts', 'titans'), ('packers', 'commanders'), ('jets', 'broncos'), ('texans', 'raiders'), ('seahawks', 'chargers'), ('chiefs', '49ers'), ('steelers', 'dolphins'), ('bears', 'patriots')], 'reg8': [('ravens', 'buccaneers'), ('broncos', 'jaguars'), ('panthers', 'falcons'), ('bears', 'cowboys'), ('dolphins', 'lions'), ('cardinals', 'vikings'), ('raiders', 'saints'), ('patriots', 'jets'), ('steelers', 'eagles'), ('titans', 'texans'), ('commanders', 'colts'), ('49ers', 'rams'), ('giants', 'seahawks'), ('packers', 'bills'), ('bengals', 'browns')], 'reg9': [('eagles', 'texans'), ('chargers', 'falcons'), ('dolphins', 'bears'), ('panthers', 'bengals'), ('packers', 'lions'), ('raiders', 'jaguars'), ('colts', 'patriots'), ('bills', 'jets'), ('vikings', 'commanders'), ('seahawks', 'cardinals'), ('rams', 'buccaneers'), ('titans', 'chiefs'), ('ravens', 'saints')], 'reg10': [('falcons', 'panthers'), ('seahawks', 'buccaneers'), ('vikings', 'bills'), ('lions', 'bears'), ('jaguars', 'chiefs'), ('browns', 'dolphins'), ('texans', 'giants'), ('saints', 'steelers'), ('broncos', 'titans'), ('colts', 'raiders'), ('cowboys', 'packers'), ('cardinals', 'rams'), ('chargers', '49ers'), ('commanders', 'eagles')], 'reg11': [('titans', 'packers'), ('bears', 'falcons'), ('panthers', 'ravens'), ('browns', 'bills'), ('commanders', 'texans'), ('eagles', 'colts'), ('jets', 'patriots'), ('rams', 'saints'), ('lions', 'giants'), ('raiders', 'broncos'), ('cowboys', 'vikings'), ('bengals', 'steelers'), ('chiefs', 'chargers'), ('49ers', 'cardinals')], 'reg12': [('bills', 'lions'), ('giants', 'cowboys'), ('patriots', 'vikings'), ('broncos', 'panthers'), ('buccaneers', 'browns'), ('ravens', 'jaguars'), ('texans', 'dolphins'), ('bears', 'jets'), ('bengals', 'titans'), ('falcons', 'commanders'), ('chargers', 'cardinals'), ('raiders', 'seahawks'), ('rams', 'chiefs'), ('saints', '49ers'), ('packers', 'eagles'), ('steelers', 'colts')], 'reg13': [('bills', 'patriots'), ('steelers', 'falcons'), ('broncos', 'ravens'), ('packers', 'bears'), ('jaguars', 'lions'), ('browns', 'texans'), ('jets', 'vikings'), ('commanders', 'giants'), ('titans', 'eagles'), ('seahawks', 'rams'), ('dolphins', '49ers'), ('chiefs', 'bengals'), ('chargers', 'raiders'), ('colts', 'cowboys'), ('saints', 'buccaneers')], 'reg14': [('raiders', 'rams'), ('jets', 'bills'), ('browns', 'bengals'), ('texans', 'cowboys'), ('vikings', 'lions'), ('eagles', 'giants'), ('ravens', 'steelers'), ('jaguars', 'titans'), ('chiefs', 'broncos'), ('panthers', 'seahawks'), ('buccaneers', '49ers'), ('dolphins', 'chargers'), ('patriots', 'cardinals')], 'reg15': [('49ers', 'seahawks'), ('colts', 'vikings'), ('ravens', 'browns'), ('dolphins', 'bills'), ('falcons', 'saints'), ('steelers', 'panthers'), ('eagles', 'bears'), ('chiefs', 'texans'), ('cowboys', 'jaguars'), ('lions', 'jets'), ('cardinals', 'broncos'), ('patriots', 'raiders'), ('titans', 'chargers'), ('bengals', 'buccaneers'), ('giants', 'commanders'), ('rams', 'packers')], 'reg16': [('jaguars', 'jets'), ('falcons', 'ravens'), ('lions', 'panthers'), ('bills', 'bears'), ('saints', 'browns'), ('seahawks', 'chiefs'), ('giants', 'vikings'), ('bengals', 'patriots'), ('texans', 'titans'), ('commanders', '49ers'), ('eagles', 'cowboys'), ('raiders', 'steelers'), ('packers', 'dolphins'), ('broncos', 'rams'), ('buccaneers', 'cardinals'), ('chargers', 'colts')], 'reg17': [('cowboys', 'titans'), ('cardinals', 'falcons'), ('bears', 'lions'), ('jaguars', 'texans'), ('broncos', 'chiefs'), ('dolphins', 'patriots'), ('colts', 'giants'), ('saints', 'eagles'), ('panthers', 'buccaneers'), ('browns', 'commanders'), ('49ers', 'raiders'), ('jets', 'seahawks'), ('vikings', 'packers'), ('rams', 'chargers'), ('steelers', 'ravens'), ('bills', 'bengals')], 'reg18': [('chiefs', 'raiders'), ('titans', 'jaguars'), ('buccaneers', 'falcons'), ('patriots', 'bills'), ('vikings', 'bears'), ('ravens', 'bengals'), ('texans', 'colts'), ('jets', 'dolphins'), ('panthers', 'saints'), ('browns', 'steelers'), ('giants', 'eagles'), ('cowboys', 'commanders'), ('chargers', 'broncos'), ('rams', 'seahawks'), ('cardinals', '49ers'), ('lions', 'packers')]}}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "638fb5e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "#RECUPERATION DES MATCHS JOUES POUR DES WEEKS ET DES YEARS DONNEES\n",
    "\n",
    "# def get_gameTeams(year, week):\n",
    "#     try :         \n",
    "#     #     url_api_request = \"https://api.nfl.com/football/v2/stats/live/\"\n",
    "#     #     url_api_reg = \"game-summaries?season={}&seasonType=REG&week={}\".format(year,week)\n",
    "#     #     url_api = url_api_request+url_api_reg\n",
    "\n",
    "#         url_api = \"https://api.nfl.com/football/v2/stats/live/game-summaries?season={}&seasonType=REG&week={}\".format(year,week)\n",
    "\n",
    "#         response_gameTeams = requests.get(url_api, headers=headers)\n",
    "#         api_matchs = json.loads(response_gameTeams.text)\n",
    "\n",
    "#         dataset_matchs = api_matchs['data']\n",
    "\n",
    "#         list_matchs = []\n",
    "#         for data_matchs in dataset_matchs : \n",
    "#             away_team_ID = data_matchs[\"awayTeam\"][\"teamId\"]\n",
    "#             home_team_ID = data_matchs[\"homeTeam\"][\"teamId\"]\n",
    "            \n",
    "#             if away_team_ID == \"10405110-ec3c-669e-2614-db3dc1736e95\":\n",
    "#                 away_team_name = dict_idTeam[away_team_ID][str(year)]\n",
    "#                 home_team_name = dict_idTeam[home_team_ID]\n",
    "                \n",
    "#             elif home_team_ID == \"10405110-ec3c-669e-2614-db3dc1736e95\":\n",
    "#                 home_team_name = dict_idTeam[home_team_ID][str(year)]\n",
    "#                 away_team_name = dict_idTeam[away_team_ID]\n",
    "            \n",
    "#             else : \n",
    "#                 away_team_name = dict_idTeam[away_team_ID]\n",
    "#                 home_team_name = dict_idTeam[home_team_ID]\n",
    "                \n",
    "#             list_matchs.append((away_team_name,home_team_name))\n",
    "        \n",
    "#         return list_matchs\n",
    "#     except :\n",
    "#         print(\"Une erreur est survenue, le header renseigné est-il bien à jour?\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a17c99b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# years = [2017, 2018, 2019, 2020, 2021, 2022]\n",
    "# weeks = [k for k in range(1,19)]\n",
    "\n",
    "# def main(years, weeks):\n",
    "#     gameTeams={}\n",
    "#     for year in years : \n",
    "#         gameTeams_year = {}\n",
    "#         for week in weeks :\n",
    "#             if get_gameTeams(year, week) != [] : \n",
    "#                 gameTeams_year[\"reg\"+str(week)] = get_gameTeams(year, week)\n",
    "            \n",
    "#         gameTeams[str(year)] = gameTeams_year\n",
    "        \n",
    "#     return gameTeams\n",
    "\n",
    "# # print(main(year,weeks))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f7e1ee70",
   "metadata": {},
   "source": [
    "### A partir du dictionanire des tuples des équipes qui se sont affrontées pour chaque semaine et chaque année, j'ai créé le dictionnaire associé avec les urls associés\n",
    "\n",
    "### Attention! Il faut que la valeur du headers soit bien mis à jour pour lancer les codes suivants sinon vous rencontrerez une erreur."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "774d08c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "gameTeamsURLs = {'2017': {'reg1': ['https://www.nfl.com/games/chiefs-at-patriots-2017-reg-1?active-tab=watch', 'https://www.nfl.com/games/jets-at-bills-2017-reg-1?active-tab=watch', 'https://www.nfl.com/games/falcons-at-bears-2017-reg-1?active-tab=watch', 'https://www.nfl.com/games/ravens-at-bengals-2017-reg-1?active-tab=watch', 'https://www.nfl.com/games/steelers-at-browns-2017-reg-1?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-lions-2017-reg-1?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-texans-2017-reg-1?active-tab=watch', 'https://www.nfl.com/games/raiders-at-titans-2017-reg-1?active-tab=watch', 'https://www.nfl.com/games/eagles-at-redskins-2017-reg-1?active-tab=watch', 'https://www.nfl.com/games/colts-at-rams-2017-reg-1?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-packers-2017-reg-1?active-tab=watch', 'https://www.nfl.com/games/panthers-at-49ers-2017-reg-1?active-tab=watch', 'https://www.nfl.com/games/giants-at-cowboys-2017-reg-1?active-tab=watch', 'https://www.nfl.com/games/saints-at-vikings-2017-reg-1?active-tab=watch', 'https://www.nfl.com/games/chargers-at-broncos-2017-reg-1?active-tab=watch'], 'reg2': ['https://www.nfl.com/games/texans-at-bengals-2017-reg-2?active-tab=watch', 'https://www.nfl.com/games/browns-at-ravens-2017-reg-2?active-tab=watch', 'https://www.nfl.com/games/bills-at-panthers-2017-reg-2?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-colts-2017-reg-2?active-tab=watch', 'https://www.nfl.com/games/titans-at-jaguars-2017-reg-2?active-tab=watch', 'https://www.nfl.com/games/eagles-at-chiefs-2017-reg-2?active-tab=watch', 'https://www.nfl.com/games/patriots-at-saints-2017-reg-2?active-tab=watch', 'https://www.nfl.com/games/vikings-at-steelers-2017-reg-2?active-tab=watch', 'https://www.nfl.com/games/bears-at-buccaneers-2017-reg-2?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-chargers-2017-reg-2?active-tab=watch', 'https://www.nfl.com/games/jets-at-raiders-2017-reg-2?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-broncos-2017-reg-2?active-tab=watch', 'https://www.nfl.com/games/redskins-at-rams-2017-reg-2?active-tab=watch', 'https://www.nfl.com/games/49ers-at-seahawks-2017-reg-2?active-tab=watch', 'https://www.nfl.com/games/packers-at-falcons-2017-reg-2?active-tab=watch', 'https://www.nfl.com/games/lions-at-giants-2017-reg-2?active-tab=watch'], 'reg3': ['https://www.nfl.com/games/rams-at-49ers-2017-reg-3?active-tab=watch', 'https://www.nfl.com/games/ravens-at-jaguars-2017-reg-3?active-tab=watch', 'https://www.nfl.com/games/broncos-at-bills-2017-reg-3?active-tab=watch', 'https://www.nfl.com/games/saints-at-panthers-2017-reg-3?active-tab=watch', 'https://www.nfl.com/games/steelers-at-bears-2017-reg-3?active-tab=watch', 'https://www.nfl.com/games/falcons-at-lions-2017-reg-3?active-tab=watch', 'https://www.nfl.com/games/browns-at-colts-2017-reg-3?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-vikings-2017-reg-3?active-tab=watch', 'https://www.nfl.com/games/texans-at-patriots-2017-reg-3?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-jets-2017-reg-3?active-tab=watch', 'https://www.nfl.com/games/giants-at-eagles-2017-reg-3?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-titans-2017-reg-3?active-tab=watch', 'https://www.nfl.com/games/bengals-at-packers-2017-reg-3?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-chargers-2017-reg-3?active-tab=watch', 'https://www.nfl.com/games/raiders-at-redskins-2017-reg-3?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-cardinals-2017-reg-3?active-tab=watch'], 'reg4': ['https://www.nfl.com/games/bears-at-packers-2017-reg-4?active-tab=watch', 'https://www.nfl.com/games/saints-at-dolphins-2017-reg-4?active-tab=watch', 'https://www.nfl.com/games/bills-at-falcons-2017-reg-4?active-tab=watch', 'https://www.nfl.com/games/steelers-at-ravens-2017-reg-4?active-tab=watch', 'https://www.nfl.com/games/bengals-at-browns-2017-reg-4?active-tab=watch', 'https://www.nfl.com/games/rams-at-cowboys-2017-reg-4?active-tab=watch', 'https://www.nfl.com/games/titans-at-texans-2017-reg-4?active-tab=watch', 'https://www.nfl.com/games/lions-at-vikings-2017-reg-4?active-tab=watch', 'https://www.nfl.com/games/panthers-at-patriots-2017-reg-4?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-jets-2017-reg-4?active-tab=watch', 'https://www.nfl.com/games/49ers-at-cardinals-2017-reg-4?active-tab=watch', 'https://www.nfl.com/games/eagles-at-chargers-2017-reg-4?active-tab=watch', 'https://www.nfl.com/games/giants-at-buccaneers-2017-reg-4?active-tab=watch', 'https://www.nfl.com/games/raiders-at-broncos-2017-reg-4?active-tab=watch', 'https://www.nfl.com/games/colts-at-seahawks-2017-reg-4?active-tab=watch', 'https://www.nfl.com/games/redskins-at-chiefs-2017-reg-4?active-tab=watch'], 'reg5': ['https://www.nfl.com/games/patriots-at-buccaneers-2017-reg-5?active-tab=watch', 'https://www.nfl.com/games/bills-at-bengals-2017-reg-5?active-tab=watch', 'https://www.nfl.com/games/jets-at-browns-2017-reg-5?active-tab=watch', 'https://www.nfl.com/games/panthers-at-lions-2017-reg-5?active-tab=watch', 'https://www.nfl.com/games/49ers-at-colts-2017-reg-5?active-tab=watch', 'https://www.nfl.com/games/titans-at-dolphins-2017-reg-5?active-tab=watch', 'https://www.nfl.com/games/chargers-at-giants-2017-reg-5?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-eagles-2017-reg-5?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-steelers-2017-reg-5?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-rams-2017-reg-5?active-tab=watch', 'https://www.nfl.com/games/ravens-at-raiders-2017-reg-5?active-tab=watch', 'https://www.nfl.com/games/packers-at-cowboys-2017-reg-5?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-texans-2017-reg-5?active-tab=watch', 'https://www.nfl.com/games/vikings-at-bears-2017-reg-5?active-tab=watch'], 'reg6': ['https://www.nfl.com/games/eagles-at-panthers-2017-reg-6?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-falcons-2017-reg-6?active-tab=watch', 'https://www.nfl.com/games/bears-at-ravens-2017-reg-6?active-tab=watch', 'https://www.nfl.com/games/browns-at-texans-2017-reg-6?active-tab=watch', 'https://www.nfl.com/games/packers-at-vikings-2017-reg-6?active-tab=watch', 'https://www.nfl.com/games/lions-at-saints-2017-reg-6?active-tab=watch', 'https://www.nfl.com/games/patriots-at-jets-2017-reg-6?active-tab=watch', 'https://www.nfl.com/games/49ers-at-redskins-2017-reg-6?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-cardinals-2017-reg-6?active-tab=watch', 'https://www.nfl.com/games/rams-at-jaguars-2017-reg-6?active-tab=watch', 'https://www.nfl.com/games/steelers-at-chiefs-2017-reg-6?active-tab=watch', 'https://www.nfl.com/games/chargers-at-raiders-2017-reg-6?active-tab=watch', 'https://www.nfl.com/games/giants-at-broncos-2017-reg-6?active-tab=watch', 'https://www.nfl.com/games/colts-at-titans-2017-reg-6?active-tab=watch'], 'reg7': ['https://www.nfl.com/games/chiefs-at-raiders-2017-reg-7?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-bills-2017-reg-7?active-tab=watch', 'https://www.nfl.com/games/panthers-at-bears-2017-reg-7?active-tab=watch', 'https://www.nfl.com/games/titans-at-browns-2017-reg-7?active-tab=watch', 'https://www.nfl.com/games/saints-at-packers-2017-reg-7?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-colts-2017-reg-7?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-rams-2017-reg-7?active-tab=watch', 'https://www.nfl.com/games/jets-at-dolphins-2017-reg-7?active-tab=watch', 'https://www.nfl.com/games/ravens-at-vikings-2017-reg-7?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-49ers-2017-reg-7?active-tab=watch', 'https://www.nfl.com/games/bengals-at-steelers-2017-reg-7?active-tab=watch', 'https://www.nfl.com/games/broncos-at-chargers-2017-reg-7?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-giants-2017-reg-7?active-tab=watch', 'https://www.nfl.com/games/falcons-at-patriots-2017-reg-7?active-tab=watch', 'https://www.nfl.com/games/redskins-at-eagles-2017-reg-7?active-tab=watch'], 'reg8': ['https://www.nfl.com/games/dolphins-at-ravens-2017-reg-8?active-tab=watch', 'https://www.nfl.com/games/vikings-at-browns-2017-reg-8?active-tab=watch', 'https://www.nfl.com/games/raiders-at-bills-2017-reg-8?active-tab=watch', 'https://www.nfl.com/games/colts-at-bengals-2017-reg-8?active-tab=watch', 'https://www.nfl.com/games/chargers-at-patriots-2017-reg-8?active-tab=watch', 'https://www.nfl.com/games/bears-at-saints-2017-reg-8?active-tab=watch', 'https://www.nfl.com/games/falcons-at-jets-2017-reg-8?active-tab=watch', 'https://www.nfl.com/games/49ers-at-eagles-2017-reg-8?active-tab=watch', 'https://www.nfl.com/games/panthers-at-buccaneers-2017-reg-8?active-tab=watch', 'https://www.nfl.com/games/texans-at-seahawks-2017-reg-8?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-redskins-2017-reg-8?active-tab=watch', 'https://www.nfl.com/games/steelers-at-lions-2017-reg-8?active-tab=watch', 'https://www.nfl.com/games/broncos-at-chiefs-2017-reg-8?active-tab=watch'], 'reg9': ['https://www.nfl.com/games/bills-at-jets-2017-reg-9?active-tab=watch', 'https://www.nfl.com/games/falcons-at-panthers-2017-reg-9?active-tab=watch', 'https://www.nfl.com/games/colts-at-texans-2017-reg-9?active-tab=watch', 'https://www.nfl.com/games/bengals-at-jaguars-2017-reg-9?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-saints-2017-reg-9?active-tab=watch', 'https://www.nfl.com/games/rams-at-giants-2017-reg-9?active-tab=watch', 'https://www.nfl.com/games/broncos-at-eagles-2017-reg-9?active-tab=watch', 'https://www.nfl.com/games/ravens-at-titans-2017-reg-9?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-49ers-2017-reg-9?active-tab=watch', 'https://www.nfl.com/games/redskins-at-seahawks-2017-reg-9?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-cowboys-2017-reg-9?active-tab=watch', 'https://www.nfl.com/games/raiders-at-dolphins-2017-reg-9?active-tab=watch', 'https://www.nfl.com/games/lions-at-packers-2017-reg-9?active-tab=watch'], 'reg10': ['https://www.nfl.com/games/seahawks-at-cardinals-2017-reg-10?active-tab=watch', 'https://www.nfl.com/games/saints-at-bills-2017-reg-10?active-tab=watch', 'https://www.nfl.com/games/packers-at-bears-2017-reg-10?active-tab=watch', 'https://www.nfl.com/games/browns-at-lions-2017-reg-10?active-tab=watch', 'https://www.nfl.com/games/steelers-at-colts-2017-reg-10?active-tab=watch', 'https://www.nfl.com/games/chargers-at-jaguars-2017-reg-10?active-tab=watch', 'https://www.nfl.com/games/jets-at-buccaneers-2017-reg-10?active-tab=watch', 'https://www.nfl.com/games/bengals-at-titans-2017-reg-10?active-tab=watch', 'https://www.nfl.com/games/vikings-at-redskins-2017-reg-10?active-tab=watch', 'https://www.nfl.com/games/texans-at-rams-2017-reg-10?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-falcons-2017-reg-10?active-tab=watch', 'https://www.nfl.com/games/giants-at-49ers-2017-reg-10?active-tab=watch', 'https://www.nfl.com/games/patriots-at-broncos-2017-reg-10?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-panthers-2017-reg-10?active-tab=watch'], 'reg11': ['https://www.nfl.com/games/titans-at-steelers-2017-reg-11?active-tab=watch', 'https://www.nfl.com/games/lions-at-bears-2017-reg-11?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-browns-2017-reg-11?active-tab=watch', 'https://www.nfl.com/games/ravens-at-packers-2017-reg-11?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-texans-2017-reg-11?active-tab=watch', 'https://www.nfl.com/games/rams-at-vikings-2017-reg-11?active-tab=watch', 'https://www.nfl.com/games/redskins-at-saints-2017-reg-11?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-giants-2017-reg-11?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-dolphins-2017-reg-11?active-tab=watch', 'https://www.nfl.com/games/bills-at-chargers-2017-reg-11?active-tab=watch', 'https://www.nfl.com/games/bengals-at-broncos-2017-reg-11?active-tab=watch', 'https://www.nfl.com/games/patriots-at-raiders-2017-reg-11?active-tab=watch', 'https://www.nfl.com/games/eagles-at-cowboys-2017-reg-11?active-tab=watch', 'https://www.nfl.com/games/falcons-at-seahawks-2017-reg-11?active-tab=watch'], 'reg12': ['https://www.nfl.com/games/vikings-at-lions-2017-reg-12?active-tab=watch', 'https://www.nfl.com/games/chargers-at-cowboys-2017-reg-12?active-tab=watch', 'https://www.nfl.com/games/giants-at-redskins-2017-reg-12?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-falcons-2017-reg-12?active-tab=watch', 'https://www.nfl.com/games/browns-at-bengals-2017-reg-12?active-tab=watch', 'https://www.nfl.com/games/titans-at-colts-2017-reg-12?active-tab=watch', 'https://www.nfl.com/games/bills-at-chiefs-2017-reg-12?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-patriots-2017-reg-12?active-tab=watch', 'https://www.nfl.com/games/panthers-at-jets-2017-reg-12?active-tab=watch', 'https://www.nfl.com/games/bears-at-eagles-2017-reg-12?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-49ers-2017-reg-12?active-tab=watch', 'https://www.nfl.com/games/saints-at-rams-2017-reg-12?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-cardinals-2017-reg-12?active-tab=watch', 'https://www.nfl.com/games/broncos-at-raiders-2017-reg-12?active-tab=watch', 'https://www.nfl.com/games/packers-at-steelers-2017-reg-12?active-tab=watch', 'https://www.nfl.com/games/texans-at-ravens-2017-reg-12?active-tab=watch'], 'reg13': ['https://www.nfl.com/games/redskins-at-cowboys-2017-reg-13?active-tab=watch', 'https://www.nfl.com/games/vikings-at-falcons-2017-reg-13?active-tab=watch', 'https://www.nfl.com/games/lions-at-ravens-2017-reg-13?active-tab=watch', 'https://www.nfl.com/games/patriots-at-bills-2017-reg-13?active-tab=watch', 'https://www.nfl.com/games/49ers-at-bears-2017-reg-13?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-packers-2017-reg-13?active-tab=watch', 'https://www.nfl.com/games/colts-at-jaguars-2017-reg-13?active-tab=watch', 'https://www.nfl.com/games/broncos-at-dolphins-2017-reg-13?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-jets-2017-reg-13?active-tab=watch', 'https://www.nfl.com/games/texans-at-titans-2017-reg-13?active-tab=watch', 'https://www.nfl.com/games/browns-at-chargers-2017-reg-13?active-tab=watch', 'https://www.nfl.com/games/panthers-at-saints-2017-reg-13?active-tab=watch', 'https://www.nfl.com/games/rams-at-cardinals-2017-reg-13?active-tab=watch', 'https://www.nfl.com/games/giants-at-raiders-2017-reg-13?active-tab=watch', 'https://www.nfl.com/games/eagles-at-seahawks-2017-reg-13?active-tab=watch', 'https://www.nfl.com/games/steelers-at-bengals-2017-reg-13?active-tab=watch'], 'reg14': ['https://www.nfl.com/games/saints-at-falcons-2017-reg-14?active-tab=watch', 'https://www.nfl.com/games/colts-at-bills-2017-reg-14?active-tab=watch', 'https://www.nfl.com/games/vikings-at-panthers-2017-reg-14?active-tab=watch', 'https://www.nfl.com/games/bears-at-bengals-2017-reg-14?active-tab=watch', 'https://www.nfl.com/games/packers-at-browns-2017-reg-14?active-tab=watch', 'https://www.nfl.com/games/49ers-at-texans-2017-reg-14?active-tab=watch', 'https://www.nfl.com/games/raiders-at-chiefs-2017-reg-14?active-tab=watch', 'https://www.nfl.com/games/lions-at-buccaneers-2017-reg-14?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-giants-2017-reg-14?active-tab=watch', 'https://www.nfl.com/games/titans-at-cardinals-2017-reg-14?active-tab=watch', 'https://www.nfl.com/games/jets-at-broncos-2017-reg-14?active-tab=watch', 'https://www.nfl.com/games/redskins-at-chargers-2017-reg-14?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-jaguars-2017-reg-14?active-tab=watch', 'https://www.nfl.com/games/eagles-at-rams-2017-reg-14?active-tab=watch', 'https://www.nfl.com/games/ravens-at-steelers-2017-reg-14?active-tab=watch', 'https://www.nfl.com/games/patriots-at-dolphins-2017-reg-14?active-tab=watch'], 'reg15': ['https://www.nfl.com/games/broncos-at-colts-2017-reg-15?active-tab=watch', 'https://www.nfl.com/games/bears-at-lions-2017-reg-15?active-tab=watch', 'https://www.nfl.com/games/chargers-at-chiefs-2017-reg-15?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-bills-2017-reg-15?active-tab=watch', 'https://www.nfl.com/games/packers-at-panthers-2017-reg-15?active-tab=watch', 'https://www.nfl.com/games/ravens-at-browns-2017-reg-15?active-tab=watch', 'https://www.nfl.com/games/texans-at-jaguars-2017-reg-15?active-tab=watch', 'https://www.nfl.com/games/bengals-at-vikings-2017-reg-15?active-tab=watch', 'https://www.nfl.com/games/jets-at-saints-2017-reg-15?active-tab=watch', 'https://www.nfl.com/games/eagles-at-giants-2017-reg-15?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-redskins-2017-reg-15?active-tab=watch', 'https://www.nfl.com/games/rams-at-seahawks-2017-reg-15?active-tab=watch', 'https://www.nfl.com/games/patriots-at-steelers-2017-reg-15?active-tab=watch', 'https://www.nfl.com/games/titans-at-49ers-2017-reg-15?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-raiders-2017-reg-15?active-tab=watch', 'https://www.nfl.com/games/falcons-at-buccaneers-2017-reg-15?active-tab=watch'], 'reg16': ['https://www.nfl.com/games/colts-at-ravens-2017-reg-16?active-tab=watch', 'https://www.nfl.com/games/vikings-at-packers-2017-reg-16?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-panthers-2017-reg-16?active-tab=watch', 'https://www.nfl.com/games/browns-at-bears-2017-reg-16?active-tab=watch', 'https://www.nfl.com/games/lions-at-bengals-2017-reg-16?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-chiefs-2017-reg-16?active-tab=watch', 'https://www.nfl.com/games/bills-at-patriots-2017-reg-16?active-tab=watch', 'https://www.nfl.com/games/falcons-at-saints-2017-reg-16?active-tab=watch', 'https://www.nfl.com/games/chargers-at-jets-2017-reg-16?active-tab=watch', 'https://www.nfl.com/games/rams-at-titans-2017-reg-16?active-tab=watch', 'https://www.nfl.com/games/broncos-at-redskins-2017-reg-16?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-49ers-2017-reg-16?active-tab=watch', 'https://www.nfl.com/games/giants-at-cardinals-2017-reg-16?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-cowboys-2017-reg-16?active-tab=watch', 'https://www.nfl.com/games/steelers-at-texans-2017-reg-16?active-tab=watch', 'https://www.nfl.com/games/raiders-at-eagles-2017-reg-16?active-tab=watch'], 'reg17': ['https://www.nfl.com/games/packers-at-lions-2017-reg-17?active-tab=watch', 'https://www.nfl.com/games/texans-at-colts-2017-reg-17?active-tab=watch', 'https://www.nfl.com/games/bears-at-vikings-2017-reg-17?active-tab=watch', 'https://www.nfl.com/games/jets-at-patriots-2017-reg-17?active-tab=watch', 'https://www.nfl.com/games/redskins-at-giants-2017-reg-17?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-eagles-2017-reg-17?active-tab=watch', 'https://www.nfl.com/games/browns-at-steelers-2017-reg-17?active-tab=watch', 'https://www.nfl.com/games/panthers-at-falcons-2017-reg-17?active-tab=watch', 'https://www.nfl.com/games/bengals-at-ravens-2017-reg-17?active-tab=watch', 'https://www.nfl.com/games/bills-at-dolphins-2017-reg-17?active-tab=watch', 'https://www.nfl.com/games/saints-at-buccaneers-2017-reg-17?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-titans-2017-reg-17?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-broncos-2017-reg-17?active-tab=watch', 'https://www.nfl.com/games/raiders-at-chargers-2017-reg-17?active-tab=watch', 'https://www.nfl.com/games/49ers-at-rams-2017-reg-17?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-seahawks-2017-reg-17?active-tab=watch']}, '2018': {'reg1': ['https://www.nfl.com/games/falcons-at-eagles-2018-reg-1?active-tab=watch', 'https://www.nfl.com/games/bills-at-ravens-2018-reg-1?active-tab=watch', 'https://www.nfl.com/games/steelers-at-browns-2018-reg-1?active-tab=watch', 'https://www.nfl.com/games/bengals-at-colts-2018-reg-1?active-tab=watch', 'https://www.nfl.com/games/titans-at-dolphins-2018-reg-1?active-tab=watch', 'https://www.nfl.com/games/49ers-at-vikings-2018-reg-1?active-tab=watch', 'https://www.nfl.com/games/texans-at-patriots-2018-reg-1?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-saints-2018-reg-1?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-giants-2018-reg-1?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-chargers-2018-reg-1?active-tab=watch', 'https://www.nfl.com/games/redskins-at-cardinals-2018-reg-1?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-panthers-2018-reg-1?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-broncos-2018-reg-1?active-tab=watch', 'https://www.nfl.com/games/bears-at-packers-2018-reg-1?active-tab=watch', 'https://www.nfl.com/games/jets-at-lions-2018-reg-1?active-tab=watch', 'https://www.nfl.com/games/rams-at-raiders-2018-reg-1?active-tab=watch'], 'reg2': ['https://www.nfl.com/games/ravens-at-bengals-2018-reg-2?active-tab=watch', 'https://www.nfl.com/games/panthers-at-falcons-2018-reg-2?active-tab=watch', 'https://www.nfl.com/games/chargers-at-bills-2018-reg-2?active-tab=watch', 'https://www.nfl.com/games/vikings-at-packers-2018-reg-2?active-tab=watch', 'https://www.nfl.com/games/browns-at-saints-2018-reg-2?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-jets-2018-reg-2?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-steelers-2018-reg-2?active-tab=watch', 'https://www.nfl.com/games/eagles-at-buccaneers-2018-reg-2?active-tab=watch', 'https://www.nfl.com/games/texans-at-titans-2018-reg-2?active-tab=watch', 'https://www.nfl.com/games/colts-at-redskins-2018-reg-2?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-rams-2018-reg-2?active-tab=watch', 'https://www.nfl.com/games/lions-at-49ers-2018-reg-2?active-tab=watch', 'https://www.nfl.com/games/raiders-at-broncos-2018-reg-2?active-tab=watch', 'https://www.nfl.com/games/patriots-at-jaguars-2018-reg-2?active-tab=watch', 'https://www.nfl.com/games/giants-at-cowboys-2018-reg-2?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-bears-2018-reg-2?active-tab=watch'], 'reg3': ['https://www.nfl.com/games/jets-at-browns-2018-reg-3?active-tab=watch', 'https://www.nfl.com/games/saints-at-falcons-2018-reg-3?active-tab=watch', 'https://www.nfl.com/games/broncos-at-ravens-2018-reg-3?active-tab=watch', 'https://www.nfl.com/games/bengals-at-panthers-2018-reg-3?active-tab=watch', 'https://www.nfl.com/games/giants-at-texans-2018-reg-3?active-tab=watch', 'https://www.nfl.com/games/titans-at-jaguars-2018-reg-3?active-tab=watch', 'https://www.nfl.com/games/49ers-at-chiefs-2018-reg-3?active-tab=watch', 'https://www.nfl.com/games/raiders-at-dolphins-2018-reg-3?active-tab=watch', 'https://www.nfl.com/games/bills-at-vikings-2018-reg-3?active-tab=watch', 'https://www.nfl.com/games/colts-at-eagles-2018-reg-3?active-tab=watch', 'https://www.nfl.com/games/packers-at-redskins-2018-reg-3?active-tab=watch', 'https://www.nfl.com/games/chargers-at-rams-2018-reg-3?active-tab=watch', 'https://www.nfl.com/games/bears-at-cardinals-2018-reg-3?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-seahawks-2018-reg-3?active-tab=watch', 'https://www.nfl.com/games/patriots-at-lions-2018-reg-3?active-tab=watch', 'https://www.nfl.com/games/steelers-at-buccaneers-2018-reg-3?active-tab=watch'], 'reg4': ['https://www.nfl.com/games/vikings-at-rams-2018-reg-4?active-tab=watch', 'https://www.nfl.com/games/bengals-at-falcons-2018-reg-4?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-bears-2018-reg-4?active-tab=watch', 'https://www.nfl.com/games/lions-at-cowboys-2018-reg-4?active-tab=watch', 'https://www.nfl.com/games/bills-at-packers-2018-reg-4?active-tab=watch', 'https://www.nfl.com/games/texans-at-colts-2018-reg-4?active-tab=watch', 'https://www.nfl.com/games/jets-at-jaguars-2018-reg-4?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-patriots-2018-reg-4?active-tab=watch', 'https://www.nfl.com/games/eagles-at-titans-2018-reg-4?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-cardinals-2018-reg-4?active-tab=watch', 'https://www.nfl.com/games/browns-at-raiders-2018-reg-4?active-tab=watch', 'https://www.nfl.com/games/49ers-at-chargers-2018-reg-4?active-tab=watch', 'https://www.nfl.com/games/saints-at-giants-2018-reg-4?active-tab=watch', 'https://www.nfl.com/games/ravens-at-steelers-2018-reg-4?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-broncos-2018-reg-4?active-tab=watch'], 'reg5': ['https://www.nfl.com/games/colts-at-patriots-2018-reg-5?active-tab=watch', 'https://www.nfl.com/games/titans-at-bills-2018-reg-5?active-tab=watch', 'https://www.nfl.com/games/giants-at-panthers-2018-reg-5?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-bengals-2018-reg-5?active-tab=watch', 'https://www.nfl.com/games/ravens-at-browns-2018-reg-5?active-tab=watch', 'https://www.nfl.com/games/packers-at-lions-2018-reg-5?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-chiefs-2018-reg-5?active-tab=watch', 'https://www.nfl.com/games/broncos-at-jets-2018-reg-5?active-tab=watch', 'https://www.nfl.com/games/falcons-at-steelers-2018-reg-5?active-tab=watch', 'https://www.nfl.com/games/raiders-at-chargers-2018-reg-5?active-tab=watch', 'https://www.nfl.com/games/vikings-at-eagles-2018-reg-5?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-49ers-2018-reg-5?active-tab=watch', 'https://www.nfl.com/games/rams-at-seahawks-2018-reg-5?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-texans-2018-reg-5?active-tab=watch', 'https://www.nfl.com/games/redskins-at-saints-2018-reg-5?active-tab=watch'], 'reg6': ['https://www.nfl.com/games/eagles-at-giants-2018-reg-6?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-falcons-2018-reg-6?active-tab=watch', 'https://www.nfl.com/games/steelers-at-bengals-2018-reg-6?active-tab=watch', 'https://www.nfl.com/games/chargers-at-browns-2018-reg-6?active-tab=watch', 'https://www.nfl.com/games/bills-at-texans-2018-reg-6?active-tab=watch', 'https://www.nfl.com/games/bears-at-dolphins-2018-reg-6?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-vikings-2018-reg-6?active-tab=watch', 'https://www.nfl.com/games/colts-at-jets-2018-reg-6?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-raiders-2018-reg-6?active-tab=watch', 'https://www.nfl.com/games/panthers-at-redskins-2018-reg-6?active-tab=watch', 'https://www.nfl.com/games/rams-at-broncos-2018-reg-6?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-cowboys-2018-reg-6?active-tab=watch', 'https://www.nfl.com/games/ravens-at-titans-2018-reg-6?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-patriots-2018-reg-6?active-tab=watch', 'https://www.nfl.com/games/49ers-at-packers-2018-reg-6?active-tab=watch'], 'reg7': ['https://www.nfl.com/games/broncos-at-cardinals-2018-reg-7?active-tab=watch', 'https://www.nfl.com/games/titans-at-chargers-2018-reg-7?active-tab=watch', 'https://www.nfl.com/games/patriots-at-bears-2018-reg-7?active-tab=watch', 'https://www.nfl.com/games/bills-at-colts-2018-reg-7?active-tab=watch', 'https://www.nfl.com/games/texans-at-jaguars-2018-reg-7?active-tab=watch', 'https://www.nfl.com/games/lions-at-dolphins-2018-reg-7?active-tab=watch', 'https://www.nfl.com/games/vikings-at-jets-2018-reg-7?active-tab=watch', 'https://www.nfl.com/games/panthers-at-eagles-2018-reg-7?active-tab=watch', 'https://www.nfl.com/games/browns-at-buccaneers-2018-reg-7?active-tab=watch', 'https://www.nfl.com/games/saints-at-ravens-2018-reg-7?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-redskins-2018-reg-7?active-tab=watch', 'https://www.nfl.com/games/rams-at-49ers-2018-reg-7?active-tab=watch', 'https://www.nfl.com/games/bengals-at-chiefs-2018-reg-7?active-tab=watch', 'https://www.nfl.com/games/giants-at-falcons-2018-reg-7?active-tab=watch'], 'reg8': ['https://www.nfl.com/games/dolphins-at-texans-2018-reg-8?active-tab=watch', 'https://www.nfl.com/games/eagles-at-jaguars-2018-reg-8?active-tab=watch', 'https://www.nfl.com/games/ravens-at-panthers-2018-reg-8?active-tab=watch', 'https://www.nfl.com/games/jets-at-bears-2018-reg-8?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-bengals-2018-reg-8?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-lions-2018-reg-8?active-tab=watch', 'https://www.nfl.com/games/broncos-at-chiefs-2018-reg-8?active-tab=watch', 'https://www.nfl.com/games/redskins-at-giants-2018-reg-8?active-tab=watch', 'https://www.nfl.com/games/browns-at-steelers-2018-reg-8?active-tab=watch', 'https://www.nfl.com/games/colts-at-raiders-2018-reg-8?active-tab=watch', 'https://www.nfl.com/games/49ers-at-cardinals-2018-reg-8?active-tab=watch', 'https://www.nfl.com/games/packers-at-rams-2018-reg-8?active-tab=watch', 'https://www.nfl.com/games/saints-at-vikings-2018-reg-8?active-tab=watch', 'https://www.nfl.com/games/patriots-at-bills-2018-reg-8?active-tab=watch'], 'reg9': ['https://www.nfl.com/games/raiders-at-49ers-2018-reg-9?active-tab=watch', 'https://www.nfl.com/games/steelers-at-ravens-2018-reg-9?active-tab=watch', 'https://www.nfl.com/games/bears-at-bills-2018-reg-9?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-panthers-2018-reg-9?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-browns-2018-reg-9?active-tab=watch', 'https://www.nfl.com/games/jets-at-dolphins-2018-reg-9?active-tab=watch', 'https://www.nfl.com/games/lions-at-vikings-2018-reg-9?active-tab=watch', 'https://www.nfl.com/games/falcons-at-redskins-2018-reg-9?active-tab=watch', 'https://www.nfl.com/games/texans-at-broncos-2018-reg-9?active-tab=watch', 'https://www.nfl.com/games/chargers-at-seahawks-2018-reg-9?active-tab=watch', 'https://www.nfl.com/games/rams-at-saints-2018-reg-9?active-tab=watch', 'https://www.nfl.com/games/packers-at-patriots-2018-reg-9?active-tab=watch', 'https://www.nfl.com/games/titans-at-cowboys-2018-reg-9?active-tab=watch'], 'reg10': ['https://www.nfl.com/games/panthers-at-steelers-2018-reg-10?active-tab=watch', 'https://www.nfl.com/games/lions-at-bears-2018-reg-10?active-tab=watch', 'https://www.nfl.com/games/saints-at-bengals-2018-reg-10?active-tab=watch', 'https://www.nfl.com/games/falcons-at-browns-2018-reg-10?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-colts-2018-reg-10?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-chiefs-2018-reg-10?active-tab=watch', 'https://www.nfl.com/games/bills-at-jets-2018-reg-10?active-tab=watch', 'https://www.nfl.com/games/redskins-at-buccaneers-2018-reg-10?active-tab=watch', 'https://www.nfl.com/games/patriots-at-titans-2018-reg-10?active-tab=watch', 'https://www.nfl.com/games/chargers-at-raiders-2018-reg-10?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-packers-2018-reg-10?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-rams-2018-reg-10?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-eagles-2018-reg-10?active-tab=watch', 'https://www.nfl.com/games/giants-at-49ers-2018-reg-10?active-tab=watch'], 'reg11': ['https://www.nfl.com/games/packers-at-seahawks-2018-reg-11?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-falcons-2018-reg-11?active-tab=watch', 'https://www.nfl.com/games/bengals-at-ravens-2018-reg-11?active-tab=watch', 'https://www.nfl.com/games/panthers-at-lions-2018-reg-11?active-tab=watch', 'https://www.nfl.com/games/titans-at-colts-2018-reg-11?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-giants-2018-reg-11?active-tab=watch', 'https://www.nfl.com/games/texans-at-redskins-2018-reg-11?active-tab=watch', 'https://www.nfl.com/games/steelers-at-jaguars-2018-reg-11?active-tab=watch', 'https://www.nfl.com/games/raiders-at-cardinals-2018-reg-11?active-tab=watch', 'https://www.nfl.com/games/broncos-at-chargers-2018-reg-11?active-tab=watch', 'https://www.nfl.com/games/eagles-at-saints-2018-reg-11?active-tab=watch', 'https://www.nfl.com/games/vikings-at-bears-2018-reg-11?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-rams-2018-reg-11?active-tab=watch'], 'reg12': ['https://www.nfl.com/games/bears-at-lions-2018-reg-12?active-tab=watch', 'https://www.nfl.com/games/redskins-at-cowboys-2018-reg-12?active-tab=watch', 'https://www.nfl.com/games/falcons-at-saints-2018-reg-12?active-tab=watch', 'https://www.nfl.com/games/raiders-at-ravens-2018-reg-12?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-bills-2018-reg-12?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-panthers-2018-reg-12?active-tab=watch', 'https://www.nfl.com/games/browns-at-bengals-2018-reg-12?active-tab=watch', 'https://www.nfl.com/games/patriots-at-jets-2018-reg-12?active-tab=watch', 'https://www.nfl.com/games/giants-at-eagles-2018-reg-12?active-tab=watch', 'https://www.nfl.com/games/49ers-at-buccaneers-2018-reg-12?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-chargers-2018-reg-12?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-colts-2018-reg-12?active-tab=watch', 'https://www.nfl.com/games/steelers-at-broncos-2018-reg-12?active-tab=watch', 'https://www.nfl.com/games/packers-at-vikings-2018-reg-12?active-tab=watch', 'https://www.nfl.com/games/titans-at-texans-2018-reg-12?active-tab=watch'], 'reg13': ['https://www.nfl.com/games/saints-at-cowboys-2018-reg-13?active-tab=watch', 'https://www.nfl.com/games/ravens-at-falcons-2018-reg-13?active-tab=watch', 'https://www.nfl.com/games/broncos-at-bengals-2018-reg-13?active-tab=watch', 'https://www.nfl.com/games/rams-at-lions-2018-reg-13?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-packers-2018-reg-13?active-tab=watch', 'https://www.nfl.com/games/browns-at-texans-2018-reg-13?active-tab=watch', 'https://www.nfl.com/games/colts-at-jaguars-2018-reg-13?active-tab=watch', 'https://www.nfl.com/games/bills-at-dolphins-2018-reg-13?active-tab=watch', 'https://www.nfl.com/games/bears-at-giants-2018-reg-13?active-tab=watch', 'https://www.nfl.com/games/panthers-at-buccaneers-2018-reg-13?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-raiders-2018-reg-13?active-tab=watch', 'https://www.nfl.com/games/jets-at-titans-2018-reg-13?active-tab=watch', 'https://www.nfl.com/games/vikings-at-patriots-2018-reg-13?active-tab=watch', 'https://www.nfl.com/games/49ers-at-seahawks-2018-reg-13?active-tab=watch', 'https://www.nfl.com/games/chargers-at-steelers-2018-reg-13?active-tab=watch', 'https://www.nfl.com/games/redskins-at-eagles-2018-reg-13?active-tab=watch'], 'reg14': ['https://www.nfl.com/games/jaguars-at-titans-2018-reg-14?active-tab=watch', 'https://www.nfl.com/games/jets-at-bills-2018-reg-14?active-tab=watch', 'https://www.nfl.com/games/panthers-at-browns-2018-reg-14?active-tab=watch', 'https://www.nfl.com/games/falcons-at-packers-2018-reg-14?active-tab=watch', 'https://www.nfl.com/games/colts-at-texans-2018-reg-14?active-tab=watch', 'https://www.nfl.com/games/ravens-at-chiefs-2018-reg-14?active-tab=watch', 'https://www.nfl.com/games/patriots-at-dolphins-2018-reg-14?active-tab=watch', 'https://www.nfl.com/games/saints-at-buccaneers-2018-reg-14?active-tab=watch', 'https://www.nfl.com/games/giants-at-redskins-2018-reg-14?active-tab=watch', 'https://www.nfl.com/games/bengals-at-chargers-2018-reg-14?active-tab=watch', 'https://www.nfl.com/games/broncos-at-49ers-2018-reg-14?active-tab=watch', 'https://www.nfl.com/games/lions-at-cardinals-2018-reg-14?active-tab=watch', 'https://www.nfl.com/games/eagles-at-cowboys-2018-reg-14?active-tab=watch', 'https://www.nfl.com/games/steelers-at-raiders-2018-reg-14?active-tab=watch', 'https://www.nfl.com/games/rams-at-bears-2018-reg-14?active-tab=watch', 'https://www.nfl.com/games/vikings-at-seahawks-2018-reg-14?active-tab=watch'], 'reg15': ['https://www.nfl.com/games/chargers-at-chiefs-2018-reg-15?active-tab=watch', 'https://www.nfl.com/games/texans-at-jets-2018-reg-15?active-tab=watch', 'https://www.nfl.com/games/browns-at-broncos-2018-reg-15?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-falcons-2018-reg-15?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-ravens-2018-reg-15?active-tab=watch', 'https://www.nfl.com/games/lions-at-bills-2018-reg-15?active-tab=watch', 'https://www.nfl.com/games/packers-at-bears-2018-reg-15?active-tab=watch', 'https://www.nfl.com/games/raiders-at-bengals-2018-reg-15?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-colts-2018-reg-15?active-tab=watch', 'https://www.nfl.com/games/redskins-at-jaguars-2018-reg-15?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-vikings-2018-reg-15?active-tab=watch', 'https://www.nfl.com/games/titans-at-giants-2018-reg-15?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-49ers-2018-reg-15?active-tab=watch', 'https://www.nfl.com/games/patriots-at-steelers-2018-reg-15?active-tab=watch', 'https://www.nfl.com/games/eagles-at-rams-2018-reg-15?active-tab=watch', 'https://www.nfl.com/games/saints-at-panthers-2018-reg-15?active-tab=watch'], 'reg16': ['https://www.nfl.com/games/redskins-at-titans-2018-reg-16?active-tab=watch', 'https://www.nfl.com/games/ravens-at-chargers-2018-reg-16?active-tab=watch', 'https://www.nfl.com/games/giants-at-colts-2018-reg-16?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-dolphins-2018-reg-16?active-tab=watch', 'https://www.nfl.com/games/falcons-at-panthers-2018-reg-16?active-tab=watch', 'https://www.nfl.com/games/bengals-at-browns-2018-reg-16?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-cowboys-2018-reg-16?active-tab=watch', 'https://www.nfl.com/games/vikings-at-lions-2018-reg-16?active-tab=watch', 'https://www.nfl.com/games/bills-at-patriots-2018-reg-16?active-tab=watch', 'https://www.nfl.com/games/packers-at-jets-2018-reg-16?active-tab=watch', 'https://www.nfl.com/games/texans-at-eagles-2018-reg-16?active-tab=watch', 'https://www.nfl.com/games/rams-at-cardinals-2018-reg-16?active-tab=watch', 'https://www.nfl.com/games/bears-at-49ers-2018-reg-16?active-tab=watch', 'https://www.nfl.com/games/steelers-at-saints-2018-reg-16?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-seahawks-2018-reg-16?active-tab=watch', 'https://www.nfl.com/games/broncos-at-raiders-2018-reg-16?active-tab=watch'], 'reg17': ['https://www.nfl.com/games/dolphins-at-bills-2018-reg-17?active-tab=watch', 'https://www.nfl.com/games/lions-at-packers-2018-reg-17?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-texans-2018-reg-17?active-tab=watch', 'https://www.nfl.com/games/jets-at-patriots-2018-reg-17?active-tab=watch', 'https://www.nfl.com/games/panthers-at-saints-2018-reg-17?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-giants-2018-reg-17?active-tab=watch', 'https://www.nfl.com/games/falcons-at-buccaneers-2018-reg-17?active-tab=watch', 'https://www.nfl.com/games/browns-at-ravens-2018-reg-17?active-tab=watch', 'https://www.nfl.com/games/raiders-at-chiefs-2018-reg-17?active-tab=watch', 'https://www.nfl.com/games/bears-at-vikings-2018-reg-17?active-tab=watch', 'https://www.nfl.com/games/bengals-at-steelers-2018-reg-17?active-tab=watch', 'https://www.nfl.com/games/eagles-at-redskins-2018-reg-17?active-tab=watch', 'https://www.nfl.com/games/chargers-at-broncos-2018-reg-17?active-tab=watch', 'https://www.nfl.com/games/49ers-at-rams-2018-reg-17?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-seahawks-2018-reg-17?active-tab=watch', 'https://www.nfl.com/games/colts-at-titans-2018-reg-17?active-tab=watch']}, '2019': {'reg1': ['https://www.nfl.com/games/packers-at-bears-2019-reg-1?active-tab=watch', 'https://www.nfl.com/games/rams-at-panthers-2019-reg-1?active-tab=watch', 'https://www.nfl.com/games/titans-at-browns-2019-reg-1?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-jaguars-2019-reg-1?active-tab=watch', 'https://www.nfl.com/games/ravens-at-dolphins-2019-reg-1?active-tab=watch', 'https://www.nfl.com/games/falcons-at-vikings-2019-reg-1?active-tab=watch', 'https://www.nfl.com/games/bills-at-jets-2019-reg-1?active-tab=watch', 'https://www.nfl.com/games/redskins-at-eagles-2019-reg-1?active-tab=watch', 'https://www.nfl.com/games/colts-at-chargers-2019-reg-1?active-tab=watch', 'https://www.nfl.com/games/bengals-at-seahawks-2019-reg-1?active-tab=watch', 'https://www.nfl.com/games/lions-at-cardinals-2019-reg-1?active-tab=watch', 'https://www.nfl.com/games/giants-at-cowboys-2019-reg-1?active-tab=watch', 'https://www.nfl.com/games/49ers-at-buccaneers-2019-reg-1?active-tab=watch', 'https://www.nfl.com/games/steelers-at-patriots-2019-reg-1?active-tab=watch', 'https://www.nfl.com/games/texans-at-saints-2019-reg-1?active-tab=watch', 'https://www.nfl.com/games/broncos-at-raiders-2019-reg-1?active-tab=watch'], 'reg2': ['https://www.nfl.com/games/buccaneers-at-panthers-2019-reg-2?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-ravens-2019-reg-2?active-tab=watch', 'https://www.nfl.com/games/49ers-at-bengals-2019-reg-2?active-tab=watch', 'https://www.nfl.com/games/chargers-at-lions-2019-reg-2?active-tab=watch', 'https://www.nfl.com/games/vikings-at-packers-2019-reg-2?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-texans-2019-reg-2?active-tab=watch', 'https://www.nfl.com/games/patriots-at-dolphins-2019-reg-2?active-tab=watch', 'https://www.nfl.com/games/bills-at-giants-2019-reg-2?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-steelers-2019-reg-2?active-tab=watch', 'https://www.nfl.com/games/colts-at-titans-2019-reg-2?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-redskins-2019-reg-2?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-raiders-2019-reg-2?active-tab=watch', 'https://www.nfl.com/games/bears-at-broncos-2019-reg-2?active-tab=watch', 'https://www.nfl.com/games/saints-at-rams-2019-reg-2?active-tab=watch', 'https://www.nfl.com/games/eagles-at-falcons-2019-reg-2?active-tab=watch', 'https://www.nfl.com/games/browns-at-jets-2019-reg-2?active-tab=watch'], 'reg3': ['https://www.nfl.com/games/titans-at-jaguars-2019-reg-3?active-tab=watch', 'https://www.nfl.com/games/bengals-at-bills-2019-reg-3?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-cowboys-2019-reg-3?active-tab=watch', 'https://www.nfl.com/games/broncos-at-packers-2019-reg-3?active-tab=watch', 'https://www.nfl.com/games/falcons-at-colts-2019-reg-3?active-tab=watch', 'https://www.nfl.com/games/ravens-at-chiefs-2019-reg-3?active-tab=watch', 'https://www.nfl.com/games/raiders-at-vikings-2019-reg-3?active-tab=watch', 'https://www.nfl.com/games/jets-at-patriots-2019-reg-3?active-tab=watch', 'https://www.nfl.com/games/lions-at-eagles-2019-reg-3?active-tab=watch', 'https://www.nfl.com/games/panthers-at-cardinals-2019-reg-3?active-tab=watch', 'https://www.nfl.com/games/giants-at-buccaneers-2019-reg-3?active-tab=watch', 'https://www.nfl.com/games/texans-at-chargers-2019-reg-3?active-tab=watch', 'https://www.nfl.com/games/saints-at-seahawks-2019-reg-3?active-tab=watch', 'https://www.nfl.com/games/steelers-at-49ers-2019-reg-3?active-tab=watch', 'https://www.nfl.com/games/rams-at-browns-2019-reg-3?active-tab=watch', 'https://www.nfl.com/games/bears-at-redskins-2019-reg-3?active-tab=watch'], 'reg4': ['https://www.nfl.com/games/eagles-at-packers-2019-reg-4?active-tab=watch', 'https://www.nfl.com/games/titans-at-falcons-2019-reg-4?active-tab=watch', 'https://www.nfl.com/games/browns-at-ravens-2019-reg-4?active-tab=watch', 'https://www.nfl.com/games/patriots-at-bills-2019-reg-4?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-lions-2019-reg-4?active-tab=watch', 'https://www.nfl.com/games/panthers-at-texans-2019-reg-4?active-tab=watch', 'https://www.nfl.com/games/raiders-at-colts-2019-reg-4?active-tab=watch', 'https://www.nfl.com/games/chargers-at-dolphins-2019-reg-4?active-tab=watch', 'https://www.nfl.com/games/redskins-at-giants-2019-reg-4?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-cardinals-2019-reg-4?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-rams-2019-reg-4?active-tab=watch', 'https://www.nfl.com/games/vikings-at-bears-2019-reg-4?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-broncos-2019-reg-4?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-saints-2019-reg-4?active-tab=watch', 'https://www.nfl.com/games/bengals-at-steelers-2019-reg-4?active-tab=watch'], 'reg5': ['https://www.nfl.com/games/rams-at-seahawks-2019-reg-5?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-panthers-2019-reg-5?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-bengals-2019-reg-5?active-tab=watch', 'https://www.nfl.com/games/falcons-at-texans-2019-reg-5?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-saints-2019-reg-5?active-tab=watch', 'https://www.nfl.com/games/vikings-at-giants-2019-reg-5?active-tab=watch', 'https://www.nfl.com/games/bears-at-raiders-2019-reg-5?active-tab=watch', 'https://www.nfl.com/games/jets-at-eagles-2019-reg-5?active-tab=watch', 'https://www.nfl.com/games/ravens-at-steelers-2019-reg-5?active-tab=watch', 'https://www.nfl.com/games/bills-at-titans-2019-reg-5?active-tab=watch', 'https://www.nfl.com/games/patriots-at-redskins-2019-reg-5?active-tab=watch', 'https://www.nfl.com/games/broncos-at-chargers-2019-reg-5?active-tab=watch', 'https://www.nfl.com/games/packers-at-cowboys-2019-reg-5?active-tab=watch', 'https://www.nfl.com/games/colts-at-chiefs-2019-reg-5?active-tab=watch', 'https://www.nfl.com/games/browns-at-49ers-2019-reg-5?active-tab=watch'], 'reg6': ['https://www.nfl.com/games/giants-at-patriots-2019-reg-6?active-tab=watch', 'https://www.nfl.com/games/panthers-at-buccaneers-2019-reg-6?active-tab=watch', 'https://www.nfl.com/games/bengals-at-ravens-2019-reg-6?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-browns-2019-reg-6?active-tab=watch', 'https://www.nfl.com/games/saints-at-jaguars-2019-reg-6?active-tab=watch', 'https://www.nfl.com/games/texans-at-chiefs-2019-reg-6?active-tab=watch', 'https://www.nfl.com/games/redskins-at-dolphins-2019-reg-6?active-tab=watch', 'https://www.nfl.com/games/eagles-at-vikings-2019-reg-6?active-tab=watch', 'https://www.nfl.com/games/falcons-at-cardinals-2019-reg-6?active-tab=watch', 'https://www.nfl.com/games/49ers-at-rams-2019-reg-6?active-tab=watch', 'https://www.nfl.com/games/titans-at-broncos-2019-reg-6?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-jets-2019-reg-6?active-tab=watch', 'https://www.nfl.com/games/steelers-at-chargers-2019-reg-6?active-tab=watch', 'https://www.nfl.com/games/lions-at-packers-2019-reg-6?active-tab=watch'], 'reg7': ['https://www.nfl.com/games/chiefs-at-broncos-2019-reg-7?active-tab=watch', 'https://www.nfl.com/games/rams-at-falcons-2019-reg-7?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-bills-2019-reg-7?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-bengals-2019-reg-7?active-tab=watch', 'https://www.nfl.com/games/vikings-at-lions-2019-reg-7?active-tab=watch', 'https://www.nfl.com/games/raiders-at-packers-2019-reg-7?active-tab=watch', 'https://www.nfl.com/games/texans-at-colts-2019-reg-7?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-giants-2019-reg-7?active-tab=watch', 'https://www.nfl.com/games/49ers-at-redskins-2019-reg-7?active-tab=watch', 'https://www.nfl.com/games/chargers-at-titans-2019-reg-7?active-tab=watch', 'https://www.nfl.com/games/saints-at-bears-2019-reg-7?active-tab=watch', 'https://www.nfl.com/games/ravens-at-seahawks-2019-reg-7?active-tab=watch', 'https://www.nfl.com/games/eagles-at-cowboys-2019-reg-7?active-tab=watch', 'https://www.nfl.com/games/patriots-at-jets-2019-reg-7?active-tab=watch'], 'reg8': ['https://www.nfl.com/games/redskins-at-vikings-2019-reg-8?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-falcons-2019-reg-8?active-tab=watch', 'https://www.nfl.com/games/eagles-at-bills-2019-reg-8?active-tab=watch', 'https://www.nfl.com/games/chargers-at-bears-2019-reg-8?active-tab=watch', 'https://www.nfl.com/games/giants-at-lions-2019-reg-8?active-tab=watch', 'https://www.nfl.com/games/jets-at-jaguars-2019-reg-8?active-tab=watch', 'https://www.nfl.com/games/bengals-at-rams-2019-reg-8?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-saints-2019-reg-8?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-titans-2019-reg-8?active-tab=watch', 'https://www.nfl.com/games/broncos-at-colts-2019-reg-8?active-tab=watch', 'https://www.nfl.com/games/panthers-at-49ers-2019-reg-8?active-tab=watch', 'https://www.nfl.com/games/raiders-at-texans-2019-reg-8?active-tab=watch', 'https://www.nfl.com/games/browns-at-patriots-2019-reg-8?active-tab=watch', 'https://www.nfl.com/games/packers-at-chiefs-2019-reg-8?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-steelers-2019-reg-8?active-tab=watch'], 'reg9': ['https://www.nfl.com/games/49ers-at-cardinals-2019-reg-9?active-tab=watch', 'https://www.nfl.com/games/texans-at-jaguars-2019-reg-9?active-tab=watch', 'https://www.nfl.com/games/redskins-at-bills-2019-reg-9?active-tab=watch', 'https://www.nfl.com/games/titans-at-panthers-2019-reg-9?active-tab=watch', 'https://www.nfl.com/games/vikings-at-chiefs-2019-reg-9?active-tab=watch', 'https://www.nfl.com/games/jets-at-dolphins-2019-reg-9?active-tab=watch', 'https://www.nfl.com/games/bears-at-eagles-2019-reg-9?active-tab=watch', 'https://www.nfl.com/games/colts-at-steelers-2019-reg-9?active-tab=watch', 'https://www.nfl.com/games/lions-at-raiders-2019-reg-9?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-seahawks-2019-reg-9?active-tab=watch', 'https://www.nfl.com/games/browns-at-broncos-2019-reg-9?active-tab=watch', 'https://www.nfl.com/games/packers-at-chargers-2019-reg-9?active-tab=watch', 'https://www.nfl.com/games/patriots-at-ravens-2019-reg-9?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-giants-2019-reg-9?active-tab=watch'], 'reg10': ['https://www.nfl.com/games/chargers-at-raiders-2019-reg-10?active-tab=watch', 'https://www.nfl.com/games/lions-at-bears-2019-reg-10?active-tab=watch', 'https://www.nfl.com/games/ravens-at-bengals-2019-reg-10?active-tab=watch', 'https://www.nfl.com/games/bills-at-browns-2019-reg-10?active-tab=watch', 'https://www.nfl.com/games/falcons-at-saints-2019-reg-10?active-tab=watch', 'https://www.nfl.com/games/giants-at-jets-2019-reg-10?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-buccaneers-2019-reg-10?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-titans-2019-reg-10?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-colts-2019-reg-10?active-tab=watch', 'https://www.nfl.com/games/panthers-at-packers-2019-reg-10?active-tab=watch', 'https://www.nfl.com/games/rams-at-steelers-2019-reg-10?active-tab=watch', 'https://www.nfl.com/games/vikings-at-cowboys-2019-reg-10?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-49ers-2019-reg-10?active-tab=watch'], 'reg11': ['https://www.nfl.com/games/steelers-at-browns-2019-reg-11?active-tab=watch', 'https://www.nfl.com/games/texans-at-ravens-2019-reg-11?active-tab=watch', 'https://www.nfl.com/games/falcons-at-panthers-2019-reg-11?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-lions-2019-reg-11?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-colts-2019-reg-11?active-tab=watch', 'https://www.nfl.com/games/bills-at-dolphins-2019-reg-11?active-tab=watch', 'https://www.nfl.com/games/broncos-at-vikings-2019-reg-11?active-tab=watch', 'https://www.nfl.com/games/saints-at-buccaneers-2019-reg-11?active-tab=watch', 'https://www.nfl.com/games/jets-at-redskins-2019-reg-11?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-49ers-2019-reg-11?active-tab=watch', 'https://www.nfl.com/games/bengals-at-raiders-2019-reg-11?active-tab=watch', 'https://www.nfl.com/games/patriots-at-eagles-2019-reg-11?active-tab=watch', 'https://www.nfl.com/games/bears-at-rams-2019-reg-11?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-chargers-2019-reg-11?active-tab=watch'], 'reg12': ['https://www.nfl.com/games/colts-at-texans-2019-reg-12?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-falcons-2019-reg-12?active-tab=watch', 'https://www.nfl.com/games/broncos-at-bills-2019-reg-12?active-tab=watch', 'https://www.nfl.com/games/giants-at-bears-2019-reg-12?active-tab=watch', 'https://www.nfl.com/games/steelers-at-bengals-2019-reg-12?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-browns-2019-reg-12?active-tab=watch', 'https://www.nfl.com/games/panthers-at-saints-2019-reg-12?active-tab=watch', 'https://www.nfl.com/games/raiders-at-jets-2019-reg-12?active-tab=watch', 'https://www.nfl.com/games/lions-at-redskins-2019-reg-12?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-eagles-2019-reg-12?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-titans-2019-reg-12?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-patriots-2019-reg-12?active-tab=watch', 'https://www.nfl.com/games/packers-at-49ers-2019-reg-12?active-tab=watch', 'https://www.nfl.com/games/ravens-at-rams-2019-reg-12?active-tab=watch'], 'reg13': ['https://www.nfl.com/games/bears-at-lions-2019-reg-13?active-tab=watch', 'https://www.nfl.com/games/bills-at-cowboys-2019-reg-13?active-tab=watch', 'https://www.nfl.com/games/saints-at-falcons-2019-reg-13?active-tab=watch', 'https://www.nfl.com/games/49ers-at-ravens-2019-reg-13?active-tab=watch', 'https://www.nfl.com/games/redskins-at-panthers-2019-reg-13?active-tab=watch', 'https://www.nfl.com/games/jets-at-bengals-2019-reg-13?active-tab=watch', 'https://www.nfl.com/games/titans-at-colts-2019-reg-13?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-jaguars-2019-reg-13?active-tab=watch', 'https://www.nfl.com/games/eagles-at-dolphins-2019-reg-13?active-tab=watch', 'https://www.nfl.com/games/packers-at-giants-2019-reg-13?active-tab=watch', 'https://www.nfl.com/games/browns-at-steelers-2019-reg-13?active-tab=watch', 'https://www.nfl.com/games/rams-at-cardinals-2019-reg-13?active-tab=watch', 'https://www.nfl.com/games/raiders-at-chiefs-2019-reg-13?active-tab=watch', 'https://www.nfl.com/games/chargers-at-broncos-2019-reg-13?active-tab=watch', 'https://www.nfl.com/games/patriots-at-texans-2019-reg-13?active-tab=watch', 'https://www.nfl.com/games/vikings-at-seahawks-2019-reg-13?active-tab=watch'], 'reg14': ['https://www.nfl.com/games/cowboys-at-bears-2019-reg-14?active-tab=watch', 'https://www.nfl.com/games/panthers-at-falcons-2019-reg-14?active-tab=watch', 'https://www.nfl.com/games/ravens-at-bills-2019-reg-14?active-tab=watch', 'https://www.nfl.com/games/bengals-at-browns-2019-reg-14?active-tab=watch', 'https://www.nfl.com/games/redskins-at-packers-2019-reg-14?active-tab=watch', 'https://www.nfl.com/games/broncos-at-texans-2019-reg-14?active-tab=watch', 'https://www.nfl.com/games/lions-at-vikings-2019-reg-14?active-tab=watch', 'https://www.nfl.com/games/49ers-at-saints-2019-reg-14?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-jets-2019-reg-14?active-tab=watch', 'https://www.nfl.com/games/colts-at-buccaneers-2019-reg-14?active-tab=watch', 'https://www.nfl.com/games/chargers-at-jaguars-2019-reg-14?active-tab=watch', 'https://www.nfl.com/games/steelers-at-cardinals-2019-reg-14?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-patriots-2019-reg-14?active-tab=watch', 'https://www.nfl.com/games/titans-at-raiders-2019-reg-14?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-rams-2019-reg-14?active-tab=watch', 'https://www.nfl.com/games/giants-at-eagles-2019-reg-14?active-tab=watch'], 'reg15': ['https://www.nfl.com/games/jets-at-ravens-2019-reg-15?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-panthers-2019-reg-15?active-tab=watch', 'https://www.nfl.com/games/patriots-at-bengals-2019-reg-15?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-lions-2019-reg-15?active-tab=watch', 'https://www.nfl.com/games/bears-at-packers-2019-reg-15?active-tab=watch', 'https://www.nfl.com/games/broncos-at-chiefs-2019-reg-15?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-giants-2019-reg-15?active-tab=watch', 'https://www.nfl.com/games/texans-at-titans-2019-reg-15?active-tab=watch', 'https://www.nfl.com/games/eagles-at-redskins-2019-reg-15?active-tab=watch', 'https://www.nfl.com/games/browns-at-cardinals-2019-reg-15?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-raiders-2019-reg-15?active-tab=watch', 'https://www.nfl.com/games/vikings-at-chargers-2019-reg-15?active-tab=watch', 'https://www.nfl.com/games/rams-at-cowboys-2019-reg-15?active-tab=watch', 'https://www.nfl.com/games/falcons-at-49ers-2019-reg-15?active-tab=watch', 'https://www.nfl.com/games/bills-at-steelers-2019-reg-15?active-tab=watch', 'https://www.nfl.com/games/colts-at-saints-2019-reg-15?active-tab=watch'], 'reg16': ['https://www.nfl.com/games/texans-at-buccaneers-2019-reg-16?active-tab=watch', 'https://www.nfl.com/games/bills-at-patriots-2019-reg-16?active-tab=watch', 'https://www.nfl.com/games/rams-at-49ers-2019-reg-16?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-falcons-2019-reg-16?active-tab=watch', 'https://www.nfl.com/games/ravens-at-browns-2019-reg-16?active-tab=watch', 'https://www.nfl.com/games/panthers-at-colts-2019-reg-16?active-tab=watch', 'https://www.nfl.com/games/bengals-at-dolphins-2019-reg-16?active-tab=watch', 'https://www.nfl.com/games/steelers-at-jets-2019-reg-16?active-tab=watch', 'https://www.nfl.com/games/saints-at-titans-2019-reg-16?active-tab=watch', 'https://www.nfl.com/games/giants-at-redskins-2019-reg-16?active-tab=watch', 'https://www.nfl.com/games/lions-at-broncos-2019-reg-16?active-tab=watch', 'https://www.nfl.com/games/raiders-at-chargers-2019-reg-16?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-eagles-2019-reg-16?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-seahawks-2019-reg-16?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-bears-2019-reg-16?active-tab=watch', 'https://www.nfl.com/games/packers-at-vikings-2019-reg-16?active-tab=watch'], 'reg17': ['https://www.nfl.com/games/jets-at-bills-2019-reg-17?active-tab=watch', 'https://www.nfl.com/games/saints-at-panthers-2019-reg-17?active-tab=watch', 'https://www.nfl.com/games/browns-at-bengals-2019-reg-17?active-tab=watch', 'https://www.nfl.com/games/packers-at-lions-2019-reg-17?active-tab=watch', 'https://www.nfl.com/games/chargers-at-chiefs-2019-reg-17?active-tab=watch', 'https://www.nfl.com/games/bears-at-vikings-2019-reg-17?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-patriots-2019-reg-17?active-tab=watch', 'https://www.nfl.com/games/falcons-at-buccaneers-2019-reg-17?active-tab=watch', 'https://www.nfl.com/games/steelers-at-ravens-2019-reg-17?active-tab=watch', 'https://www.nfl.com/games/redskins-at-cowboys-2019-reg-17?active-tab=watch', 'https://www.nfl.com/games/titans-at-texans-2019-reg-17?active-tab=watch', 'https://www.nfl.com/games/colts-at-jaguars-2019-reg-17?active-tab=watch', 'https://www.nfl.com/games/eagles-at-giants-2019-reg-17?active-tab=watch', 'https://www.nfl.com/games/raiders-at-broncos-2019-reg-17?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-rams-2019-reg-17?active-tab=watch', 'https://www.nfl.com/games/49ers-at-seahawks-2019-reg-17?active-tab=watch']}, '2020': {'reg1': ['https://www.nfl.com/games/texans-at-chiefs-2020-reg-1?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-falcons-2020-reg-1?active-tab=watch', 'https://www.nfl.com/games/browns-at-ravens-2020-reg-1?active-tab=watch', 'https://www.nfl.com/games/jets-at-bills-2020-reg-1?active-tab=watch', 'https://www.nfl.com/games/raiders-at-panthers-2020-reg-1?active-tab=watch', 'https://www.nfl.com/games/bears-at-lions-2020-reg-1?active-tab=watch', 'https://www.nfl.com/games/colts-at-jaguars-2020-reg-1?active-tab=watch', 'https://www.nfl.com/games/packers-at-vikings-2020-reg-1?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-patriots-2020-reg-1?active-tab=watch', 'https://www.nfl.com/games/eagles-at-football-team-2020-reg-1?active-tab=watch', 'https://www.nfl.com/games/chargers-at-bengals-2020-reg-1?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-saints-2020-reg-1?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-49ers-2020-reg-1?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-rams-2020-reg-1?active-tab=watch', 'https://www.nfl.com/games/steelers-at-giants-2020-reg-1?active-tab=watch', 'https://www.nfl.com/games/titans-at-broncos-2020-reg-1?active-tab=watch'], 'reg2': ['https://www.nfl.com/games/bengals-at-browns-2020-reg-2?active-tab=watch', 'https://www.nfl.com/games/giants-at-bears-2020-reg-2?active-tab=watch', 'https://www.nfl.com/games/falcons-at-cowboys-2020-reg-2?active-tab=watch', 'https://www.nfl.com/games/lions-at-packers-2020-reg-2?active-tab=watch', 'https://www.nfl.com/games/vikings-at-colts-2020-reg-2?active-tab=watch', 'https://www.nfl.com/games/bills-at-dolphins-2020-reg-2?active-tab=watch', 'https://www.nfl.com/games/49ers-at-jets-2020-reg-2?active-tab=watch', 'https://www.nfl.com/games/rams-at-eagles-2020-reg-2?active-tab=watch', 'https://www.nfl.com/games/broncos-at-steelers-2020-reg-2?active-tab=watch', 'https://www.nfl.com/games/panthers-at-buccaneers-2020-reg-2?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-titans-2020-reg-2?active-tab=watch', 'https://www.nfl.com/games/football-team-at-cardinals-2020-reg-2?active-tab=watch', 'https://www.nfl.com/games/ravens-at-texans-2020-reg-2?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-chargers-2020-reg-2?active-tab=watch', 'https://www.nfl.com/games/patriots-at-seahawks-2020-reg-2?active-tab=watch', 'https://www.nfl.com/games/saints-at-raiders-2020-reg-2?active-tab=watch'], 'reg3': ['https://www.nfl.com/games/dolphins-at-jaguars-2020-reg-3?active-tab=watch', 'https://www.nfl.com/games/bears-at-falcons-2020-reg-3?active-tab=watch', 'https://www.nfl.com/games/rams-at-bills-2020-reg-3?active-tab=watch', 'https://www.nfl.com/games/football-team-at-browns-2020-reg-3?active-tab=watch', 'https://www.nfl.com/games/titans-at-vikings-2020-reg-3?active-tab=watch', 'https://www.nfl.com/games/raiders-at-patriots-2020-reg-3?active-tab=watch', 'https://www.nfl.com/games/49ers-at-giants-2020-reg-3?active-tab=watch', 'https://www.nfl.com/games/bengals-at-eagles-2020-reg-3?active-tab=watch', 'https://www.nfl.com/games/texans-at-steelers-2020-reg-3?active-tab=watch', 'https://www.nfl.com/games/jets-at-colts-2020-reg-3?active-tab=watch', 'https://www.nfl.com/games/panthers-at-chargers-2020-reg-3?active-tab=watch', 'https://www.nfl.com/games/lions-at-cardinals-2020-reg-3?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-broncos-2020-reg-3?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-seahawks-2020-reg-3?active-tab=watch', 'https://www.nfl.com/games/packers-at-saints-2020-reg-3?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-ravens-2020-reg-3?active-tab=watch'], 'reg4': ['https://www.nfl.com/games/broncos-at-jets-2020-reg-4?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-panthers-2020-reg-4?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-bengals-2020-reg-4?active-tab=watch', 'https://www.nfl.com/games/browns-at-cowboys-2020-reg-4?active-tab=watch', 'https://www.nfl.com/games/saints-at-lions-2020-reg-4?active-tab=watch', 'https://www.nfl.com/games/vikings-at-texans-2020-reg-4?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-dolphins-2020-reg-4?active-tab=watch', 'https://www.nfl.com/games/chargers-at-buccaneers-2020-reg-4?active-tab=watch', 'https://www.nfl.com/games/ravens-at-football-team-2020-reg-4?active-tab=watch', 'https://www.nfl.com/games/giants-at-rams-2020-reg-4?active-tab=watch', 'https://www.nfl.com/games/colts-at-bears-2020-reg-4-x4464?active-tab=watch', 'https://www.nfl.com/games/bills-at-raiders-2020-reg-4?active-tab=watch', 'https://www.nfl.com/games/eagles-at-49ers-2020-reg-4?active-tab=watch', 'https://www.nfl.com/games/patriots-at-chiefs-2020-reg-4?active-tab=watch', 'https://www.nfl.com/games/falcons-at-packers-2020-reg-4?active-tab=watch'], 'reg5': ['https://www.nfl.com/games/buccaneers-at-bears-2020-reg-5?active-tab=watch', 'https://www.nfl.com/games/panthers-at-falcons-2020-reg-5?active-tab=watch', 'https://www.nfl.com/games/bengals-at-ravens-2020-reg-5?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-texans-2020-reg-5?active-tab=watch', 'https://www.nfl.com/games/raiders-at-chiefs-2020-reg-5?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-jets-2020-reg-5?active-tab=watch', 'https://www.nfl.com/games/eagles-at-steelers-2020-reg-5?active-tab=watch', 'https://www.nfl.com/games/rams-at-football-team-2020-reg-5?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-49ers-2020-reg-5?active-tab=watch', 'https://www.nfl.com/games/colts-at-browns-2020-reg-5?active-tab=watch', 'https://www.nfl.com/games/giants-at-cowboys-2020-reg-5?active-tab=watch', 'https://www.nfl.com/games/vikings-at-seahawks-2020-reg-5?active-tab=watch', 'https://www.nfl.com/games/chargers-at-saints-2020-reg-5?active-tab=watch', 'https://www.nfl.com/games/bills-at-titans-2020-reg-5?active-tab=watch'], 'reg6': ['https://www.nfl.com/games/bears-at-panthers-2020-reg-6?active-tab=watch', 'https://www.nfl.com/games/bengals-at-colts-2020-reg-6?active-tab=watch', 'https://www.nfl.com/games/lions-at-jaguars-2020-reg-6?active-tab=watch', 'https://www.nfl.com/games/falcons-at-vikings-2020-reg-6?active-tab=watch', 'https://www.nfl.com/games/football-team-at-giants-2020-reg-6?active-tab=watch', 'https://www.nfl.com/games/ravens-at-eagles-2020-reg-6?active-tab=watch', 'https://www.nfl.com/games/browns-at-steelers-2020-reg-6?active-tab=watch', 'https://www.nfl.com/games/texans-at-titans-2020-reg-6?active-tab=watch', 'https://www.nfl.com/games/broncos-at-patriots-2020-reg-6?active-tab=watch', 'https://www.nfl.com/games/jets-at-dolphins-2020-reg-6?active-tab=watch', 'https://www.nfl.com/games/packers-at-buccaneers-2020-reg-6?active-tab=watch', 'https://www.nfl.com/games/rams-at-49ers-2020-reg-6?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-bills-2020-reg-6?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-cowboys-2020-reg-6?active-tab=watch'], 'reg7': ['https://www.nfl.com/games/giants-at-eagles-2020-reg-7?active-tab=watch', 'https://www.nfl.com/games/lions-at-falcons-2020-reg-7?active-tab=watch', 'https://www.nfl.com/games/browns-at-bengals-2020-reg-7?active-tab=watch', 'https://www.nfl.com/games/packers-at-texans-2020-reg-7?active-tab=watch', 'https://www.nfl.com/games/panthers-at-saints-2020-reg-7?active-tab=watch', 'https://www.nfl.com/games/bills-at-jets-2020-reg-7?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-football-team-2020-reg-7?active-tab=watch', 'https://www.nfl.com/games/steelers-at-titans-2020-reg-7?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-raiders-2020-reg-7?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-broncos-2020-reg-7?active-tab=watch', 'https://www.nfl.com/games/49ers-at-patriots-2020-reg-7?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-chargers-2020-reg-7?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-cardinals-2020-reg-7?active-tab=watch', 'https://www.nfl.com/games/bears-at-rams-2020-reg-7?active-tab=watch'], 'reg8': ['https://www.nfl.com/games/falcons-at-panthers-2020-reg-8?active-tab=watch', 'https://www.nfl.com/games/patriots-at-bills-2020-reg-8?active-tab=watch', 'https://www.nfl.com/games/titans-at-bengals-2020-reg-8?active-tab=watch', 'https://www.nfl.com/games/raiders-at-browns-2020-reg-8?active-tab=watch', 'https://www.nfl.com/games/colts-at-lions-2020-reg-8?active-tab=watch', 'https://www.nfl.com/games/vikings-at-packers-2020-reg-8?active-tab=watch', 'https://www.nfl.com/games/jets-at-chiefs-2020-reg-8?active-tab=watch', 'https://www.nfl.com/games/rams-at-dolphins-2020-reg-8?active-tab=watch', 'https://www.nfl.com/games/steelers-at-ravens-2020-reg-8?active-tab=watch', 'https://www.nfl.com/games/chargers-at-broncos-2020-reg-8?active-tab=watch', 'https://www.nfl.com/games/saints-at-bears-2020-reg-8?active-tab=watch', 'https://www.nfl.com/games/49ers-at-seahawks-2020-reg-8?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-eagles-2020-reg-8?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-giants-2020-reg-8?active-tab=watch'], 'reg9': ['https://www.nfl.com/games/packers-at-49ers-2020-reg-9?active-tab=watch', 'https://www.nfl.com/games/broncos-at-falcons-2020-reg-9?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-bills-2020-reg-9?active-tab=watch', 'https://www.nfl.com/games/ravens-at-colts-2020-reg-9?active-tab=watch', 'https://www.nfl.com/games/texans-at-jaguars-2020-reg-9?active-tab=watch', 'https://www.nfl.com/games/panthers-at-chiefs-2020-reg-9?active-tab=watch', 'https://www.nfl.com/games/lions-at-vikings-2020-reg-9?active-tab=watch', 'https://www.nfl.com/games/bears-at-titans-2020-reg-9?active-tab=watch', 'https://www.nfl.com/games/giants-at-football-team-2020-reg-9?active-tab=watch', 'https://www.nfl.com/games/raiders-at-chargers-2020-reg-9?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-cardinals-2020-reg-9?active-tab=watch', 'https://www.nfl.com/games/steelers-at-cowboys-2020-reg-9?active-tab=watch', 'https://www.nfl.com/games/saints-at-buccaneers-2020-reg-9?active-tab=watch', 'https://www.nfl.com/games/patriots-at-jets-2020-reg-9?active-tab=watch'], 'reg10': ['https://www.nfl.com/games/colts-at-titans-2020-reg-10?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-panthers-2020-reg-10?active-tab=watch', 'https://www.nfl.com/games/texans-at-browns-2020-reg-10?active-tab=watch', 'https://www.nfl.com/games/football-team-at-lions-2020-reg-10?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-packers-2020-reg-10?active-tab=watch', 'https://www.nfl.com/games/eagles-at-giants-2020-reg-10?active-tab=watch', 'https://www.nfl.com/games/bills-at-cardinals-2020-reg-10?active-tab=watch', 'https://www.nfl.com/games/broncos-at-raiders-2020-reg-10?active-tab=watch', 'https://www.nfl.com/games/chargers-at-dolphins-2020-reg-10?active-tab=watch', 'https://www.nfl.com/games/bengals-at-steelers-2020-reg-10?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-rams-2020-reg-10?active-tab=watch', 'https://www.nfl.com/games/49ers-at-saints-2020-reg-10?active-tab=watch', 'https://www.nfl.com/games/ravens-at-patriots-2020-reg-10?active-tab=watch', 'https://www.nfl.com/games/vikings-at-bears-2020-reg-10?active-tab=watch'], 'reg11': ['https://www.nfl.com/games/cardinals-at-seahawks-2020-reg-11?active-tab=watch', 'https://www.nfl.com/games/titans-at-ravens-2020-reg-11?active-tab=watch', 'https://www.nfl.com/games/lions-at-panthers-2020-reg-11?active-tab=watch', 'https://www.nfl.com/games/eagles-at-browns-2020-reg-11?active-tab=watch', 'https://www.nfl.com/games/patriots-at-texans-2020-reg-11?active-tab=watch', 'https://www.nfl.com/games/steelers-at-jaguars-2020-reg-11?active-tab=watch', 'https://www.nfl.com/games/falcons-at-saints-2020-reg-11?active-tab=watch', 'https://www.nfl.com/games/bengals-at-football-team-2020-reg-11?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-broncos-2020-reg-11?active-tab=watch', 'https://www.nfl.com/games/jets-at-chargers-2020-reg-11?active-tab=watch', 'https://www.nfl.com/games/packers-at-colts-2020-reg-11?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-vikings-2020-reg-11?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-raiders-2020-reg-11?active-tab=watch', 'https://www.nfl.com/games/rams-at-buccaneers-2020-reg-11?active-tab=watch'], 'reg12': ['https://www.nfl.com/games/texans-at-lions-2020-reg-12?active-tab=watch', 'https://www.nfl.com/games/football-team-at-cowboys-2020-reg-12?active-tab=watch', 'https://www.nfl.com/games/raiders-at-falcons-2020-reg-12?active-tab=watch', 'https://www.nfl.com/games/chargers-at-bills-2020-reg-12?active-tab=watch', 'https://www.nfl.com/games/giants-at-bengals-2020-reg-12?active-tab=watch', 'https://www.nfl.com/games/titans-at-colts-2020-reg-12?active-tab=watch', 'https://www.nfl.com/games/browns-at-jaguars-2020-reg-12?active-tab=watch', 'https://www.nfl.com/games/panthers-at-vikings-2020-reg-12?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-patriots-2020-reg-12?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-jets-2020-reg-12?active-tab=watch', 'https://www.nfl.com/games/saints-at-broncos-2020-reg-12?active-tab=watch', 'https://www.nfl.com/games/49ers-at-rams-2020-reg-12?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-buccaneers-2020-reg-12?active-tab=watch', 'https://www.nfl.com/games/bears-at-packers-2020-reg-12?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-eagles-2020-reg-12?active-tab=watch', 'https://www.nfl.com/games/ravens-at-steelers-2020-reg-12?active-tab=watch'], 'reg13': ['https://www.nfl.com/games/saints-at-falcons-2020-reg-13?active-tab=watch', 'https://www.nfl.com/games/lions-at-bears-2020-reg-13?active-tab=watch', 'https://www.nfl.com/games/colts-at-texans-2020-reg-13?active-tab=watch', 'https://www.nfl.com/games/bengals-at-dolphins-2020-reg-13?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-vikings-2020-reg-13?active-tab=watch', 'https://www.nfl.com/games/raiders-at-jets-2020-reg-13?active-tab=watch', 'https://www.nfl.com/games/browns-at-titans-2020-reg-13?active-tab=watch', 'https://www.nfl.com/games/rams-at-cardinals-2020-reg-13?active-tab=watch', 'https://www.nfl.com/games/giants-at-seahawks-2020-reg-13?active-tab=watch', 'https://www.nfl.com/games/eagles-at-packers-2020-reg-13?active-tab=watch', 'https://www.nfl.com/games/patriots-at-chargers-2020-reg-13?active-tab=watch', 'https://www.nfl.com/games/broncos-at-chiefs-2020-reg-13?active-tab=watch', 'https://www.nfl.com/games/football-team-at-steelers-2020-reg-13?active-tab=watch', 'https://www.nfl.com/games/bills-at-49ers-2020-reg-13?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-ravens-2020-reg-13?active-tab=watch'], 'reg14': ['https://www.nfl.com/games/patriots-at-rams-2020-reg-14?active-tab=watch', 'https://www.nfl.com/games/broncos-at-panthers-2020-reg-14?active-tab=watch', 'https://www.nfl.com/games/texans-at-bears-2020-reg-14?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-bengals-2020-reg-14?active-tab=watch', 'https://www.nfl.com/games/titans-at-jaguars-2020-reg-14?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-dolphins-2020-reg-14?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-giants-2020-reg-14?active-tab=watch', 'https://www.nfl.com/games/vikings-at-buccaneers-2020-reg-14?active-tab=watch', 'https://www.nfl.com/games/colts-at-raiders-2020-reg-14?active-tab=watch', 'https://www.nfl.com/games/jets-at-seahawks-2020-reg-14?active-tab=watch', 'https://www.nfl.com/games/packers-at-lions-2020-reg-14?active-tab=watch', 'https://www.nfl.com/games/falcons-at-chargers-2020-reg-14?active-tab=watch', 'https://www.nfl.com/games/saints-at-eagles-2020-reg-14?active-tab=watch', 'https://www.nfl.com/games/football-team-at-49ers-2020-reg-14?active-tab=watch', 'https://www.nfl.com/games/steelers-at-bills-2020-reg-14?active-tab=watch', 'https://www.nfl.com/games/ravens-at-browns-2020-reg-14?active-tab=watch'], 'reg15': ['https://www.nfl.com/games/chargers-at-raiders-2020-reg-15?active-tab=watch', 'https://www.nfl.com/games/bills-at-broncos-2020-reg-15?active-tab=watch', 'https://www.nfl.com/games/panthers-at-packers-2020-reg-15?active-tab=watch', 'https://www.nfl.com/games/texans-at-colts-2020-reg-15?active-tab=watch', 'https://www.nfl.com/games/lions-at-titans-2020-reg-15?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-falcons-2020-reg-15?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-ravens-2020-reg-15?active-tab=watch', 'https://www.nfl.com/games/patriots-at-dolphins-2020-reg-15?active-tab=watch', 'https://www.nfl.com/games/bears-at-vikings-2020-reg-15?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-football-team-2020-reg-15?active-tab=watch', 'https://www.nfl.com/games/49ers-at-cowboys-2020-reg-15?active-tab=watch', 'https://www.nfl.com/games/jets-at-rams-2020-reg-15?active-tab=watch', 'https://www.nfl.com/games/eagles-at-cardinals-2020-reg-15?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-saints-2020-reg-15?active-tab=watch', 'https://www.nfl.com/games/browns-at-giants-2020-reg-15?active-tab=watch', 'https://www.nfl.com/games/steelers-at-bengals-2020-reg-15?active-tab=watch'], 'reg16': ['https://www.nfl.com/games/vikings-at-saints-2020-reg-16?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-lions-2020-reg-16?active-tab=watch', 'https://www.nfl.com/games/49ers-at-cardinals-2020-reg-16?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-raiders-2020-reg-16?active-tab=watch', 'https://www.nfl.com/games/browns-at-jets-2020-reg-16?active-tab=watch', 'https://www.nfl.com/games/giants-at-ravens-2020-reg-16?active-tab=watch', 'https://www.nfl.com/games/bengals-at-texans-2020-reg-16?active-tab=watch', 'https://www.nfl.com/games/bears-at-jaguars-2020-reg-16?active-tab=watch', 'https://www.nfl.com/games/falcons-at-chiefs-2020-reg-16?active-tab=watch', 'https://www.nfl.com/games/colts-at-steelers-2020-reg-16?active-tab=watch', 'https://www.nfl.com/games/broncos-at-chargers-2020-reg-16?active-tab=watch', 'https://www.nfl.com/games/panthers-at-football-team-2020-reg-16?active-tab=watch', 'https://www.nfl.com/games/rams-at-seahawks-2020-reg-16?active-tab=watch', 'https://www.nfl.com/games/eagles-at-cowboys-2020-reg-16?active-tab=watch', 'https://www.nfl.com/games/titans-at-packers-2020-reg-16?active-tab=watch', 'https://www.nfl.com/games/bills-at-patriots-2020-reg-16?active-tab=watch'], 'reg17': ['https://www.nfl.com/games/dolphins-at-bills-2020-reg-17?active-tab=watch', 'https://www.nfl.com/games/ravens-at-bengals-2020-reg-17?active-tab=watch', 'https://www.nfl.com/games/steelers-at-browns-2020-reg-17?active-tab=watch', 'https://www.nfl.com/games/vikings-at-lions-2020-reg-17?active-tab=watch', 'https://www.nfl.com/games/jets-at-patriots-2020-reg-17?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-giants-2020-reg-17?active-tab=watch', 'https://www.nfl.com/games/falcons-at-buccaneers-2020-reg-17?active-tab=watch', 'https://www.nfl.com/games/saints-at-panthers-2020-reg-17?active-tab=watch', 'https://www.nfl.com/games/packers-at-bears-2020-reg-17?active-tab=watch', 'https://www.nfl.com/games/chargers-at-chiefs-2020-reg-17?active-tab=watch', 'https://www.nfl.com/games/raiders-at-broncos-2020-reg-17?active-tab=watch', 'https://www.nfl.com/games/titans-at-texans-2020-reg-17?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-colts-2020-reg-17?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-rams-2020-reg-17?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-49ers-2020-reg-17?active-tab=watch', 'https://www.nfl.com/games/football-team-at-eagles-2020-reg-17?active-tab=watch']}, '2021': {'reg1': ['https://www.nfl.com/games/cowboys-at-buccaneers-2021-reg-1?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-texans-2021-reg-1?active-tab=watch', 'https://www.nfl.com/games/chargers-at-football-team-2021-reg-1?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-colts-2021-reg-1?active-tab=watch', 'https://www.nfl.com/games/jets-at-panthers-2021-reg-1?active-tab=watch', 'https://www.nfl.com/games/vikings-at-bengals-2021-reg-1?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-titans-2021-reg-1?active-tab=watch', 'https://www.nfl.com/games/49ers-at-lions-2021-reg-1?active-tab=watch', 'https://www.nfl.com/games/steelers-at-bills-2021-reg-1?active-tab=watch', 'https://www.nfl.com/games/eagles-at-falcons-2021-reg-1?active-tab=watch', 'https://www.nfl.com/games/browns-at-chiefs-2021-reg-1?active-tab=watch', 'https://www.nfl.com/games/packers-at-saints-2021-reg-1?active-tab=watch', 'https://www.nfl.com/games/broncos-at-giants-2021-reg-1?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-patriots-2021-reg-1?active-tab=watch', 'https://www.nfl.com/games/bears-at-rams-2021-reg-1?active-tab=watch', 'https://www.nfl.com/games/ravens-at-raiders-2021-reg-1?active-tab=watch'], 'reg2': ['https://www.nfl.com/games/giants-at-football-team-2021-reg-2?active-tab=watch', 'https://www.nfl.com/games/patriots-at-jets-2021-reg-2?active-tab=watch', 'https://www.nfl.com/games/broncos-at-jaguars-2021-reg-2?active-tab=watch', 'https://www.nfl.com/games/bills-at-dolphins-2021-reg-2?active-tab=watch', 'https://www.nfl.com/games/49ers-at-eagles-2021-reg-2?active-tab=watch', 'https://www.nfl.com/games/rams-at-colts-2021-reg-2?active-tab=watch', 'https://www.nfl.com/games/raiders-at-steelers-2021-reg-2?active-tab=watch', 'https://www.nfl.com/games/bengals-at-bears-2021-reg-2?active-tab=watch', 'https://www.nfl.com/games/texans-at-browns-2021-reg-2?active-tab=watch', 'https://www.nfl.com/games/saints-at-panthers-2021-reg-2?active-tab=watch', 'https://www.nfl.com/games/vikings-at-cardinals-2021-reg-2?active-tab=watch', 'https://www.nfl.com/games/falcons-at-buccaneers-2021-reg-2?active-tab=watch', 'https://www.nfl.com/games/titans-at-seahawks-2021-reg-2?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-chargers-2021-reg-2?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-ravens-2021-reg-2?active-tab=watch', 'https://www.nfl.com/games/lions-at-packers-2021-reg-2?active-tab=watch'], 'reg3': ['https://www.nfl.com/games/panthers-at-texans-2021-reg-3?active-tab=watch', 'https://www.nfl.com/games/colts-at-titans-2021-reg-3?active-tab=watch', 'https://www.nfl.com/games/falcons-at-giants-2021-reg-3?active-tab=watch', 'https://www.nfl.com/games/chargers-at-chiefs-2021-reg-3?active-tab=watch', 'https://www.nfl.com/games/bengals-at-steelers-2021-reg-3?active-tab=watch', 'https://www.nfl.com/games/bears-at-browns-2021-reg-3?active-tab=watch', 'https://www.nfl.com/games/ravens-at-lions-2021-reg-3?active-tab=watch', 'https://www.nfl.com/games/saints-at-patriots-2021-reg-3?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-jaguars-2021-reg-3?active-tab=watch', 'https://www.nfl.com/games/football-team-at-bills-2021-reg-3?active-tab=watch', 'https://www.nfl.com/games/jets-at-broncos-2021-reg-3?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-raiders-2021-reg-3?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-vikings-2021-reg-3?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-rams-2021-reg-3?active-tab=watch', 'https://www.nfl.com/games/packers-at-49ers-2021-reg-3?active-tab=watch', 'https://www.nfl.com/games/eagles-at-cowboys-2021-reg-3?active-tab=watch'], 'reg4': ['https://www.nfl.com/games/jaguars-at-bengals-2021-reg-4?active-tab=watch', 'https://www.nfl.com/games/titans-at-jets-2021-reg-4?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-eagles-2021-reg-4?active-tab=watch', 'https://www.nfl.com/games/panthers-at-cowboys-2021-reg-4?active-tab=watch', 'https://www.nfl.com/games/giants-at-saints-2021-reg-4?active-tab=watch', 'https://www.nfl.com/games/browns-at-vikings-2021-reg-4?active-tab=watch', 'https://www.nfl.com/games/lions-at-bears-2021-reg-4?active-tab=watch', 'https://www.nfl.com/games/texans-at-bills-2021-reg-4?active-tab=watch', 'https://www.nfl.com/games/colts-at-dolphins-2021-reg-4?active-tab=watch', 'https://www.nfl.com/games/football-team-at-falcons-2021-reg-4?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-49ers-2021-reg-4?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-rams-2021-reg-4?active-tab=watch', 'https://www.nfl.com/games/steelers-at-packers-2021-reg-4?active-tab=watch', 'https://www.nfl.com/games/ravens-at-broncos-2021-reg-4?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-patriots-2021-reg-4?active-tab=watch', 'https://www.nfl.com/games/raiders-at-chargers-2021-reg-4?active-tab=watch'], 'reg5': ['https://www.nfl.com/games/rams-at-seahawks-2021-reg-5?active-tab=watch', 'https://www.nfl.com/games/jets-at-falcons-2021-reg-5?active-tab=watch', 'https://www.nfl.com/games/lions-at-vikings-2021-reg-5?active-tab=watch', 'https://www.nfl.com/games/saints-at-football-team-2021-reg-5?active-tab=watch', 'https://www.nfl.com/games/patriots-at-texans-2021-reg-5?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-buccaneers-2021-reg-5?active-tab=watch', 'https://www.nfl.com/games/packers-at-bengals-2021-reg-5?active-tab=watch', 'https://www.nfl.com/games/broncos-at-steelers-2021-reg-5?active-tab=watch', 'https://www.nfl.com/games/eagles-at-panthers-2021-reg-5?active-tab=watch', 'https://www.nfl.com/games/titans-at-jaguars-2021-reg-5?active-tab=watch', 'https://www.nfl.com/games/browns-at-chargers-2021-reg-5?active-tab=watch', 'https://www.nfl.com/games/bears-at-raiders-2021-reg-5?active-tab=watch', 'https://www.nfl.com/games/49ers-at-cardinals-2021-reg-5?active-tab=watch', 'https://www.nfl.com/games/giants-at-cowboys-2021-reg-5?active-tab=watch', 'https://www.nfl.com/games/bills-at-chiefs-2021-reg-5?active-tab=watch', 'https://www.nfl.com/games/colts-at-ravens-2021-reg-5?active-tab=watch'], 'reg6': ['https://www.nfl.com/games/buccaneers-at-eagles-2021-reg-6?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-jaguars-2021-reg-6?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-football-team-2021-reg-6?active-tab=watch', 'https://www.nfl.com/games/rams-at-giants-2021-reg-6?active-tab=watch', 'https://www.nfl.com/games/texans-at-colts-2021-reg-6?active-tab=watch', 'https://www.nfl.com/games/bengals-at-lions-2021-reg-6?active-tab=watch', 'https://www.nfl.com/games/packers-at-bears-2021-reg-6?active-tab=watch', 'https://www.nfl.com/games/chargers-at-ravens-2021-reg-6?active-tab=watch', 'https://www.nfl.com/games/vikings-at-panthers-2021-reg-6?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-browns-2021-reg-6?active-tab=watch', 'https://www.nfl.com/games/raiders-at-broncos-2021-reg-6?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-patriots-2021-reg-6?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-steelers-2021-reg-6?active-tab=watch', 'https://www.nfl.com/games/bills-at-titans-2021-reg-6?active-tab=watch'], 'reg7': ['https://www.nfl.com/games/broncos-at-browns-2021-reg-7?active-tab=watch', 'https://www.nfl.com/games/panthers-at-giants-2021-reg-7?active-tab=watch', 'https://www.nfl.com/games/jets-at-patriots-2021-reg-7?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-titans-2021-reg-7?active-tab=watch', 'https://www.nfl.com/games/football-team-at-packers-2021-reg-7?active-tab=watch', 'https://www.nfl.com/games/falcons-at-dolphins-2021-reg-7?active-tab=watch', 'https://www.nfl.com/games/bengals-at-ravens-2021-reg-7?active-tab=watch', 'https://www.nfl.com/games/lions-at-rams-2021-reg-7?active-tab=watch', 'https://www.nfl.com/games/eagles-at-raiders-2021-reg-7?active-tab=watch', 'https://www.nfl.com/games/texans-at-cardinals-2021-reg-7?active-tab=watch', 'https://www.nfl.com/games/bears-at-buccaneers-2021-reg-7?active-tab=watch', 'https://www.nfl.com/games/colts-at-49ers-2021-reg-7?active-tab=watch', 'https://www.nfl.com/games/saints-at-seahawks-2021-reg-7?active-tab=watch'], 'reg8': ['https://www.nfl.com/games/packers-at-cardinals-2021-reg-8?active-tab=watch', 'https://www.nfl.com/games/bengals-at-jets-2021-reg-8?active-tab=watch', 'https://www.nfl.com/games/titans-at-colts-2021-reg-8?active-tab=watch', 'https://www.nfl.com/games/rams-at-texans-2021-reg-8?active-tab=watch', 'https://www.nfl.com/games/steelers-at-browns-2021-reg-8?active-tab=watch', 'https://www.nfl.com/games/eagles-at-lions-2021-reg-8?active-tab=watch', 'https://www.nfl.com/games/49ers-at-bears-2021-reg-8?active-tab=watch', 'https://www.nfl.com/games/panthers-at-falcons-2021-reg-8?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-bills-2021-reg-8?active-tab=watch', 'https://www.nfl.com/games/patriots-at-chargers-2021-reg-8?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-seahawks-2021-reg-8?active-tab=watch', 'https://www.nfl.com/games/football-team-at-broncos-2021-reg-8?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-saints-2021-reg-8?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-vikings-2021-reg-8?active-tab=watch', 'https://www.nfl.com/games/giants-at-chiefs-2021-reg-8?active-tab=watch'], 'reg9': ['https://www.nfl.com/games/jets-at-colts-2021-reg-9?active-tab=watch', 'https://www.nfl.com/games/falcons-at-saints-2021-reg-9?active-tab=watch', 'https://www.nfl.com/games/broncos-at-cowboys-2021-reg-9?active-tab=watch', 'https://www.nfl.com/games/patriots-at-panthers-2021-reg-9?active-tab=watch', 'https://www.nfl.com/games/vikings-at-ravens-2021-reg-9?active-tab=watch', 'https://www.nfl.com/games/browns-at-bengals-2021-reg-9?active-tab=watch', 'https://www.nfl.com/games/bills-at-jaguars-2021-reg-9?active-tab=watch', 'https://www.nfl.com/games/texans-at-dolphins-2021-reg-9?active-tab=watch', 'https://www.nfl.com/games/raiders-at-giants-2021-reg-9?active-tab=watch', 'https://www.nfl.com/games/chargers-at-eagles-2021-reg-9?active-tab=watch', 'https://www.nfl.com/games/packers-at-chiefs-2021-reg-9?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-49ers-2021-reg-9?active-tab=watch', 'https://www.nfl.com/games/titans-at-rams-2021-reg-9?active-tab=watch', 'https://www.nfl.com/games/bears-at-steelers-2021-reg-9?active-tab=watch'], 'reg10': ['https://www.nfl.com/games/ravens-at-dolphins-2021-reg-10?active-tab=watch', 'https://www.nfl.com/games/bills-at-jets-2021-reg-10?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-football-team-2021-reg-10?active-tab=watch', 'https://www.nfl.com/games/falcons-at-cowboys-2021-reg-10?active-tab=watch', 'https://www.nfl.com/games/saints-at-titans-2021-reg-10?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-colts-2021-reg-10?active-tab=watch', 'https://www.nfl.com/games/lions-at-steelers-2021-reg-10?active-tab=watch', 'https://www.nfl.com/games/browns-at-patriots-2021-reg-10?active-tab=watch', 'https://www.nfl.com/games/vikings-at-chargers-2021-reg-10?active-tab=watch', 'https://www.nfl.com/games/panthers-at-cardinals-2021-reg-10?active-tab=watch', 'https://www.nfl.com/games/eagles-at-broncos-2021-reg-10?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-packers-2021-reg-10?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-raiders-2021-reg-10?active-tab=watch', 'https://www.nfl.com/games/rams-at-49ers-2021-reg-10?active-tab=watch'], 'reg11': ['https://www.nfl.com/games/patriots-at-falcons-2021-reg-11?active-tab=watch', 'https://www.nfl.com/games/saints-at-eagles-2021-reg-11?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-jets-2021-reg-11?active-tab=watch', 'https://www.nfl.com/games/football-team-at-panthers-2021-reg-11?active-tab=watch', 'https://www.nfl.com/games/colts-at-bills-2021-reg-11?active-tab=watch', 'https://www.nfl.com/games/lions-at-browns-2021-reg-11?active-tab=watch', 'https://www.nfl.com/games/49ers-at-jaguars-2021-reg-11?active-tab=watch', 'https://www.nfl.com/games/texans-at-titans-2021-reg-11?active-tab=watch', 'https://www.nfl.com/games/packers-at-vikings-2021-reg-11?active-tab=watch', 'https://www.nfl.com/games/ravens-at-bears-2021-reg-11?active-tab=watch', 'https://www.nfl.com/games/bengals-at-raiders-2021-reg-11?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-seahawks-2021-reg-11?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-chiefs-2021-reg-11?active-tab=watch', 'https://www.nfl.com/games/steelers-at-chargers-2021-reg-11?active-tab=watch', 'https://www.nfl.com/games/giants-at-buccaneers-2021-reg-11?active-tab=watch'], 'reg12': ['https://www.nfl.com/games/bears-at-lions-2021-reg-12?active-tab=watch', 'https://www.nfl.com/games/raiders-at-cowboys-2021-reg-12?active-tab=watch', 'https://www.nfl.com/games/bills-at-saints-2021-reg-12?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-colts-2021-reg-12?active-tab=watch', 'https://www.nfl.com/games/jets-at-texans-2021-reg-12?active-tab=watch', 'https://www.nfl.com/games/eagles-at-giants-2021-reg-12?active-tab=watch', 'https://www.nfl.com/games/panthers-at-dolphins-2021-reg-12?active-tab=watch', 'https://www.nfl.com/games/titans-at-patriots-2021-reg-12?active-tab=watch', 'https://www.nfl.com/games/steelers-at-bengals-2021-reg-12?active-tab=watch', 'https://www.nfl.com/games/falcons-at-jaguars-2021-reg-12?active-tab=watch', 'https://www.nfl.com/games/chargers-at-broncos-2021-reg-12?active-tab=watch', 'https://www.nfl.com/games/rams-at-packers-2021-reg-12?active-tab=watch', 'https://www.nfl.com/games/vikings-at-49ers-2021-reg-12?active-tab=watch', 'https://www.nfl.com/games/browns-at-ravens-2021-reg-12?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-football-team-2021-reg-12?active-tab=watch'], 'reg13': ['https://www.nfl.com/games/cowboys-at-saints-2021-reg-13?active-tab=watch', 'https://www.nfl.com/games/giants-at-dolphins-2021-reg-13?active-tab=watch', 'https://www.nfl.com/games/colts-at-texans-2021-reg-13?active-tab=watch', 'https://www.nfl.com/games/vikings-at-lions-2021-reg-13?active-tab=watch', 'https://www.nfl.com/games/eagles-at-jets-2021-reg-13?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-bears-2021-reg-13?active-tab=watch', 'https://www.nfl.com/games/chargers-at-bengals-2021-reg-13?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-falcons-2021-reg-13?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-rams-2021-reg-13?active-tab=watch', 'https://www.nfl.com/games/football-team-at-raiders-2021-reg-13?active-tab=watch', 'https://www.nfl.com/games/ravens-at-steelers-2021-reg-13?active-tab=watch', 'https://www.nfl.com/games/49ers-at-seahawks-2021-reg-13?active-tab=watch', 'https://www.nfl.com/games/broncos-at-chiefs-2021-reg-13?active-tab=watch', 'https://www.nfl.com/games/patriots-at-bills-2021-reg-13?active-tab=watch'], 'reg14': ['https://www.nfl.com/games/steelers-at-vikings-2021-reg-14?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-football-team-2021-reg-14?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-titans-2021-reg-14?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-texans-2021-reg-14?active-tab=watch', 'https://www.nfl.com/games/raiders-at-chiefs-2021-reg-14?active-tab=watch', 'https://www.nfl.com/games/saints-at-jets-2021-reg-14?active-tab=watch', 'https://www.nfl.com/games/falcons-at-panthers-2021-reg-14?active-tab=watch', 'https://www.nfl.com/games/ravens-at-browns-2021-reg-14?active-tab=watch', 'https://www.nfl.com/games/giants-at-chargers-2021-reg-14?active-tab=watch', 'https://www.nfl.com/games/lions-at-broncos-2021-reg-14?active-tab=watch', 'https://www.nfl.com/games/49ers-at-bengals-2021-reg-14?active-tab=watch', 'https://www.nfl.com/games/bills-at-buccaneers-2021-reg-14?active-tab=watch', 'https://www.nfl.com/games/bears-at-packers-2021-reg-14?active-tab=watch', 'https://www.nfl.com/games/rams-at-cardinals-2021-reg-14?active-tab=watch'], 'reg15': ['https://www.nfl.com/games/chiefs-at-chargers-2021-reg-15?active-tab=watch', 'https://www.nfl.com/games/patriots-at-colts-2021-reg-15?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-giants-2021-reg-15?active-tab=watch', 'https://www.nfl.com/games/texans-at-jaguars-2021-reg-15?active-tab=watch', 'https://www.nfl.com/games/titans-at-steelers-2021-reg-15?active-tab=watch', 'https://www.nfl.com/games/jets-at-dolphins-2021-reg-15?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-lions-2021-reg-15?active-tab=watch', 'https://www.nfl.com/games/panthers-at-bills-2021-reg-15?active-tab=watch', 'https://www.nfl.com/games/bengals-at-broncos-2021-reg-15?active-tab=watch', 'https://www.nfl.com/games/falcons-at-49ers-2021-reg-15?active-tab=watch', 'https://www.nfl.com/games/packers-at-ravens-2021-reg-15?active-tab=watch', 'https://www.nfl.com/games/saints-at-buccaneers-2021-reg-15?active-tab=watch', 'https://www.nfl.com/games/raiders-at-browns-2021-reg-15?active-tab=watch', 'https://www.nfl.com/games/vikings-at-bears-2021-reg-15?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-rams-2021-reg-15?active-tab=watch', 'https://www.nfl.com/games/football-team-at-eagles-2021-reg-15?active-tab=watch'], 'reg16': ['https://www.nfl.com/games/49ers-at-titans-2021-reg-16?active-tab=watch', 'https://www.nfl.com/games/browns-at-packers-2021-reg-16?active-tab=watch', 'https://www.nfl.com/games/colts-at-cardinals-2021-reg-16?active-tab=watch', 'https://www.nfl.com/games/giants-at-eagles-2021-reg-16?active-tab=watch', 'https://www.nfl.com/games/rams-at-vikings-2021-reg-16?active-tab=watch', 'https://www.nfl.com/games/bills-at-patriots-2021-reg-16?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-panthers-2021-reg-16?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-jets-2021-reg-16?active-tab=watch', 'https://www.nfl.com/games/lions-at-falcons-2021-reg-16?active-tab=watch', 'https://www.nfl.com/games/chargers-at-texans-2021-reg-16?active-tab=watch', 'https://www.nfl.com/games/ravens-at-bengals-2021-reg-16?active-tab=watch', 'https://www.nfl.com/games/bears-at-seahawks-2021-reg-16?active-tab=watch', 'https://www.nfl.com/games/steelers-at-chiefs-2021-reg-16?active-tab=watch', 'https://www.nfl.com/games/broncos-at-raiders-2021-reg-16?active-tab=watch', 'https://www.nfl.com/games/football-team-at-cowboys-2021-reg-16?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-saints-2021-reg-16?active-tab=watch'], 'reg17': ['https://www.nfl.com/games/eagles-at-football-team-2021-reg-17?active-tab=watch', 'https://www.nfl.com/games/rams-at-ravens-2021-reg-17?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-jets-2021-reg-17?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-titans-2021-reg-17?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-patriots-2021-reg-17?active-tab=watch', 'https://www.nfl.com/games/raiders-at-colts-2021-reg-17?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-bengals-2021-reg-17?active-tab=watch', 'https://www.nfl.com/games/giants-at-bears-2021-reg-17?active-tab=watch', 'https://www.nfl.com/games/falcons-at-bills-2021-reg-17?active-tab=watch', 'https://www.nfl.com/games/texans-at-49ers-2021-reg-17?active-tab=watch', 'https://www.nfl.com/games/broncos-at-chargers-2021-reg-17?active-tab=watch', 'https://www.nfl.com/games/panthers-at-saints-2021-reg-17?active-tab=watch', 'https://www.nfl.com/games/lions-at-seahawks-2021-reg-17?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-cowboys-2021-reg-17?active-tab=watch', 'https://www.nfl.com/games/vikings-at-packers-2021-reg-17?active-tab=watch', 'https://www.nfl.com/games/browns-at-steelers-2021-reg-17?active-tab=watch'], 'reg18': ['https://www.nfl.com/games/chiefs-at-broncos-2021-reg-18?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-eagles-2021-reg-18?active-tab=watch', 'https://www.nfl.com/games/packers-at-lions-2021-reg-18?active-tab=watch', 'https://www.nfl.com/games/colts-at-jaguars-2021-reg-18?active-tab=watch', 'https://www.nfl.com/games/football-team-at-giants-2021-reg-18?active-tab=watch', 'https://www.nfl.com/games/bears-at-vikings-2021-reg-18?active-tab=watch', 'https://www.nfl.com/games/titans-at-texans-2021-reg-18?active-tab=watch', 'https://www.nfl.com/games/steelers-at-ravens-2021-reg-18?active-tab=watch', 'https://www.nfl.com/games/bengals-at-browns-2021-reg-18?active-tab=watch', 'https://www.nfl.com/games/49ers-at-rams-2021-reg-18?active-tab=watch', 'https://www.nfl.com/games/panthers-at-buccaneers-2021-reg-18?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-cardinals-2021-reg-18?active-tab=watch', 'https://www.nfl.com/games/patriots-at-dolphins-2021-reg-18?active-tab=watch', 'https://www.nfl.com/games/saints-at-falcons-2021-reg-18?active-tab=watch', 'https://www.nfl.com/games/jets-at-bills-2021-reg-18?active-tab=watch', 'https://www.nfl.com/games/chargers-at-raiders-2021-reg-18?active-tab=watch']}, '2022': {'reg1': ['https://www.nfl.com/games/bills-at-rams-2022-reg-1?active-tab=watch', 'https://www.nfl.com/games/saints-at-falcons-2022-reg-1?active-tab=watch', 'https://www.nfl.com/games/browns-at-panthers-2022-reg-1?active-tab=watch', 'https://www.nfl.com/games/49ers-at-bears-2022-reg-1?active-tab=watch', 'https://www.nfl.com/games/steelers-at-bengals-2022-reg-1?active-tab=watch', 'https://www.nfl.com/games/eagles-at-lions-2022-reg-1?active-tab=watch', 'https://www.nfl.com/games/colts-at-texans-2022-reg-1?active-tab=watch', 'https://www.nfl.com/games/patriots-at-dolphins-2022-reg-1?active-tab=watch', 'https://www.nfl.com/games/ravens-at-jets-2022-reg-1?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-commanders-2022-reg-1?active-tab=watch', 'https://www.nfl.com/games/giants-at-titans-2022-reg-1?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-cardinals-2022-reg-1?active-tab=watch', 'https://www.nfl.com/games/raiders-at-chargers-2022-reg-1?active-tab=watch', 'https://www.nfl.com/games/packers-at-vikings-2022-reg-1?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-cowboys-2022-reg-1?active-tab=watch', 'https://www.nfl.com/games/broncos-at-seahawks-2022-reg-1?active-tab=watch'], 'reg2': ['https://www.nfl.com/games/chargers-at-chiefs-2022-reg-2?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-ravens-2022-reg-2?active-tab=watch', 'https://www.nfl.com/games/jets-at-browns-2022-reg-2?active-tab=watch', 'https://www.nfl.com/games/commanders-at-lions-2022-reg-2?active-tab=watch', 'https://www.nfl.com/games/colts-at-jaguars-2022-reg-2?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-saints-2022-reg-2?active-tab=watch', 'https://www.nfl.com/games/panthers-at-giants-2022-reg-2?active-tab=watch', 'https://www.nfl.com/games/patriots-at-steelers-2022-reg-2?active-tab=watch', 'https://www.nfl.com/games/falcons-at-rams-2022-reg-2?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-49ers-2022-reg-2?active-tab=watch', 'https://www.nfl.com/games/bengals-at-cowboys-2022-reg-2?active-tab=watch', 'https://www.nfl.com/games/texans-at-broncos-2022-reg-2?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-raiders-2022-reg-2?active-tab=watch', 'https://www.nfl.com/games/bears-at-packers-2022-reg-2?active-tab=watch', 'https://www.nfl.com/games/titans-at-bills-2022-reg-2?active-tab=watch', 'https://www.nfl.com/games/vikings-at-eagles-2022-reg-2?active-tab=watch'], 'reg3': ['https://www.nfl.com/games/steelers-at-browns-2022-reg-3?active-tab=watch', 'https://www.nfl.com/games/saints-at-panthers-2022-reg-3?active-tab=watch', 'https://www.nfl.com/games/texans-at-bears-2022-reg-3?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-colts-2022-reg-3?active-tab=watch', 'https://www.nfl.com/games/bills-at-dolphins-2022-reg-3?active-tab=watch', 'https://www.nfl.com/games/lions-at-vikings-2022-reg-3?active-tab=watch', 'https://www.nfl.com/games/ravens-at-patriots-2022-reg-3?active-tab=watch', 'https://www.nfl.com/games/bengals-at-jets-2022-reg-3?active-tab=watch', 'https://www.nfl.com/games/raiders-at-titans-2022-reg-3?active-tab=watch', 'https://www.nfl.com/games/eagles-at-commanders-2022-reg-3?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-chargers-2022-reg-3?active-tab=watch', 'https://www.nfl.com/games/rams-at-cardinals-2022-reg-3?active-tab=watch', 'https://www.nfl.com/games/falcons-at-seahawks-2022-reg-3?active-tab=watch', 'https://www.nfl.com/games/packers-at-buccaneers-2022-reg-3?active-tab=watch', 'https://www.nfl.com/games/49ers-at-broncos-2022-reg-3?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-giants-2022-reg-3?active-tab=watch'], 'reg4': ['https://www.nfl.com/games/dolphins-at-bengals-2022-reg-4?active-tab=watch', 'https://www.nfl.com/games/vikings-at-saints-2022-reg-4?active-tab=watch', 'https://www.nfl.com/games/browns-at-falcons-2022-reg-4?active-tab=watch', 'https://www.nfl.com/games/bills-at-ravens-2022-reg-4?active-tab=watch', 'https://www.nfl.com/games/commanders-at-cowboys-2022-reg-4?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-lions-2022-reg-4?active-tab=watch', 'https://www.nfl.com/games/chargers-at-texans-2022-reg-4?active-tab=watch', 'https://www.nfl.com/games/titans-at-colts-2022-reg-4?active-tab=watch', 'https://www.nfl.com/games/bears-at-giants-2022-reg-4?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-eagles-2022-reg-4?active-tab=watch', 'https://www.nfl.com/games/jets-at-steelers-2022-reg-4?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-panthers-2022-reg-4?active-tab=watch', 'https://www.nfl.com/games/patriots-at-packers-2022-reg-4?active-tab=watch', 'https://www.nfl.com/games/broncos-at-raiders-2022-reg-4?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-buccaneers-2022-reg-4?active-tab=watch', 'https://www.nfl.com/games/rams-at-49ers-2022-reg-4?active-tab=watch'], 'reg5': ['https://www.nfl.com/games/colts-at-broncos-2022-reg-5?active-tab=watch', 'https://www.nfl.com/games/giants-at-packers-2022-reg-5?active-tab=watch', 'https://www.nfl.com/games/steelers-at-bills-2022-reg-5?active-tab=watch', 'https://www.nfl.com/games/chargers-at-browns-2022-reg-5?active-tab=watch', 'https://www.nfl.com/games/texans-at-jaguars-2022-reg-5?active-tab=watch', 'https://www.nfl.com/games/bears-at-vikings-2022-reg-5?active-tab=watch', 'https://www.nfl.com/games/lions-at-patriots-2022-reg-5?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-saints-2022-reg-5?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-jets-2022-reg-5?active-tab=watch', 'https://www.nfl.com/games/falcons-at-buccaneers-2022-reg-5?active-tab=watch', 'https://www.nfl.com/games/titans-at-commanders-2022-reg-5?active-tab=watch', 'https://www.nfl.com/games/49ers-at-panthers-2022-reg-5?active-tab=watch', 'https://www.nfl.com/games/eagles-at-cardinals-2022-reg-5?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-rams-2022-reg-5?active-tab=watch', 'https://www.nfl.com/games/bengals-at-ravens-2022-reg-5?active-tab=watch', 'https://www.nfl.com/games/raiders-at-chiefs-2022-reg-5?active-tab=watch'], 'reg6': ['https://www.nfl.com/games/commanders-at-bears-2022-reg-6?active-tab=watch', 'https://www.nfl.com/games/49ers-at-falcons-2022-reg-6?active-tab=watch', 'https://www.nfl.com/games/patriots-at-browns-2022-reg-6?active-tab=watch', 'https://www.nfl.com/games/jets-at-packers-2022-reg-6?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-colts-2022-reg-6?active-tab=watch', 'https://www.nfl.com/games/vikings-at-dolphins-2022-reg-6?active-tab=watch', 'https://www.nfl.com/games/bengals-at-saints-2022-reg-6?active-tab=watch', 'https://www.nfl.com/games/ravens-at-giants-2022-reg-6?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-steelers-2022-reg-6?active-tab=watch', 'https://www.nfl.com/games/panthers-at-rams-2022-reg-6?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-seahawks-2022-reg-6?active-tab=watch', 'https://www.nfl.com/games/bills-at-chiefs-2022-reg-6?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-eagles-2022-reg-6?active-tab=watch', 'https://www.nfl.com/games/broncos-at-chargers-2022-reg-6?active-tab=watch'], 'reg7': ['https://www.nfl.com/games/saints-at-cardinals-2022-reg-7?active-tab=watch', 'https://www.nfl.com/games/browns-at-ravens-2022-reg-7?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-panthers-2022-reg-7?active-tab=watch', 'https://www.nfl.com/games/falcons-at-bengals-2022-reg-7?active-tab=watch', 'https://www.nfl.com/games/lions-at-cowboys-2022-reg-7?active-tab=watch', 'https://www.nfl.com/games/giants-at-jaguars-2022-reg-7?active-tab=watch', 'https://www.nfl.com/games/colts-at-titans-2022-reg-7?active-tab=watch', 'https://www.nfl.com/games/packers-at-commanders-2022-reg-7?active-tab=watch', 'https://www.nfl.com/games/jets-at-broncos-2022-reg-7?active-tab=watch', 'https://www.nfl.com/games/texans-at-raiders-2022-reg-7?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-chargers-2022-reg-7?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-49ers-2022-reg-7?active-tab=watch', 'https://www.nfl.com/games/steelers-at-dolphins-2022-reg-7?active-tab=watch', 'https://www.nfl.com/games/bears-at-patriots-2022-reg-7?active-tab=watch'], 'reg8': ['https://www.nfl.com/games/ravens-at-buccaneers-2022-reg-8?active-tab=watch', 'https://www.nfl.com/games/broncos-at-jaguars-2022-reg-8?active-tab=watch', 'https://www.nfl.com/games/panthers-at-falcons-2022-reg-8?active-tab=watch', 'https://www.nfl.com/games/bears-at-cowboys-2022-reg-8?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-lions-2022-reg-8?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-vikings-2022-reg-8?active-tab=watch', 'https://www.nfl.com/games/raiders-at-saints-2022-reg-8?active-tab=watch', 'https://www.nfl.com/games/patriots-at-jets-2022-reg-8?active-tab=watch', 'https://www.nfl.com/games/steelers-at-eagles-2022-reg-8?active-tab=watch', 'https://www.nfl.com/games/titans-at-texans-2022-reg-8?active-tab=watch', 'https://www.nfl.com/games/commanders-at-colts-2022-reg-8?active-tab=watch', 'https://www.nfl.com/games/49ers-at-rams-2022-reg-8?active-tab=watch', 'https://www.nfl.com/games/giants-at-seahawks-2022-reg-8?active-tab=watch', 'https://www.nfl.com/games/packers-at-bills-2022-reg-8?active-tab=watch', 'https://www.nfl.com/games/bengals-at-browns-2022-reg-8?active-tab=watch'], 'reg9': ['https://www.nfl.com/games/eagles-at-texans-2022-reg-9?active-tab=watch', 'https://www.nfl.com/games/chargers-at-falcons-2022-reg-9?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-bears-2022-reg-9?active-tab=watch', 'https://www.nfl.com/games/panthers-at-bengals-2022-reg-9?active-tab=watch', 'https://www.nfl.com/games/packers-at-lions-2022-reg-9?active-tab=watch', 'https://www.nfl.com/games/raiders-at-jaguars-2022-reg-9?active-tab=watch', 'https://www.nfl.com/games/colts-at-patriots-2022-reg-9?active-tab=watch', 'https://www.nfl.com/games/bills-at-jets-2022-reg-9?active-tab=watch', 'https://www.nfl.com/games/vikings-at-commanders-2022-reg-9?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-cardinals-2022-reg-9?active-tab=watch', 'https://www.nfl.com/games/rams-at-buccaneers-2022-reg-9?active-tab=watch', 'https://www.nfl.com/games/titans-at-chiefs-2022-reg-9?active-tab=watch', 'https://www.nfl.com/games/ravens-at-saints-2022-reg-9?active-tab=watch'], 'reg10': ['https://www.nfl.com/games/falcons-at-panthers-2022-reg-10?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-buccaneers-2022-reg-10?active-tab=watch', 'https://www.nfl.com/games/vikings-at-bills-2022-reg-10?active-tab=watch', 'https://www.nfl.com/games/lions-at-bears-2022-reg-10?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-chiefs-2022-reg-10?active-tab=watch', 'https://www.nfl.com/games/browns-at-dolphins-2022-reg-10?active-tab=watch', 'https://www.nfl.com/games/texans-at-giants-2022-reg-10?active-tab=watch', 'https://www.nfl.com/games/saints-at-steelers-2022-reg-10?active-tab=watch', 'https://www.nfl.com/games/broncos-at-titans-2022-reg-10?active-tab=watch', 'https://www.nfl.com/games/colts-at-raiders-2022-reg-10?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-packers-2022-reg-10?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-rams-2022-reg-10?active-tab=watch', 'https://www.nfl.com/games/chargers-at-49ers-2022-reg-10?active-tab=watch', 'https://www.nfl.com/games/commanders-at-eagles-2022-reg-10?active-tab=watch'], 'reg11': ['https://www.nfl.com/games/titans-at-packers-2022-reg-11?active-tab=watch', 'https://www.nfl.com/games/bears-at-falcons-2022-reg-11?active-tab=watch', 'https://www.nfl.com/games/panthers-at-ravens-2022-reg-11?active-tab=watch', 'https://www.nfl.com/games/browns-at-bills-2022-reg-11?active-tab=watch', 'https://www.nfl.com/games/commanders-at-texans-2022-reg-11?active-tab=watch', 'https://www.nfl.com/games/eagles-at-colts-2022-reg-11?active-tab=watch', 'https://www.nfl.com/games/jets-at-patriots-2022-reg-11?active-tab=watch', 'https://www.nfl.com/games/rams-at-saints-2022-reg-11?active-tab=watch', 'https://www.nfl.com/games/lions-at-giants-2022-reg-11?active-tab=watch', 'https://www.nfl.com/games/raiders-at-broncos-2022-reg-11?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-vikings-2022-reg-11?active-tab=watch', 'https://www.nfl.com/games/bengals-at-steelers-2022-reg-11?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-chargers-2022-reg-11?active-tab=watch', 'https://www.nfl.com/games/49ers-at-cardinals-2022-reg-11?active-tab=watch'], 'reg12': ['https://www.nfl.com/games/bills-at-lions-2022-reg-12?active-tab=watch', 'https://www.nfl.com/games/giants-at-cowboys-2022-reg-12?active-tab=watch', 'https://www.nfl.com/games/patriots-at-vikings-2022-reg-12?active-tab=watch', 'https://www.nfl.com/games/broncos-at-panthers-2022-reg-12?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-browns-2022-reg-12?active-tab=watch', 'https://www.nfl.com/games/ravens-at-jaguars-2022-reg-12?active-tab=watch', 'https://www.nfl.com/games/texans-at-dolphins-2022-reg-12?active-tab=watch', 'https://www.nfl.com/games/bears-at-jets-2022-reg-12?active-tab=watch', 'https://www.nfl.com/games/bengals-at-titans-2022-reg-12?active-tab=watch', 'https://www.nfl.com/games/falcons-at-commanders-2022-reg-12?active-tab=watch', 'https://www.nfl.com/games/chargers-at-cardinals-2022-reg-12?active-tab=watch', 'https://www.nfl.com/games/raiders-at-seahawks-2022-reg-12?active-tab=watch', 'https://www.nfl.com/games/rams-at-chiefs-2022-reg-12?active-tab=watch', 'https://www.nfl.com/games/saints-at-49ers-2022-reg-12?active-tab=watch', 'https://www.nfl.com/games/packers-at-eagles-2022-reg-12?active-tab=watch', 'https://www.nfl.com/games/steelers-at-colts-2022-reg-12?active-tab=watch'], 'reg13': ['https://www.nfl.com/games/bills-at-patriots-2022-reg-13?active-tab=watch', 'https://www.nfl.com/games/steelers-at-falcons-2022-reg-13?active-tab=watch', 'https://www.nfl.com/games/broncos-at-ravens-2022-reg-13?active-tab=watch', 'https://www.nfl.com/games/packers-at-bears-2022-reg-13?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-lions-2022-reg-13?active-tab=watch', 'https://www.nfl.com/games/browns-at-texans-2022-reg-13?active-tab=watch', 'https://www.nfl.com/games/jets-at-vikings-2022-reg-13?active-tab=watch', 'https://www.nfl.com/games/commanders-at-giants-2022-reg-13?active-tab=watch', 'https://www.nfl.com/games/titans-at-eagles-2022-reg-13?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-rams-2022-reg-13?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-49ers-2022-reg-13?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-bengals-2022-reg-13?active-tab=watch', 'https://www.nfl.com/games/chargers-at-raiders-2022-reg-13?active-tab=watch', 'https://www.nfl.com/games/colts-at-cowboys-2022-reg-13?active-tab=watch', 'https://www.nfl.com/games/saints-at-buccaneers-2022-reg-13?active-tab=watch'], 'reg14': ['https://www.nfl.com/games/raiders-at-rams-2022-reg-14?active-tab=watch', 'https://www.nfl.com/games/jets-at-bills-2022-reg-14?active-tab=watch', 'https://www.nfl.com/games/browns-at-bengals-2022-reg-14?active-tab=watch', 'https://www.nfl.com/games/texans-at-cowboys-2022-reg-14?active-tab=watch', 'https://www.nfl.com/games/vikings-at-lions-2022-reg-14?active-tab=watch', 'https://www.nfl.com/games/eagles-at-giants-2022-reg-14?active-tab=watch', 'https://www.nfl.com/games/ravens-at-steelers-2022-reg-14?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-titans-2022-reg-14?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-broncos-2022-reg-14?active-tab=watch', 'https://www.nfl.com/games/panthers-at-seahawks-2022-reg-14?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-49ers-2022-reg-14?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-chargers-2022-reg-14?active-tab=watch', 'https://www.nfl.com/games/patriots-at-cardinals-2022-reg-14?active-tab=watch'], 'reg15': ['https://www.nfl.com/games/49ers-at-seahawks-2022-reg-15?active-tab=watch', 'https://www.nfl.com/games/colts-at-vikings-2022-reg-15?active-tab=watch', 'https://www.nfl.com/games/ravens-at-browns-2022-reg-15?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-bills-2022-reg-15?active-tab=watch', 'https://www.nfl.com/games/falcons-at-saints-2022-reg-15?active-tab=watch', 'https://www.nfl.com/games/steelers-at-panthers-2022-reg-15?active-tab=watch', 'https://www.nfl.com/games/eagles-at-bears-2022-reg-15?active-tab=watch', 'https://www.nfl.com/games/chiefs-at-texans-2022-reg-15?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-jaguars-2022-reg-15?active-tab=watch', 'https://www.nfl.com/games/lions-at-jets-2022-reg-15?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-broncos-2022-reg-15?active-tab=watch', 'https://www.nfl.com/games/patriots-at-raiders-2022-reg-15?active-tab=watch', 'https://www.nfl.com/games/titans-at-chargers-2022-reg-15?active-tab=watch', 'https://www.nfl.com/games/bengals-at-buccaneers-2022-reg-15?active-tab=watch', 'https://www.nfl.com/games/giants-at-commanders-2022-reg-15?active-tab=watch', 'https://www.nfl.com/games/rams-at-packers-2022-reg-15?active-tab=watch'], 'reg16': ['https://www.nfl.com/games/jaguars-at-jets-2022-reg-16?active-tab=watch', 'https://www.nfl.com/games/falcons-at-ravens-2022-reg-16?active-tab=watch', 'https://www.nfl.com/games/lions-at-panthers-2022-reg-16?active-tab=watch', 'https://www.nfl.com/games/bills-at-bears-2022-reg-16?active-tab=watch', 'https://www.nfl.com/games/saints-at-browns-2022-reg-16?active-tab=watch', 'https://www.nfl.com/games/seahawks-at-chiefs-2022-reg-16?active-tab=watch', 'https://www.nfl.com/games/giants-at-vikings-2022-reg-16?active-tab=watch', 'https://www.nfl.com/games/bengals-at-patriots-2022-reg-16?active-tab=watch', 'https://www.nfl.com/games/texans-at-titans-2022-reg-16?active-tab=watch', 'https://www.nfl.com/games/commanders-at-49ers-2022-reg-16?active-tab=watch', 'https://www.nfl.com/games/eagles-at-cowboys-2022-reg-16?active-tab=watch', 'https://www.nfl.com/games/raiders-at-steelers-2022-reg-16?active-tab=watch', 'https://www.nfl.com/games/packers-at-dolphins-2022-reg-16?active-tab=watch', 'https://www.nfl.com/games/broncos-at-rams-2022-reg-16?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-cardinals-2022-reg-16?active-tab=watch', 'https://www.nfl.com/games/chargers-at-colts-2022-reg-16?active-tab=watch'], 'reg17': ['https://www.nfl.com/games/cowboys-at-titans-2022-reg-17?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-falcons-2022-reg-17?active-tab=watch', 'https://www.nfl.com/games/bears-at-lions-2022-reg-17?active-tab=watch', 'https://www.nfl.com/games/jaguars-at-texans-2022-reg-17?active-tab=watch', 'https://www.nfl.com/games/broncos-at-chiefs-2022-reg-17?active-tab=watch', 'https://www.nfl.com/games/dolphins-at-patriots-2022-reg-17?active-tab=watch', 'https://www.nfl.com/games/colts-at-giants-2022-reg-17?active-tab=watch', 'https://www.nfl.com/games/saints-at-eagles-2022-reg-17?active-tab=watch', 'https://www.nfl.com/games/panthers-at-buccaneers-2022-reg-17?active-tab=watch', 'https://www.nfl.com/games/browns-at-commanders-2022-reg-17?active-tab=watch', 'https://www.nfl.com/games/49ers-at-raiders-2022-reg-17?active-tab=watch', 'https://www.nfl.com/games/jets-at-seahawks-2022-reg-17?active-tab=watch', 'https://www.nfl.com/games/vikings-at-packers-2022-reg-17?active-tab=watch', 'https://www.nfl.com/games/rams-at-chargers-2022-reg-17?active-tab=watch', 'https://www.nfl.com/games/steelers-at-ravens-2022-reg-17?active-tab=watch', 'https://www.nfl.com/games/bills-at-bengals-2022-reg-17?active-tab=watch'], 'reg18': ['https://www.nfl.com/games/chiefs-at-raiders-2022-reg-18?active-tab=watch', 'https://www.nfl.com/games/titans-at-jaguars-2022-reg-18?active-tab=watch', 'https://www.nfl.com/games/buccaneers-at-falcons-2022-reg-18?active-tab=watch', 'https://www.nfl.com/games/patriots-at-bills-2022-reg-18?active-tab=watch', 'https://www.nfl.com/games/vikings-at-bears-2022-reg-18?active-tab=watch', 'https://www.nfl.com/games/ravens-at-bengals-2022-reg-18?active-tab=watch', 'https://www.nfl.com/games/texans-at-colts-2022-reg-18?active-tab=watch', 'https://www.nfl.com/games/jets-at-dolphins-2022-reg-18?active-tab=watch', 'https://www.nfl.com/games/panthers-at-saints-2022-reg-18?active-tab=watch', 'https://www.nfl.com/games/browns-at-steelers-2022-reg-18?active-tab=watch', 'https://www.nfl.com/games/giants-at-eagles-2022-reg-18?active-tab=watch', 'https://www.nfl.com/games/cowboys-at-commanders-2022-reg-18?active-tab=watch', 'https://www.nfl.com/games/chargers-at-broncos-2022-reg-18?active-tab=watch', 'https://www.nfl.com/games/rams-at-seahawks-2022-reg-18?active-tab=watch', 'https://www.nfl.com/games/cardinals-at-49ers-2022-reg-18?active-tab=watch', 'https://www.nfl.com/games/lions-at-packers-2022-reg-18?active-tab=watch']}}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "d3bc01fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "#RECUPERATION DES URLS DES MATCHS\n",
    "# def get_url_match(matchs, year, week):\n",
    "#     list_url_matchs =[]\n",
    "    \n",
    "#     for match in matchs:\n",
    "#         url_nfl= \"https://www.nfl.com/games/\"\n",
    "#         end_url = \"?active-tab=watch\"\n",
    "#         #print(\"Affichage des URLS pour les différents matchs :\")\n",
    "#         url_match = url_nfl + str(match[0]) + \"-at-\"+str(match[1])+\"-\"+str(year)+\"-reg-\"+str(week) + end_url\n",
    "#         list_url_matchs.append(url_match)\n",
    "#         #print(url_match+\"\\n\")\n",
    "        \n",
    "#     return list_url_matchs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5e1df5fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "# def main_gameURL(gameTeams):\n",
    "#     gameTeamsURLs={}\n",
    "#     for key_year in gameTeams.keys() :\n",
    "#         gameTeamsURLs_year = {}\n",
    "#         for key_week in gameTeams[key_year].keys(): \n",
    "#             gameTeamsURLs_year[key_week]= get_url_match(gameTeams[key_year][key_week], int(key_year), int(key_week.split('g')[1]))\n",
    "#         gameTeamsURLs[key_year] = gameTeamsURLs_year\n",
    "        \n",
    "#     return gameTeamsURLs\n",
    "    \n",
    "# print(main_gameURL(gameTeams))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "67efa13a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#RECUPERATION DE GAMEID\n",
    "def get_gameId(url):\n",
    "    response_url = requests.get(url)\n",
    "    soup_gamePage = BeautifulSoup(response_url.text,'html.parser')\n",
    "    find_gameId = soup_gamePage.findAll('div', {'data-require':\"modules/nfl-components/game-center-page\"},{'class':\"nfl-c-page\"})\n",
    "    to_string = str(find_gameId[0])\n",
    "    # print(to_string)\n",
    "    \n",
    "    gameId = to_string.split(sep=',')[1].split(sep=':')[1].replace('\"','')\n",
    "    \n",
    "    return gameId"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "89f6830a",
   "metadata": {},
   "source": [
    "### 2. Post saison"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "82b4ff99",
   "metadata": {},
   "outputs": [],
   "source": [
    "#RECUPERATION GAMEID MATCHS POST REGULAR SEASON (SUPERBWOL, FINAL DE CONFERENCE)\n",
    "def get_gameId_postSeason(years, weeks):\n",
    "    \n",
    "    dict_gameIds = {}\n",
    "    for year in years :\n",
    "        dict_gameIds[str(year)] ={}\n",
    "        for week in weeks : \n",
    "            \n",
    "            url_api = \"https://api.nfl.com/football/v2/stats/live/game-summaries?season=\"+str(year)+\"&seasonType=POST&week=\"+str(week)\n",
    "    \n",
    "            response_postSeason = requests.get(url_api, headers = headers)\n",
    "            gameIds = json.loads(response_postSeason.text)\n",
    "            \n",
    "            list_gameIds=gameIds['data']\n",
    "            dict_gameIds[str(year)][postSeason[week]]= []\n",
    "            for game in list_gameIds : \n",
    "                dict_gameIds[str(year)][postSeason[week]].append(game['gameId'])\n",
    "    \n",
    "    return dict_gameIds"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ea82415e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# years = [2017, 2018, 2019, 2020, 2021, 2022]\n",
    "# weeks = [k for k in range(1,5)]\n",
    "\n",
    "# print(get_gameId_postSeason(years, weeks))\n",
    "\n",
    "gameIdPostSeason = {'2017': {'Wild Card Weekend': ['10012018-0106-00e8-ac85-d2fa663251dc', '10012018-0106-01eb-45eb-1255e2c5e9ab', '10012018-0107-00c0-ebb3-fbe0ed9b55f2', '10012018-0107-0124-d89f-fab5ec67ec2c'], 'Divisional Playoffs': ['10012018-0113-0027-5ad4-10e6067ae155', '10012018-0113-01fb-8f68-4a5449c4641c', '10012018-0114-0048-dd02-c0f3428876ed', '10012018-0114-01c7-b88f-d11a8fa16678'], 'Conference Championships': ['10012018-0121-0047-90d5-63b8ae515160', '10012018-0121-01be-4e6e-7f0f493bd683'], 'Super Bowl': ['10012018-0204-00f8-9eca-052dd7e9e25e']}, '2018': {'Wild Card Weekend': ['10012019-0105-00a9-4c2e-a3dae7c9bb57', '10012019-0105-0116-362d-e4e3c48adfb3', '10012019-0106-005a-574f-475280a046b5', '10012019-0106-0146-759e-b95a216e1855'], 'Divisional Playoffs': ['10012019-0112-00b6-5b83-663c8c413f66', '10012019-0112-01bc-4205-aee1cde7ae7e', '10012019-0113-00b7-fcb7-3bd66f10a085', '10012019-0113-01af-5524-49630f415bc6'], 'Conference Championships': ['10012019-0120-00d2-9c6a-c240b0871487', '10012019-0120-012d-af52-66102bbef4f9'], 'Super Bowl': ['10012019-0203-0011-323b-548fe39c23df']}, '2019': {'Wild Card Weekend': ['10012020-0104-00e9-ee54-d4659e34f0ef', '10012020-0104-0116-24ed-ba717e240de6', '10012020-0105-004c-37e6-466d8ad28fe6', '10012020-0105-01cf-ea98-be288c530432'], 'Divisional Playoffs': ['10012020-0111-0036-d1bd-2eaa582b2504', '10012020-0111-016d-1f6d-d3756f62d34d', '10012020-0112-006a-8a5b-7b7fbc8ee635', '10012020-0112-01d6-42be-62616873ed8a'], 'Conference Championships': ['10012020-0119-0040-dd1f-94f7b421fbe8', '10012020-0119-0143-6536-3e1a08f53fca'], 'Super Bowl': ['10012020-0202-00b8-acb1-7ee139d04911']}, '2020': {'Wild Card Weekend': ['10012021-0109-0030-5d40-56e11c9b08de', '10012021-0109-0116-3edd-4a182c7e9bc7', '10012021-0109-021a-ff10-b3eb76081d4e', '10012021-0110-0095-d448-3199331664e8', '10012021-0110-0151-a068-21cd61def9ed', '10012021-0110-02cc-d00c-c0d4d285bdcc'], 'Divisional Playoffs': ['10012021-0116-00d3-e1c6-a199dd7be4e4', '10012021-0116-0189-0785-9fab11c5c116', '10012021-0117-006b-7bf8-29ac7d13d5d1', '10012021-0117-01f0-2754-b233f5467d9f'], 'Conference Championships': ['10012021-0124-00e4-9394-bdae155be446', '10012021-0124-01c1-69ad-1ab676fd990a'], 'Super Bowl': ['10012021-0207-0069-5207-a78dd8bf8075']}, '2021': {'Wild Card Weekend': ['487cf9a5-71b0-11ec-9fcd-de7ed4db3526', '64353102-71b0-11ec-9fcd-de7ed4db3526', '85c2567f-71b0-11ec-8c0c-efbc3bdccf8f', 'a447da6f-71b0-11ec-8c0c-efbc3bdccf8f', 'c3d33bd6-71b0-11ec-8c0c-efbc3bdccf8f', 'f5ec45a2-71b0-11ec-90f0-5bfd5be65b5b'], 'Divisional Playoffs': ['ab2d01cc-71ac-11ec-a6f7-85513e732977', 'c74c9331-71ac-11ec-a6f7-85513e732977', '114974ad-71ad-11ec-a493-77fb1cc3a88e', '34f0d976-71ad-11ec-a493-77fb1cc3a88e'], 'Conference Championships': ['67a557e3-71ad-11ec-aca1-684d5ebaef68', '825dda63-71ad-11ec-aca1-684d5ebaef68'], 'Super Bowl': ['757bbb2a-71a2-11ec-8e86-ebe0df6765ab']}, '2022': {'Wild Card Weekend': ['f4ed1058-8fd5-11ed-9789-5c606116f089', '27a7c406-8fd6-11ed-9789-5c606116f089', '4f7ad01f-8fd6-11ed-9789-5c606116f089', '73f9964d-8fd6-11ed-9789-5c606116f089', '92a33669-8fd6-11ed-9789-5c606116f089', 'b513b28d-8fd6-11ed-9789-5c606116f089'], 'Divisional Playoffs': ['0399c7f4-9556-11ed-b824-0d7028be3cee', '26af553e-9556-11ed-b824-0d7028be3cee', '4d476c73-9556-11ed-b824-0d7028be3cee', '6f445459-9556-11ed-b824-0d7028be3cee'], 'Conference Championships': ['b271e50f-9aa9-11ed-99e5-6b206f74937e', '44497169-9a0b-11ed-99e5-6b206f74937e'], 'Super Bowl': ['70e5ba20-9aaa-11ed-99e5-6b206f74937e']}}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0284f5ea",
   "metadata": {},
   "source": [
    "### 3. Récupération des données de joueurs pour chaque match à partir de l'ID du match\n",
    "\n",
    "Une fois les Urls récupérées de chaque match, je peux récupérer les données des joueurs. Dans la fonction qui suit je fais un appel d'api pour récupérer le document Json contenant les données."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "31dbf0ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "#RECUPERATION DES DATAS DES MATCHS A PARTIR DE L'ID DE LA GAME\n",
    "def get_game_data(game_id):\n",
    "    url ='https://api.nfl.com/experience/v1/stats/{}/players'.format(game_id)\n",
    "\n",
    "    response_gameData = requests.get(url, headers=headers)\n",
    "    result = json.loads(response_gameData.text)\n",
    "    \n",
    "    return result['data']['viewer']['live']['playerGameStats']\n",
    "#     return result\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f2c76281",
   "metadata": {},
   "source": [
    "# 3. Création de la database MongoDB"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "59edee70",
   "metadata": {},
   "outputs": [],
   "source": [
    "from pymongo import MongoClient\n",
    "client = MongoClient(\"localhost\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "1052fb9b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['admin', 'config', 'local', 'nfl', 'series']\n"
     ]
    }
   ],
   "source": [
    "print(client.list_database_names())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "5490d454",
   "metadata": {},
   "outputs": [],
   "source": [
    "db_projet = client.nfl\n",
    "\n",
    "collection_projet = db_projet['projet']\n",
    "projet_players = collection_projet['players']\n",
    "\n",
    "# print(db_projet.list_collection_names())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a796a625",
   "metadata": {},
   "source": [
    "# 4. Alimentation des collections MongoDB\n",
    "\n",
    "### Alimentation des collections pour les saisons régulières."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "f390f974",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fun_scraping_regular(year):\n",
    "    print(\"Début du téléchargement\")\n",
    "    gameTeamsURLs_year = gameTeamsURLs[year]\n",
    "    compteur = 0\n",
    "    for week in gameTeamsURLs_year.keys():\n",
    "\n",
    "        gameTeamsURLs_week = gameTeamsURLs_year[week]\n",
    "\n",
    "        projet_players.insert_one({\"year{}\".format(year):\"{}\".format(week)})\n",
    "\n",
    "        for url in gameTeamsURLs_week : \n",
    "    #         time.sleep(1)\n",
    "            compteur +=1\n",
    "            try : \n",
    "                gameID = get_gameId(url)\n",
    "                data_match = get_game_data(gameID)\n",
    "                \n",
    "                for stat_player in data_match : \n",
    "                    #On a rencontré des données \"particulières\" qui ressemblaient à des pièges pour empêcher le scrapping\n",
    "                    #Une solution pour le premier type de données particulières est la suivante :\n",
    "                    \n",
    "                    if 'team' in stat_player.keys() : \n",
    "                        if stat_player['team']['nickName'] != \"\":\n",
    "                            #dictionnaire des valeurs du joueur associé à la clé 'gameStats'\n",
    "                            for _ in stat_player['gameStats'].keys() :\n",
    "                                stat_player[_] = stat_player['gameStats'][_]\n",
    "                            del stat_player['gameStats']\n",
    "\n",
    "                            del stat_player['lastModifiedDate']\n",
    "\n",
    "                            stat_player['teamName'] = stat_player['team']['nickName']\n",
    "                            del stat_player['team']\n",
    "\n",
    "                            stat_player['nickName'] = stat_player['player']['nickName']\n",
    "                            stat_player['firstName'] = stat_player['player']['firstName']\n",
    "                            stat_player['lastName'] = stat_player['player']['lastName']\n",
    "                            stat_player['displayName'] = stat_player['player']['displayName']\n",
    "                            stat_player['position']= stat_player['player']['currentPlayer']['position']\n",
    "                            del stat_player['player']\n",
    "\n",
    "                projet_players['year{}'.format(year)][week].insert_many(data_match) \n",
    "\n",
    "            except IndexError : \n",
    "                print(\"Error\")\n",
    "                print(f\"Attention il y a un problème avec l'année et la semaine : {year} {week} et l'url : {url}\")\n",
    "                \n",
    "            if compteur % 99 == 0:\n",
    "                print(\"Téléchargement en cours...\")\n",
    "                print(\"------\")\n",
    "\n",
    "\n",
    "    print(\"Téléchargement des données terminé.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "086eef53",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Début du téléchargement\n",
      "Téléchargement en cours...\n",
      "------\n",
      "Téléchargement en cours...\n",
      "------\n",
      "Téléchargement des données terminé.\n"
     ]
    }
   ],
   "source": [
    "year = '2017'\n",
    "fun_scraping_regular(year)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "e18c18b9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Début du téléchargement\n",
      "Téléchargement en cours...\n",
      "------\n",
      "Téléchargement en cours...\n",
      "------\n",
      "Téléchargement des données terminé.\n"
     ]
    }
   ],
   "source": [
    "year = '2018'\n",
    "fun_scraping_regular(year)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "41ba0467",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Début du téléchargement\n",
      "Téléchargement en cours...\n",
      "------\n",
      "Téléchargement en cours...\n",
      "------\n",
      "Téléchargement des données terminé.\n"
     ]
    }
   ],
   "source": [
    "year = '2019'\n",
    "fun_scraping_regular(year)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "2dcb970f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Début du téléchargement\n",
      "Téléchargement en cours...\n",
      "------\n",
      "Téléchargement en cours...\n",
      "------\n",
      "Téléchargement des données terminé.\n"
     ]
    }
   ],
   "source": [
    "year = '2020'\n",
    "fun_scraping_regular(year)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "0f3423e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Début du téléchargement\n",
      "Téléchargement en cours...\n",
      "------\n",
      "Téléchargement en cours...\n",
      "------\n",
      "Téléchargement des données terminé.\n"
     ]
    }
   ],
   "source": [
    "year = '2021'\n",
    "fun_scraping_regular(year)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "10d0ad67",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Début du téléchargement\n",
      "Téléchargement en cours...\n",
      "------\n",
      "Téléchargement en cours...\n",
      "------\n",
      "Téléchargement des données terminé.\n"
     ]
    }
   ],
   "source": [
    "year = '2022'\n",
    "fun_scraping_regular(year)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5d8009e4",
   "metadata": {},
   "source": [
    "### Alimentation des collections pour les post saisons"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "eb68d21e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fun_scraping_post():\n",
    "    print(\"Début du téléchargement\")\n",
    "    \n",
    "    compteur = 0\n",
    "    \n",
    "    for  year in gameIdPostSeason.keys() : \n",
    "        gameIdPostSeason_year = gameIdPostSeason[year]\n",
    "        \n",
    "        for week in gameIdPostSeason_year.keys():\n",
    "\n",
    "            gameIdPostSeason_week = gameIdPostSeason_year[week]\n",
    "\n",
    "            projet_players.insert_one({\"year{}\".format(year):\"{}\".format(dict_postSeason[week])})\n",
    "\n",
    "            for id in gameIdPostSeason_week : \n",
    "        #         time.sleep(1)\n",
    "                compteur +=1\n",
    "                \n",
    "                data_match = get_game_data(id)\n",
    "                \n",
    "                for stat_player in data_match : \n",
    "                    #On a rencontré des données \"particulières\" qui ressemblaient à des pièges pour empêcher le scrapping\n",
    "                    #Une solution pour le premier type de données particulières est la suivante :\n",
    "                    \n",
    "                    if 'team' in stat_player.keys() : \n",
    "                        if stat_player['team']['nickName'] != \"\":\n",
    "                            #dictionnaire des valeurs du joueur associé à la clé 'gameStats'\n",
    "                            for _ in stat_player['gameStats'].keys() :\n",
    "                                stat_player[_] = stat_player['gameStats'][_]\n",
    "                            del stat_player['gameStats']\n",
    "\n",
    "                            del stat_player['lastModifiedDate']\n",
    "\n",
    "                            stat_player['teamName'] = stat_player['team']['nickName']\n",
    "                            del stat_player['team']\n",
    "\n",
    "                            stat_player['nickName'] = stat_player['player']['nickName']\n",
    "                            stat_player['firstName'] = stat_player['player']['firstName']\n",
    "                            stat_player['lastName'] = stat_player['player']['lastName']\n",
    "                            stat_player['displayName'] = stat_player['player']['displayName']\n",
    "                            stat_player['position']= stat_player['player']['currentPlayer']['position']\n",
    "                            del stat_player['player']\n",
    "\n",
    "                projet_players[\"year{}\".format(year)][\"{}\".format(dict_postSeason[week])].insert_many(data_match) \n",
    "                    \n",
    "                if compteur % 50 == 0:\n",
    "                    print(\"Téléchargement en cours...\")\n",
    "                    print(\"------\")\n",
    "\n",
    "\n",
    "    print(\"Téléchargement des données terminé.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "d621ca6f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Début du téléchargement\n",
      "Téléchargement en cours...\n",
      "------\n",
      "Téléchargement des données terminé.\n"
     ]
    }
   ],
   "source": [
    "fun_scraping_post()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4dc29072",
   "metadata": {},
   "source": [
    "### Partie traitement des données \n",
    "\n",
    "Les données dans les documents JSON obtenus par le scrapping de la page officielle de la NFL sont pour certaines superflues. \n",
    "Pour les données relatives aux joueurs, je retire les données qui ne m'interessent pas et qui ne seront pas utiles pour mon application."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1b23ea16",
   "metadata": {},
   "source": [
    "Pour des raisons de faisabilité, j'ai directement intégré la partie traitement des données dans les codes d'alimentation des données"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7fe0f294",
   "metadata": {},
   "source": [
    "# Affichage des données et quelques graphes à afficher"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8be90f97",
   "metadata": {},
   "source": [
    "### Stats à la passe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "3d73e244",
   "metadata": {},
   "outputs": [],
   "source": [
    "dfs = []\n",
    "for _ in range(1,18):\n",
    "    df = pd.DataFrame(list(client['nfl']['projet']['players']['year2017'][f\"reg{_}\"].find({\"$and\":[{\"position\":\"QB\"},{\"teamName\":\"Steelers\"}]})))\n",
    "    df[\"week\"] = f\"reg{_}\"\n",
    "\n",
    "    dfs.append(df)\n",
    "    \n",
    "for _ in range(1,5):\n",
    "    df = pd.DataFrame(list(client['nfl']['projet']['players']['year2017'][f\"post{_}\"].find({\"$and\":[{\"position\":\"QB\"},{\"teamName\":\"Steelers\"}]})))\n",
    "    df[\"week\"] = dict_postSeasonKey[f\"post{_}\"]\n",
    "    \n",
    "    dfs.append(df)\n",
    "    \n",
    "dataFrame = pd.concat(dfs)\n",
    "# print(dataFrame)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "56695268",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "legendgroup": "Ben Roethlisberger",
         "line": {
          "color": "#636efa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "Ben Roethlisberger",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          36,
          35,
          39,
          30,
          55,
          25,
          24,
          31,
          31,
          45,
          45,
          40,
          66,
          30,
          29,
          58
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Ben Roethlisberger",
         "line": {
          "color": "#636efa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "Ben Roethlisberger",
         "orientation": "v",
         "showlegend": false,
         "type": "scatter",
         "x": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          24,
          23,
          22,
          18,
          33,
          17,
          14,
          17,
          19,
          30,
          33,
          24,
          44,
          22,
          20,
          37
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Landry Jones",
         "line": {
          "color": "#EF553B",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "Landry Jones",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg11",
          "reg16",
          "reg17"
         ],
         "xaxis": "x",
         "y": [
          0,
          1,
          27
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Landry Jones",
         "line": {
          "color": "#EF553B",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "Landry Jones",
         "orientation": "v",
         "showlegend": false,
         "type": "scatter",
         "x": [
          "reg11",
          "reg16",
          "reg17"
         ],
         "xaxis": "x",
         "y": [
          0,
          0,
          23
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "hovermode": "x",
        "legend": {
         "bgcolor": "rgba(255, 255, 255, 0)",
         "bordercolor": "rgba(255, 255, 255, 0)",
         "title": {
          "text": "displayName"
         },
         "tracegroupgap": 0,
         "x": 0,
         "y": 1
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Passing rates from Pittsburgh Steelers players"
        },
        "xaxis": {
         "anchor": "y",
         "categoryarray": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg9",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "reg17",
          "reg18",
          "Wild Card Weekend",
          "Divisional Playoffs",
          "Conference Championships",
          "Super Bowl"
         ],
         "categoryorder": "array",
         "domain": [
          0,
          1
         ],
         "tickfont": {
          "size": 14
         },
         "title": {
          "text": "Weeks"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "tickfont": {
          "size": 14
         },
         "title": {
          "font": {
           "size": 16
          },
          "text": "Passing completions function of passing attempts"
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"9e2fa195-a3ab-43a8-b997-f293f8f5b2d0\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"9e2fa195-a3ab-43a8-b997-f293f8f5b2d0\")) {                    Plotly.newPlot(                        \"9e2fa195-a3ab-43a8-b997-f293f8f5b2d0\",                        [{\"legendgroup\":\"Ben Roethlisberger\",\"line\":{\"color\":\"#636efa\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"Ben Roethlisberger\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[36.0,35.0,39.0,30.0,55.0,25.0,24.0,31.0,31.0,45.0,45.0,40.0,66.0,30.0,29.0,58.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Ben Roethlisberger\",\"line\":{\"color\":\"#636efa\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"Ben Roethlisberger\",\"orientation\":\"v\",\"showlegend\":false,\"x\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[24.0,23.0,22.0,18.0,33.0,17.0,14.0,17.0,19.0,30.0,33.0,24.0,44.0,22.0,20.0,37.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Landry Jones\",\"line\":{\"color\":\"#EF553B\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"Landry Jones\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg11\",\"reg16\",\"reg17\"],\"xaxis\":\"x\",\"y\":[0.0,1.0,27.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Landry Jones\",\"line\":{\"color\":\"#EF553B\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"Landry Jones\",\"orientation\":\"v\",\"showlegend\":false,\"x\":[\"reg11\",\"reg16\",\"reg17\"],\"xaxis\":\"x\",\"y\":[0.0,0.0,23.0],\"yaxis\":\"y\",\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Weeks\"},\"categoryorder\":\"array\",\"categoryarray\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg9\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg17\",\"reg18\",\"Wild Card Weekend\",\"Divisional Playoffs\",\"Conference Championships\",\"Super Bowl\"],\"tickfont\":{\"size\":14}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Passing completions function of passing attempts\",\"font\":{\"size\":16}},\"tickfont\":{\"size\":14}},\"legend\":{\"title\":{\"text\":\"displayName\"},\"tracegroupgap\":0,\"x\":0,\"y\":1.0,\"bgcolor\":\"rgba(255, 255, 255, 0)\",\"bordercolor\":\"rgba(255, 255, 255, 0)\"},\"margin\":{\"t\":60},\"hovermode\":\"x\",\"title\":{\"text\":\"Passing rates from Pittsburgh Steelers players\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('9e2fa195-a3ab-43a8-b997-f293f8f5b2d0');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# dataFrame.tail(), dataFrame.head()\n",
    "ordered_weeks=[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg9\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg17\",\"reg18\",\"Wild Card Weekend\",\"Divisional Playoffs\" ,\"Conference Championships\",\"Super Bowl\"]\n",
    "passing_stats = ['passingAttempts', 'passingCompletions', 'passingTouchdowns', 'passingYards','passingInterceptions']\n",
    "\n",
    "fig = px.line(dataFrame, x= 'week', y =[passing_stats[0],passing_stats[1]], color='displayName', markers=True, category_orders={\"week\" :ordered_weeks })\n",
    "fig.update_traces(mode=\"markers+lines\", hovertemplate=None)\n",
    "fig.update_layout(hovermode=\"x\")\n",
    "fig.update_layout(\n",
    "    title='Passing rates from Pittsburgh Steelers players',\n",
    "    xaxis_tickfont_size=14,\n",
    "    xaxis_title='Weeks',\n",
    "    yaxis=dict(\n",
    "        title='Passing completions function of passing attempts',\n",
    "        titlefont_size=16,\n",
    "        tickfont_size=14,\n",
    "    ),\n",
    "    legend=dict(\n",
    "        x=0,\n",
    "        y=1.0,\n",
    "        bgcolor='rgba(255, 255, 255, 0)',\n",
    "        bordercolor='rgba(255, 255, 255, 0)'\n",
    "    ),\n",
    ")\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "04ddf31e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "legendgroup": "Ben Roethlisberger",
         "line": {
          "color": "#636efa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "Ben Roethlisberger",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          263,
          243,
          235,
          216,
          312,
          252,
          224,
          317,
          236,
          299,
          351,
          290,
          506,
          281,
          226,
          469
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Landry Jones",
         "line": {
          "color": "#EF553B",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "Landry Jones",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg11",
          "reg16",
          "reg17"
         ],
         "xaxis": "x",
         "y": [
          0,
          0,
          239
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "hovermode": "x",
        "legend": {
         "bgcolor": "rgba(255, 255, 255, 0)",
         "bordercolor": "rgba(255, 255, 255, 0)",
         "title": {
          "text": "displayName"
         },
         "tracegroupgap": 0,
         "x": 0,
         "y": 1
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Passing yards Pittsburgh Steelers players"
        },
        "xaxis": {
         "anchor": "y",
         "categoryarray": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg9",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "reg17",
          "reg18",
          "Wild Card Weekend",
          "Divisional Playoffs",
          "Conference Championships",
          "Super Bowl"
         ],
         "categoryorder": "array",
         "domain": [
          0,
          1
         ],
         "tickfont": {
          "size": 14
         },
         "title": {
          "text": "Weeks"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "tickfont": {
          "size": 14
         },
         "title": {
          "font": {
           "size": 16
          },
          "text": "Passing yards"
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"70c667b8-54f0-4b8a-8ffc-62c172f681e4\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"70c667b8-54f0-4b8a-8ffc-62c172f681e4\")) {                    Plotly.newPlot(                        \"70c667b8-54f0-4b8a-8ffc-62c172f681e4\",                        [{\"legendgroup\":\"Ben Roethlisberger\",\"line\":{\"color\":\"#636efa\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"Ben Roethlisberger\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[263.0,243.0,235.0,216.0,312.0,252.0,224.0,317.0,236.0,299.0,351.0,290.0,506.0,281.0,226.0,469.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Landry Jones\",\"line\":{\"color\":\"#EF553B\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"Landry Jones\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg11\",\"reg16\",\"reg17\"],\"xaxis\":\"x\",\"y\":[0.0,0.0,239.0],\"yaxis\":\"y\",\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Weeks\"},\"categoryorder\":\"array\",\"categoryarray\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg9\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg17\",\"reg18\",\"Wild Card Weekend\",\"Divisional Playoffs\",\"Conference Championships\",\"Super Bowl\"],\"tickfont\":{\"size\":14}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Passing yards\",\"font\":{\"size\":16}},\"tickfont\":{\"size\":14}},\"legend\":{\"title\":{\"text\":\"displayName\"},\"tracegroupgap\":0,\"x\":0,\"y\":1.0,\"bgcolor\":\"rgba(255, 255, 255, 0)\",\"bordercolor\":\"rgba(255, 255, 255, 0)\"},\"margin\":{\"t\":60},\"hovermode\":\"x\",\"title\":{\"text\":\"Passing yards Pittsburgh Steelers players\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('70c667b8-54f0-4b8a-8ffc-62c172f681e4');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = px.line(dataFrame, x= 'week', y =passing_stats[3], labels={'x':'Weeks', 'y':'Total Yards'}, color='displayName', markers=True, category_orders={\"week\" :ordered_weeks } )\n",
    "fig.update_traces(mode=\"markers+lines\", hovertemplate=None)\n",
    "fig.update_layout(hovermode=\"x\")\n",
    "fig.update_layout(\n",
    "    title='Passing yards Pittsburgh Steelers players',\n",
    "    xaxis_tickfont_size=14,\n",
    "    xaxis_title='Weeks',\n",
    "    yaxis=dict(\n",
    "        title='Passing yards',\n",
    "        titlefont_size=16,\n",
    "        tickfont_size=14,\n",
    "    ),\n",
    "    legend=dict(\n",
    "        x=0,\n",
    "        y=1.0,\n",
    "        bgcolor='rgba(255, 255, 255, 0)',\n",
    "        bordercolor='rgba(255, 255, 255, 0)'\n",
    "    ),\n",
    ")\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "5659733b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "passing touchdowns: %{y}",
         "marker": {
          "color": "rgb(55, 83, 109)"
         },
         "name": "Total touchdown passes",
         "text": [
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Landry Jones",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Landry Jones",
          "Landry Jones",
          "Ben Roethlisberger"
         ],
         "type": "bar",
         "x": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg10",
          "reg11",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "reg16",
          "reg17",
          "Divisional Playoffs"
         ],
         "y": [
          2,
          2,
          1,
          1,
          0,
          1,
          2,
          1,
          2,
          4,
          0,
          4,
          2,
          2,
          2,
          2,
          0,
          1,
          5
         ]
        },
        {
         "hovertemplate": "passing attempts: %{y}",
         "marker": {
          "color": "rgb(26, 118, 255)"
         },
         "name": "Total intercepted passes",
         "text": [
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Landry Jones",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Ben Roethlisberger",
          "Landry Jones",
          "Landry Jones",
          "Ben Roethlisberger"
         ],
         "type": "bar",
         "x": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg10",
          "reg11",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "reg16",
          "reg17",
          "Divisional Playoffs"
         ],
         "y": [
          1,
          0,
          0,
          1,
          5,
          1,
          0,
          1,
          1,
          0,
          0,
          2,
          1,
          0,
          1,
          0,
          0,
          1,
          1
         ]
        }
       ],
       "layout": {
        "bargap": 0.15,
        "bargroupgap": 0.1,
        "barmode": "group",
        "hovermode": "x",
        "legend": {
         "bgcolor": "rgba(255, 255, 255, 0)",
         "bordercolor": "rgba(255, 255, 255, 0)",
         "x": 0,
         "y": 1
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Pass Touchdowns and pass interceptions of QB players from Pittsburgh Steelers"
        },
        "xaxis": {
         "tickangle": 90,
         "tickfont": {
          "size": 14
         }
        },
        "yaxis": {
         "tickfont": {
          "size": 14
         },
         "title": {
          "font": {
           "size": 16
          },
          "text": "Pass touchdown and pass interception"
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"35f8efc1-689a-4b4c-92cf-748eb485ce18\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"35f8efc1-689a-4b4c-92cf-748eb485ce18\")) {                    Plotly.newPlot(                        \"35f8efc1-689a-4b4c-92cf-748eb485ce18\",                        [{\"hovertemplate\":\"passing touchdowns: %{y}\",\"marker\":{\"color\":\"rgb(55, 83, 109)\"},\"name\":\"Total touchdown passes\",\"text\":[\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Landry Jones\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Landry Jones\",\"Landry Jones\",\"Ben Roethlisberger\"],\"x\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg10\",\"reg11\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg16\",\"reg17\",\"Divisional Playoffs\"],\"y\":[2.0,2.0,1.0,1.0,0.0,1.0,2.0,1.0,2.0,4.0,0.0,4.0,2.0,2.0,2.0,2.0,0.0,1.0,5.0],\"type\":\"bar\"},{\"hovertemplate\":\"passing attempts: %{y}\",\"marker\":{\"color\":\"rgb(26, 118, 255)\"},\"name\":\"Total intercepted passes\",\"text\":[\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Landry Jones\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Ben Roethlisberger\",\"Landry Jones\",\"Landry Jones\",\"Ben Roethlisberger\"],\"x\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg10\",\"reg11\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg16\",\"reg17\",\"Divisional Playoffs\"],\"y\":[1.0,0.0,0.0,1.0,5.0,1.0,0.0,1.0,1.0,0.0,0.0,2.0,1.0,0.0,1.0,0.0,0.0,1.0,1.0],\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"xaxis\":{\"tickangle\":90,\"tickfont\":{\"size\":14}},\"barmode\":\"group\",\"hovermode\":\"x\",\"yaxis\":{\"title\":{\"text\":\"Pass touchdown and pass interception\",\"font\":{\"size\":16}},\"tickfont\":{\"size\":14}},\"legend\":{\"x\":0,\"y\":1.0,\"bgcolor\":\"rgba(255, 255, 255, 0)\",\"bordercolor\":\"rgba(255, 255, 255, 0)\"},\"title\":{\"text\":\"Pass Touchdowns and pass interceptions of QB players from Pittsburgh Steelers\"},\"bargap\":0.15,\"bargroupgap\":0.1},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('35f8efc1-689a-4b4c-92cf-748eb485ce18');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = go.Figure()\n",
    "fig.add_trace(go.Bar(\n",
    "    x=dataFrame[\"week\"],\n",
    "    y=dataFrame[passing_stats[2]],\n",
    "    name='Total touchdown passes',\n",
    "    marker_color='rgb(55, 83, 109)',\n",
    "    text=dataFrame[\"displayName\"],\n",
    "    hovertemplate=\"<br>\".join([\n",
    "            \"passing touchdowns: %{y}\",\n",
    "        ])\n",
    "    \n",
    "))\n",
    "fig.add_trace(go.Bar(\n",
    "    x=dataFrame[\"week\"],\n",
    "    y=dataFrame[passing_stats[4]],\n",
    "    name='Total intercepted passes',\n",
    "    marker_color='rgb(26, 118, 255)',\n",
    "    text=dataFrame[\"displayName\"],\n",
    "    hovertemplate=\"<br>\".join([\n",
    "            \"passing attempts: %{y}\",\n",
    "        ])\n",
    "))\n",
    "\n",
    "# Here we modify the tickangle of the xaxis, resulting in rotated labels.\n",
    "fig.update_layout(barmode='group', xaxis_tickangle=90, hovermode=\"x\")\n",
    "fig.update_layout(\n",
    "    title='Pass Touchdowns and pass interceptions of QB players from Pittsburgh Steelers',\n",
    "    xaxis_tickfont_size=14,\n",
    "    yaxis=dict(\n",
    "        title='Pass touchdown and pass interception',\n",
    "        titlefont_size=16,\n",
    "        tickfont_size=14,\n",
    "    ),\n",
    "    legend=dict(\n",
    "        x=0,\n",
    "        y=1.0,\n",
    "        bgcolor='rgba(255, 255, 255, 0)',\n",
    "        bordercolor='rgba(255, 255, 255, 0)'\n",
    "    ),\n",
    "    barmode='group',\n",
    "    bargap=0.15, # gap between bars of adjacent location coordinates.\n",
    "    bargroupgap=0.1, # gap between bars of the same location coordinate.\n",
    ")\n",
    "\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ec97faa1",
   "metadata": {},
   "source": [
    "### Stats à la course"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "d3b48502",
   "metadata": {},
   "outputs": [],
   "source": [
    "dfs = []\n",
    "for _ in range(1,18):\n",
    "    df = pd.DataFrame(list(client['nfl']['projet']['players']['year2017'][f\"reg{_}\"].find({\"$and\":[{\"$or\":[{\"position\":\"RB\"},{\"position\":\"FB\"}]},{\"teamName\":\"Steelers\"}]})))\n",
    "    df[\"week\"] = f\"reg{_}\"\n",
    "\n",
    "    dfs.append(df)\n",
    "\n",
    "for _ in range(1,5):\n",
    "    df = pd.DataFrame(list(client['nfl']['projet']['players']['year2017'][f\"post{_}\"].find({\"$and\":[{\"$or\":[{\"position\":\"RB\"},{\"position\":\"FB\"}]},{\"teamName\":\"Steelers\"}]})))\n",
    "    df[\"week\"] = dict_postSeasonKey[f\"post{_}\"]\n",
    "    \n",
    "    dfs.append(df)\n",
    "    \n",
    "dataFrame = pd.concat(dfs)\n",
    "# print(dataFrame)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "6778a0b8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "legendgroup": "Le'Veon Bell",
         "marker": {
          "color": "#636efa",
          "size": [
           3.2,
           3.2,
           4.1,
           4.1,
           3.1,
           5.6,
           3.8,
           3,
           3.1,
           3.8,
           4.8,
           4.2,
           3.7,
           4.9,
           4.9,
           4.2
          ],
          "sizemode": "area",
          "sizeref": 0.03,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Le'Veon Bell",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          32,
          87,
          61,
          144,
          47,
          179,
          134,
          76,
          80,
          46,
          95,
          76,
          48,
          117,
          69,
          67
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "James Conner",
         "marker": {
          "color": "#EF553B",
          "size": [
           2.8,
           9,
           6.5,
           3,
           7,
           6.3,
           1,
           12,
           2.4,
           4,
           3,
           4.3
          ],
          "sizemode": "area",
          "sizeref": 0.03,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "James Conner",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg2",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg10",
          "reg11",
          "reg13",
          "reg14",
          "reg15"
         ],
         "xaxis": "x",
         "y": [
          11,
          9,
          26,
          9,
          14,
          19,
          1,
          12,
          12,
          12,
          6,
          13
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Terrell Watson",
         "marker": {
          "color": "#00cc96",
          "size": [
           1,
           3,
           1,
           3,
           0,
           0,
           0
          ],
          "sizemode": "area",
          "sizeref": 0.03,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Terrell Watson",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg2",
          "reg3",
          "reg4",
          "reg6",
          "reg7",
          "reg10",
          "reg11"
         ],
         "xaxis": "x",
         "y": [
          1,
          3,
          1,
          3,
          0,
          0,
          0
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Roosevelt Nix-Jones",
         "marker": {
          "color": "#ab63fa",
          "size": [
           0,
           0,
           0,
           0,
           0,
           0,
           0,
           0,
           1,
           0.5
          ],
          "sizemode": "area",
          "sizeref": 0.03,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Roosevelt Nix-Jones",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg6",
          "reg7",
          "reg8",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "reg17"
         ],
         "xaxis": "x",
         "y": [
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          1,
          -1
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Fitzgerald Toussaint",
         "marker": {
          "color": "#FFA15A",
          "size": [
           0,
           3,
           4.4,
           0
          ],
          "sizemode": "area",
          "sizeref": 0.03,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Fitzgerald Toussaint",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg14",
          "reg15",
          "reg17",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          0,
          3,
          22,
          0
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Stevan Ridley",
         "marker": {
          "color": "#19d3f3",
          "size": [
           3.1,
           4.7
          ],
          "sizemode": "area",
          "sizeref": 0.03,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Stevan Ridley",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg16",
          "reg17"
         ],
         "xaxis": "x",
         "y": [
          28,
          80
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "hovermode": "x",
        "legend": {
         "bgcolor": "rgba(255, 255, 255, 0)",
         "bordercolor": "rgba(255, 255, 255, 0)",
         "itemsizing": "constant",
         "title": {
          "text": "displayName"
         },
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Rushing yards Pittsburgh Steelers players"
        },
        "xaxis": {
         "anchor": "y",
         "categoryarray": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg9",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "reg17",
          "reg18",
          "Wild Card Weekend",
          "Divisional Playoffs",
          "Conference Championships",
          "Super Bowl"
         ],
         "categoryorder": "array",
         "domain": [
          0,
          1
         ],
         "tickangle": 90,
         "tickfont": {
          "size": 14
         },
         "title": {
          "text": "Weeks"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "tickfont": {
          "size": 14
         },
         "title": {
          "font": {
           "size": 16
          },
          "text": "Rushing yards"
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"97039e53-e050-4255-927b-e9688afffe0f\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"97039e53-e050-4255-927b-e9688afffe0f\")) {                    Plotly.newPlot(                        \"97039e53-e050-4255-927b-e9688afffe0f\",                        [{\"legendgroup\":\"Le'Veon Bell\",\"marker\":{\"color\":\"#636efa\",\"size\":[3.2,3.2,4.1,4.1,3.1,5.6,3.8,3.0,3.1,3.8,4.8,4.2,3.7,4.9,4.9,4.2],\"sizemode\":\"area\",\"sizeref\":0.03,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Le'Veon Bell\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[32.0,87.0,61.0,144.0,47.0,179.0,134.0,76.0,80.0,46.0,95.0,76.0,48.0,117.0,69.0,67.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"James Conner\",\"marker\":{\"color\":\"#EF553B\",\"size\":[2.8,9.0,6.5,3.0,7.0,6.3,1.0,12.0,2.4,4.0,3.0,4.3],\"sizemode\":\"area\",\"sizeref\":0.03,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"James Conner\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg2\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg10\",\"reg11\",\"reg13\",\"reg14\",\"reg15\"],\"xaxis\":\"x\",\"y\":[11.0,9.0,26.0,9.0,14.0,19.0,1.0,12.0,12.0,12.0,6.0,13.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Terrell Watson\",\"marker\":{\"color\":\"#00cc96\",\"size\":[1.0,3.0,1.0,3.0,0.0,0.0,0.0],\"sizemode\":\"area\",\"sizeref\":0.03,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Terrell Watson\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg2\",\"reg3\",\"reg4\",\"reg6\",\"reg7\",\"reg10\",\"reg11\"],\"xaxis\":\"x\",\"y\":[1.0,3.0,1.0,3.0,0.0,0.0,0.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Roosevelt Nix-Jones\",\"marker\":{\"color\":\"#ab63fa\",\"size\":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.5],\"sizemode\":\"area\",\"sizeref\":0.03,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Roosevelt Nix-Jones\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg6\",\"reg7\",\"reg8\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg17\"],\"xaxis\":\"x\",\"y\":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,-1.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Fitzgerald Toussaint\",\"marker\":{\"color\":\"#FFA15A\",\"size\":[0.0,3.0,4.4,0.0],\"sizemode\":\"area\",\"sizeref\":0.03,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Fitzgerald Toussaint\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg14\",\"reg15\",\"reg17\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[0.0,3.0,22.0,0.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Stevan Ridley\",\"marker\":{\"color\":\"#19d3f3\",\"size\":[3.1,4.7],\"sizemode\":\"area\",\"sizeref\":0.03,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Stevan Ridley\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg16\",\"reg17\"],\"xaxis\":\"x\",\"y\":[28.0,80.0],\"yaxis\":\"y\",\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Weeks\"},\"categoryorder\":\"array\",\"categoryarray\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg9\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg17\",\"reg18\",\"Wild Card Weekend\",\"Divisional Playoffs\",\"Conference Championships\",\"Super Bowl\"],\"tickangle\":90,\"tickfont\":{\"size\":14}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Rushing yards\",\"font\":{\"size\":16}},\"tickfont\":{\"size\":14}},\"legend\":{\"title\":{\"text\":\"displayName\"},\"tracegroupgap\":0,\"itemsizing\":\"constant\",\"bgcolor\":\"rgba(255, 255, 255, 0)\",\"bordercolor\":\"rgba(255, 255, 255, 0)\"},\"margin\":{\"t\":60},\"hovermode\":\"x\",\"title\":{\"text\":\"Rushing yards Pittsburgh Steelers players\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('97039e53-e050-4255-927b-e9688afffe0f');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "rushing_stats =['rushingAttempts', 'rushingAverageYards', 'rushingTouchdowns', 'rushingYards']\n",
    "\n",
    "dataFrame['abs_rushAverage'] = np.abs(dataFrame['rushingAverageYards'])\n",
    "\n",
    "fig_11 = px.scatter(dataFrame, x = \"week\", y = \"rushingYards\", size = \"abs_rushAverage\", color = \"displayName\", category_orders={\"week\" :ordered_weeks } )\n",
    "fig_11.update_traces(hovertemplate =None)\n",
    "fig_11.update_layout(hovermode=\"x\", xaxis_tickangle=90)\n",
    "fig_11.update_layout(\n",
    "    title='Rushing yards Pittsburgh Steelers players',\n",
    "    xaxis_tickfont_size=14,\n",
    "    xaxis_title='Weeks',\n",
    "    yaxis=dict(\n",
    "        title='Rushing yards',\n",
    "        titlefont_size=16,\n",
    "        tickfont_size=14,\n",
    "    ),\n",
    "    legend=dict(\n",
    "        bgcolor='rgba(255, 255, 255, 0)',\n",
    "        bordercolor='rgba(255, 255, 255, 0)'\n",
    "    ),\n",
    ")\n",
    "fig_11.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "ad276856",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "legendgroup": "Le'Veon Bell",
         "marker": {
          "color": "#636efa",
          "size": [
           10,
           27,
           15,
           35,
           15,
           32,
           35,
           25,
           26,
           12,
           20,
           18,
           13,
           24,
           14,
           16
          ],
          "sizemode": "area",
          "sizeref": 0.0875,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Le'Veon Bell",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          10,
          27,
          15,
          35,
          15,
          32,
          35,
          25,
          26,
          12,
          20,
          18,
          13,
          24,
          14,
          16
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "James Conner",
         "marker": {
          "color": "#EF553B",
          "size": [
           4,
           1,
           4,
           3,
           2,
           3,
           1,
           1,
           5,
           3,
           2,
           3
          ],
          "sizemode": "area",
          "sizeref": 0.0875,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "James Conner",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg2",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg10",
          "reg11",
          "reg13",
          "reg14",
          "reg15"
         ],
         "xaxis": "x",
         "y": [
          4,
          1,
          4,
          3,
          2,
          3,
          1,
          1,
          5,
          3,
          2,
          3
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Terrell Watson",
         "marker": {
          "color": "#00cc96",
          "size": [
           1,
           1,
           1,
           1,
           1,
           0,
           0
          ],
          "sizemode": "area",
          "sizeref": 0.0875,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Terrell Watson",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg2",
          "reg3",
          "reg4",
          "reg6",
          "reg7",
          "reg10",
          "reg11"
         ],
         "xaxis": "x",
         "y": [
          1,
          1,
          1,
          1,
          1,
          0,
          0
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Roosevelt Nix-Jones",
         "marker": {
          "color": "#ab63fa",
          "size": [
           0,
           0,
           0,
           0,
           0,
           0,
           0,
           0,
           1,
           2
          ],
          "sizemode": "area",
          "sizeref": 0.0875,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Roosevelt Nix-Jones",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg6",
          "reg7",
          "reg8",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "reg17"
         ],
         "xaxis": "x",
         "y": [
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          1,
          2
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Fitzgerald Toussaint",
         "marker": {
          "color": "#FFA15A",
          "size": [
           0,
           1,
           5,
           0
          ],
          "sizemode": "area",
          "sizeref": 0.0875,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Fitzgerald Toussaint",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg14",
          "reg15",
          "reg17",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          0,
          1,
          5,
          0
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Stevan Ridley",
         "marker": {
          "color": "#19d3f3",
          "size": [
           9,
           17
          ],
          "sizemode": "area",
          "sizeref": 0.0875,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Stevan Ridley",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg16",
          "reg17"
         ],
         "xaxis": "x",
         "y": [
          9,
          17
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "hovermode": "x",
        "legend": {
         "bgcolor": "rgba(255, 255, 255, 0)",
         "bordercolor": "rgba(255, 255, 255, 0)",
         "itemsizing": "constant",
         "title": {
          "text": "displayName"
         },
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Rushing attempts Pittsburgh Steelers players"
        },
        "xaxis": {
         "anchor": "y",
         "categoryarray": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg9",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "reg17",
          "reg18",
          "Wild Card Weekend",
          "Divisional Playoffs",
          "Conference Championships",
          "Super Bowl"
         ],
         "categoryorder": "array",
         "domain": [
          0,
          1
         ],
         "tickangle": 90,
         "title": {
          "text": "Weeks"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "font": {
           "size": 16
          },
          "text": "Rushing attempts"
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"5969aba4-6aea-4563-9d4c-e0cce6bfe362\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"5969aba4-6aea-4563-9d4c-e0cce6bfe362\")) {                    Plotly.newPlot(                        \"5969aba4-6aea-4563-9d4c-e0cce6bfe362\",                        [{\"legendgroup\":\"Le'Veon Bell\",\"marker\":{\"color\":\"#636efa\",\"size\":[10.0,27.0,15.0,35.0,15.0,32.0,35.0,25.0,26.0,12.0,20.0,18.0,13.0,24.0,14.0,16.0],\"sizemode\":\"area\",\"sizeref\":0.0875,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Le'Veon Bell\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[10.0,27.0,15.0,35.0,15.0,32.0,35.0,25.0,26.0,12.0,20.0,18.0,13.0,24.0,14.0,16.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"James Conner\",\"marker\":{\"color\":\"#EF553B\",\"size\":[4.0,1.0,4.0,3.0,2.0,3.0,1.0,1.0,5.0,3.0,2.0,3.0],\"sizemode\":\"area\",\"sizeref\":0.0875,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"James Conner\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg2\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg10\",\"reg11\",\"reg13\",\"reg14\",\"reg15\"],\"xaxis\":\"x\",\"y\":[4.0,1.0,4.0,3.0,2.0,3.0,1.0,1.0,5.0,3.0,2.0,3.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Terrell Watson\",\"marker\":{\"color\":\"#00cc96\",\"size\":[1.0,1.0,1.0,1.0,1.0,0.0,0.0],\"sizemode\":\"area\",\"sizeref\":0.0875,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Terrell Watson\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg2\",\"reg3\",\"reg4\",\"reg6\",\"reg7\",\"reg10\",\"reg11\"],\"xaxis\":\"x\",\"y\":[1.0,1.0,1.0,1.0,1.0,0.0,0.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Roosevelt Nix-Jones\",\"marker\":{\"color\":\"#ab63fa\",\"size\":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,2.0],\"sizemode\":\"area\",\"sizeref\":0.0875,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Roosevelt Nix-Jones\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg6\",\"reg7\",\"reg8\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg17\"],\"xaxis\":\"x\",\"y\":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,2.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Fitzgerald Toussaint\",\"marker\":{\"color\":\"#FFA15A\",\"size\":[0.0,1.0,5.0,0.0],\"sizemode\":\"area\",\"sizeref\":0.0875,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Fitzgerald Toussaint\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg14\",\"reg15\",\"reg17\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[0.0,1.0,5.0,0.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Stevan Ridley\",\"marker\":{\"color\":\"#19d3f3\",\"size\":[9.0,17.0],\"sizemode\":\"area\",\"sizeref\":0.0875,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Stevan Ridley\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg16\",\"reg17\"],\"xaxis\":\"x\",\"y\":[9.0,17.0],\"yaxis\":\"y\",\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Weeks\"},\"categoryorder\":\"array\",\"categoryarray\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg9\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg17\",\"reg18\",\"Wild Card Weekend\",\"Divisional Playoffs\",\"Conference Championships\",\"Super Bowl\"],\"tickangle\":90},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Rushing attempts\",\"font\":{\"size\":16}}},\"legend\":{\"title\":{\"text\":\"displayName\"},\"tracegroupgap\":0,\"itemsizing\":\"constant\",\"bgcolor\":\"rgba(255, 255, 255, 0)\",\"bordercolor\":\"rgba(255, 255, 255, 0)\"},\"margin\":{\"t\":60},\"hovermode\":\"x\",\"title\":{\"text\":\"Rushing attempts Pittsburgh Steelers players\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('5969aba4-6aea-4563-9d4c-e0cce6bfe362');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig_12 = px.scatter(dataFrame, x=\"week\", y=\"rushingAttempts\", size= 'rushingAttempts', color = \"displayName\", category_orders={\"week\" :ordered_weeks })\n",
    "fig_12.update_traces( hovertemplate=None)\n",
    "fig_12.update_layout(hovermode=\"x\", xaxis_tickangle=90)\n",
    "fig_12.update_layout(\n",
    "    title='Rushing attempts Pittsburgh Steelers players',\n",
    "\n",
    "    xaxis_title='Weeks',\n",
    "    yaxis=dict(\n",
    "        title='Rushing attempts',\n",
    "        titlefont_size=16,\n",
    "    ),\n",
    "    legend=dict(\n",
    "        bgcolor='rgba(255, 255, 255, 0)',\n",
    "        bordercolor='rgba(255, 255, 255, 0)'\n",
    "    ),\n",
    ")\n",
    "\n",
    "fig_12.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "f6de8a7a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "legendgroup": "Bell",
         "marker": {
          "color": "#636efa",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Bell",
         "offsetgroup": "Bell",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "reg3",
          "reg4",
          "reg6",
          "reg8",
          "reg14",
          "reg15",
          "reg16",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          1,
          2,
          1,
          1,
          2,
          1,
          1,
          1
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "legendgroup": "Nix-Jones",
         "marker": {
          "color": "#EF553B",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Nix-Jones",
         "offsetgroup": "Nix-Jones",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "reg16"
         ],
         "xaxis": "x",
         "y": [
          1
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "legendgroup": "Ridley",
         "marker": {
          "color": "#00cc96",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Ridley",
         "offsetgroup": "Ridley",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "reg17"
         ],
         "xaxis": "x",
         "y": [
          1
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "barmode": "group",
        "hovermode": "x unified",
        "legend": {
         "bgcolor": "rgba(255, 255, 255, 0)",
         "bordercolor": "rgba(255, 255, 255, 0)",
         "title": {
          "text": "lastName"
         },
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "plot_bgcolor": "#FFF",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Bar plot of touchdowns by rushing from Steelers players"
        },
        "xaxis": {
         "anchor": "y",
         "categoryarray": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg9",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "reg17",
          "reg18",
          "Wild Card Weekend",
          "Divisional Playoffs",
          "Conference Championships",
          "Super Bowl"
         ],
         "categoryorder": "array",
         "domain": [
          0,
          1
         ],
         "linecolor": "#BCCCDC",
         "showgrid": false,
         "tickangle": 90,
         "title": {
          "text": "Weeks"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "linecolor": "#BCCCDC",
         "showgrid": false,
         "title": {
          "font": {
           "size": 16
          },
          "text": "Rushing touchdowns"
         },
         "visible": false
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"3a2be0e6-93c9-46b9-a609-8d842ad48b41\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"3a2be0e6-93c9-46b9-a609-8d842ad48b41\")) {                    Plotly.newPlot(                        \"3a2be0e6-93c9-46b9-a609-8d842ad48b41\",                        [{\"alignmentgroup\":\"True\",\"legendgroup\":\"Bell\",\"marker\":{\"color\":\"#636efa\",\"pattern\":{\"shape\":\"\"}},\"name\":\"Bell\",\"offsetgroup\":\"Bell\",\"orientation\":\"v\",\"showlegend\":true,\"textposition\":\"auto\",\"x\":[\"reg3\",\"reg4\",\"reg6\",\"reg8\",\"reg14\",\"reg15\",\"reg16\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[1.0,2.0,1.0,1.0,2.0,1.0,1.0,1.0],\"yaxis\":\"y\",\"type\":\"bar\"},{\"alignmentgroup\":\"True\",\"legendgroup\":\"Nix-Jones\",\"marker\":{\"color\":\"#EF553B\",\"pattern\":{\"shape\":\"\"}},\"name\":\"Nix-Jones\",\"offsetgroup\":\"Nix-Jones\",\"orientation\":\"v\",\"showlegend\":true,\"textposition\":\"auto\",\"x\":[\"reg16\"],\"xaxis\":\"x\",\"y\":[1.0],\"yaxis\":\"y\",\"type\":\"bar\"},{\"alignmentgroup\":\"True\",\"legendgroup\":\"Ridley\",\"marker\":{\"color\":\"#00cc96\",\"pattern\":{\"shape\":\"\"}},\"name\":\"Ridley\",\"offsetgroup\":\"Ridley\",\"orientation\":\"v\",\"showlegend\":true,\"textposition\":\"auto\",\"x\":[\"reg17\"],\"xaxis\":\"x\",\"y\":[1.0],\"yaxis\":\"y\",\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Weeks\"},\"categoryorder\":\"array\",\"categoryarray\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg9\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg17\",\"reg18\",\"Wild Card Weekend\",\"Divisional Playoffs\",\"Conference Championships\",\"Super Bowl\"],\"tickangle\":90,\"showgrid\":false,\"linecolor\":\"#BCCCDC\"},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Rushing touchdowns\",\"font\":{\"size\":16}},\"showgrid\":false,\"linecolor\":\"#BCCCDC\",\"visible\":false},\"legend\":{\"title\":{\"text\":\"lastName\"},\"tracegroupgap\":0,\"bgcolor\":\"rgba(255, 255, 255, 0)\",\"bordercolor\":\"rgba(255, 255, 255, 0)\"},\"margin\":{\"t\":60},\"barmode\":\"group\",\"hovermode\":\"x unified\",\"title\":{\"text\":\"Bar plot of touchdowns by rushing from Steelers players\"},\"plot_bgcolor\":\"#FFF\"},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('3a2be0e6-93c9-46b9-a609-8d842ad48b41');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#bar plot des touchdowns à la course \n",
    "fig3 = px.bar(dataFrame.query('rushingTouchdowns != 0'), x=\"week\", y=\"rushingTouchdowns\", color='lastName', category_orders={\"week\" :ordered_weeks })\n",
    "fig3.update_traces( hovertemplate=None)\n",
    "fig3.update_layout(barmode='group', hovermode=\"x unified\", xaxis_tickangle=90)\n",
    "fig3.update_layout(\n",
    "    title='Bar plot of touchdowns by rushing from Steelers players',\n",
    "    xaxis_title='Weeks',\n",
    "    xaxis_showgrid=False,   #désactivation des lignes des axes\n",
    "    xaxis_linecolor=\"#BCCCDC\",\n",
    "    plot_bgcolor=\"#FFF\", \n",
    "    yaxis=dict(\n",
    "        title='Rushing touchdowns',\n",
    "        titlefont_size=16,\n",
    "        showgrid=False, #désactivation des lignes des axes\n",
    "        linecolor=\"#BCCCDC\",\n",
    "        visible=False\n",
    "    ),\n",
    "    legend=dict(\n",
    "        bgcolor='rgba(255, 255, 255, 0)',\n",
    "        bordercolor='rgba(255, 255, 255, 0)'\n",
    "    ),\n",
    ")\n",
    "fig3.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "022fadcb",
   "metadata": {},
   "source": [
    "### Stats à la réception"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "b75e960c",
   "metadata": {},
   "outputs": [],
   "source": [
    "dfs = []\n",
    "for _ in range(1,18):\n",
    "    df = pd.DataFrame(list(client['nfl']['projet']['players']['year2017'][f\"reg{_}\"].find({\"$and\":[{\"$or\":[{\"position\":\"RB\"},{\"position\":\"WR\"},{\"position\":\"TE\"}]},{\"teamName\":\"Steelers\"}]})))\n",
    "    df[\"week\"] = f\"reg{_}\"\n",
    "\n",
    "    dfs.append(df)\n",
    "    \n",
    "for _ in range(1,5):\n",
    "    df = pd.DataFrame(list(client['nfl']['projet']['players']['year2017'][f\"post{_}\"].find({\"$and\":[{\"$or\":[{\"position\":\"RB\"},{\"position\":\"WR\"},{\"position\":\"TE\"}]},{\"teamName\":\"Steelers\"}]})))\n",
    "    df[\"week\"] = dict_postSeasonKey[f\"post{_}\"]\n",
    "    \n",
    "    dfs.append(df)\n",
    "\n",
    "dataFrame = pd.concat(dfs)\n",
    "# print(dataFrame)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "ee18bc22",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "legendgroup": "Antonio Brown",
         "marker": {
          "color": "#636efa",
          "size": [
           0,
           6,
           4,
           5,
           9,
           2,
           6,
           5,
           4,
           3,
           2,
           8,
           7,
           1,
           4
          ],
          "sizemode": "area",
          "sizeref": 0.0225,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Antonio Brown",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          11,
          5,
          10,
          4,
          10,
          8,
          4,
          5,
          3,
          10,
          10,
          8,
          11,
          2,
          7
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Le'Veon Bell",
         "marker": {
          "color": "#EF553B",
          "size": [
           3,
           0,
           1,
           2,
           0,
           3,
           0,
           1,
           1,
           2,
           2,
           1,
           1,
           1,
           3,
           4
          ],
          "sizemode": "area",
          "sizeref": 0.0225,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Le'Veon Bell",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          3,
          4,
          6,
          4,
          10,
          3,
          3,
          2,
          5,
          9,
          12,
          5,
          9,
          5,
          5,
          9
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Martavis Bryant",
         "marker": {
          "color": "#00cc96",
          "size": [
           4,
           1,
           6,
           2,
           3,
           1,
           1,
           2,
           2,
           2,
           2,
           4,
           2,
           1,
           1,
           2
          ],
          "sizemode": "area",
          "sizeref": 0.0225,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Martavis Bryant",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "reg17",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          2,
          3,
          2,
          3,
          5,
          2,
          1,
          3,
          2,
          4,
          4,
          6,
          4,
          3,
          6,
          2
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Eli Rogers",
         "marker": {
          "color": "#ab63fa",
          "size": [
           2,
           3,
           1,
           0,
           4,
           1,
           2,
           1,
           3,
           0,
           0
          ],
          "sizemode": "area",
          "sizeref": 0.0225,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Eli Rogers",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg2",
          "reg7",
          "reg10",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "reg17",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          2,
          4,
          1,
          1,
          3,
          1,
          3,
          1,
          1,
          1,
          5
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Jesse James",
         "marker": {
          "color": "#FFA15A",
          "size": [
           2,
           1,
           2,
           0,
           2,
           1,
           3,
           1,
           0,
           2,
           3,
           0,
           0
          ],
          "sizemode": "area",
          "sizeref": 0.0225,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Jesse James",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg8",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg17",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          6,
          4,
          2,
          3,
          3,
          2,
          5,
          3,
          1,
          10,
          2,
          2,
          1
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "JuJu Smith-Schuster",
         "marker": {
          "color": "#19d3f3",
          "size": [
           1,
           4,
           1,
           2,
           0,
           1,
           3,
           2,
           4,
           1,
           0,
           1,
           1,
           2
          ],
          "sizemode": "area",
          "sizeref": 0.0225,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "JuJu Smith-Schuster",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg10",
          "reg11",
          "reg13",
          "reg15",
          "reg16",
          "reg17",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          3,
          2,
          3,
          4,
          3,
          2,
          7,
          5,
          4,
          4,
          6,
          6,
          9,
          3
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Justin Hunter",
         "marker": {
          "color": "#FF6692",
          "size": [
           1,
           2,
           2,
           0
          ],
          "sizemode": "area",
          "sizeref": 0.0225,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Justin Hunter",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg4",
          "reg5",
          "reg8",
          "reg16"
         ],
         "xaxis": "x",
         "y": [
          1,
          1,
          1,
          1
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Vance McDonald",
         "marker": {
          "color": "#B6E880",
          "size": [
           1,
           1,
           0,
           2,
           1,
           1,
           6
          ],
          "sizemode": "area",
          "sizeref": 0.0225,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Vance McDonald",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg6",
          "reg7",
          "reg10",
          "reg14",
          "reg16",
          "reg17",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          1,
          2,
          2,
          4,
          4,
          1,
          10
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Darrius Heyward-Bey",
         "marker": {
          "color": "#FF97FF",
          "size": [
           0,
           0
          ],
          "sizemode": "area",
          "sizeref": 0.0225,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Darrius Heyward-Bey",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg7",
          "reg15"
         ],
         "xaxis": "x",
         "y": [
          1,
          1
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Xavier Grimble",
         "marker": {
          "color": "#FECB52",
          "size": [
           0,
           0,
           2,
           0,
           0
          ],
          "sizemode": "area",
          "sizeref": 0.0225,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Xavier Grimble",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg7",
          "reg12",
          "reg13",
          "reg15",
          "reg17"
         ],
         "xaxis": "x",
         "y": [
          1,
          1,
          1,
          1,
          1
         ],
         "yaxis": "y"
        },
        {
         "legendgroup": "Fitzgerald Toussaint",
         "marker": {
          "color": "#636efa",
          "size": [
           1
          ],
          "sizemode": "area",
          "sizeref": 0.0225,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Fitzgerald Toussaint",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg17"
         ],
         "xaxis": "x",
         "y": [
          2
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "hovermode": "x",
        "legend": {
         "bgcolor": "rgba(255, 255, 255, 0)",
         "bordercolor": "rgba(255, 255, 255, 0)",
         "itemsizing": "constant",
         "title": {
          "text": "displayName"
         },
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Nombre de passes réceptionnées par les joueurs des Steelers dont la taille dépend du nombre de passes non réceptionnées"
        },
        "xaxis": {
         "anchor": "y",
         "categoryarray": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg9",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "reg17",
          "reg18",
          "Wild Card Weekend",
          "Divisional Playoffs",
          "Conference Championships",
          "Super Bowl"
         ],
         "categoryorder": "array",
         "domain": [
          0,
          1
         ],
         "tickangle": 90,
         "title": {
          "text": "Weeks"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "font": {
           "size": 16
          },
          "text": "Receiving receptions"
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"a145d85c-b302-450d-9915-44dfbf904b0e\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"a145d85c-b302-450d-9915-44dfbf904b0e\")) {                    Plotly.newPlot(                        \"a145d85c-b302-450d-9915-44dfbf904b0e\",                        [{\"legendgroup\":\"Antonio Brown\",\"marker\":{\"color\":\"#636efa\",\"size\":[0.0,6.0,4.0,5.0,9.0,2.0,6.0,5.0,4.0,3.0,2.0,8.0,7.0,1.0,4.0],\"sizemode\":\"area\",\"sizeref\":0.0225,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Antonio Brown\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[11.0,5.0,10.0,4.0,10.0,8.0,4.0,5.0,3.0,10.0,10.0,8.0,11.0,2.0,7.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Le'Veon Bell\",\"marker\":{\"color\":\"#EF553B\",\"size\":[3.0,0.0,1.0,2.0,0.0,3.0,0.0,1.0,1.0,2.0,2.0,1.0,1.0,1.0,3.0,4.0],\"sizemode\":\"area\",\"sizeref\":0.0225,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Le'Veon Bell\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[3.0,4.0,6.0,4.0,10.0,3.0,3.0,2.0,5.0,9.0,12.0,5.0,9.0,5.0,5.0,9.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Martavis Bryant\",\"marker\":{\"color\":\"#00cc96\",\"size\":[4.0,1.0,6.0,2.0,3.0,1.0,1.0,2.0,2.0,2.0,2.0,4.0,2.0,1.0,1.0,2.0],\"sizemode\":\"area\",\"sizeref\":0.0225,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Martavis Bryant\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg17\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[2.0,3.0,2.0,3.0,5.0,2.0,1.0,3.0,2.0,4.0,4.0,6.0,4.0,3.0,6.0,2.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Eli Rogers\",\"marker\":{\"color\":\"#ab63fa\",\"size\":[2.0,3.0,1.0,0.0,4.0,1.0,2.0,1.0,3.0,0.0,0.0],\"sizemode\":\"area\",\"sizeref\":0.0225,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Eli Rogers\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg2\",\"reg7\",\"reg10\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg17\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[2.0,4.0,1.0,1.0,3.0,1.0,3.0,1.0,1.0,1.0,5.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Jesse James\",\"marker\":{\"color\":\"#FFA15A\",\"size\":[2.0,1.0,2.0,0.0,2.0,1.0,3.0,1.0,0.0,2.0,3.0,0.0,0.0],\"sizemode\":\"area\",\"sizeref\":0.0225,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Jesse James\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg8\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg17\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[6.0,4.0,2.0,3.0,3.0,2.0,5.0,3.0,1.0,10.0,2.0,2.0,1.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"JuJu Smith-Schuster\",\"marker\":{\"color\":\"#19d3f3\",\"size\":[1.0,4.0,1.0,2.0,0.0,1.0,3.0,2.0,4.0,1.0,0.0,1.0,1.0,2.0],\"sizemode\":\"area\",\"sizeref\":0.0225,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"JuJu Smith-Schuster\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg10\",\"reg11\",\"reg13\",\"reg15\",\"reg16\",\"reg17\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[3.0,2.0,3.0,4.0,3.0,2.0,7.0,5.0,4.0,4.0,6.0,6.0,9.0,3.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Justin Hunter\",\"marker\":{\"color\":\"#FF6692\",\"size\":[1.0,2.0,2.0,0.0],\"sizemode\":\"area\",\"sizeref\":0.0225,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Justin Hunter\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg4\",\"reg5\",\"reg8\",\"reg16\"],\"xaxis\":\"x\",\"y\":[1.0,1.0,1.0,1.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Vance McDonald\",\"marker\":{\"color\":\"#B6E880\",\"size\":[1.0,1.0,0.0,2.0,1.0,1.0,6.0],\"sizemode\":\"area\",\"sizeref\":0.0225,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Vance McDonald\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg6\",\"reg7\",\"reg10\",\"reg14\",\"reg16\",\"reg17\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[1.0,2.0,2.0,4.0,4.0,1.0,10.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Darrius Heyward-Bey\",\"marker\":{\"color\":\"#FF97FF\",\"size\":[0.0,0.0],\"sizemode\":\"area\",\"sizeref\":0.0225,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Darrius Heyward-Bey\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg7\",\"reg15\"],\"xaxis\":\"x\",\"y\":[1.0,1.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Xavier Grimble\",\"marker\":{\"color\":\"#FECB52\",\"size\":[0.0,0.0,2.0,0.0,0.0],\"sizemode\":\"area\",\"sizeref\":0.0225,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Xavier Grimble\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg7\",\"reg12\",\"reg13\",\"reg15\",\"reg17\"],\"xaxis\":\"x\",\"y\":[1.0,1.0,1.0,1.0,1.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"legendgroup\":\"Fitzgerald Toussaint\",\"marker\":{\"color\":\"#636efa\",\"size\":[1.0],\"sizemode\":\"area\",\"sizeref\":0.0225,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Fitzgerald Toussaint\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg17\"],\"xaxis\":\"x\",\"y\":[2.0],\"yaxis\":\"y\",\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Weeks\"},\"categoryorder\":\"array\",\"categoryarray\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg9\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg17\",\"reg18\",\"Wild Card Weekend\",\"Divisional Playoffs\",\"Conference Championships\",\"Super Bowl\"],\"tickangle\":90},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Receiving receptions\",\"font\":{\"size\":16}}},\"legend\":{\"title\":{\"text\":\"displayName\"},\"tracegroupgap\":0,\"itemsizing\":\"constant\",\"bgcolor\":\"rgba(255, 255, 255, 0)\",\"bordercolor\":\"rgba(255, 255, 255, 0)\"},\"margin\":{\"t\":60},\"hovermode\":\"x\",\"title\":{\"text\":\"Nombre de passes r\\u00e9ceptionn\\u00e9es par les joueurs des Steelers dont la taille d\\u00e9pend du nombre de passes non r\\u00e9ceptionn\\u00e9es\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('a145d85c-b302-450d-9915-44dfbf904b0e');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "receiving_stats = ['receivingReceptions', 'receivingTarget', 'receivingTouchdowns', 'receivingYards']\n",
    "\n",
    "dataFrame[\"inv_receivingFail\"] = np.abs(dataFrame[\"receivingTarget\"] - dataFrame[\"receivingReceptions\"])\n",
    "\n",
    "fig = px.scatter(dataFrame.query('receivingReceptions!=0'), x=\"week\", y='receivingReceptions',size='inv_receivingFail', color='displayName', category_orders={\"week\" :ordered_weeks })\n",
    "fig.update_traces( hovertemplate=None)\n",
    "fig.update_layout(hovermode=\"x\", xaxis_tickangle=90)\n",
    "fig.update_layout(\n",
    "    title='Nombre de passes réceptionnées par les joueurs des Steelers dont la taille dépend du nombre de passes non réceptionnées',\n",
    "\n",
    "    xaxis_title='Weeks',\n",
    "    yaxis=dict(\n",
    "        title='Receiving receptions',\n",
    "        titlefont_size=16,\n",
    "\n",
    "    ),\n",
    "    legend=dict(\n",
    "\n",
    "        bgcolor='rgba(255, 255, 255, 0)',\n",
    "        bordercolor='rgba(255, 255, 255, 0)'\n",
    "    ),\n",
    ")\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "93081c39",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "displayName=Darrius Heyward-Bey<br>week=%{x}<br>receivingYards=%{y}<extra></extra>",
         "legendgroup": "Darrius Heyward-Bey",
         "line": {
          "color": "#636efa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "Darrius Heyward-Bey",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg3",
          "reg4",
          "reg7",
          "reg8",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "reg17",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          0,
          0,
          0,
          44,
          0,
          0,
          0,
          3,
          0,
          0,
          0
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "displayName=Antonio Brown<br>week=%{x}<br>receivingYards=%{y}<extra></extra>",
         "legendgroup": "Antonio Brown",
         "line": {
          "color": "#EF553B",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "Antonio Brown",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          182,
          62,
          110,
          34,
          157,
          155,
          65,
          70,
          47,
          144,
          169,
          101,
          213,
          24,
          132
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "displayName=Vance McDonald<br>week=%{x}<br>receivingYards=%{y}<extra></extra>",
         "legendgroup": "Vance McDonald",
         "line": {
          "color": "#00cc96",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "Vance McDonald",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg10",
          "reg14",
          "reg16",
          "reg17",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          0,
          0,
          0,
          0,
          26,
          37,
          16,
          52,
          52,
          5,
          112
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "displayName=Le'Veon Bell<br>week=%{x}<br>receivingYards=%{y}<extra></extra>",
         "legendgroup": "Le'Veon Bell",
         "line": {
          "color": "#ab63fa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "Le'Veon Bell",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          15,
          4,
          37,
          42,
          46,
          12,
          58,
          5,
          32,
          57,
          88,
          106,
          77,
          48,
          28,
          88
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "displayName=Martavis Bryant<br>week=%{x}<br>receivingYards=%{y}<extra></extra>",
         "legendgroup": "Martavis Bryant",
         "line": {
          "color": "#FFA15A",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "Martavis Bryant",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "reg17",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          14,
          91,
          30,
          48,
          21,
          27,
          3,
          42,
          30,
          40,
          40,
          33,
          59,
          60,
          65,
          78
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "displayName=Eli Rogers<br>week=%{x}<br>receivingYards=%{y}<extra></extra>",
         "legendgroup": "Eli Rogers",
         "line": {
          "color": "#19d3f3",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "Eli Rogers",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg2",
          "reg3",
          "reg7",
          "reg8",
          "reg10",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "reg17",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          11,
          43,
          0,
          10,
          0,
          2,
          21,
          4,
          33,
          18,
          6,
          1,
          42
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "displayName=Jesse James<br>week=%{x}<br>receivingYards=%{y}<extra></extra>",
         "legendgroup": "Jesse James",
         "line": {
          "color": "#FF6692",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "Jesse James",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg8",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "reg17",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          41,
          27,
          19,
          40,
          24,
          42,
          0,
          21,
          32,
          13,
          97,
          7,
          0,
          9,
          12
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "displayName=James Conner<br>week=%{x}<br>receivingYards=%{y}<extra></extra>",
         "legendgroup": "James Conner",
         "line": {
          "color": "#B6E880",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "James Conner",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg2",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg10",
          "reg11",
          "reg13",
          "reg14",
          "reg15"
         ],
         "xaxis": "x",
         "y": [
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "displayName=JuJu Smith-Schuster<br>week=%{x}<br>receivingYards=%{y}<extra></extra>",
         "legendgroup": "JuJu Smith-Schuster",
         "line": {
          "color": "#FF97FF",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "JuJu Smith-Schuster",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg10",
          "reg11",
          "reg13",
          "reg15",
          "reg16",
          "reg17",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          0,
          16,
          39,
          47,
          58,
          32,
          39,
          193,
          97,
          47,
          17,
          114,
          75,
          143,
          5
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "displayName=Terrell Watson<br>week=%{x}<br>receivingYards=%{y}<extra></extra>",
         "legendgroup": "Terrell Watson",
         "line": {
          "color": "#FECB52",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "Terrell Watson",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg2",
          "reg3",
          "reg4",
          "reg6",
          "reg7",
          "reg10",
          "reg11"
         ],
         "xaxis": "x",
         "y": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "displayName=Xavier Grimble<br>week=%{x}<br>receivingYards=%{y}<extra></extra>",
         "legendgroup": "Xavier Grimble",
         "line": {
          "color": "#636efa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "Xavier Grimble",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg3",
          "reg7",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "reg17",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          0,
          12,
          1,
          9,
          0,
          8,
          0,
          2,
          0
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "displayName=Justin Hunter<br>week=%{x}<br>receivingYards=%{y}<extra></extra>",
         "legendgroup": "Justin Hunter",
         "line": {
          "color": "#EF553B",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "Justin Hunter",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg4",
          "reg5",
          "reg8",
          "reg12",
          "reg16"
         ],
         "xaxis": "x",
         "y": [
          5,
          6,
          7,
          0,
          5
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "displayName=Fitzgerald Toussaint<br>week=%{x}<br>receivingYards=%{y}<extra></extra>",
         "legendgroup": "Fitzgerald Toussaint",
         "line": {
          "color": "#00cc96",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "Fitzgerald Toussaint",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg14",
          "reg15",
          "reg17",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          0,
          0,
          9,
          0
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "displayName=Stevan Ridley<br>week=%{x}<br>receivingYards=%{y}<extra></extra>",
         "legendgroup": "Stevan Ridley",
         "line": {
          "color": "#ab63fa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "markers+lines",
         "name": "Stevan Ridley",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "reg16",
          "reg17"
         ],
         "xaxis": "x",
         "y": [
          0,
          0
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "legend": {
         "bgcolor": "rgba(255, 255, 255, 0)",
         "bordercolor": "rgba(255, 255, 255, 0)",
         "title": {
          "text": "displayName"
         },
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Reciving yards from Pittsburgh Steelers players"
        },
        "xaxis": {
         "anchor": "y",
         "categoryarray": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg9",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "reg17",
          "reg18",
          "Wild Card Weekend",
          "Divisional Playoffs",
          "Conference Championships",
          "Super Bowl"
         ],
         "categoryorder": "array",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Weeks"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "font": {
           "size": 16
          },
          "text": "Receiving yards (Yards)"
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"379f9312-abf0-4ca9-b28e-87ebf04ffe2a\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"379f9312-abf0-4ca9-b28e-87ebf04ffe2a\")) {                    Plotly.newPlot(                        \"379f9312-abf0-4ca9-b28e-87ebf04ffe2a\",                        [{\"hovertemplate\":\"displayName=Darrius Heyward-Bey<br>week=%{x}<br>receivingYards=%{y}<extra></extra>\",\"legendgroup\":\"Darrius Heyward-Bey\",\"line\":{\"color\":\"#636efa\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"Darrius Heyward-Bey\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg3\",\"reg4\",\"reg7\",\"reg8\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg17\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[0.0,0.0,0.0,44.0,0.0,0.0,0.0,3.0,0.0,0.0,0.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"displayName=Antonio Brown<br>week=%{x}<br>receivingYards=%{y}<extra></extra>\",\"legendgroup\":\"Antonio Brown\",\"line\":{\"color\":\"#EF553B\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"Antonio Brown\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[182.0,62.0,110.0,34.0,157.0,155.0,65.0,70.0,47.0,144.0,169.0,101.0,213.0,24.0,132.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"displayName=Vance McDonald<br>week=%{x}<br>receivingYards=%{y}<extra></extra>\",\"legendgroup\":\"Vance McDonald\",\"line\":{\"color\":\"#00cc96\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"Vance McDonald\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg10\",\"reg14\",\"reg16\",\"reg17\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[0.0,0.0,0.0,0.0,26.0,37.0,16.0,52.0,52.0,5.0,112.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"displayName=Le'Veon Bell<br>week=%{x}<br>receivingYards=%{y}<extra></extra>\",\"legendgroup\":\"Le'Veon Bell\",\"line\":{\"color\":\"#ab63fa\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"Le'Veon Bell\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[15.0,4.0,37.0,42.0,46.0,12.0,58.0,5.0,32.0,57.0,88.0,106.0,77.0,48.0,28.0,88.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"displayName=Martavis Bryant<br>week=%{x}<br>receivingYards=%{y}<extra></extra>\",\"legendgroup\":\"Martavis Bryant\",\"line\":{\"color\":\"#FFA15A\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"Martavis Bryant\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg17\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[14.0,91.0,30.0,48.0,21.0,27.0,3.0,42.0,30.0,40.0,40.0,33.0,59.0,60.0,65.0,78.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"displayName=Eli Rogers<br>week=%{x}<br>receivingYards=%{y}<extra></extra>\",\"legendgroup\":\"Eli Rogers\",\"line\":{\"color\":\"#19d3f3\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"Eli Rogers\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg2\",\"reg3\",\"reg7\",\"reg8\",\"reg10\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg17\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[11.0,43.0,0.0,10.0,0.0,2.0,21.0,4.0,33.0,18.0,6.0,1.0,42.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"displayName=Jesse James<br>week=%{x}<br>receivingYards=%{y}<extra></extra>\",\"legendgroup\":\"Jesse James\",\"line\":{\"color\":\"#FF6692\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"Jesse James\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg8\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg17\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[41.0,27.0,19.0,40.0,24.0,42.0,0.0,21.0,32.0,13.0,97.0,7.0,0.0,9.0,12.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"displayName=James Conner<br>week=%{x}<br>receivingYards=%{y}<extra></extra>\",\"legendgroup\":\"James Conner\",\"line\":{\"color\":\"#B6E880\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"James Conner\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg2\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg10\",\"reg11\",\"reg13\",\"reg14\",\"reg15\"],\"xaxis\":\"x\",\"y\":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"displayName=JuJu Smith-Schuster<br>week=%{x}<br>receivingYards=%{y}<extra></extra>\",\"legendgroup\":\"JuJu Smith-Schuster\",\"line\":{\"color\":\"#FF97FF\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"JuJu Smith-Schuster\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg10\",\"reg11\",\"reg13\",\"reg15\",\"reg16\",\"reg17\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[0.0,16.0,39.0,47.0,58.0,32.0,39.0,193.0,97.0,47.0,17.0,114.0,75.0,143.0,5.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"displayName=Terrell Watson<br>week=%{x}<br>receivingYards=%{y}<extra></extra>\",\"legendgroup\":\"Terrell Watson\",\"line\":{\"color\":\"#FECB52\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"Terrell Watson\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg2\",\"reg3\",\"reg4\",\"reg6\",\"reg7\",\"reg10\",\"reg11\"],\"xaxis\":\"x\",\"y\":[0.0,0.0,0.0,0.0,0.0,0.0,0.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"displayName=Xavier Grimble<br>week=%{x}<br>receivingYards=%{y}<extra></extra>\",\"legendgroup\":\"Xavier Grimble\",\"line\":{\"color\":\"#636efa\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"Xavier Grimble\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg3\",\"reg7\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg17\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[0.0,12.0,1.0,9.0,0.0,8.0,0.0,2.0,0.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"displayName=Justin Hunter<br>week=%{x}<br>receivingYards=%{y}<extra></extra>\",\"legendgroup\":\"Justin Hunter\",\"line\":{\"color\":\"#EF553B\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"Justin Hunter\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg4\",\"reg5\",\"reg8\",\"reg12\",\"reg16\"],\"xaxis\":\"x\",\"y\":[5.0,6.0,7.0,0.0,5.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"displayName=Fitzgerald Toussaint<br>week=%{x}<br>receivingYards=%{y}<extra></extra>\",\"legendgroup\":\"Fitzgerald Toussaint\",\"line\":{\"color\":\"#00cc96\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"Fitzgerald Toussaint\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg14\",\"reg15\",\"reg17\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[0.0,0.0,9.0,0.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"displayName=Stevan Ridley<br>week=%{x}<br>receivingYards=%{y}<extra></extra>\",\"legendgroup\":\"Stevan Ridley\",\"line\":{\"color\":\"#ab63fa\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"markers+lines\",\"name\":\"Stevan Ridley\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"reg16\",\"reg17\"],\"xaxis\":\"x\",\"y\":[0.0,0.0],\"yaxis\":\"y\",\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Weeks\"},\"categoryorder\":\"array\",\"categoryarray\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg9\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg17\",\"reg18\",\"Wild Card Weekend\",\"Divisional Playoffs\",\"Conference Championships\",\"Super Bowl\"]},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Receiving yards (Yards)\",\"font\":{\"size\":16}}},\"legend\":{\"title\":{\"text\":\"displayName\"},\"tracegroupgap\":0,\"bgcolor\":\"rgba(255, 255, 255, 0)\",\"bordercolor\":\"rgba(255, 255, 255, 0)\"},\"margin\":{\"t\":60},\"title\":{\"text\":\"Reciving yards from Pittsburgh Steelers players\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('379f9312-abf0-4ca9-b28e-87ebf04ffe2a');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = px.line(dataFrame, x='week', y='receivingYards', color='displayName', category_orders={\"week\" :ordered_weeks }, markers=True)\n",
    "fig.update_layout(\n",
    "    title='Reciving yards from Pittsburgh Steelers players',\n",
    "    xaxis_title='Weeks',\n",
    "    yaxis=dict(\n",
    "        title='Receiving yards (Yards)',\n",
    "        titlefont_size=16,\n",
    "    ),\n",
    "    legend=dict(\n",
    "        bgcolor='rgba(255, 255, 255, 0)',\n",
    "        bordercolor='rgba(255, 255, 255, 0)'\n",
    "    ),\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "1df9dbf5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "legendgroup": "Jesse James",
         "marker": {
          "color": "#636efa",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Jesse James",
         "offsetgroup": "Jesse James",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "reg1",
          "reg11"
         ],
         "xaxis": "x",
         "y": [
          2,
          1
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "legendgroup": "Martavis Bryant",
         "marker": {
          "color": "#EF553B",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Martavis Bryant",
         "offsetgroup": "Martavis Bryant",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "reg2",
          "reg12",
          "reg15",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          1,
          1,
          1,
          1
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "legendgroup": "JuJu Smith-Schuster",
         "marker": {
          "color": "#00cc96",
          "pattern": {
           "shape": ""
          }
         },
         "name": "JuJu Smith-Schuster",
         "offsetgroup": "JuJu Smith-Schuster",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "reg2",
          "reg4",
          "reg7",
          "reg8",
          "reg10",
          "reg16",
          "reg17",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "legendgroup": "Antonio Brown",
         "marker": {
          "color": "#ab63fa",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Antonio Brown",
         "offsetgroup": "Antonio Brown",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "reg3",
          "reg6",
          "reg7",
          "reg11",
          "reg12",
          "reg13",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          1,
          1,
          1,
          3,
          2,
          1,
          2
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "legendgroup": "Vance McDonald",
         "marker": {
          "color": "#FFA15A",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Vance McDonald",
         "offsetgroup": "Vance McDonald",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "reg10"
         ],
         "xaxis": "x",
         "y": [
          1
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "legendgroup": "Xavier Grimble",
         "marker": {
          "color": "#19d3f3",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Xavier Grimble",
         "offsetgroup": "Xavier Grimble",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "reg12"
         ],
         "xaxis": "x",
         "y": [
          1
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "legendgroup": "Le'Veon Bell",
         "marker": {
          "color": "#FF6692",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Le'Veon Bell",
         "offsetgroup": "Le'Veon Bell",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "reg13",
          "reg14",
          "Divisional Playoffs"
         ],
         "xaxis": "x",
         "y": [
          1,
          1,
          1
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "legendgroup": "Eli Rogers",
         "marker": {
          "color": "#B6E880",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Eli Rogers",
         "offsetgroup": "Eli Rogers",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "reg15"
         ],
         "xaxis": "x",
         "y": [
          1
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "legendgroup": "Justin Hunter",
         "marker": {
          "color": "#FF97FF",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Justin Hunter",
         "offsetgroup": "Justin Hunter",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "reg16"
         ],
         "xaxis": "x",
         "y": [
          1
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "barmode": "group",
        "hovermode": "x",
        "legend": {
         "bgcolor": "rgba(255, 255, 255, 0)",
         "bordercolor": "rgba(255, 255, 255, 0)",
         "title": {
          "text": "displayName"
         },
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Bar plot du nombre de touchdowns à la passe"
        },
        "xaxis": {
         "anchor": "y",
         "categoryarray": [
          "reg1",
          "reg2",
          "reg3",
          "reg4",
          "reg5",
          "reg6",
          "reg7",
          "reg8",
          "reg9",
          "reg10",
          "reg11",
          "reg12",
          "reg13",
          "reg14",
          "reg15",
          "reg16",
          "reg17",
          "reg18",
          "Wild Card Weekend",
          "Divisional Playoffs",
          "Conference Championships",
          "Super Bowl"
         ],
         "categoryorder": "array",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Weeks"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "font": {
           "size": 16
          },
          "text": "Receiving touchdowns "
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"ddae2562-49b8-4209-8c8f-e4306479c90d\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"ddae2562-49b8-4209-8c8f-e4306479c90d\")) {                    Plotly.newPlot(                        \"ddae2562-49b8-4209-8c8f-e4306479c90d\",                        [{\"alignmentgroup\":\"True\",\"legendgroup\":\"Jesse James\",\"marker\":{\"color\":\"#636efa\",\"pattern\":{\"shape\":\"\"}},\"name\":\"Jesse James\",\"offsetgroup\":\"Jesse James\",\"orientation\":\"v\",\"showlegend\":true,\"textposition\":\"auto\",\"x\":[\"reg1\",\"reg11\"],\"xaxis\":\"x\",\"y\":[2.0,1.0],\"yaxis\":\"y\",\"type\":\"bar\"},{\"alignmentgroup\":\"True\",\"legendgroup\":\"Martavis Bryant\",\"marker\":{\"color\":\"#EF553B\",\"pattern\":{\"shape\":\"\"}},\"name\":\"Martavis Bryant\",\"offsetgroup\":\"Martavis Bryant\",\"orientation\":\"v\",\"showlegend\":true,\"textposition\":\"auto\",\"x\":[\"reg2\",\"reg12\",\"reg15\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[1.0,1.0,1.0,1.0],\"yaxis\":\"y\",\"type\":\"bar\"},{\"alignmentgroup\":\"True\",\"legendgroup\":\"JuJu Smith-Schuster\",\"marker\":{\"color\":\"#00cc96\",\"pattern\":{\"shape\":\"\"}},\"name\":\"JuJu Smith-Schuster\",\"offsetgroup\":\"JuJu Smith-Schuster\",\"orientation\":\"v\",\"showlegend\":true,\"textposition\":\"auto\",\"x\":[\"reg2\",\"reg4\",\"reg7\",\"reg8\",\"reg10\",\"reg16\",\"reg17\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],\"yaxis\":\"y\",\"type\":\"bar\"},{\"alignmentgroup\":\"True\",\"legendgroup\":\"Antonio Brown\",\"marker\":{\"color\":\"#ab63fa\",\"pattern\":{\"shape\":\"\"}},\"name\":\"Antonio Brown\",\"offsetgroup\":\"Antonio Brown\",\"orientation\":\"v\",\"showlegend\":true,\"textposition\":\"auto\",\"x\":[\"reg3\",\"reg6\",\"reg7\",\"reg11\",\"reg12\",\"reg13\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[1.0,1.0,1.0,3.0,2.0,1.0,2.0],\"yaxis\":\"y\",\"type\":\"bar\"},{\"alignmentgroup\":\"True\",\"legendgroup\":\"Vance McDonald\",\"marker\":{\"color\":\"#FFA15A\",\"pattern\":{\"shape\":\"\"}},\"name\":\"Vance McDonald\",\"offsetgroup\":\"Vance McDonald\",\"orientation\":\"v\",\"showlegend\":true,\"textposition\":\"auto\",\"x\":[\"reg10\"],\"xaxis\":\"x\",\"y\":[1.0],\"yaxis\":\"y\",\"type\":\"bar\"},{\"alignmentgroup\":\"True\",\"legendgroup\":\"Xavier Grimble\",\"marker\":{\"color\":\"#19d3f3\",\"pattern\":{\"shape\":\"\"}},\"name\":\"Xavier Grimble\",\"offsetgroup\":\"Xavier Grimble\",\"orientation\":\"v\",\"showlegend\":true,\"textposition\":\"auto\",\"x\":[\"reg12\"],\"xaxis\":\"x\",\"y\":[1.0],\"yaxis\":\"y\",\"type\":\"bar\"},{\"alignmentgroup\":\"True\",\"legendgroup\":\"Le'Veon Bell\",\"marker\":{\"color\":\"#FF6692\",\"pattern\":{\"shape\":\"\"}},\"name\":\"Le'Veon Bell\",\"offsetgroup\":\"Le'Veon Bell\",\"orientation\":\"v\",\"showlegend\":true,\"textposition\":\"auto\",\"x\":[\"reg13\",\"reg14\",\"Divisional Playoffs\"],\"xaxis\":\"x\",\"y\":[1.0,1.0,1.0],\"yaxis\":\"y\",\"type\":\"bar\"},{\"alignmentgroup\":\"True\",\"legendgroup\":\"Eli Rogers\",\"marker\":{\"color\":\"#B6E880\",\"pattern\":{\"shape\":\"\"}},\"name\":\"Eli Rogers\",\"offsetgroup\":\"Eli Rogers\",\"orientation\":\"v\",\"showlegend\":true,\"textposition\":\"auto\",\"x\":[\"reg15\"],\"xaxis\":\"x\",\"y\":[1.0],\"yaxis\":\"y\",\"type\":\"bar\"},{\"alignmentgroup\":\"True\",\"legendgroup\":\"Justin Hunter\",\"marker\":{\"color\":\"#FF97FF\",\"pattern\":{\"shape\":\"\"}},\"name\":\"Justin Hunter\",\"offsetgroup\":\"Justin Hunter\",\"orientation\":\"v\",\"showlegend\":true,\"textposition\":\"auto\",\"x\":[\"reg16\"],\"xaxis\":\"x\",\"y\":[1.0],\"yaxis\":\"y\",\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Weeks\"},\"categoryorder\":\"array\",\"categoryarray\":[\"reg1\",\"reg2\",\"reg3\",\"reg4\",\"reg5\",\"reg6\",\"reg7\",\"reg8\",\"reg9\",\"reg10\",\"reg11\",\"reg12\",\"reg13\",\"reg14\",\"reg15\",\"reg16\",\"reg17\",\"reg18\",\"Wild Card Weekend\",\"Divisional Playoffs\",\"Conference Championships\",\"Super Bowl\"]},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Receiving touchdowns \",\"font\":{\"size\":16}}},\"legend\":{\"title\":{\"text\":\"displayName\"},\"tracegroupgap\":0,\"bgcolor\":\"rgba(255, 255, 255, 0)\",\"bordercolor\":\"rgba(255, 255, 255, 0)\"},\"margin\":{\"t\":60},\"barmode\":\"group\",\"hovermode\":\"x\",\"title\":{\"text\":\"Bar plot du nombre de touchdowns \\u00e0 la passe\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('ddae2562-49b8-4209-8c8f-e4306479c90d');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = px.bar(dataFrame.query(\"receivingTouchdowns!=0\"), x=\"week\", y=\"receivingTouchdowns\",color=\"displayName\", category_orders={\"week\" :ordered_weeks })\n",
    "fig.update_layout(barmode='group', hovermode=\"x\")\n",
    "fig.update_traces( hovertemplate=None)\n",
    "fig.update_layout(\n",
    "    title='Bar plot du nombre de touchdowns à la passe',\n",
    "    xaxis_title='Weeks',\n",
    "    yaxis=dict(\n",
    "        title='Receiving touchdowns ',\n",
    "        titlefont_size=16,\n",
    "    ),\n",
    "    legend=dict(\n",
    "        bgcolor='rgba(255, 255, 255, 0)',\n",
    "        bordercolor='rgba(255, 255, 255, 0)'\n",
    "    ),\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "122813af",
   "metadata": {},
   "source": [
    "## Ceci est la fin de ce jupyter notebook pour le scraping des données, l'alimentation de la base pymongo DB et l'affichage de quelques graphiques utilisés dans le dashboard du projet."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  },
  "vscode": {
   "interpreter": {
    "hash": "8e7af5626c7e654314ce176c299bd4d61dd6a36e86a9674195997ac339225326"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
