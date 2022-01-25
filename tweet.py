import random
import os
import time
import pandas as pd, numpy as np

movies_pd = pd.read_csv("movies_metadata.csv")

movies = list(movies_pd["original_title"])

tiempos = range(180, 360)
frases = ["Disfrutaría la película "," Maratón de ","Volvería a ver ","Reviviría ","Otra oportunidad para ", " " , "Vería "]
while(True):

    print('#ConcursoProyector ' + random.choice(frases) + random.choice(movies))
    tiempo = random.choice(tiempos)
    print(tiempo)
    time.sleep(tiempo)
