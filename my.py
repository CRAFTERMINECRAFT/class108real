import csv
import plotly.figure_factory as pf
import pandas as p


df = p.read_csv("my.csv")
fig = pf.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist = False)
fig.show()