#1 Starting with the games dataset, create a pie plot breaking down the total game sales (Global_Sales) by gaming console (Platform).
games.groupby('Platform').Global_Sales.sum().plot(kind='pie')

#2 From the games datase, create a similar DF that contains total Global_Sales across Platforms from all realeases in the sports genre. Set Name as the index of this new DF and assign it to the variable sports_games.
sport_games = games.loc[games.Genre=='Sports', ['Name', 'Global_Sales']]

sport_games.nlargest(20, 'Global_Sales').plot(kind='bar', figsize=(14, 14))

#3 Using the sport_games DF, create a bar chart of the top 20 best selling games. 
sport_games.nlargest(20, 'Global_Sales').plot(kind='bar', figsize=(14, 14))