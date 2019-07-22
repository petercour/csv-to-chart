import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

movie = pd.read_csv("IMDB-Movie-Data.csv")

movie["Rating"].mean()
movie["Rating"].plot(kind="hist", figsize=(20, 8))

plt.figure(figsize=(20, 8), dpi=80)
plt.hist(movie["Rating"], 20)
plt.xticks(np.linspace(movie["Rating"].min(), movie["Rating"].max(), 21))
plt.grid(linestyle="--", alpha=0.5)
plt.show()
