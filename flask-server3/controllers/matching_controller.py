
from flask import Blueprint, jsonify
from models.user import User
from services.matching_service import MatchingService

matching_blueprint = Blueprint("matching", __name__)

@matching_blueprint.route("/match/<int:mentee_id>", methods=["GET"])
def match_user(mentee_id):
    mentee = User(id=mentee_id,
        role="mentee",
        availability=[(9, 12)],
        language="en",
        category=["AI"],
        experience=1,
        goals="learn AI and get job",
        region="Gaza",
        gender="female"
        )

    mentors = [
        User(1, "mentor", [(8, 13)], "en", ["AI", "Web"], 4, "help others", "Gaza", "male"),
        User(2, "mentor", [(8, 18)], "en", ["Data"], 2, "support mentees", "Gaza", "female"),
        User(3, "mentor", [(1, 8)], "en", ["Data"], 2, "support mentees", "Gaza", "female"),
        User(4, "mentor", [(4, 8)], "ar", ["ai"], 2, "support soft skilles", "egypt", "male")
    ]

    service = MatchingService()
    best = service.find_best_matches(mentee, mentors)
    #score = service.calculate_total_score(mentee, best)

    return jsonify({
        "mentee_id": mentee.id,
        "matched_mentor_id": [mentor.id for mentor in best] if best else None, #best.join(",")
    })
