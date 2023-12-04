import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the provided CSV file
file_path = 'data/updated_wind_data.csv'
wind_data = pd.read_csv(file_path)

# Display the first few rows of the dataset
wind_data.head()

# Dropping columns that are deprecated or not relevant for correlation analysis
wind_data_cleaned = wind_data.drop(columns=['density - DEPRECATED', 'power - DEPRECATED', 'Timestamp'])

# Computing the correlation matrix
correlation_matrix = wind_data_cleaned.corr()

# Focusing on the correlation of different factors with wind power generation
correlation_with_p_wind = correlation_matrix['p_wind'].sort_values(ascending=False)

# Plotting the correlations
plt.figure(figsize=(16, 12))
sns.barplot(y=correlation_with_p_wind.index, x=correlation_with_p_wind.values)
plt.title('Correlation of Various Factors with Wind Power Generation')
plt.xlabel('Correlation Coefficient')
plt.ylabel('Factors')
plt.tight_layout()
plt.savefig('plots/correlation_anaysis.png')
plt.show()
