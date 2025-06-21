from ..matcher_interface import MatchScorer

class TimeOverlapScorer(MatchScorer):
    def score(self, mentor, mentee):
        overlap = 0
        total = 0
        for m_start, m_end in mentor.availability:
            for n_start, n_end in mentee.availability:
                start = max(m_start, n_start)
                end = min(m_end, n_end)
                if start < end:
                    overlap += (end - start)
                total += (m_end - m_start)
        return overlap / total if total > 0 else 0
