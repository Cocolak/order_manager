import pandas as pd
df = pd.read_excel("_dane/dane.xlsx")
data = df.loc[df["Zlecenie"] == 2].reset_index()
print(data["Gotowe"])