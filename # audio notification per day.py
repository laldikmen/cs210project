# audio notification per day
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = "/mnt/data/HKQuantityTypeIdentifierHeadphoneAudioExposure.csv"
audioDB = pd.read_csv(file_path, usecols=["startDate", "endDate"])

# Convert 'startDate' to datetime
audioDB['date'] = pd.to_datetime(audioDB['startDate'])

# Drop unnecessary columns
audioDB = audioDB.drop(columns=["startDate", "endDate"])

# Add a 'value' column for counting
audioDB["value"] = 1

# Group by day and sum values
audioDB_GroupedByDay = audioDB.groupby(audioDB["date"].dt.to_period("D"))["value"].sum().reset_index()

# Convert the 'date' column to string for visualization
dateList = [str(i) for i in audioDB_GroupedByDay["date"]]

# Plot the data
plt.figure(figsize=(14, 6))
plt.bar(dateList, audioDB_GroupedByDay['value'], color='skyblue')

plt.xticks(rotation=45, fontsize=8)
plt.title('High Volume Notifications by Day')
plt.xlabel('Day')
plt.ylabel('High Volume Notifications')

plt.tight_layout()
plt.show()
