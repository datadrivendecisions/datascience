# app.py
# This is the complete, consolidated backend application script.
# This version has been updated to use anonymized user data (nicknames instead of names).

import os
import requests
import random
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

# -----------------------------------------------------------------------------
# App Configuration
# -----------------------------------------------------------------------------

app = Flask(__name__)
# Replace with your actual GitHub Pages URL for production
CORS(app, resources={r"/api/*": {"origins": "https://YOUR-USERNAME.github.io"}})

# -----------------------------------------------------------------------------
# Baserow Configuration
# -----------------------------------------------------------------------------

BASEROW_API_URL = "https://api.baserow.io/api"
BASEROW_API_KEY = os.environ.get("BASEROW_API_KEY", "YOUR_BASEROW_API_KEY_PLACEHOLDER")
BASEROW_DATABASE_ID = 12345  # REPLACE with your Database ID
BASEROW_TABLE_IDS = {
    "users": 10001,
    "courses": 10002,
    "activities": 10003,
    "learning_objectives": 10004,
    "expert_topics": 10005,
    "quizzes": 10006,
    "questions": 10007,
    "submissions": 10008,
    "mastery_scores": 10009,
}

# -----------------------------------------------------------------------------
# Core Logic / Services
# -----------------------------------------------------------------------------


def calculate_mastery(prior_alpha, prior_beta, num_correct, num_incorrect):
    if num_correct < 0 or num_incorrect < 0:
        raise ValueError("Number of correct/incorrect answers cannot be negative.")
    posterior_alpha = prior_alpha + num_correct
    posterior_beta = prior_beta + num_incorrect
    mastery = posterior_alpha / (posterior_alpha + posterior_beta)
    return {
        "alpha": posterior_alpha,
        "beta": posterior_beta,
        "mastery_estimate": round(mastery, 4),
    }


def get_class_roster(activity_id):
    """
    Fetches the list of students for a given activity.
    Updated to return anonymous 'nickname' and 'avatar_url' instead of real names.
    """
    print(f"Fetching roster for activity {activity_id}...")
    return [
        {
            "id": 101,
            "nickname": "PixelPioneer",
            "avatar_url": "https://placehold.co/100x100/A9C5E8/333333?text=PP",
        },
        {
            "id": 102,
            "nickname": "DataDynamo",
            "avatar_url": "https://placehold.co/100x100/E8A9A9/333333?text=DD",
        },
        {
            "id": 103,
            "nickname": "QueryQueen",
            "avatar_url": "https://placehold.co/100x100/A9E8B8/333333?text=QQ",
        },
        {
            "id": 104,
            "nickname": "AlgoAce",
            "avatar_url": "https://placehold.co/100x100/E8D2A9/333333?text=AA",
        },
        {
            "id": 105,
            "nickname": "SyntaxSeeker",
            "avatar_url": "https://placehold.co/100x100/C1A9E8/333333?text=SS",
        },
        {
            "id": 106,
            "nickname": "LogicLord",
            "avatar_url": "https://placehold.co/100x100/A9E8E8/333333?text=LL",
        },
        {
            "id": 107,
            "nickname": "VectorViper",
            "avatar_url": "https://placehold.co/100x100/E8A9D2/333333?text=VV",
        },
        {
            "id": 108,
            "nickname": "KernelKnight",
            "avatar_url": "https://placehold.co/100x100/C5E8A9/333333?text=KK",
        },
        {
            "id": 109,
            "nickname": "MatrixMaverick",
            "avatar_url": "https://placehold.co/100x100/E8B8A9/333333?text=MM",
        },
    ]


def get_expert_topics(activity_id):
    print(f"Fetching expert topics for activity {activity_id}...")
    return [
        {"id": 201, "title": "K-Means Clustering"},
        {"id": 202, "title": "DBSCAN"},
        {"id": 203, "title": "Hierarchical Clustering"},
    ]


def assign_expert_groups(student_roster, expert_topics):
    if not expert_topics:
        return {}
    shuffled_students = random.sample(student_roster, len(student_roster))
    expert_groups = {topic["title"]: [] for topic in expert_topics}
    topic_titles = list(expert_groups.keys())
    for i, student in enumerate(shuffled_students):
        assigned_topic_title = topic_titles[i % len(topic_titles)]
        expert_groups[assigned_topic_title].append(student)
    return expert_groups


def assign_jigsaw_groups(expert_groups):
    if not expert_groups:
        return {}
    num_jigsaw_groups = max((len(s) for s in expert_groups.values()), default=0)
    jigsaw_groups = {f"Jigsaw Group {i+1}": [] for i in range(num_jigsaw_groups)}
    for topic, students in expert_groups.items():
        for i, student in enumerate(students):
            student_with_topic = student.copy()
            student_with_topic["expert_topic"] = topic
            jigsaw_groups[f"Jigsaw Group {i+1}"].append(student_with_topic)
    return jigsaw_groups


# --- Baserow Helper ---
def baserow_api_request(method, table_name, row_id=None, json_data=None):
    table_id = BASEROW_TABLE_IDS.get(table_name)
    if not table_id:
        return {"error": f"Table '{table_name}' not found"}, 400
    url = (
        f"{BASEROW_API_URL}/database/rows/table/{table_id}/{row_id if row_id else ''}/"
    )
    headers = {
        "Authorization": f"Token {BASEROW_API_KEY}",
        "Content-Type": "application/json",
    }
    try:
        response = requests.request(
            method.upper(), url, headers=headers, json=json_data
        )
        response.raise_for_status()
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}, 500


# --- API Routes ---
@app.route("/api/activities/<int:activity_id>/start", methods=["POST"])
def start_activity(activity_id):
    try:
        student_roster = get_class_roster(activity_id)
        expert_topics = get_expert_topics(activity_id)
        if not student_roster or not expert_topics:
            return jsonify({"error": "Roster or topics not found"}), 404
        expert_groups = assign_expert_groups(student_roster, expert_topics)
        jigsaw_groups = assign_jigsaw_groups(expert_groups)
        return (
            jsonify(
                {
                    "message": "OK",
                    "expert_groups": expert_groups,
                    "jigsaw_groups": jigsaw_groups,
                }
            ),
            200,
        )
    except Exception as e:
        return (
            jsonify({"error": "An unexpected error occurred", "details": str(e)}),
            500,
        )


# ... other placeholder routes ...
@app.route("/api/activities", methods=["POST"])
def create_activity():
    return jsonify({"message": "Activity created placeholder"}), 201


@app.route("/api/quizzes", methods=["POST"])
def create_quiz():
    return jsonify({"message": "Quiz created placeholder"}), 201


if __name__ == "__main__":
    app.run(debug=True)
