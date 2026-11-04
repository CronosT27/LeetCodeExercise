#Libraries that I'm going to use
import pandas as pd


#Problem
'''Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

The scores should be ranked from the highest to the lowest.
If there is a tie between two scores, both should have the same ranking.
After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
Return the result table ordered by score in descending order.

The result format is in the following example.'''


#Solution 

def raked_table(scores: pd.DataFrame) -> pd.DataFrame:
    #Create the rank column, and rank score.
    scores['rank']= scores.score.rank(method= 'dense', ascending= False)
    # Return only the score and rank column sorted.
    return scores[['score', 'rank']].sort_values('score', ascending=False)