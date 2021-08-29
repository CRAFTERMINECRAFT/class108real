import csv
import plotly.figure_factory as pf
import pandas as p


df = p.read_csv("my.csv")
fig = pf.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"],show_hist = False)
fig.show()
print(df["Weight(Pounds)"].mean())