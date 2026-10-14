import pandas as pd

#===== loading the DataFrame =====
df = pd.read_excel(
    "data/raw/37077-SOPI-June-2026-web-data-release.xlsx", sheet_name="Total primary industry exports", header=2
)


#===== inspecting the original DataFrame =====
print("=="*25)
print("inspecting the original DataFrame")
print("=="*25)

print(df.head())
print(df.columns)

print("=="*25)
print("=="*25)


#===== Reshaping the original DataFrame =====
print("=="*25)
print("Reshaping the original DataFrame")
print("=="*25)

df_clean = df.rename(
    columns={'Unnamed: 0': 'sector', 
             'Year to 30 June': 'measure'}
)      

df_clean = df_clean.drop(index=0)

print(df_clean.head())
print(df_clean.columns)

print("=="*25)
print("=="*25)