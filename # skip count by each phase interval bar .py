# skip count by each phase interval bar chart

cycle_data_cleaned = cycle_data_fixed[['Start', 'End', 'Unnamed: 2', 'Skipped song count']].dropna()
cycle_data_cleaned.columns = ['start_date', 'end_date', 'phase', 'skipped_count']

# Convert dates to datetime format
cycle_data_cleaned['start_date'] = pd.to_datetime(cycle_data_cleaned['start_date'])
cycle_data_cleaned['end_date'] = pd.to_datetime(cycle_data_cleaned['end_date'])

# Generate the bar chart
plt.figure(figsize=(10, 6))
plt.bar(cycle_data_cleaned['phase'], cycle_data_cleaned['skipped_count'], color='blue')
plt.title("Skipped Songs by Menstrual Cycle Phase")
plt.xlabel("Menstrual Cycle Phase")
plt.ylabel("Skipped Song Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()