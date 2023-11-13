import pandas as pd
df = pd.read_excel("_dane/danecp.xlsx")

editIndex = df.index[df['Zlecenie'] == 2].tolist()[0]
print(df)
df.loc[editIndex, ["Gotowe", "Opis", "Dlanas", "Nrtel"]] = ["test", "dasdasdLKITEST", "NAJWIEKSZasdaYTEST", "JEasdasdaWIEKSZY"]

print(df)
df.to_excel("_dane/danecp.xlsx", sheet_name="Sheet1", index=False)