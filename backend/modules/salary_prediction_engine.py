import numpy as np

class SalaryPredictionEngine:

    def predict(self, experience, skill_score):

        # validation
        if experience is None:
            experience = 0

        if skill_score is None:
            skill_score = 0

        try:
            experience = float(experience)
            skill_score = float(skill_score)
        except:
            return {
                "error": "Invalid input for experience or skill_score"
            }

        # base salary (LPA)
        base_salary = 4

        # salary calculation
        salary = base_salary + (experience * 1.8) + (skill_score * 0.05)

        # expected range
        min_salary = round(salary - 2, 2)
        max_salary = round(salary + 2, 2)

        return {
            "predicted_salary_LPA": round(salary, 2),
            "expected_range": f"{min_salary} - {max_salary} LPA"
        }