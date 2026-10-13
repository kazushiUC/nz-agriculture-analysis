import pandas as pd

df = pd.read_excel(
        "data/raw/37077-SOPI-June-2026-web-data-release.xlsx",
        sheet_name="Total primary industry exports"
)

print(df.head())