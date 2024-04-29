import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('airline-safety.csv')

# Summarize incidents and fatal accidents for each airline
summary = df.groupby('airline')[['incidents_85_99', 'fatal_accidents_85_99', 'incidents_00_14', 'fatal_accidents_00_14']].sum()

# Plot
summary.plot(kind='bar', figsize=(14, 7))
plt.title('Airline Safety: Incidents and Fatal Accidents 1985-1999 vs 2000-2014')
plt.ylabel('Number of Incidents/Accidents')
plt.xlabel('Airline')
plt.tight_layout()
plt.savefig('airline_safety_comparison.png')
