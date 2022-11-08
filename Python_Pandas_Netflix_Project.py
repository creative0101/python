
# Import netflix data

import pandas as pd

file_name = "https://raw.githubusercontent.com/practiceprobs/datasets/main/netflix-titles/netflix-titles.csv"
df = pd.read_csv(file_name)
df.head()

df

# TASK 1 = Find the most profilic TV show director on Netflix and her/his shows

# Get a new df that only includes TV Shows

yearly = df.loc[df['type']=='TV Show']

yearly.head(10)

# Find the director with the most shows and their titles

yearly[['director', 'title']].value_counts('director').head(1)

yearly.loc[df['director'] == 'Alastair Fothergill']

"""Result 1: Alastair Fothergill is the most profilific director on Netflix. """

# TASK 2: Which year has the most titles?

df.info()

import seaborn as sns
df['release_year']\
  .plot(kind='hist', bins=100, figsize =(20,15))

"""Result 2: Netflix library is mainly consisting of recently released titles."""

# TASK 3: Extract the 5 most common categories.

# split listed in column

df.info()

# count the values for each category with using split

# Split into categories

categories = df['listed_in'].str.split(',', expand = True)

categories

# transform the df, so that it can be counted with value counts

# approach 1

long_list = categories[0].append(categories[1]).append(categories[2])

long_list

long_list.value_counts().nlargest(5)

# approach 2

long_list2 = categories.stack().reset_index()

long_list2

long_list2[0].value_counts().head(5)

"""Result 3: The biggest categories on Netflix are International Movies, Dramas, Comedies, Action & Adventure, and finally Documentaries."""