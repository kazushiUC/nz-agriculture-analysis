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
print(df.isna().sum())

print("=="*25)
print("=="*25)


#===== Reshaping the original DataFrame =====
# print("=="*25)
# print("Reshaping the original DataFrame")
# print("=="*25)

df_clean = df.rename(
    columns={'Unnamed: 0': 'sector', 
             'Year to 30 June': 'measure'}
)      

df_clean = df_clean.drop(index=0)

# print(df_clean.head())
# print(df_clean.columns)
# print(df_clean.isna().sum())

# print("=="*25)
# print("=="*25)


#===== Remove blank row =====
# print("=="*25)
# print("Remove blank row")
# print("=="*25)

df_clean = df_clean.drop(
    index=[9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
)

# print(df_clean.isna().sum())
# print(df_clean.columns)
# print(df_clean.head(8))

# print("=="*25)
# print("=="*25)


#===== Select 2006-2025 + relevent descriptive columns =====
print("=="*25)
print("Select 2006-2025 + relevent descriptive columns")
print("=="*25)

df_clean = df_clean.drop(
    columns=[2004, 2005, '2026F', '2027F', '2028F', '2029F', '2030F']
)

print(df_clean.columns)
print(df_clean.head(8))