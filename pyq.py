import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Initialize a new Firebase app with your service account credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)

# Access your Firestore database
db = firestore.client()

l = [
    {"title": "foundation",
        "quiz_1": {

            "jan_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "https://drive.google.com/file/d/1TDniJNsSrauTIou_7eITkZO6TOSCs_TQ/view?usp=sharing",
                    "paper 2": "https://drive.google.com/file/d/1uDL1s6jQ6BLtUp-9ssBtlKUUSWg_LGfj/view?usp=share_link",
                    "paper 3": "https://drive.google.com/file/d/1F0v3W3WNJqHovfv5UafaV1rzuilmaROq/view?usp=share_link",
                    "paper 4": "https://drive.google.com/file/d/1rQ4lBOgnAZYZ685J5or-2iC-Df-oAp3b/view?usp=share_link",
                    "paper 5": "https://drive.google.com/file/d/1vdfopjhuCSe5ifnYXJ5H0yCYhEK-TqPo/view?usp=sharing",
                    "paper 6": "https://drive.google.com/file/d/1bGvdF5e-BeAVPX88q57hq7lcRH3r0WhA/view?usp=share_link"

                }

            },
            "may_2022": {
                "shift": "Enter shift",
                "paper": {
                    "paper 1": "https://drive.google.com/file/d/1ZAW_4wBJ5gfN6eCkVogTIKLmAW05Z5OX/view?usp=sharing",
                    "paper 2": "https://drive.google.com/file/d/1uSBgxJqwe9QUT1lmGsweN4i5-Qwd35er/view?usp=share_link",
                    "paper 3": "https://drive.google.com/file/d/1zI-5W1GAg-krYGcUXo_veWnEd1_i2T3q/view?usp=sharing"


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
                    "paper 1": "https://drive.google.com/file/d/17pS8hnAfuMnJpJf2W2CDBHbF-G_0Qb3Q/view?usp=sharing",
                    "paper 2": "https://drive.google.com/file/d/1zJst0w42CFwP3Qo_dXCrZM4GdY-yn0e3/view?usp=sharing",
                    "paper 3": "https://drive.google.com/file/d/1uQ84iiwcKQ3cguGZse69lv_aXjdKO7tP/view?usp=sharing",
                    "paper 4": "https://drive.google.com/file/d/1f_r_08Xr6LiadXMkrnXualV5UDrRwrDn/view?usp=sharing",
                    "paper 5": "https://drive.google.com/file/d/1ESgm19hQLS2cwHhTdG9Pa49JKRdG_OIZ/view?usp=sharing",
                    "paper 6": "https://drive.google.com/file/d/1R5YZiBMKQF7X8DxXUcsEvNL9nsCgqOw7/view?usp=sharing"


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
                    "paper 1": "https://drive.google.com/file/d/1mbK0WosI6NkmDrw5DJK2sSMQpKA71x7e/view?usp=sharing",
                    "paper 2": "https://drive.google.com/file/d/1EwpI2rRL8dpuAU8ybdt23Vn86YmAKHcF/view?usp=sharing",
                    "paper 3": "https://drive.google.com/file/d/1ZOPNxFko_XbfwxeihptgP1qMcEo1TcLP/view?usp=sharing",
                    "paper 4": "https://drive.google.com/file/d/1IpJB-rV3yBps4Txnnp_8a3JsFFMsNz5C/view?usp=sharing"


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
