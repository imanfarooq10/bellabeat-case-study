# Data Sources

## Source
FitBit Fitness Tracker Data whihc is made available on Kaggle through Möbius.
License: CC0: Public Domain.
Link: https://www.kaggle.com/datasets/arashnic/fitbit

## Description
Personal fitness tracker data from thirty FitBit users who consented to submit their data, including minute-level output for physical activity, heart rate, and sleep monitoring. It includes information about daily activity, steps, and heart rate
that can be used to explore users’ habits.
This data was collected across two time periods in early 2016.

## Files Used
Using the `mturkfitbit_export_4.12.16-5.12.16` folder (18 files), which is the complete dataset covering, daily activity, daily calories, daily intensities, daily steps, hourly activity, minute-level activity, heart rate, sleep, and weight log data.

## Files Excluded
The `mturkfitbit_export_3.12.16-4.11.16` folder (11 files) was excluded from this analysis. It is missing `sleepDay_merged` and the daily summary files (`dailyCalories`, `dailyIntensities`, `dailySteps`), which are core to answering the business questions.

## Credibility (ROCCC)
**Reliable**: Low, only 30 users, a small and self-selected sample
**Original**: Third-party (collected via Amazon Mechanical Turk), not first-party Bellabeat data
**Comprehensive**: Moderate, covers activity, sleep, heart rate, and weight, but lacks demographic data (age, gender, location)
**Current**: Low, data is from 2016, nearly a decade old, smart device usage habits may have shifted since
**Cited**: Public domain (CC0), source and collection method disclosed

## Limitations
- Small, non-representative sample size, only 30 users
- No demographic breakdown, so findings may not generalize     across all Bellabeat customer segments
- Data is outdated relative to current smart device usage patterns
- Self-reported data may contain gaps or inaccuracies
  (e.g. users not wearing the device, missed sleep logs)