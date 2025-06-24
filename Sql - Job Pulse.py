import pandas as pd
import sqlite3
layoffs = pd.read_csv("C:/Users/sathv/Downloads/Project/layoffs_cleaned.csv")
jobs = pd.read_csv("C:/Users/sathv/Downloads/Project/jobs_cleaned.csv")
conn = sqlite3.connect("C:/Users/sathv/Downloads/Project/job_market.db")
layoffs.to_sql('layoffs', conn, if_exists='replace', index=False)
jobs.to_sql('jobs', conn, if_exists='replace', index=False)
query = """
SELECT Company, SUM([# Laid Off]) AS total_laid_off
FROM layoffs
GROUP BY Company
ORDER BY total_laid_off DESC
LIMIT 10;
"""
top_companies = pd.read_sql_query(query, conn)
print("Top 10 Companies by Layoffs")
print(top_companies)
top_companies.to_csv("C:/Users/sathv/Downloads/Project/top_layoff_companies.csv", index=False)

query = """
SELECT Year, Month, SUM([# Laid Off]) AS total_laid_off
FROM layoffs
GROUP BY Year, Month
ORDER BY Year, Month;
"""

monthly_layoffs = pd.read_sql_query(query, conn)
print("Layoffs by Year and Month")
print(monthly_layoffs)
monthly_layoffs.to_csv("C:/Users/sathv/Downloads/Project/monthly_layoffs.csv", index=False)

