import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset directly by specifying the relative or absolute path.
# Make sure the CSV file "dalys-rate-from-all-causes.csv" is in the same folder as this script,
# or provide the full path (e.g., "C:/path/to/dalys-rate-from-all-causes.csv").
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Preview the first few rows of the dataset
print(dalys_data.head())
# Show general information about columns, data types, and non-null counts
dalys_data.info()
# Display summary statistics for numerical columns
print(dalys_data.describe())

# Show the third and fourth columns (Year, DALYs) for the first 10 rows (0–9)
print("\nYear and DALYs for the first 10 rows:")
print(dalys_data.iloc[0:10, [2, 3]])

# Find DALYs recorded in Afghanistan in 1992
afghan_1992 = dalys_data.loc[
    (dalys_data["Entity"] == "Afghanistan") & (dalys_data["Year"] == 1992),
    "DALYs"
].values[0]
print(f"\nDALYs recorded in Afghanistan in 1992: {afghan_1992}")

# Boolean indexing – show DALYs for all countries in 1990
print("\nDALYs for all countries in 1990:")
print(dalys_data.loc[dalys_data["Year"] == 1990, ["Entity", "DALYs"]])

# Find max and min DALYs for China
china = dalys_data.loc[dalys_data["Entity"] == "China", ["Year", "DALYs"]]
china_max = china.loc[china["DALYs"].idxmax()]
china_min = china.loc[china["DALYs"].idxmin()]
print(f"\nMax DALYs in China: {china_max['DALYs']} in {int(china_max['Year'])}")
print(f"Min DALYs in China: {china_min['DALYs']} in {int(china_min['Year'])}")

# Plot DALYs in China over time
plt.plot(china.Year, china.DALYs, 'g--o', label="China")
plt.xticks(china.Year, rotation=-90)
plt.title("DALYs in China over Time")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.tight_layout()
plt.savefig("china_dalys_trend.png")
plt.close()

# Custom question – China vs UK DALYs difference (starts at line 50)
# Extract data for the UK
uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["Year", "DALYs"]]

# Plot comparison between China and the UK
plt.plot(china.Year, china.DALYs, 'r-o', label="China")
plt.plot(uk.Year, uk.DALYs, 'b--s', label="United Kingdom")
plt.title("DALYs over Time: China vs United Kingdom")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(china.Year, rotation=-90)
plt.legend()
plt.tight_layout()
plt.savefig("china_uk_dalys_comparison.png")
plt.close()

# Calculate and print difference (China - UK) for each year
china_values = np.array(china["DALYs"])
uk_values = np.array(uk["DALYs"])
diff = china_values - uk_values
print("\nDifference in DALYs (China - UK) by year:")
print(diff)
