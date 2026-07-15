# Cleaning Log

## daily_activity
- Checked for duplicate rows (same Id, ActivityDate, and full-row match),none found
- Checked for nulls in Id, ActivityDate, TotalSteps, and Calories, none found
- Checked for wrong values (activity minutes over 1440 per day), none found
- Found 73 rows (of 940) where TotalSteps = 0 but Calories > 0, likely days the device wasn't worn. Decision was to exclude these rows from step/activity based analysis (e.g. average daily steps), but keep them in the full table and disclose the exclusion in the final write-up
- Unique users: 33 (case study brief states 30, noted as a data discrepancy in data_sources.md)

## sleep_day
- Found 3 exact duplicate rows (same Id, SleepDay, TotalSleepRecords, 
  TotalMinutesAsleep, TotalTimeInBed all matching)
- Removed duplicates in SQL using rowid, keeping the first occurrence of each duplicate group
- Row count before: 413 → after: 410
- 24 of 33 users in daily_activity have any sleep data logged. Sleep-based findings will not represent the full user base
- SleepDay was stored as a datetime string (e.g. "4/12/2016 12:00:00 AM"), while daily_activity's ActivityDate was not, this mismatch 
  caused the JOIN between the two tables to return zero rows
- Fix: added a new column, SleepDateClean, extracting just the date portion of SleepDay using substr()/instr(), so it matches ActivityDate's format
- After the fix, joining daily_activity to sleep_day on Id + date returned 410 matched rows, as expected

## Process notes
- All cleaning performed in SQLite (bellabeat.db) via SQLTools in VS Code
- Original raw CSVs left untouched in raw_data/; all cleaning done directly on the imported SQL tables