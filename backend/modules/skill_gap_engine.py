class SkillGapEngine:

    def __init__(self):

        self.required_skills = [
            "python",
            "machine learning",
            "deep learning",
            "sql",
            "data structures",
            "algorithms",
            "aws"
        ]

    def find_gap(self, skills):

        gap = []

        for skill in self.required_skills:
            if skill not in skills:
                gap.append(skill)

        return gap