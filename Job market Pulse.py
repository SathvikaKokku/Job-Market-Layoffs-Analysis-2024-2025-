import pandas as pd

layoffs = pd.read_csv("C:/Users/sathv/Downloads/Project/Layoffs.fyi  - Tech Layoffs Tracker.csv")
layoffs['Date'] = pd.to_datetime(layoffs['Date'], errors='coerce')  # Parse date safely
layoffs = layoffs.dropna(subset=['Company', 'Date', '# Laid Off'])

# Filter and copy
layoffs_recent = layoffs[layoffs['Date'] >= '2024-01-01'].copy()
layoffs_recent['Year'] = layoffs_recent['Date'].dt.year
layoffs_recent['Month'] = layoffs_recent['Date'].dt.month

layoffs_recent.to_csv("C:/Users/sathv/Downloads/Project/layoffs_cleaned.csv", index=False)
jobs = pd.read_csv("C:/Users/sathv/Downloads/Project/monster_com-job_sample.csv")
