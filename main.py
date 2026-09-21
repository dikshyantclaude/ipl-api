import pandas as pd  
import numpy as np 
from fastapi import FastAPI


app = FastAPI()


ipl = pd.read_csv("IPL_Matches_2008_2022.csv")

@app.get("/")
def root():
    return {'Message':"IPL Data Loaded Successful"}

@app.get("/ipl/teams")
def return_unique_teams() -> dict:
    unique_teams = ipl['Team1'].value_counts() + ipl['Team2'].value_counts()
    return unique_teams.to_dict()
    
    


print( ipl['Team1'].value_counts() + ipl['Team2'].value_counts())
