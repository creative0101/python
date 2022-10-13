# Create a pivot table of high school students from the Queens borough containing the SAT section scores, i.e. SAT Section, Scores as columns and school name as index. 
# Sort the table descending by math section scores.

sat[sat.Borough == "Queens"].pivot_table(index='School Name', values='Score', columns='SAT Section')\
                            .sort_values(by='Math', ascending=False)

