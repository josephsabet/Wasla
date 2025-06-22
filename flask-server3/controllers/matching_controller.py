
from flask import Blueprint, jsonify
from models.user import User
from services.matching_service import MatchingService

matching_blueprint = Blueprint("matching", __name__)

@matching_blueprint.route("/match/<int:mentee_id>", methods=["GET"])
def match_user(mentee_id):
    mentee = User(id=mentee_id,
        role="mentee",
        name="Mentee A",
        availability=[(9, 12)],
        language="en",
        category=["AI"],
        experience=1,
        goals="learn AI and get job",
        region="Gaza",
        gender="female"
        )

    mentors = [
        User(1, "Mentor Alice","mentor", [(8, 13)], "en", ["AI", "Web"], 4, "help others", "Gaza", "male"),
        User(2, "Mentor Bob","mentor", [(8, 18)], "en", ["Data"], 2, "support mentees", "Gaza", "female"),
        User(3, "Mentor Carol","mentor", [(1, 8)], "en", ["Data"], 2, "support mentees", "Gaza", "female"),
        User(4,"Mentor alaan" ,"mentor", [(4, 8)], "ar", ["ai"], 2, "support soft skilles", "egypt", "male")
    ]

    service = MatchingService()
    best = service.find_best_matches(mentee, mentors)
    scores = [service.calculate_total_score(mentee, mentor) for mentor in best]
    mentors_with_scores = [
        {"mentor": mentor, "score": service.calculate_total_score(mentee, mentor)}
        for mentor in mentors
    ]
    mentors_with_scores.sort(key=lambda m: m["score"], reverse=True)
    
    top_matches = mentors_with_scores[:3]



    return jsonify({
        "mentee_id": mentee.id,
        "matched_mentor_id": [mentor.id for mentor in best] if best else None, #best.join(",")
        "matched_mentor_score": [score for score in scores] if scores else None, #best.join(",")
        # 
    })
    return jsonify({
        "mentee": {
            "id": mentee.id,
            "name": mentee.name
        },
        "matched_mentors": [
            {
                "id": m["mentor"].id,
                "name": m["mentor"].name,
                "score": round(m["score"], 2)
            }
            for m in top_matches
        ]
    })