import pdfplumber
import re
class ResumeIntelligenceEngine:
    def __init__(self):
        self.skills_db = [
            "python","machine learning","deep learning","sql","aws",
            "docker","kubernetes","nlp","data science","tensorflow",
            "pandas","numpy","flask","react","linux"
        ]

        self.important_skills = [
            "python","machine learning","sql","aws","data structures"
        ]

    def extract_text(self, file):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

        return text.lower()

    def analyze(self, file):
        text = self.extract_text(file)
        # -----------------------
        # SKILL DETECTION
        # -----------------------
        detected_skills = [
            skill for skill in self.skills_db if skill in text
        ]
        # -----------------------
        # EXPERIENCE DETECTION
        # -----------------------
        experience = 0
        exp_matches = re.findall(r'(\d+)\+?\s*(year|yr)', text)
        if exp_matches:
            experience = max([int(x[0]) for x in exp_matches])
        # -----------------------
        # ATS SCORE
        # -----------------------
        ats_score = min(100, len(detected_skills) * 6 + experience * 8)
        # -----------------------
        # MISSING SKILLS
        # -----------------------
        missing_skills = [
            s for s in self.important_skills if s not in detected_skills
        ]
        # -----------------------
        # SECTION CHECK
        # -----------------------
        sections = {
            "projects": "project" in text,
            "experience": "experience" in text,
            "education": "education" in text,
            "certifications": "certification" in text
        }
        # -----------------------
        # SUGGESTIONS
        # -----------------------
        suggestions = []
        if len(detected_skills) < 5:
            suggestions.append("Add more relevant technical skills")
        if experience == 0:
            suggestions.append("Mention internship or work experience")
        if not sections["projects"]:
            suggestions.append("Add strong project section with details")
        if not sections["certifications"]:
            suggestions.append("Add certifications (AWS, ML, etc.)")
        if len(text) < 1500:
            suggestions.append("Resume content is too short, expand details")
        # -----------------------
        # FINAL OUTPUT
        # -----------------------
        return {
            "summary": {
                "resume_strength": "Strong" if ats_score > 70 else "Average" if ats_score > 40 else "Weak",
                "ats_score": ats_score
            },
            "skills_analysis": {
                "detected_skills": detected_skills,
                "total_skills": len(detected_skills),
                "missing_important_skills": missing_skills
            },
            "experience_analysis": {
                "experience_years": experience
            },
            "section_analysis": sections,
            "improvement_suggestions": suggestions,
            "resume_length": len(text)
        }