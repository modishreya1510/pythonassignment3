import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Country': ['USA', 'India', 'Brazil', 'Russia', 'UK'],
    'Total Cases': [34000000, 31000000, 19000000, 6000000, 5000000],
    'Total Deaths': [609000, 410000, 530000, 150000, 130000],
    'Total Recovered': [28000000, 30000000, 17000000, 5800000, 4800000]
}
df = pd.DataFrame(data)

# Plot Total Cases
plt.figure(figsize=(10, 6))
plt.bar(df['Country'], df['Total Cases'], color='skyblue')
plt.title('COVID-19 Total Cases by Country')
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.grid(axis='y')
plt.tight_layout()
plt.show()