#===== load the processed dataset and calculate results =====

import pandas as pd

#===== load the DataFrame =====
df = pd.read_csv(
    "data/processed/primary_industry_exports_2016_2025.csv"
)

print(df.head())

#===== get the 2016 value and the 2025 value =====
print(df.year.value_counts())

df_growth = df[df["year"].isin([2016, 2025])]

print(df_growth)
print(df_growth.shape)
print(df.dtypes)

#===== reshape the DataFrame =====
df_growth = df_growth.pivot(
    index=["sector","measure","Units"],
    columns="year",
    values="export_value"
)

print(df_growth)