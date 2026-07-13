import pandas as pd
df = pd.read_csv('NoFth.csv')

df.to_html('name_misc.html')
