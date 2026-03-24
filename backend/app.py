from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

# ===== IMPORTS =====
from modules.skill_assessment_engine import SkillAssessmentEngine
from modules.career_match_engine import CareerMatchEngine
from modules.skill_gap_engine import SkillGapEngine
from modules.job_recommendation_engine import JobRecommendationEngine
from modules.project_recommender import ProjectRecommender
from modules.learning_roadmap_generator import LearningRoadmapGenerator
from modules.salary_prediction_engine import SalaryPredictionEngine
from modules.certification_recommender import CertificationRecommender
from modules.learning_resource_engine import LearningResourceEngine
from modules.study_planner_engine import StudyPlannerEngine
from modules.interview_preparation_engine import InterviewPreparationEngine
from modules.job_market_intelligence import JobMarketIntelligence
from modules.career_growth_engine import CareerGrowthEngine
from modules.github_profile_analyzer import GitHubProfileAnalyzer
from modules.resume_intelligence_engine import ResumeIntelligenceEngine
from modules.resume_job_matcher import ResumeJobMatcher
from modules.portfolio_analyzer import PortfolioAnalyzer
from modules.ai_career_mentor import AICareerMentor
from modules.mentor_memory_engine import MentorMemoryEngine

app = Flask(__name__)
CORS(app)

# ===== INIT =====
skill_engine = SkillAssessmentEngine()
career_engine = CareerMatchEngine()
gap_engine = SkillGapEngine()
job_engine = JobRecommendationEngine()
project_engine = ProjectRecommender()
roadmap_engine = LearningRoadmapGenerator()
salary_engine = SalaryPredictionEngine()
cert_engine = CertificationRecommender()
learning_engine = LearningResourceEngine()
study_engine = StudyPlannerEngine()
interview_engine = InterviewPreparationEngine()
market_engine = JobMarketIntelligence()
growth_engine = CareerGrowthEngine()

github_engine = GitHubProfileAnalyzer()
resume_engine = ResumeIntelligenceEngine()
resume_match_engine = ResumeJobMatcher()
portfolio_engine = PortfolioAnalyzer()

mentor_engine = AICareerMentor()
memory_engine = MentorMemoryEngine()

# ================= CORE =================
def generate_full_analysis(skills, experience):

    skill_score = len(skills) * 10

    jobs = job_engine.recommend(skills)

    career_match = [
        {
            "career": j["job_title"],
            "match_score": j.get("match_score", 3) * 20
        }
        for j in jobs
    ]

    best_career = career_match[0]["career"] if career_match else "AI Engineer"

    return {
        "skill_assessment": skill_engine.evaluate(skills),
        "career_match": career_match,
        "skill_gap": gap_engine.find_gap(skills),
        "projects": project_engine.recommend(skills),
        "learning_resources": learning_engine.recommend(skills),
        "study_plan": study_engine.generate(skills),
        "certifications": cert_engine.recommend(skills),
        "salary_prediction": salary_engine.predict(experience, skill_score),
        "jobs": jobs,
        "roadmap": roadmap_engine.generate(best_career),
        "interview_questions": interview_engine.generate(best_career),
        "career_growth": growth_engine.simulate(best_career),
        "job_market_skill_demand": market_engine.skill_demand(),
        "job_market_city_demand": market_engine.city_demand()
    }

# ================= API =================
@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.json
    skills = data.get("skills", [])
    experience = int(data.get("experience", 1))
    return jsonify(generate_full_analysis(skills, experience))

@app.route("/api/resume", methods=["POST"])
def resume():
    file = request.files["resume"]
    parsed = resume_engine.analyze(file)

    skills = parsed["skills_analysis"]["detected_skills"]
    experience = parsed["experience_analysis"]["experience_years"]

    full = generate_full_analysis(skills, experience)

    return jsonify({
        "resume_analysis": parsed,
        **full
    })

@app.route("/api/github", methods=["POST"])
def github():
    username = request.json["username"]
    return jsonify(github_engine.analyze(username))

@app.route("/api/portfolio", methods=["POST"])
def portfolio():
    projects = request.json["projects"]
    return jsonify(portfolio_engine.analyze(projects))

@app.route("/api/mentor", methods=["POST"])
def mentor():

    data = request.json

    question = data.get("question", "")
    skills = data.get("skills", "")
    experience = data.get("experience", 0)

    answer = mentor_engine.ask(question, skills, experience)

    return jsonify(answer)

# ================= FRONTEND =================
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

@app.route("/")
def home():
    return send_from_directory(os.path.join(BASE_DIR, "frontend"), "index.html")

@app.route("/dashboard.js")
def js():
    return send_from_directory(os.path.join(BASE_DIR, "frontend"), "dashboard.js")
# ================= RUN =================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)