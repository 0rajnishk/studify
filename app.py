import json
import re
from flask import Flask, jsonify, make_response, render_template, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from user_agents import parse

cred = credentials.Certificate('static/cred/studify2.0.json')

firebase_admin.initialize_app(cred)
db = firestore.client()
# app = Flask(__name__)


app = Flask(__name__)


def regex_search(value, pattern):
    return re.search(pattern, value) is not None

@app.template_filter('regex_search') 
def regex_search_filter(value, pattern):
    return regex_search(value, pattern)
# above lines are for trial



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashbord():
    active_page = 'dashboard'
    return render_template ('dashboard.html', active_page=active_page)

@app.route('/settings')
def settings():
    active_page = 'settings'
    return render_template('settings.html', active_page=active_page)

@app.route('/pyq')
def pyqchoose():
    active_page = 'pyq'
    return render_template('pyqchoose.html', active_page=active_page)

@app.route('/notes')
def noteschoose():
    active_page = 'notes'
    return render_template('noteschoose.html', active_page = active_page)
@app.route('/notes/<course_id>')
def notes(course_id):
    active_page = 'notes'
    notes_ref = db.collection("ds_notes").document(course_id)
    notes = notes_ref.get()
    if notes.exists:
        notesexist = True
    else:
        notesexist = False
    return render_template('notes.html', data=notes.to_dict(), notesexist = notesexist, active_page=active_page)

@app.route('/shop')
def shop():
    active_page = 'shop'
    return render_template('shop.html', active_page = active_page)

@app.route('/exam_eval')
def exam():
    active_page = 'exam'
    return render_template('exam.html' , active_page = active_page)

@app.route('/Fmarks')
def Fmarks():
    return render_template('finalcal.html')



# ===================YouTube Lecture Player =========================================
@app.route("/course/<course_id>", methods=["GET"])
def fetch_post(course_id):
    user_agent_string = request.user_agent.string
    user_agent = parse(user_agent_string)

    is_mobile = user_agent.is_mobile
    is_tablet = user_agent.is_tablet
    course_id = course_id.split("_")
    if course_id[-1] == 'hs1001' or course_id[-1] == 'cs1001':
        course_id[1] = course_id[1].replace('t', 'q')

    course_ref = db.collection(
        f"ds_courses/{course_id[1]}/{course_id[2]}").document("course")
    data = course_ref.get()

    if data.exists:
        if request.args.get("json"):
            return jsonify(data.to_dict())

        if is_mobile or is_tablet:
            template_name = "lecture-mobile.html"
        else:
            template_name = "lecture-desk.html"

        return render_template(template_name, data=data.to_dict())

    else:
        return make_response({"message": "course not found"}, 404)
# ==========================Previous Year Questions ==============
@app.route('/pyq/<subject>/<quiz>')
def pyq(subject, quiz):
    active_page = 'pyq'
    doc_ref = db.collection('ds_courses').document('23t1').collection(subject).document('pyq')
    doc = doc_ref.get()
    
    if doc.exists:
        doc_data = doc.to_dict()
        
        if quiz in doc_data:
            quiz_data = doc_data[quiz]
            return render_template('pyq.html', data=quiz_data, notesexist=True)
        else:
            notesexist = False
    else:
        notesexist = False
        
    return render_template('pyq.html', notesexist=notesexist, active_page=active_page)

if __name__ == '__main__':
    app.run(debug=True)
