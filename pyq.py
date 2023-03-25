import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Initialize a new Firebase app with your service account credentials
cred = credentials.Certificate('firebase.json')
firebase_admin.initialize_app(cred)

# Access your Firestore database
db = firestore.client()

l = [
    {
        "level": "foundation",
        "Foundation": {
            "Quiz 1": {
                "Paper 1": "",
                "Paper 2": "",
                "Paper 3": ""
            },
            "Quiz 2": {
                "Paper 1": "https://drive.google.com/file/d/1AbiYyDbqy0uBlnPcwTi4JdvGc0S29oFV/view?usp=sharing",
                "Paper 2": "https://drive.google.com/file/d/1A_Tfw0qHWhxjtPoXtecYJ_w_JqRgy9LH/view?usp=sharing",
                "Paper 3": "https://drive.google.com/file/d/1AWm0eKTBv8jk10C7_AMBXZHbeLLHRrsw/view?usp=sharing"
            },
            "End Term": {
                "Paper 1": "",
                "Paper 2": "",
                "Paper 3": ""
            }
        }
    },
    {
        "level": "Diploma",
        "Diploma": {
            "Quiz 1": {
                "Paper 1": "",
                "Paper 2": "",
                "Paper 3": ""
            },
            "Quiz 2": {
                "Paper 1": "https://drive.google.com/file/d/1AolZXOmI6CkkxBH5yh5K_hTgj3llxrje/view?usp=sharing",
                "Paper 2": "https://drive.google.com/file/d/1AmCqwDF4YGVkupd12vEOHPMuz9QK-JoB/view?usp=sharing",
                "Paper 3": "https://drive.google.com/file/d/1AfCdv2z9jYOT2Y_3PynGIJkEZ8ykHk0_/view?usp=sharing"
            },
            "End Term": {
                "Paper 1": "",
                "Paper 2": "",
                "Paper 3": ""
            }
        }
    }
]

for course in l:
    # Use the level as the document ID
    pyq_ref = db.collection("ds_pyq").document(course['level'])
    # Update the document with the course data
    pyq_ref.set(course)
    print(json.dumps(course))
