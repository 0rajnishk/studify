import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, make_response, request, render_template

import json
import os

# Use the application default credentials.
cred = credentials.ApplicationDefault()

firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

# route to intake course
@app.route("/course", methods=["POST"])
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
    course_level = ["foundation", "diploma", "degree"][int(course_id[2][2])-1] 

    # store  the contents corresponding to the course
    course_ref = db.collection("ds_courses").document(course_id[1]).collection(course_id[2]).document("course")
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


    return make_response("file written successfully", 200)

@app.route("/course/<course_id>", methods=["GET"])
def fetch_post(course_id):
    course_id = course_id.split("_")

    # read the contents of {course_id}.json
    course_ref = db.collection(f"ds_courses/{course_id[1]}/{course_id[2]}").document("course")
    data = course_ref.get()
    
    if data.exists:
        return data.to_dict()
    else:
        return make_response("course not found", 404)

@app.route("/terms", methods=["GET"])
def list_terms():
    terms = []
    terms_ref = db.collection("ds_courses")
    for document in terms_ref.list_documents():
        terms.append(document.id)
    return make_response(sorted(terms, reverse=True), 200)

@app.route("/term/<term_id>", methods=["GET"])
def get_term_metadata(term_id):
    term_metadata_ref = db.document(f"ds_courses/{term_id}")
    data = term_metadata_ref.get()
    if data.exists:
        return data.to_dict()
    else:
        return make_response({"metadata for course not found"}, 404)

@app.route("/test")
def test():
    data = {
    "course_metadata": {
        "degree": {
            "cs3003": "Degree Test"
        },
        "diploma": {
            "cs2002": "Diploma Test"
        },
        "foundation": {
            "cs1002": "Jan 2023 - Python",
            "hs1002": "Jan 2023 - English II",
            "ma1003": "Jan 2023 - Mathematics II"
        }
    },
    "prefix": "ns",
    "term": "23t1"
}
    return render_template("test.html", data=data)

if __name__ == "__main__":
    app.run(debug=True, port = 5000)