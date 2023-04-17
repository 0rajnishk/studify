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
    {"title": "foundation",
        "quiz_1": {

            "jan_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            },
            "may_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            },
            "dec_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            }
        },
        "quiz_2": {

            "jan_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            },
            "may_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            },
            "dec_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            }
        },
        "endterm": {

            "jan_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            },
            "may_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            },
            "dec_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            }
        }
     },
    {"title": "diploma",
        "quiz_1": {

            "jan_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            },
            "may_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            },
            "dec_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            }
        },
        "quiz_2": {

            "jan_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            },
            "may_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            },
            "dec_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            }
        },
        "endterm": {

            "jan_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            },
            "may_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            },
            "dec_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            }
        }
     },
    {"title": "degree",
        "quiz_1": {

            "jan_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            },
            "may_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            },
            "dec_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            }
        },
        "quiz_2": {

            "jan_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            },
            "may_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            },
            "dec_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            }
        },
        "endterm": {

            "jan_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            },
            "may_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            },
            "dec_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "upload_question_drive_link",
                    "paper 2": "upload_question_drive_link",
                    "paper 3 ": "upload_question_drive_link"


                }

            }
        }
     }
]


for course in l:
    # Use the level as the document ID
    pyq_ref = db.collection("ds_pyq").document(course['title'])
    # Update the document with the course data
    pyq_ref.update(course)
    print(json.dumps(course))
