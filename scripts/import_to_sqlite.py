import pandas as pd
import sqlite3
import os

# Get the folder this script lives in, and always work relative to it
script_dir = os.path.dirname(os.path.abspath(__file__))

# Connect to (or create) a SQLite database file in the project's sql folder
db_path = os.path.join(script_dir, '..', 'sql', 'bellabeat.db')
conn = sqlite3.connect(db_path)

# Path to the raw data folder we're using
data_dir = os.path.join(script_dir, '..', 'raw_data', 'mturkfitbit_export_4.12.16-5.12.16', 'Fitabase Data 4.12.16-5.12.16')

# Load and push each CSV into its own table
tables = {
    'daily_activity': 'dailyActivity_merged.csv',
    'sleep_day': 'sleepDay_merged.csv'
}

for table_name, csv_file in tables.items():
    csv_path = os.path.join(data_dir, csv_file)
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Loaded '{csv_file}' into table '{table_name}' ({len(df)} rows).")

conn.close()
print("Done! All tables created.")