import pandas as pd
import matplotlib.pyplot as plt

# Re-loading the data as the code execution state was reset
file_paths = [
    "data/WIND-Toolkit_lat35.13_lon-117.99_2014_5min_rolling_hills_southern_ca.csv",
    "data/WIND-Toolkit_lat43.68_lon-114.36_2014_5min_mountainous_southern_id.csv",
    "data/WIND-Toolkit_lat44.32_lon-74.13_2014_5min_flat_lands_northern_ny.csv"
]

# Read the CSV files, skipping the first row which contains metadata
rolling_hills_data = pd.read_csv(file_paths[0], skiprows=1)
mountainous_data = pd.read_csv(file_paths[1], skiprows=1)
flat_lands_data = pd.read_csv(file_paths[2], skiprows=1)

# Function to convert the date and time columns into a datetime object
def create_datetime(df):
    df["Datetime"] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour', 'Minute']])
    return df.set_index("Datetime")

# Convert the date and time into a datetime object for each dataset
rolling_hills_data = create_datetime(rolling_hills_data)
mountainous_data = create_datetime(mountainous_data)
flat_lands_data = create_datetime(flat_lands_data)

# Selecting a one day period for detailed analysis
selected_day = "2020-01-01"

rolling_hills_day = rolling_hills_data.loc[selected_day]
mountainous_day = mountainous_data.loc[selected_day]
flat_lands_day = flat_lands_data.loc[selected_day]

# Plotting the wind speed for the selected day across the three terrains
plt.figure(figsize=(15, 6))

plt.plot(rolling_hills_day.index, rolling_hills_day['wind speed at 100m (m/s)'], label='Rolling Hills (CA)', color='green')
plt.plot(mountainous_day.index, mountainous_day['wind speed at 100m (m/s)'], label='Mountainous (ID)', color='blue')
plt.plot(flat_lands_day.index, flat_lands_day['wind speed at 100m (m/s)'], label='Flat Lands (NY)', color='red')

plt.title('Wind Speed at 100m over January 1st 2020 across Different Terrains')
plt.xlabel('Time')
plt.ylabel('Wind Speed at 100m (m/s)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('plots/terrain_comparison_1_day.png')
plt.show()
