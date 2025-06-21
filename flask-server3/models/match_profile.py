# models/match_profile.py

class MatchProfile:
    def __init__(self, role, availability, language, category, experience, goals, region, gender):
        self.role = role
        self.availability = availability
        self.language = language
        self.category = set(category)
        self.experience = experience
        self.goals = goals
        self.region = region
        self.gender = gender
