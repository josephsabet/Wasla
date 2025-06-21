# adapters/user_adapter.py

from models.match_profile import MatchProfile

class UserAdapter:
    @staticmethod
    def from_user(user):
        return MatchProfile(
            role=user.role,
            availability=user.availability,
            language=user.language,
            category=user.category,
            experience=user.experience,
            goals=user.goals,
            region=user.region,
            gender=user.gender
        )
