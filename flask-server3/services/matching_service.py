
from utils.config_loader import config
from .scoringFunction.time_overlap_scorer import TimeOverlapScorer
from .scoringFunction.language_scorer import LanguageScorer
from .scoringFunction.category_scorer import CategoryScorer
from adapters.user_adapter import UserAdapter

class MatchingService:
    def __init__(self):
        self.weights = config["scoring_weights"]
        self.scorers = [
            (TimeOverlapScorer(), self.weights["time_overlap"]),
            (LanguageScorer(), self.weights["language"]),
            (CategoryScorer(), self.weights["category"])
            # more scorers...
        ]

    def calculate_total_score(self, user1, user2):
        profile1 = UserAdapter.from_user(user1)
        profile2 = UserAdapter.from_user(user2)

        return sum(
            scorer.score(profile1, profile2) * weight
            for scorer, weight in self.scorers
        )
    
    def find_best_matches(self, base_user, candidates, n=3):
        return sorted(candidates, key=lambda candidate: self.calculate_total_score(base_user, candidate), reverse=True)[:n]
    