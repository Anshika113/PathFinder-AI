import json
import os

class AICareerMentor:

    def __init__(self):
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "..", "data", "jobs_dataset.json")

        with open(file_path, "r") as f:
            self.jobs = json.load(f)

    def ask(self, question, skills, experience):

        question = question.lower()

        # =========================
        # SAFE SKILLS PARSE
        # =========================
        if isinstance(skills, str):
            skills = [s.strip().lower() for s in skills.split(",") if s.strip()]
        else:
            skills = []

        # =========================
        # IF NO SKILLS → USE QUESTION
        # =========================
        if not skills:
            for job in self.jobs:
                if any(word in job["job_title"].lower() for word in question.split()):
                    skills = [s.lower() for s in job.get("required_skills", [])]
                    break

        # =========================
        # JOB MATCHING (SMART)
        # =========================
        scored_jobs = []

        for job in self.jobs:

            job_skills = [s.lower() for s in job.get("required_skills", [])]

            match_skills = set(skills) & set(job_skills)
            missing_skills = set(job_skills) - set(skills)

            match = len(match_skills)

            # ❗ IMPORTANT: penalty for mismatch
            penalty = len(missing_skills) * 0.3

            score = match - penalty

            # ❗ ignore weak matches
            if match < 2:
                continue

            # ❗ question boost
            if any(word in job["job_title"].lower() for word in question.split()):
                score += 2

            scored_jobs.append((job, score, match_skills, missing_skills))

        # =========================
        # SORT BEST MATCH
        # =========================
        scored_jobs.sort(key=lambda x: x[1], reverse=True)

        # =========================
        # FALLBACK
        # =========================
        if not scored_jobs:
            return {
                "answer": "Start with fundamentals: Python, SQL, Data Structures. Then explore AI, Web, or Cyber Security based on your interest."
            }

        # =========================
        # BEST JOB
        # =========================
        best_job, score, matched, missing = scored_jobs[0]

        title = best_job["job_title"]
        skills_needed = best_job["required_skills"]
        salary = best_job["salary_range"]
        exp_req = best_job["experience_required"]

        # =========================
        # RESPONSE TYPES
        # =========================

        # 👉 START ROADMAP
        if "start" in question:
            return {
                "answer": f"""
Start with fundamentals → Python + core concepts.

Then move towards {title}:

Required skills:
{', '.join(skills_needed)}

Missing skills (focus here):
{', '.join(missing) if missing else "None"}

Steps:
- Learn basics properly
- Build 2–3 projects
- Practice consistently

Salary: {salary}
"""
            }

        # 👉 RESUME
        if "resume" in question:
            return {
                "answer": f"""
To improve your resume for {title}:

- Add projects using: {', '.join(list(matched)[:3])}
- Focus on measurable results (accuracy, performance)
- Add GitHub + real-world work

Missing skills to include:
{', '.join(missing)}
"""
            }

        # 👉 JOB MATCH
        if "job" in question:
            return {
                "answer": f"""
Best role for you: {title}

Matched skills:
{', '.join(matched)}

Missing skills:
{', '.join(missing)}

Salary: {salary}
Experience: {exp_req}
"""
            }

        # 👉 SKILL IMPROVEMENT
        if "skill" in question or "improve" in question:
            return {
                "answer": f"""
To become {title}, focus on these missing skills:

{', '.join(missing)}

Keep practicing and build real projects.
"""
            }

        # 👉 DEFAULT
        return {
            "answer": f"""
Based on your profile, {title} is a strong career path.

Matched skills:
{', '.join(matched)}

To improve:
{', '.join(missing)}

Next steps:
- Learn advanced concepts
- Build projects
- Apply for internships

Salary range: {salary}
"""
        }
