import pandas as pd
import plotly.express as pe

df = pd.read_csv("covid-chart.csv")

fig = pe.line(df,x="date",y="cases",color="country")
fig.show()