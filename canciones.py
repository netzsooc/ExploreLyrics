#%%
import os
import requests
import pandas as pd

#%%
df = pd.read_csv("lyrics/billboard_lyrics_1964-2015.csv", encoding="cp1252")

#%%
con_letras = df[df["Lyrics"].notnull()]

#%%
