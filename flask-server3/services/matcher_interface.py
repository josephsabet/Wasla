# from abc import ABC, abstractmethod

from abc import ABC, abstractmethod
class MatcherInterface(ABC):
    @abstractmethod
    def match(self, mentee, mentors):
        pass
# scoringFunction/match_interface.py

class MatchScorer(ABC):
    @abstractmethod
    def score(self, mentor, mentee):
        pass

