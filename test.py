# d1 = {'term': '23t1', 'course_metadata': {'foundation': {'hs1002': 'Jan 2023 - English II', 'ma1003': 'Jan 2023 - Mathematics II', 'ma1004': 'Jan 2023 - Statistics II', 'cs1002': 'Jan 2023 - Python'}, 'degree': {'gn3001': 'Jan 2023 - Strategies for Professional Growth', 'cs3001': 'Jan 2023 - Software Engineering'}, 'diploma': {'se2002': 'Jan 2023 - TDS', 'cs2007': 'Jan 2023 - MLT', 'cs2004': 'Jan 2023 - ML Foundations', 'ms2001': 'Jan 2023 - BDM', 'ms2002': 'Jan 2023 - BA', 'cs2008': 'Jan 2023 - MLP', 'se2001': 'Jan 2023 - System Commands', 'cs2006': 'Jan 2023 - MAD II', 'ma2001': 'Jan 2023 - Linear Statistical Models', 'cs2005': 'Jan 2023 - JAVA', 'cs2003': 'Jan 2023 - MAD I', 'cs2002': 'Jan 2023 - PDSA', 'cs2001': 'Jan 2023 - DBMS'}}, 'prefix': 'ns'}

# d2 = {'term': '23q1', 'course_metadata': {'foundation': {'cs1001': 'Jan Qualifier - 2023: CT', 'ma1002': 'Jan Qualifier - 2023: Statistics I', 'hs1001': 'Jan Qualifier - 2023: English I', 'ma1001': 'Jan Qualifier - 2023: Mathematics I'}}, 'prefix': 'ns'}

# d1['course_metadata']['foundation'].update(d2['course_metadata']['foundation'])

# print(d1)


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
        "subject 1": {

            "quiz_1": {
                "quiz": "quiz_1",
                "jan_2022": {

                    "paper": {
                        "paper 1": "",
                        "paper 2": "",
                        "paper 3": ""
                    }
                }

            },
            "quiz_2": {
                "quiz": "quiz_1",
                "jan_2022": {

                    "paper": {
                        "paper 1": "",
                        "paper 2": "",
                        "paper 3": ""
                    }
                }

            },
            "endterm": {
                "quiz": "quiz_1",
                "jan_2022": {

                    "paper": {
                        "paper 1": "",
                        "paper 2": "",
                        "paper 3": ""
                    }
                }

            }
        },
        "subject 2": {

            "quiz_1": {
                "quiz": "quiz_1",
                "jan_2022": {

                    "paper": {
                        "paper 1": "",
                        "paper 2": "",
                        "paper 3": ""
                    }
                }

            },
            "quiz_2": {
                "quiz": "quiz_2",
                "jan_2022": {

                    "paper": {
                        "paper 1": "",
                        "paper 2": "",
                        "paper 3": ""
                    }
                }

            },
            "endterm": {
                "quiz": "endterm",
                "jan_2022": {

                    "paper": {
                        "paper 1": "",
                        "paper 2": "",
                        "paper 3": ""
                    }
                }

            }
        }

    },
    {
        "level": "diploma",
        "subject 1": {

            "quiz_1": {
                "quiz": "quiz_1",
                "jan_2022": {

                    "paper": {
                        "paper 1": "",
                        "paper 2": "",
                        "paper 3": ""
                    }
                }

            },
            "quiz_2": {
                "quiz": "quiz_1",
                "jan_2022": {

                    "paper": {
                        "paper 1": "",
                        "paper 2": "",
                        "paper 3": ""
                    }
                }

            },
            "endterm": {
                "quiz": "quiz_1",
                "jan_2022": {

                    "paper": {
                        "paper 1": "",
                        "paper 2": "",
                        "paper 3": ""
                    }
                }

            }
        },
        "subject 2": {

            "quiz_1": {
                "quiz": "quiz_1",
                "jan_2022": {

                    "paper": {
                        "paper 1": "",
                        "paper 2": "",
                        "paper 3": ""
                    }
                }

            },
            "quiz_2": {
                "quiz": "quiz_2",
                "jan_2022": {

                    "paper": {
                        "paper 1": "",
                        "paper 2": "",
                        "paper 3": ""
                    }
                }

            },
            "endterm": {
                "quiz": "endterm",
                "jan_2022": {

                    "paper": {
                        "paper 1": "",
                        "paper 2": "",
                        "paper 3": ""
                    }
                }

            }
        }

    },
    {
        "level": "degre",
        "subject 1": {

            "quiz_1": {
                "quiz": "quiz_1",
                "jan_2022": {

                    "paper": {
                        "paper 1": "",
                        "paper 2": "",
                        "paper 3": ""
                    }
                }

            },
            "quiz_2": {
                "quiz": "quiz_1",
                "jan_2022": {

                    "paper": {
                        "paper 1": "",
                        "paper 2": "",
                        "paper 3": ""
                    }
                }

            },
            "endterm": {
                "quiz": "quiz_1",
                "jan_2022": {

                    "paper": {
                        "paper 1": "",
                        "paper 2": "",
                        "paper 3": ""
                    }
                }

            }
        },
        "subject 2": {

            "quiz_1": {
                "quiz": "quiz_1",
                "jan_2022": {

                    "paper": {
                        "paper 1": "",
                        "paper 2": "",
                        "paper 3": ""
                    }
                }

            },
            "quiz_2": {
                "quiz": "quiz_2",
                "jan_2022": {

                    "paper": {
                        "paper 1": "",
                        "paper 2": "",
                        "paper 3": ""
                    }
                }

            },
            "endterm": {
                "quiz": "endterm",
                "jan_2022": {

                    "paper": {
                        "paper 1": "",
                        "paper 2": "",
                        "paper 3": ""
                    }
                }

            }
        }

    }

]

for course in l:
    level = course['level']
    print(level, "this is level")
    for subject in course:
        if subject != "level":
            print(subject)
            level_ref = db.collection("ds_pyq").document(
                level).collection(subject)
            # for sub in su:
            #  print(sub)
        for quiz_key, quiz_value in course.items():
            if quiz_key != 'level':
                quiz_ref = level_ref.document(quiz_key)
                quiz_ref.set(quiz_value)
                print(json.dumps(quiz_value))


# for course in l:
#     # Use the level as the document ID
#     level = course['level']
#     level_ref = db.collection("ds_pyq").document(level)

#     # Store quiz data under each level document
        # for quiz_key, quiz_value in course.items():
        #     if quiz_key != 'level':
        #         quiz_ref = level_ref.collection(quiz_key).document(quiz_key)
        #         quiz_ref.set(quiz_value)
        #         print(json.dumps(quiz_value))
