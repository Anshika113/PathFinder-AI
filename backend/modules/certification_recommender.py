class CertificationRecommender:
    def recommend(self, skills):
        skills = [s.lower() for s in skills]
        certs = []
        if "aws" in skills:
            certs.append("AWS Certified Solutions Architect")
        if "machine learning" in skills:
            certs.append("Google Professional ML Engineer")
        if "python" in skills:
            certs.append("Python Institute Certification")
        if "data science" in skills:
            certs.append("IBM Data Science Professional Certificate")
        if not certs:
            certs.append("Coursera AI Foundations")

        return certs