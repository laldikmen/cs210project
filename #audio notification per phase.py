#audio notification per phase
import pandas as pd
import matplotlib.pyplot as plt

# Load the audio notifications data
audio_file_path = "/mnt/data/HKQuantityTypeIdentifierHeadphoneAudioExposure.csv"
audioDB = pd.read_csv(audio_file_path, usecols=["startDate"])
audioDB['date'] = pd.to_datetime(audioDB['startDate'])
audioDB = audioDB.drop(columns=["startDate"])

# Load the cycle phases data
cycle_file_path = "/mnt/data/cycle_timeline.csv"
cycle_data = pd.read_csv(cycle_file_path)
cycle_data['Start'] = pd.to_datetime(cycle_data['Start'])
cycle_data['End'] = pd.to_datetime(cycle_data['End'])

# Add phase names with intervals
cycle_data['Phase_Label'] = None
phase_counter = {"Follicular": 1, "Ovulation": 1, "Luteal": 1}

for i, row in cycle_data.iterrows():
    phase_type = row['Phase']
    start_date = row['Start'].strftime('%m.%d')
    end_date = row['End'].strftime('%m.%d') if not pd.isnull(row['End']) else None
    phase_label = None
    
    if phase_type == "Follicular Phase":
        phase_label = f"follicular phase{phase_counter['Follicular']} ({start_date}-{end_date})"
        phase_counter["Follicular"] += 1
    elif phase_type == "Ovulation Phase":
        phase_label = f"ovulation{phase_counter['Ovulation']} ({start_date})"
        phase_counter["Ovulation"] += 1
    elif phase_type == "Luteal Phase":
        phase_label = f"luteal phase{phase_counter['Luteal']} ({start_date}-{end_date})"
        phase_counter["Luteal"] += 1

    cycle_data.at[i, 'Phase_Label'] = phase_label

# Map each audioDB record to a cycle phase
audioDB['Phase'] = None

for _, row in cycle_data.iterrows():
    mask = (audioDB['date'] >= row['Start']) & (audioDB['date'] <= row['End'])
    audioDB.loc[mask, 'Phase'] = row['Phase_Label']

# Group by phase and count notifications
audioDB_GroupedByPhase = audioDB.groupby('Phase')['date'].count().reset_index()
audioDB_GroupedByPhase.columns = ['Phase', 'High Volume Notifications']

# Merge with cycle_data to preserve the order of phases by their start date
audioDB_GroupedByPhase = pd.merge(audioDB_GroupedByPhase, cycle_data[['Phase_Label', 'Start']], 
                                  left_on='Phase', right_on='Phase_Label')
audioDB_GroupedByPhase = audioDB_GroupedByPhase.sort_values(by='Start')

# Plot the data
plt.figure(figsize=(14, 6))
plt.bar(audioDB_GroupedByPhase['Phase'], audioDB_GroupedByPhase['High Volume Notifications'], color='skyblue')

plt.title('High Volume Notifications by Cycle Phases')
plt.xlabel('Cycle Phase')
plt.ylabel('High Volume Notifications')
plt.xticks(rotation=45, ha='right', fontsize=8)

plt.tight_layout()
plt.show()

