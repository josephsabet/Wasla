# from abc import ABC, abstractmethod

from abc import ABC, abstractmethod
class MatcherInterface(ABC):
    @abstractmethod
    def match(self, mentee, mentors):
        pass
# scoringFunction/match_interface.py

class MatchScorer(ABC):
    def __init__(self, threshold_range):
        self.min_threshold = threshold_range[0]
        self.max_threshold = threshold_range[1]
        
    @abstractmethod
    def score(self, mentor, mentee):
        pass

    def isValid(self, mentor, mentee):
        score = self.score(mentor, mentee)
        return self.min_threshold <= score <= self.max_threshold
    