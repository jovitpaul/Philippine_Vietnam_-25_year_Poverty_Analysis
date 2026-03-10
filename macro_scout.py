import wbgapi as wb
import pandas as pd
import matplotlib.pyplot as plt

# These are the codes the World Bank uses for Industry, Services, and Poverty
indicators = {
    'NV.IND.MANF.ZS': 'Manufacturing',
    'NV.SRV.TOTL.ZS': 'Services',
    'SI.POV.NAHC': 'Poverty'
}

print("Connecting to World Bank... please wait.")

# Pull data for Philippines (PHL) and Vietnam (VNM) 
# We use a wide range to get as much data as possible
df = wb.data.DataFrame(indicators.keys(), ['PHL', 'VNM'], time=range(2000, 2025), numericTimeKeys=True)

# This reorganizes the data so 'Manufacturing', 'Services', and 'Poverty' are columns
df = df.T.rename(columns=indicators)

# Let's see the first 5 rows in the console
print("Data successfully retrieved!")
print(df.head())

# Save a copy to your folder as a CSV so you can open it in Excel too!
df.to_csv('ph_vn_data.csv')
print("A copy has been saved as ph_vn_data.csv in your folder.")

# --- FIXED VISUALIZATION SECTION ---

# Instead of 'xs', we use simple column filtering
# Since the columns are 'PHL' and 'VNM', we grab Manufacturing from there
ph_mfg = df[('PHL', 'Manufacturing')]
vn_mfg = df[('VNM', 'Manufacturing')]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(ph_mfg.index, ph_mfg.values, label='PH Manufacturing (% of GDP)', color='blue', marker='o')
plt.plot(vn_mfg.index, vn_mfg.values, label='Vietnam Manufacturing (% of GDP)', color='red', marker='s')

# Add labels and title
plt.title('The Industrialization Gap: Philippines vs. Vietnam (2000-2024)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Manufacturing Value Added (% of GDP)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Save the graph
plt.savefig('industrialization_gap.png')
print("Graph saved successfully!")

# Show the graph
plt.show()
