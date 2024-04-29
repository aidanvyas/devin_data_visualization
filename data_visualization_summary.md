# Data Visualization Summary

## Task Overview
The task involved developing a data visualization use case. The chosen dataset was the "Airline Safety" dataset from FiveThirtyEight, which includes information on airline incidents, fatal accidents, and fatalities for two time periods: 1985-1999 and 2000-2014.

## Dataset
- **Source**: FiveThirtyEight GitHub repository
- **File Name**: `airline-safety.csv`
- **Contents**: Data on airline incidents, fatal accidents, and fatalities for the years 1985-1999 and 2000-2014.

## Visualization Development
### Libraries Used
- pandas: For data manipulation and analysis.
- matplotlib: For creating static, interactive, and animated visualizations in Python.

### Visualization Type
A bar chart was chosen as the most effective way to compare the number of incidents and fatal accidents across different airlines and time periods.

### Python Script
The script `visualize_airline_safety.py` was written to process the dataset and generate the visualization. The script:
- Reads the dataset using pandas.
- Groups the data by airline and aggregates the incidents and fatal accidents for both time periods.
- Generates a bar chart comparing these figures.
- Saves the chart as `airline_safety_comparison.png`.

### Challenges
The initial attempt to visualize the data included a `plt.show()` command, which caused the process to hang since the script was running in a non-interactive environment. The command was removed, and the script was rerun to successfully save the visualization as an image file.

## Conclusion
The bar chart visualization was created and sent to the user for feedback. It effectively displays the safety record of each airline, allowing for easy comparison and analysis of the data across the two time periods.

## Additional Notes
- The visualization process highlighted the importance of selecting the right type of chart to convey the data story effectively.
- Future enhancements could include interactive elements to the visualization for a more engaging user experience.
