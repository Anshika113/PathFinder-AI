import json

class CareerMatchEngine:

    def __init__(self):

        with open("data/jobs_dataset.json") as f:
            self.jobs = json.load(f)

    def match(self, user_skills):

        results = []

        for job in self.jobs:

            required = job["required_skills"]

            match = len(set(user_skills) & set(required)) / len(required)

            results.append({

            "career": job["job_title"],

            "match_score": round(match*100,2),

            "location": job["location"],

            "salary_range": job["salary_range"],

            "work_mode": job["work_mode"]

            })

        results.sort(key=lambda x: x["match_score"], reverse=True)

        return results[:10]