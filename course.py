from flask import Blueprint, render_template
from flask import jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, jsonify, make_response, request, render_template, Blueprint, session

import json
import os
import re
from datetime import datetime
from typing import Union


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
        course_ref.set(data)
    else:
        course_ref.update(
            {"week_wise": firestore.ArrayUnion(data['week_wise'])})

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

    return make_response([], 404)


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
            qualifier_metadata_ref = db.document(
                f"ds_courses/{term_id.replace('t', 'q')}")
            qualifier_data = qualifier_metadata_ref.get()
            if qualifier_data.exists:
                qualifier_data = qualifier_data.to_dict()
                term_data['course_metadata']['foundation'].update(
                    qualifier_data['course_metadata']['foundation'])

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
@login_required
def index():
    return render_template('pyq_choose.html')


@course.route('/get_options/<category>')
def get_options(category):
    metadata_ref = db.document(f"ds_courses/23t1")
    data = metadata_ref.get()
    # course_id = course_id.split("_")
    if data.exists:
        data = data.to_dict()
        options = []
        course_metadata = data["course_metadata"]

        for level in course_metadata:
            print(f"\n{category} Courses:")
            for course_id, subject in course_metadata[category].items():
                subject = (subject.split('-')[-1])
                if level:
                    options.append({'value': course_id, 'label': subject})
            return options
    else:
        return f"No data found"

# course = Blueprint('course', __name__)


def sort_by_key(value):
    if isinstance(value, dict):
        return sorted(value.items())
    elif isinstance(value, (list, tuple)):
        return sorted(value)
    else:
        return value


@course.app_template_filter('sort_by_key')
def sort_by_key_filter(value):
    return sort_by_key(value)


def format_date(date_string: str) -> str:
    if date_string == 'quiz':
        return datetime.now().strftime('%b %Y')
    else:
        date_obj = datetime.strptime(date_string, '%b %Y')
        return date_obj.strftime('%b %Y')


@course.app_template_filter('format_date')
def format_date_filter(date_string: str) -> str:
    return format_date(date_string)


@course.route('/pyq/<level>/<subject>/<quiz_key>')
def pyq(level, subject, quiz_key):
    doc_ref = db.collection("ds_pyq").document(
        level).collection(subject).document(quiz_key)
    doc = doc_ref.get()
    if doc.exists:
        quiz_data = doc.to_dict()
        print(quiz_data)
        sorted_data = sorted(quiz_data.items(), key=lambda x: datetime.now(
        ) if x[0] == 'quiz' else datetime.strptime(x[0], '%b %Y'), reverse=True)

        # return jsonify(sorted_data)

        return render_template('pyq.html', data=sorted_data)
    else:
        return f"No data found for {level}/{quiz_key}"
