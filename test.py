import pandas as pd
df = pd.read_excel("_dane/dane.xlsx")
df = df.sort_values(["Zlecenie"], ascending=[False])
print(df["Zlecenie"].tolist())