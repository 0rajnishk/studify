import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Initialize a new Firebase app with your service account credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)

# Access your Firestore database
db = firestore.client()

data = [
    {
        "level": "foundation",
        "cs1001": {
            "quiz-1": {
                "jan_2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1G6j7KKrGlaSMVZ1_GG7eYBlwMiSxivSO/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1PLh9LcUBhgRA5Yp6zDz4j5wlUQp3ZPbV/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/17nt0LxktlpUrnA1J4npjvghAHMH562ca/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/17ZbiSzgxuNPD6_fLoDG_pfVyoe_ZZ-xa/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1G6j7KKrGlaSMVZ1_GG7eYBlwMiSxivSO/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1PLh9LcUBhgRA5Yp6zDz4j5wlUQp3ZPbV/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/17nt0LxktlpUrnA1J4npjvghAHMH562ca/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/17ZbiSzgxuNPD6_fLoDG_pfVyoe_ZZ-xa/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "jan_2022": {
                    "paper": {}
                }
            }
        },
        "hs1001": {
            "quiz-1": {
                "jan_2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1ZcQYNnngToREO-aF_1gYs43KKvmOMgyO/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1ApBxWmNXsefrhY1L9LXZCbaVrHpOWgDA/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1KUzeD5DI5vTaBbLdhg8zuk3Bz2SdUFCE/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/19sQJllYUh0JTMjiD3Kvn-I7vPhAkfk0l/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1ZcQYNnngToREO-aF_1gYs43KKvmOMgyO/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1ApBxWmNXsefrhY1L9LXZCbaVrHpOWgDA/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1KUzeD5DI5vTaBbLdhg8zuk3Bz2SdUFCE/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/19sQJllYUh0JTMjiD3Kvn-I7vPhAkfk0l/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "jan_2022": {
                    "paper": {}
                }
            }
        },
        "ma1001": {
            "quiz-1": {
                "jan_2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1PU9vyToPcPQ_ygDI9pWhymjQfa5ILdoZ/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/15QHJf8_I5IfQs3KqteiGDBdt8eyo0YrA/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1DykccO3F6ZNU5LJd0N5pcVqNzAXypY-z/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1mPFU9R0FTjmF5x57qe7yqYYYxgOuHArg/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1PU9vyToPcPQ_ygDI9pWhymjQfa5ILdoZ/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/15QHJf8_I5IfQs3KqteiGDBdt8eyo0YrA/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1DykccO3F6ZNU5LJd0N5pcVqNzAXypY-z/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1mPFU9R0FTjmF5x57qe7yqYYYxgOuHArg/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "jan_2022": {
                    "paper": {}
                }
            }
        },
        "ma1002": {
            "quiz-1": {
                "jan_2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1U1KiPhULl9EWu5mZGnLdHgVPxd9FY22a/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1ZZhIkn3mYGI-SHEWn4-1H_k9cfdPxOyz/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1whiemJE119EUXWmHYdGpL7ZEzV7OIS7p/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1iAXAXzCJyhYcn8L9rgVjqT4qra7tEb7S/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1U1KiPhULl9EWu5mZGnLdHgVPxd9FY22a/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1ZZhIkn3mYGI-SHEWn4-1H_k9cfdPxOyz/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1whiemJE119EUXWmHYdGpL7ZEzV7OIS7p/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1iAXAXzCJyhYcn8L9rgVjqT4qra7tEb7S/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "jan_2022": {
                    "paper": {}
                }
            }
        },
        "hs1002": {
            "quiz-1": {
                "jan_2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1RQixMuPci9_dmDtQMwolJ2wWb1KW8ABQ/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1mCVEQlKdmyvTsfy-G34MDYyCBHAWLPco/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1jHa3CpQon1LUhwg37Z2z7bJN43dtekcH/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1rydIfh_2jL2VcNxCTzjqH_KmxbsiXUw6/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1RQixMuPci9_dmDtQMwolJ2wWb1KW8ABQ/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1mCVEQlKdmyvTsfy-G34MDYyCBHAWLPco/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1jHa3CpQon1LUhwg37Z2z7bJN43dtekcH/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1rydIfh_2jL2VcNxCTzjqH_KmxbsiXUw6/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "jan_2022": {
                    "paper": {}
                }
            }
        },
        "ma1004": {
            "quiz-1": {
                "jan_2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1l8zF-nlimE1lzvINL7i3nbADBg4ngULU/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/16hwM7gSFP4FnoM71dzrMTtLQKMz6Xr9w/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1wAGbtF7pw6k5--yEHxz2Wl2UcDiPNCF6/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1qF-cL8rjYWlZjVnFzrkbOYiiyfHgtwj2/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1l8zF-nlimE1lzvINL7i3nbADBg4ngULU/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/16hwM7gSFP4FnoM71dzrMTtLQKMz6Xr9w/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1wAGbtF7pw6k5--yEHxz2Wl2UcDiPNCF6/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1qF-cL8rjYWlZjVnFzrkbOYiiyfHgtwj2/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "jan_2022": {
                    "paper": {}
                }
            }
        },
        "ma1003": {
            "quiz-1": {
                "jan_2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1UFdrtsFoMu2Lf80_o8IWt0lFPmP-HCC5/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/19bZ_s55gDUGY0vrLva09dnMsqo01QDmX/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1QN3N-B_Y8uqpPZMI0NYBU6S5aXmbR0xQ/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1rwHS2ySvHUnPGRZSv8JXaSZxa0rtj0rT/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1UFdrtsFoMu2Lf80_o8IWt0lFPmP-HCC5/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/19bZ_s55gDUGY0vrLva09dnMsqo01QDmX/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1QN3N-B_Y8uqpPZMI0NYBU6S5aXmbR0xQ/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1rwHS2ySvHUnPGRZSv8JXaSZxa0rtj0rT/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "jan_2022": {
                    "paper": {}
                }
            }
        },
        "cs1002": {
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

# for course in data:
#     level = course['level']
#     print(level, " level \n\n\n")
#     for key, value in course.items():
#         if key != "level":
#             print(key, "\n", value)
#             # ======%%%%%%%%%%%%%%%%%=======%%%%%%%%%%%%%%%%%====%%%%%%%%%%%%%%%%%==
#             level_ref = db.collection("ds_pyq").document(
#                 level).collection(key)

#             for sub, sub_value in value.items():
#                 level_ref = db.collection(
#                     "ds_pyq").document(level).collection(sub)
#                 for quiz_key, quiz_value in sub_value.items():
#                     quiz_ref = level_ref.document(quiz_key)
#                     quiz_ref.set(quiz_value)
#                     print(quiz_key, "\n\n\n", quiz_value)


for course in data:
    level = course['level']
    print(level, " level \n\n\n")
    for key, value in course.items():
        if key != "level":
            # print(key, "\n", value)
            # ======%%%%%%%%%%%%%%%%%=======%%%%%%%%%%%%%%%%%====%%%%%%%%%%%%%%%%%==
            level_ref = db.collection("ds_pyq").document(
                level).collection(key)

            for quiz_key, quiz_value in value.items():
                quiz_ref = level_ref.document(quiz_key)
                quiz_ref.set(quiz_value)
                print(json.dumps(quiz_value), "\n\n\n")
