class ProjectRecommender:
    PROJECT_DB = {
        "ai": [
            "AI Chatbot",
            "Deepfake Detection System",
            "AI Resume Analyzer"
        ],
        "data": [
            "Stock Price Prediction",
            "Data Visualization Dashboard",
            "Recommendation System"
        ],
        "web": [
            "Portfolio Website",
            "Blog Platform",
            "E-commerce Website"
        ]
    }

    def recommend(self, skills):
        skills = [s.lower() for s in skills]
        if "machine learning" in skills or "ai" in skills:
            return self.PROJECT_DB["ai"]
        elif "sql" in skills or "data" in skills:
            return self.PROJECT_DB["data"]
        else:
            return self.PROJECT_DB["web"]