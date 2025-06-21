from ..matcher_interface import MatchScorer

class LanguageScorer(MatchScorer):
    def score(self, mentor, mentee):
        return 1 if mentor.language == mentee.language else 0
    