import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, make_response, request, render_template, Blueprint, session

import json
import os
import re


from utils import login_required

# Use the application default credentials.
cred = credentials.ApplicationDefault()

firebase_admin.initialize_app(cred)
db = firestore.client()

# app = Flask(__name__)
course = Blueprint('course', __name__)

# Define the regex_search filter function


def regex_search(value, pattern):
    return re.search(pattern, value) is not None

# Add the regex_search filter to the Jinja2 environment of the Blueprint


@course.app_template_filter('regex_search')
def regex_search_filter(value, pattern):
    return regex_search(value, pattern)


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
    course_level = ["foundation", "diploma",
                    "BSc degree", "BS degree"][int(course_id[2][2])-1]

    # store  the contents corresponding to the course
    course_ref = db.collection("ds_courses").document(
        course_id[1]).collection(course_id[2]).document("course")
    flag = False
    if not course_ref.get().exists:
        # new course, set flag to write metadata
        flag = True
    course_ref.set(data, merge=True)

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

    return make_response({"message": "file written successfully"}, 200)


@course.route("/course/<course_id>", methods=["GET"])
@login_required
def fetch_post(course_id):
    course_id = course_id.split("_")

    course_ref = db.collection(
        f"ds_courses/{course_id[1]}/{course_id[2]}").document("course")
    data = course_ref.get()

    if data.exists:
        if request.args.get("json"):
            return data.to_dict()
        return render_template("lecture.html", data=data.to_dict())

    else:
        return make_response({"message": "course not found"}, 404)

@course.route("/cache/<course_id>", methods=["GET"])
def cached_course_content(course_id):
    course_id = course_id.split("_")

    course_ref = db.collection(
        f"ds_courses/{course_id[1]}/{course_id[2]}").document("course")
    data = course_ref.get()

    if data.exists:
        content = data.to_dict()
        return make_response([content["week_wise"][i]["title"] for i in range(len(content["week_wise"]))])
    
    return make_response({"message": "course not found"}, 404)

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
    term_data = term_metadata_ref.get()
    if term_data.exists:
        term_data = term_data.to_dict()
        print(term_data)
        # bundle qualifier content while 
        # fetching term content
        if term_id[2] == "t":
            qualifier_metadata_ref = db.document(f"ds_courses/{term_id.replace('t', 'q')}")
            qualifier_data = qualifier_metadata_ref.get()
            if qualifier_data.exists:
                qualifier_data = qualifier_data.to_dict()
                term_data['course_metadata']['foundation'].update(qualifier_data['course_metadata']['foundation'])

        return render_template("course.html", data=term_data)

    else:
        return make_response({"message": "metadata for course not found"}, 404)


@course.route('/notes/<course_id>')
def notes(course_id):
    notes_ref = db.collection("ds_notes").document(course_id)
    notes = notes_ref.get()
    if notes.exists:
        return render_template('notes.html', data=notes.to_dict())

    else:
        return make_response({"message": "notes for course not found"}, 404)


@course.route('/pyq')
def pyq():
    pyq = {
        'Foundation': {
            'Quiz 1': {
                'Paper 1': '',
                'Paper 2': '',
                'Paper 3': ''
            },
            'Quiz 2': {
                'Paper 1': 'https://drive.google.com/file/d/1AbiYyDbqy0uBlnPcwTi4JdvGc0S29oFV/view?usp=sharing',
                'Paper 2': 'https://drive.google.com/file/d/1A_Tfw0qHWhxjtPoXtecYJ_w_JqRgy9LH/view?usp=sharing',
                'Paper 3': 'https://drive.google.com/file/d/1AWm0eKTBv8jk10C7_AMBXZHbeLLHRrsw/view?usp=sharing'
            },
            'End Term': {
                'Paper 1': '',
                'Paper 2': '',
                'Paper 3': ''
            }
        },
        'Diploma': {
            'Quiz 1': {
                'Paper 1': '',
                'Paper 2': '',
                'Paper 3': ''
            },
            'Quiz 2': {
                'Paper 1': 'https://drive.google.com/file/d/1AolZXOmI6CkkxBH5yh5K_hTgj3llxrje/view?usp=sharing',
                'Paper 2': 'https://drive.google.com/file/d/1AmCqwDF4YGVkupd12vEOHPMuz9QK-JoB/view?usp=sharing',
                'Paper 3': 'https://drive.google.com/file/d/1AfCdv2z9jYOT2Y_3PynGIJkEZ8ykHk0_/view?usp=sharing'
            },
            'End Term': {
                'Paper 1': '',
                'Paper 2': '',
                'Paper 3': ''
            }
        }
    }

    return render_template('pyq.html', data=pyq)
