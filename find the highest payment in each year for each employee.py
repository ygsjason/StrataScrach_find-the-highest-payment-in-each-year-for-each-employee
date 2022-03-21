# Import your libraries
import pandas as pd

# Start writing code
df = sf_public_salaries

df1 = df.pivot(index = 'employeename', columns = 'year', values = 'totalpaybenefits').reset_index()

df2 = df.pivot_table(index = 'employeename', columns = 'year', values = 'totalpaybenefits', aggfunc = 'max').reset_index()

df3 = pd.pivot_table(data = sf_public_salaries, columns = ['year'], 
index = 'employeename', values = 'totalpay', aggfunc = 
'max', fill_value = 0).reset_index()
