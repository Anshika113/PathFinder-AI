class StudyPlannerEngine:

    def generate(self, skills):

        plan = []

        if "python" in skills:
            plan.append("Week 1-2: Python Basics")

        if "machine learning" in skills:
            plan.append("Week 3-4: Machine Learning Fundamentals")

        if "sql" in skills:
            plan.append("Week 5: SQL Practice")

        if not plan:
            plan.append("Start with Computer Science Fundamentals")

        return plan