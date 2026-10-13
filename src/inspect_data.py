import pandas as pd

#===== loading the DataFrame =====
df = pd.read_excel(
        "data/raw/37077-SOPI-June-2026-web-data-release.xlsx",
        sheet_name="Total primary industry exports"
)

#===== inspecting the structure =====
# print("=="*25)
# print("Inspecting the structure")
# print("=="*25)
# print(df.head(10))
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print("=="*25)
# print("=="*25)

#===== inspecting data-quality =====
print(df.isna().sum())