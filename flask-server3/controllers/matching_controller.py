# from flask import Blueprint, jsonify
# from services.matching_service import *

# matching_blueprint = Blueprint("matching", __name__)

# @matching_blueprint.route("/hello/<name>")
# def hello(name):
#     result = say_hello(name)  # 👉 call the service function
#     return jsonify({"message": result})
# from flask import Blueprint, jsonify
# from models.user import User
# from services.matching_service import SimpleMatcher

# matching_blueprint = Blueprint("matching", __name__)

# # Dummy data
# mentors = [
#     User(1, "mentor", [(8, 12)], "en", ["AI", "Web"], 5, "career growth", "Gaza", "male"),
#     User(2, "mentor", [(14, 18)], "en", ["Data"], 3, "skill building", "Gaza", "female")
# ]

# @matching_blueprint.route("/match/<int:mentee_id>", methods=["GET"])
# def match_user(mentee_id):
#     # For testing, just use a static mentee
#     mentee = User(mentee_id, "mentee", [(10, 12)], "en", ["AI"], 2, "career growth", "Gaza", "female")
#     matcher = SimpleMatcher()
#     match = matcher.match(mentee, mentors)
#     return jsonify({"mentee_id": mentee.id, "matched_mentor_id": match.id})
from flask import Blueprint, jsonify
from models.user import User
from services.matching_service import MatchingService

matching_blueprint = Blueprint("matching", __name__)

@matching_blueprint.route("/match/<int:mentee_id>", methods=["GET"])
def match_user(mentee_id):
    mentee = User(mentee_id, "mentee", [(9, 12)], "en", ["AI"], 1, "career growth", "Gaza", "female")
    mentors = [
        User(1, "mentor", [(8, 13)], "en", ["AI", "Web"], 4, "help mentees", "Gaza", "male"),
        User(2, "mentor", [(14, 18)], "en", ["Data"], 2, "share skills", "Gaza", "female")
    ]

    service = MatchingService()
    best = service.find_best_match(mentee, mentors)

    return jsonify({
        "mentee_id": mentee.id,
        "matched_mentor_id": best.id
    })
