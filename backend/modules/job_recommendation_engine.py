import json
import os

class JobRecommendationEngine:

    def __init__(self):

        BASE_DIR = os.path.dirname(os.path.dirname(__file__))

        file_path = os.path.join(BASE_DIR, "data", "jobs_dataset.json")

        with open(file_path, "r", encoding="utf-8") as f:
            self.jobs = json.load(f)

    def recommend(self, skills):

        matched_jobs = []

        for job in self.jobs:

            required = job["required_skills"]

            match_score = len(set(skills) & set(required))

            if match_score > 0:
                matched_jobs.append({
                    "job_title": job["job_title"],
                    "location": job["location"],
                    "salary": job["salary_range"],
                    "experience": job["experience_required"],
                    "work_mode": job["work_mode"],
                    "match_score": match_score
                })

        matched_jobs = sorted(
            matched_jobs,
            key=lambda x: x["match_score"],
            reverse=True
        )

        return matched_jobs[:5]