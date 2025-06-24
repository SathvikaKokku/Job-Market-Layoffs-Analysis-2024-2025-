import pandas as pd
jobs = pd.read_csv("C:/Users/sathv/Downloads/Project/monster_com-job_sample.csv")
print("Before cleaning:", jobs.shape)
jobs = jobs.dropna(subset=['job_title', 'location', 'job_description'])
jobs['job_title'] = jobs['job_title'].str.strip()
jobs['location'] = jobs['location'].str.strip()
jobs['job_description'] = jobs['job_description'].str.strip()
skills = ['Python', 'SQL', 'Excel', 'Power BI', 'Tableau', 'Communication', 'Machine Learning']
for skill in skills:c
    jobs[skill] = jobs['job_description'].str.contains(skill, case=False, na=False)
jobs['num_skills_matched'] = jobs[skills].sum(axis=1)
jobs.to_csv("C:/Users/sathv/Downloads/Project/jobs_cleaned.csv", index=False)
print("Job postings cleaned and saved to jobs_cleaned.csv")