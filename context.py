import pandas as pd

df = pd.read_csv("big_five_context.txt", sep=":", usecols=[0,1,2], header=0)

print(df.head())
