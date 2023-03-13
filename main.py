import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, make_response, request

import json

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

    # figure out the course from the data
    course_id = data['course_id'].split("_")
    course_level = ["foundation", "diploma", "degree"][int(course_id[2][3])] 

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

if __name__ == "__main__":
    app.run(debug=True, port = 5000)