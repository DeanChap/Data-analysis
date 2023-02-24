import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

data = pd.read_csv("Virat_Kohli.csv")
#print(data.head())

#print(data.isnull().sum())

# Total Runs Between 18-Aug-08 - 22-Jan-17
total_runs = data["Runs"].sum()
# Average Runs Between 18-Aug-08 - 22-Jan-17
avg_runs = data["Runs"].mean()

matches = data.index
figure = px.line(data, x=matches, y="Runs", 
                 title='Runs Scored by Virat Kohli Between 18-Aug-08 - 22-Jan-17')
#figure.show()

