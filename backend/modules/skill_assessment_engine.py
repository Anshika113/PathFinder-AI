from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SkillAssessmentEngine:

    # Skill knowledge base
    SKILL_DATABASE = [
        "python programming",
        "machine learning",
        "deep learning",
        "data science",
        "sql databases",
        "data analysis",
        "cloud computing aws",
        "docker containerization",
        "kubernetes orchestration",
        "natural language processing",
        "computer vision",
        "javascript frontend",
        "react frontend development",
        "backend development",
        "devops engineering"
    ]

    def evaluate(self, skills):

        if not skills:
            return {
                "detected_skills": [],
                "matched_domains": [],
                "score": 0,
                "level": "No skills"
            }

        skills_text = " ".join(skills)

        documents = self.SKILL_DATABASE + [skills_text]

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(documents)

        user_vector = vectors[-1]

        similarities = cosine_similarity(user_vector, vectors[:-1])[0]

        matched = []

        for i, score in enumerate(similarities):
            if score > 0.2:
                matched.append(self.SKILL_DATABASE[i])

        skill_score = len(matched) * 10

        if skill_score >= 80:
            level = "Advanced"
        elif skill_score >= 50:
            level = "Intermediate"
        else:
            level = "Beginner"

        return {
            "detected_skills": skills,
            "matched_domains": matched,
            "score": skill_score,
            "level": level
        }