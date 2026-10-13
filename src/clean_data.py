import pandas as pd

#===== loading the DataFrame =====
df = pd.read_excel(
    "data/raw/37077-SOPI-June-2026-web-data-release.xlsx"
)

print(df.shape)