class User:
    def __init__(self, id, role, availability, language, category, experience, goals, region, gender):
        self.id = id
        self.role = role  # "mentor" or "mentee"
        self.availability = availability  # list of (start, end) tuples
        self.language = language
        self.category = set(category)
        self.experience = experience
        self.goals = goals
        self.region = region
        self.gender = gender

