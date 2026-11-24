import pandas as pd

workbook = pd.ExcelFile("data/raw/veh0142.ods", engine="odf")

df = pd.read_excel(workbook, sheet_name="VEH0142", header=4)
bev_df = df[df["Fuel"] == "Battery electric"].copy()
bev_cars_df = bev_df[bev_df["BodyType"] == "Cars"].copy()
bev_cars_df = bev_cars_df[bev_cars_df["Keepership"] == "Total"].copy()
bev_cars_df["ONS Geography"] = bev_cars_df["ONS Geography"].str.strip()

cities = ["London", "Birmingham", "Leeds", "Glasgow City", "Sheffield"]
city_df = bev_cars_df[bev_cars_df["ONS Geography"].isin(cities)].copy()

print(city_df.shape)
print(city_df["ONS Geography"].value_counts())
print(city_df[["ONS Geography", "2026 Q2"]].to_string(index=False))

