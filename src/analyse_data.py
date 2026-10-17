#===== load the processed dataset and calculate results =====

import pandas as pd

#===== load the DataFrame =====
df = pd.read_csv(
    "data/processed/primary_industry_exports_2016_2025.csv"
)

# print(df.head())

#===== get the 2016 value and the 2025 value =====
# print("=="*25)
# print("get the 2016 value and the 2025 value")
# print("=="*25)
# print(df.year.value_counts())

df_growth = df[df["year"].isin([2016, 2025])]

# print(df_growth.head(5))
# print(df_growth.tail(5))
# print(df_growth.shape)
# print(df.dtypes)
# print("=="*25)
# print("=="*25)

#===== reshape the DataFrame =====
# print("=="*25)
# print("reshape the DataFrame")
# print("=="*25)
df_growth = df_growth.pivot(
    index=["sector","measure","Units"],
    columns="year",
    values="export_value"
)

# print(df_growth.head())
# print("=="*25)
# print("=="*25)


#===== create "percentage_growth" column =====
print("=="*25)
print("create 'percentage_growth' column")
print("=="*25)

df_growth["percentage_growth"] = (
    (df_growth[2025] - df_growth[2016])
    / df_growth[2016]
    * 100
)

df_primary = df_growth.loc[
    ["Primary industries"]
]

df_growth = df_growth.drop(
    index="Primary industries"
)

print(df_growth.shape)

df_growth = df_growth.sort_values(
    by="percentage_growth",
    ascending=False
)

print(df_growth.head(7))

print("=="*25)
print("=="*25)


#===== Save the DataFrame as "xyz.csv" form =====
df_growth = df_growth.reset_index()
print(df_growth)

df_growth.to_csv(
    "output/sector_growth_2016_2025.csv",
    index=False
)

df_growth = df_primary.reset_index()

df_primary.to_csv(
    "output/primary_growth_2016_2025.csv",
    index=False
)