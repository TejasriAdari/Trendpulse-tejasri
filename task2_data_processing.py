import pandas as pd
import json

# Load data from JSON
with open("reddit_data.json") as f:
    data = json.load(f)

# Convert data that we collected in first code as DataFrame
dataFrame = pd.DataFrame(data)

# To remove duplicates that post in reddit
dataFrame = dataFrame.drop_duplicates()

# If any data is missing in reddit
dataFrame =dataFrame.dropna()

# To Convert timestamp to readable date
dataFrame['created'] = pd.to_datetime(dataFrame['created'], unit='s')

# Save data as CSV
dataFrame.to_csv("cleaned_data.csv", index=False)

print("Cleaned data saved")