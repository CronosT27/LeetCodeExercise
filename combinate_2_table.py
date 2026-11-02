import pandas as pd

def merge_table(person:pd.DataFrame, address:pd.DataFrame) -> pd.DataFrame:

#Using how and on, to select the user by id and left the user that don't have address information.
    table= pd.merge(person, address, on='personId', how='left')

    #Here I return the specifics columns.
    return table[['firstName', 'lastName', 'city', 'state']]



person= pd.DataFrame({
    'personId': [1,2],
    'lastName': ['Wang', 'Alice'],
    'firstName': ['Allen', 'Bod']
})

address= pd.DataFrame({
    'addressId': [1,2],
    'personId': [2,3],
    'city': ['New York City', 'Leetcode'],
    'state': ['New York', 'California']
})


print(merge_table(person, address))