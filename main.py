import pandas as pd
df = pd.read_csv('misc.csv')

df.to_html('name_misc.html')
