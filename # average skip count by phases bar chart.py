# average skip count by phases bar chart
# Categorize phases as either Follicular or Luteal

cycle_data_cleaned['phase_category'] = cycle_data_cleaned['phase'].apply(
    lambda x: 'Follicular Phase' if 'Follicular' in x else 'Luteal Phase'
)

# Calculate the average skipped song count for each phase category
average_skipped_counts = cycle_data_cleaned.groupby('phase_category')['skipped_count'].mean()

# Generate the bar chart
plt.figure(figsize=(8, 5))
plt.bar(average_skipped_counts.index, average_skipped_counts.values, color='green')
plt.title("Average Skipped Songs by Menstrual Cycle Phase Category")
plt.xlabel("Menstrual Cycle Phase Category")
plt.ylabel("Average Skipped Song Count")
plt.tight_layout()
plt.show()