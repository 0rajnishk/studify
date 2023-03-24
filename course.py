import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, make_response, request, render_template, Blueprint

import json
import os

from utils import login_required

# Use the application default credentials.
cred = credentials.ApplicationDefault()

firebase_admin.initialize_app(cred)
db = firestore.client()

# app = Flask(__name__)
course = Blueprint('course', __name__, template_folder='templates')


# route to intake course
@course.route("/course", methods=["POST"])
def ingest_course():
    # extract data from the request
    data = request.get_json()

    # sanity check to confirm Notebook version
    try:
        assert data['ALE_VERSION'] == os.environ.get("ALE_VERSION")
        del data['ALE_VERSION']
    except AssertionError:
        return make_response({"message": "Please update your script"}, 412)

    # figure out the course from the data
    course_id = data['course_id'].split("_")
    course_level = ["foundation", "diploma", "BSc degree", "BS degree"][int(course_id[2][2])-1]

    # store  the contents corresponding to the course
    course_ref = db.collection("ds_courses").document(
        course_id[1]).collection(course_id[2]).document("course")
    flag = False
    if not course_ref.get().exists:
        # new course, set flag to write metadata
        flag = True
    course_ref.set(data)

    if flag:
        print("writing metadata")
        metadata_ref = db.document(f"ds_courses/{course_id[1]}")
        if metadata_ref.get().exists:
            print("term reference exists")
            metadata_ref.update({
                f"course_metadata.{course_level}.{course_id[2]}": data['title']
            })
        else:
            metadata_ref.set({
                "prefix": course_id[0],
                "term": course_id[1],
                "course_metadata": {
                    course_level: {
                        course_id[2]: data['title']
                    }
                }
            })

    return make_response({"message":"file written successfully"}, 200)


@course.route("/course/<course_id>", methods=["GET"])
@login_required
def fetch_post(course_id):
    course_id = course_id.split("_")

    course_ref = db.collection(
        f"ds_courses/{course_id[1]}/{course_id[2]}").document("course")
    data = course_ref.get()

    if data.exists:
        return render_template("lecture.html", data=data.to_dict())

    else:
        return make_response({"message":"course not found"}, 404)


@course.route("/terms", methods=["GET"])
@login_required
def list_terms():
    terms = []
    terms_ref = db.collection("ds_courses")
    for document in terms_ref.list_documents():
        terms.append(document.id)
    return make_response(sorted(terms, reverse=True), 200)


@course.route("/term/<term_id>", methods=["GET"])
@login_required
def get_term_metadata(term_id):
    term_metadata_ref = db.document(f"ds_courses/{term_id}")
    data = term_metadata_ref.get()
    if data.exists:
        return render_template("course.html", data=data.to_dict())

    else:
        return make_response({"message":"metadata for course not found"}, 404)


@course.route('/notes/<course_id>')
def notes(course_id):
    notes_ref = db.collection("ds_notes").document(course_id)
    notes = notes_ref.get()
    if notes.exists:
        return render_template('notes.html', data=notes.to_dict())
        
    else:
        return make_response({"message": "notes for course not found"}, 404)