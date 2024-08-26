# global_temp_trends.py
# Visualization of global temperature trends using Berkeley Earth data.

import matplotlib.pyplot as plt
import pandas as pd

# Load the data
# Dataset URL: http://berkeleyearth.org/data/
# The following URL points to a dataset that is free and open-source.
url = "./Complete_TAVG_complete.txt"

# Load the dataset into a DataFrame
# Prompt: Consider using a different dataset or a subset of this data.
df = pd.read_csv(url, delim_whitespace=True, comment='%', header=None)

# Set column names
# Prompt: Suggest better column names or include only specific columns.
df.columns = ["Year", "Month", "Monthly_Anomaly_C", "Annual_Mean", "Five_Year_Mean", "Ten_Year_Mean", "Twenty_Year_Mean"]

# Filter the data to include only annual mean temperatures
# Prompt: Add a feature to filter by different means or time periods.
df = df[df["Year"] >= 1880]  # Considering data from 1880 onwards

# Plotting
plt.figure(figsize=(14, 7))
plt.plot(df["Year"], df["Annual_Mean"], label='Annual Mean Temperature', color='blue')
plt.plot(df["Year"], df["Five_Year_Mean"], label='Five-Year Mean Temperature', color='orange')

# Add plot details
plt.title('Global Temperature Trends (1880 - Present)')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (°C)')
plt.legend()

# Prompt: Consider adding interactivity with Plotly or enhancing the visualization with Seaborn.
plt.show()

# Prompt: Suggest adding a feature to save the plot to a file or to a different format.
