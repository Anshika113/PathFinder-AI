class PortfolioAnalyzer:

    def analyze(self, projects):

        score = len(projects) * 10

        feedback = []

        if score < 50:
            feedback.append("Add more real world projects")

        return {
            "portfolio_score":score,
            "feedback":feedback
        }