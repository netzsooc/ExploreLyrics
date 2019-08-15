#%%
import os
import requests
import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/walkerkq/musiclyrics/master/billboard_lyrics_1964-2015.csv", encoding="cp1252")
con_letra = data[data["Lyrics"].notnull()]
con_letra["Length"] = con_letra.Lyrics.apply(len)

# Determinar estadísticas
longitud = con_letra.Length
num_dev = 1
mean = longitud.mean()
std = longitud.std()
theta = int(mean - (num_dev * std))
con_letra = con_letra[con_letra["Length"] > theta]
#%%
def tokenize(cadena):
    tokens = cadena.split()
    retoks = []
    for token in tokens:
        retok = ""
        for char in token:
            if char.isalpha():
                retok += char
            else:
                if retok:
                    retoks.append(retok)
                    retok = ""
                retoks.append(char)
    return retoks