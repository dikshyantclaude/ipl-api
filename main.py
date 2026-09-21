import pandas as pd  
import numpy as np 
from fastapi import FastAPI


app = FastAPI()


ipl = pd.read_csv("IPL_Matches_2008_2022.csv")

@app.get("/")
def root():
    return {'Message':"IPL Data Loaded Successful"}

@app.get("/ipl/teams")
def return_unique_teams():
    unique_teams = list(set(ipl['Team1']))
    return {'Teams':unique_teams}  

@app.get("/ipl/faceoff/{team1_name}/{team2_name}")
def team_1_vs_team_2(team1_name:str, team2_name:str):
    matches_played = ipl[((ipl['Team1'] == team1_name) & (ipl['Team2'] == team2_name) ) | (ipl['Team1']==team2_name) & (ipl['Team2'] == team1_name) ]
    matches_count = matches_played.shape[0]
    if matches_count == 0:
        return {'Message':'No matches played between these two teams'}
    matches_won_by_first = matches_played[matches_played['WinningTeam'] == team1_name]
    matches_won_by_second = matches_played[matches_played['WinningTeam'] == team2_name]
    first_team_matches_won = matches_won_by_first.shape[0]
    second_team_matches_won = matches_won_by_second.shape[0]
    return {'Matches Played':matches_count, team1_name+' Wins':first_team_matches_won, team2_name+' Wins':second_team_matches_won}
    
