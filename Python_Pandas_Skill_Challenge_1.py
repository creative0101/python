#1 Select 10 days at random from tech_df2, containing Apple price data.

# First new slice of the DF is needed
tech_df2 = tech.loc[slice('2015-06-13', '2016-08-17'), :]

#Then .xs() for sampling from the multi index
tech_df2.xs('AAPL', level=1, drop_level=False).sample(10)