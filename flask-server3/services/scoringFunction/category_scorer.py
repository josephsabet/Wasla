from ..matcher_interface import MatchScorer

class CategoryScorer(MatchScorer):
    
    def score(self, mentor, mentee):
        mentor_cat = set(mentor.category)
        mentee_cat = set(mentee.category)
        intersection = mentor_cat & mentee_cat
        union = mentor_cat | mentee_cat
        return len(intersection) / len(union) if union else 0

