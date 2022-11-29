
import pandas as pd

data_url = 'https://en.wikipedia.org/wiki/List_of_UFC_events'

ufc_events = pd.read_html(data_url)

# Get the table with the events

event_list = ufc_events[1]

#TASK 1: Find the 10 most frequent headliners

event_list.head()

# split after the ':'

event_headliners = event_list['Event'].str.split(':', expand=True)

event_headliners[1]

headliners_split = event_headliners[1].str.split(' vs. ', expand=True)

headliners_split.head()

# Stack the dataframes together

stacked_list = headliners_split[0].append(headliners_split[1])

stacked_list.dropna().value_counts().head(10)

#Task 2: Isolate events outside of the US and display the amount of events per country

non_us = event_list[~event_list['Location'].str.endswith('U.S.')]

non_us

#split countries from non_us as an own column

non_us[['city', 'country', 'entity']] = non_us['Location'].str.split(',', expand=True)

non_us.head(30)

#remove entities associated with the US and Canada to clean the data

# non_us_clean = non_us.loc[~((non_us['entity'] == 'U.S') | (non_us['entity'] == 'Canada')), :]

non_us_clean = non_us.loc[((non_us['entity'] != 'U.S') | (non_us['entity'] == 'Canada')), :]

non_us_clean.head(30)

# Count the number of events per country

non_us_clean.value_counts(subset='country')
