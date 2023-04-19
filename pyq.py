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
        "Sem1 CT": {
            "quiz-1": {
                "jan_2022": {
                 "paper": {}
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1wPkl9v6m1JcirpVJqcl97K0RAezB2MML/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1H8YpCkYkxTwk8kdIvgtUepMEfesZbd1h/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1nLYdd8YaQqNUqC_9keSLiBy0qZotwKln/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1ZWu7cjUzDPLlbrDsSG5rleHIHClwcraS/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1wPkl9v6m1JcirpVJqcl97K0RAezB2MML/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1H8YpCkYkxTwk8kdIvgtUepMEfesZbd1h/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1nLYdd8YaQqNUqC_9keSLiBy0qZotwKln/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1ZWu7cjUzDPLlbrDsSG5rleHIHClwcraS/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "jan_2022": {
                    "paper": {}
                }
            }
        },
        "Sem1 English1": {
            "quiz-1": {
                "jan_2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1kD3kvPyaZiGPUOC_dRL1XIK1Ekv8MhYF/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1Ml0N1oaK9I1mHpTiB4_RyP2RrV6ScR8S/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1vYwOG4EwHVyP-uZnT0J5YUcsvc9KHGzq/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1hnz3xlozYgqrx4PKZPUYeYHaoRMlmaKu/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1kD3kvPyaZiGPUOC_dRL1XIK1Ekv8MhYF/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1Ml0N1oaK9I1mHpTiB4_RyP2RrV6ScR8S/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1vYwOG4EwHVyP-uZnT0J5YUcsvc9KHGzq/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1hnz3xlozYgqrx4PKZPUYeYHaoRMlmaKu/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "jan_2022": {
                    "paper": {}
                }
            }
        },
        "Sem1 Maths1": {
            "quiz-1": {
                "jan_2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1q_bohj_DgewQOY_sTiHQZhPMgP85yBP4/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1pySmiPYlVUkH4R1LdWDwvPCbGec10TVQ/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1F8ddKEfDQrKPxHRu6UwrTpbjCn523nb7/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1HBfd37LVqPfazNaGhIF5H1u1mTR8yrLO/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1q_bohj_DgewQOY_sTiHQZhPMgP85yBP4/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1pySmiPYlVUkH4R1LdWDwvPCbGec10TVQ/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1F8ddKEfDQrKPxHRu6UwrTpbjCn523nb7/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1HBfd37LVqPfazNaGhIF5H1u1mTR8yrLO/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "jan_2022": {
                    "paper": {}
                }
            }
        },
        "Sem1 Statistics1": {
            "quiz-1": {
                "jan_2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1jiWhGbFrJv9wfJAqE87y1U_Mtn6-Q5rY/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1rAQmZP6rtKK5suNr6WDWkRI8CGx21H3f/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1-2fkHQPwvV8AIqVI59rL8KHCfkuBludl/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1RkM6b2YI8jnsA90sQ9-fIepIrBGhUP1i/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1jiWhGbFrJv9wfJAqE87y1U_Mtn6-Q5rY/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1rAQmZP6rtKK5suNr6WDWkRI8CGx21H3f/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1-2fkHQPwvV8AIqVI59rL8KHCfkuBludl/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1RkM6b2YI8jnsA90sQ9-fIepIrBGhUP1i/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "jan_2022": {
                    "paper": {}
                }
            }
        },
        "Sem2 English2": {
            "quiz-1": {
                "jan_2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/127C9eGqzivymuyVNdVvQeN6FIcN5YT_-/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1ibGZNAibr6crlk8v-toliBZJ1DnMXGsx/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1Acx8UgNUXhHUEsG4dvuz4EKBSVyTt6Sw/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1SiNDUuFre93thyQ50JCA5OTUEp7ODQgl/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/127C9eGqzivymuyVNdVvQeN6FIcN5YT_-/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1ibGZNAibr6crlk8v-toliBZJ1DnMXGsx/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1Acx8UgNUXhHUEsG4dvuz4EKBSVyTt6Sw/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1SiNDUuFre93thyQ50JCA5OTUEp7ODQgl/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "jan_2022": {
                    "paper": {}
                }
            }
        },
        "Sem2 Statistics2": {
            "quiz-1": {
                "jan_2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1z9SskGSdCmXEY-Z48VjGB1sjMUlV7tSv/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1gNI0nXPkGN4cgidSTBtclscgEmS04y_U/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/14s0SscsX3c3RLm_pgMCeJ7j7_sdgkcL6/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1Fk0iYAomKpeVgPAXhDteN8pDDpJsPjwu/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1z9SskGSdCmXEY-Z48VjGB1sjMUlV7tSv/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1gNI0nXPkGN4cgidSTBtclscgEmS04y_U/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/14s0SscsX3c3RLm_pgMCeJ7j7_sdgkcL6/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1Fk0iYAomKpeVgPAXhDteN8pDDpJsPjwu/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "jan_2022": {
                    "paper": {}
                }
            }
        },
        "Sem1 Maths2": {
            "quiz-1": {
                "jan_2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {}
                },
                "Nov 2022": {
                    "paper": {}
                }
            },
            "endterm": {
                "jan_2022": {
                    "paper": {}
                }
            }
        }
    },
    {
        "level": "diploma",
        "subject 1": {
            "quiz-1": {
                "jan_2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {}
                },
                "Nov 2022": {
                    "paper": {}
                }
            },
            "endterm": {
                "jan_2022": {
                    "paper": {}
                }
            }
        },
        "subject 2": {
            "quiz-1": {
                "jan_2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {}
                },
                "Nov 2022": {
                    "paper": {}
                }
            },
            "endterm": {
                "jan_2022": {
                    "paper": {}
                }
            }
        }
    },
    {
        "level": "degre",
        "subject 1": {
            "quiz-1": {
                "jan_2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {}
                },
                "Nov 2022": {
                    "paper": {}
                }
            },
            "endterm": {
                "jan_2022": {
                    "paper": {}
                }
            }
        },
        "subject 2": {
            "quiz-1": {
                "jan_2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {}
                },
                "Nov 2022": {
                    "paper": {}
                }
            },
            "endterm": {
                "jan_2022": {
                    "paper": {}
                }
            }
        }
    }
]

for course in l:
    level = course['level']
    print(level, " level \n\n\n")
    for key, value in course.items():
        if key != "level":
            # print(key, "\n", value)
            # ======%%%%%%%%%%%%%%%%%=======%%%%%%%%%%%%%%%%%====%%%%%%%%%%%%%%%%%==
            level_ref = db.collection("ds_pyq").document(level).collection(key)

            for quiz_key, quiz_value in value.items():
                quiz_ref = level_ref.document(quiz_key)
                quiz_ref.set(quiz_value)
                print(json.dumps(quiz_value), "\n\n\n")

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
