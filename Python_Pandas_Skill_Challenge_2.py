#2 What game genre, in what year, for what platform sold the most in Europe?

games.groupby(['Genre', 'Year', 'Platform'])\
    .sum()\
    .sort_values(by='EU_Sales', ascending=False)