# # def say_hello(name):
# #     return f"Hello, {name}! From Matching Service."
# # from services.matcher_interface import MatcherInterface

# # class SimpleMatcher(MatcherInterface):
# #     def match(self, mentee, mentors):
# #         return max(mentors, key=lambda m: self._score(m, mentee))

# #     def _score(self, mentor, mentee):
# #         score = 0
# #         if mentor.language == mentee.language:
# #             score += 1
# #         if mentor.region == mentee.region:
# #             score += 1
# #         return score  # Add more rules later
# # from scoringFunction.time_overlap_scorer import TimeOverlapScorer
# # from .scoringFunction.time_overlap_scorer import TimeOverlapScorer
# # from .scoringFunction.language_scorer import LanguageScorer
# # from .scoringFunction.category_scorer import CategoryScorer
# from adapters.user_adapter import UserAdapter
# class MatchingService:
#     def __init__(self):
        
#         self.scorers = [
#             TimeOverlapScorer(),
#             LanguageScorer(),
#             CategoryScorer()
#         ]

#     # def calculate_total_score(self, mentor, mentee):
#     #     return sum([scorer.score(mentor, mentee) for scorer in self.scorers])

#     # def find_best_match(self, mentee, mentors):
#     #     return max(mentors, key=lambda mentor: self.calculate_total_score(mentor, mentee))

# def calculate_total_score(self, user1, user2):
#         profile1 = UserAdapter.from_user(user1)
#         profile2 = UserAdapter.from_user(user2)

#         return sum([scorer.score(profile1, profile2) for scorer in self.scorers])

# def find_best_match(self, base_user, candidates):
#         return max(candidates, key=lambda candidate: self.calculate_total_score(base_user, candidate))


from .scoringFunction.time_overlap_scorer import TimeOverlapScorer
from .scoringFunction.language_scorer import LanguageScorer
from .scoringFunction.category_scorer import CategoryScorer
# from adapters.user_adapter import UserAdapter

from adapters.user_adapter import UserAdapter

class MatchingService:
    def __init__(self):
        self.scorers = [
            TimeOverlapScorer(),
            LanguageScorer(),
            CategoryScorer(),
            # more scorers...
        ]

    def calculate_total_score(self, user1, user2):
        profile1 = UserAdapter.from_user(user1)
        profile2 = UserAdapter.from_user(user2)

        return sum([scorer.score(profile1, profile2) for scorer in self.scorers])

    def find_best_match(self, base_user, candidates):
        return max(candidates, key=lambda candidate: self.calculate_total_score(base_user, candidate))
