import json
from collections import Counter

class JobMarketIntelligence:

    def __init__(self):

        with open("data/jobs_dataset.json") as f:
            self.jobs = json.load(f)

    def city_demand(self):

        cities = []

        for job in self.jobs:

            if isinstance(job["location"], list):

                cities.extend(job["location"])

            else:

                cities.append(job["location"])

        return Counter(cities)


    def skill_demand(self):

        skills = []

        for job in self.jobs:

            skills.extend(job["required_skills"])

        return Counter(skills)