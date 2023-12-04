import pandas as pd
import matplotlib.pyplot as plt

# File paths for the uploaded data
file_paths = {
    "rolling_hills": "data/WIND-Toolkit_lat35.13_lon-117.99_2014_5min_rolling_hills_southern_ca.csv",
    "mountainous": "data/WIND-Toolkit_lat43.68_lon-114.36_2014_5min_mountainous_southern_id.csv",
    "flat_lands": "data/WIND-Toolkit_lat44.32_lon-74.13_2014_5min_flat_lands_northern_ny.csv"
}

# Load the data from the three files, skipping the first row which contains metadata
rolling_hills_data = pd.read_csv(file_paths["rolling_hills"], skiprows=1)
mountainous_data = pd.read_csv(file_paths["mountainous"], skiprows=1)
flat_lands_data = pd.read_csv(file_paths["flat_lands"], skiprows=1)

# Displaying the first few rows of each dataset to understand their structure
rolling_hills_data.head(), mountainous_data.head(), flat_lands_data.head()

# Function to convert the date and time columns into a datetime object
def create_datetime(df):
    df["Datetime"] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour', 'Minute']])
    return df.set_index("Datetime")

# Convert the date and time into a datetime object for each dataset
rolling_hills_data = create_datetime(rolling_hills_data)
mountainous_data = create_datetime(mountainous_data)
flat_lands_data = create_datetime(flat_lands_data)

# Resampling data to get 3-day averages for the entire year of 2020
rolling_hills_3day_avg = rolling_hills_data.resample('3D').mean()
mountainous_3day_avg = mountainous_data.resample('3D').mean()
flat_lands_3day_avg = flat_lands_data.resample('3D').mean()

# Plotting the 3-day average wind speed for the entire year across the three terrains
plt.figure(figsize=(15, 6))

plt.plot(rolling_hills_3day_avg.index, rolling_hills_3day_avg['wind speed at 100m (m/s)'], label='Rolling Hills (CA)', color='green')
plt.plot(mountainous_3day_avg.index, mountainous_3day_avg['wind speed at 100m (m/s)'], label='Mountainous (ID)', color='blue')
plt.plot(flat_lands_3day_avg.index, flat_lands_3day_avg['wind speed at 100m (m/s)'], label='Flat Lands (NY)', color='red')

plt.title('3-Day Average Wind Speed at 100m Over the Year 2020 across Different Terrains')
plt.xlabel('Date')
plt.ylabel('Average Wind Speed at 100m (m/s)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('plots/terrain_comparison_3_day_averages_2020.png')
plt.show()
