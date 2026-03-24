import requests
class GitHubProfileAnalyzer:
    def analyze(self, username):
        url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(url)
        if response.status_code != 200:
            return {"error":"GitHub user not found"}
        repos = response.json()
        languages = {}

        for r in repos:
            lang = r.get("language")
            if lang:
                if lang not in languages:
                    languages[lang] = 0
                languages[lang] += 1

        return {
            "total_repos": len(repos),
            "languages": languages
        }