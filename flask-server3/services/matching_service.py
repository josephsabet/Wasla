
from utils.config_loader import config
from .scoringFunction.time_overlap_scorer import TimeOverlapScorer
from .scoringFunction.language_scorer import LanguageScorer
from .scoringFunction.category_scorer import CategoryScorer
from adapters.user_adapter import UserAdapter

class MatchingService:
    def __init__(self):
        self.weights = config["scoring_weights"]
        self.thresholds = config["scoring_thresholds"]

        self.scorers = [
            (TimeOverlapScorer(self.thresholds["time_overlap"]), self.weights["time_overlap"]),
            (LanguageScorer(self.thresholds["language"]),self.weights["language"]),
            (CategoryScorer(self.thresholds["category"]),self.weights["category"])
        ]

    def calculate_total_score(self, user1, user2):
        profile1 = UserAdapter.from_user(user1)
        profile2 = UserAdapter.from_user(user2)

        total = 0
        for scorer, weight in self.scorers:
            if scorer.isValid(profile1, profile2):
                score = scorer.score(profile1, profile2)
                total += score * weight
        return total
    
    def find_best_matches(self, base_user, candidates, n=3):
        return sorted(candidates, key=lambda candidate: self.calculate_total_score(base_user, candidate), reverse=True)[:n]
    