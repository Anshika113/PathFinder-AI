class LearningResourceEngine:

    def recommend(self, skills):

        skills = [s.lower() for s in skills]

        resources = []

        if "python" in skills:
            resources.append("Python for Everybody - Coursera")

        if "machine learning" in skills or "ml" in skills:
            resources.append("Machine Learning by Andrew Ng - Coursera")

        if "deep learning" in skills:
            resources.append("Deep Learning Specialization - Coursera")

        if "aws" in skills:
            resources.append("AWS Cloud Practitioner Essentials")

        if "sql" in skills:
            resources.append("SQL for Data Science - Coursera")

        if not resources:
            resources.append("Computer Science Fundamentals - Harvard CS50")

        return resources