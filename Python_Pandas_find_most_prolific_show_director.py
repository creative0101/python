
# Import netflix data

import pandas as pd

file_name = "https://raw.githubusercontent.com/practiceprobs/datasets/main/netflix-titles/netflix-titles.csv"
df = pd.read_csv(file_name)
df.head()

df

# TASK = Find the most profilic TV show director on Netflix and her/his shows

# Get a new df that only includes TV Shows

yearly = df.loc[df['type']=='TV Show']

yearly.head(10)

# Find the director with the most shows and their titles

yearly[['director', 'title']].value_counts('director').head(1)

yearly.loc[df['director'] == 'Alastair Fothergill']

