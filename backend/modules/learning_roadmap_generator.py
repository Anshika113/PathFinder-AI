import json

class LearningRoadmapGenerator:

    def __init__(self):

        with open("data/learning_resource.json") as f:
            self.resources = json.load(f)

    def generate(self, career):

        roadmap = {

        "Phase 1 Foundations":{

        "duration_weeks":4,

        "topics":[
        "Python",
        "Statistics",
        "Git"
        ],

        "projects":[
        "Data Analysis Mini Project"
        ],

        "resources":self.resources.get("python",[])

        },

        "Phase 2 Core Skills":{

        "duration_weeks":6,

        "topics":[
        "Machine Learning",
        "SQL",
        "Data Visualization"
        ],

        "projects":[
        "ML Prediction System"
        ],

        "resources":self.resources.get("machine learning",[])

        },

        "Phase 3 Advanced":{

        "duration_weeks":6,

        "topics":[
        "Deep Learning",
        "NLP",
        "Model Deployment"
        ],

        "projects":[
        "Deepfake Detection System"
        ]

        },

        "Phase 4 Industry Projects":{

        "duration_weeks":4,

        "projects":[
        "AI Resume Analyzer",
        "Career Intelligence Dashboard"
        ]

        }

        }

        return roadmap