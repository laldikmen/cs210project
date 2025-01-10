from datetime import datetime, timedelta
import csv

# Step 1: Enter period start dates manually
print("Enter your period start dates (YYYY-MM-DD format). Type 'done' when finished:")
period_dates = []
while True:
    date_input = input("Enter period start date: ")
    if date_input.lower() == "done":
        break
    try:
        period_date = datetime.strptime(date_input, "%Y-%m-%d")
        period_dates.append(period_date)
    except ValueError:
        print("Invalid date format. Please enter in YYYY-MM-DD format.")

# Step 2: Calculate phases
timeline = []
for i in range(len(period_dates) - 1):  # Exclude the last period as there's no "next period"
    start_date = period_dates[i]
    next_start_date = period_dates[i + 1]
    ovulation_date = next_start_date - timedelta(days=14)
    follicular_end = ovulation_date - timedelta(days=1)
    luteal_start = ovulation_date + timedelta(days=1)

    # Append phase timelines
    timeline.append((start_date, follicular_end, "Follicular Phase"))
    timeline.append((ovulation_date, ovulation_date, "Ovulation Phase"))
    timeline.append((luteal_start, next_start_date - timedelta(days=1), "Luteal Phase"))

# Step 3: Save to CSV
csv_file = "cycle_timeline.csv"
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Start", "End", "Phase"])
    for start, end, phase in timeline:
        writer.writerow([start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d"), phase])

print(f"Cycle timeline saved to '{csv_file}'.")

