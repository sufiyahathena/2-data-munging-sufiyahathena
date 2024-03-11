# Raw Data Munging

# Implemented Data Cleaning and Analysis for Temperature Anomalies

In `munge.py`, I've addressed several data integrity issues from the raw NASA temperature anomalies data set:
- Removed extraneous header and footer notes.
- Eliminated duplicate column headers and blank lines.
- Handled missing data marked with "***" by replacing with "NA".
- Converted temperature anomalies from 0.01 degrees Celsius to Fahrenheit with precision to one decimal place.
- Normalized data spacing for a cleaner, CSV-formatted `clean_data.csv` output in the `data` directory. 

For `analyze.py`, developed a program to calculate and output the average temperature anomaly in Fahrenheit for each decade since 1880, using Python's `csv` module for data handling. The analysis covers each decade up to the present, showcasing trends in temperature change over time.

These enhancements ensure accurate data munging and meaningful analysis of temperature anomalies, adhering strictly to the assignment's constraints against using data analysis modules like `pandas`.