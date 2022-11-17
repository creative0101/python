
import pandas as pd

file_name = "https://raw.githubusercontent.com/practiceprobs/datasets/main/netflix-titles/netflix-titles.csv"
df = pd.read_csv(file_name)
df.head()

# TASKS: Find the average and median runtimes for movies and compare them. Evaluate the distribution and the skewedness.

# Isolate movies

movies = df[df['type'] == 'Movie']

# remove the 'Season(s)' and convert the data type

duration = movies['duration'].str.replace('min', '').str.replace(' ', '')

duration.head()

# label infinite value(s) as NaNs and remove them

#dropna because they are irrelevant and can not be used for functions

import numpy as np

duration2 = duration.replace([np.inf, -np.inf], 0).fillna(0)

# convert values to int

duration3 = duration2.astype('int')

duration3.describe()

duration3.mean().round(2)

duration3.median()

duration3.std().round(2)

duration3.skew()

"""Conclusion: The duration distribution is fairly symmetrical. And the measurements not too far apart. """
