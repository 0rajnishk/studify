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
                "Feb 2023": {
                    "paper": {
                        "paper 5": "https://drive.google.com/file/d/1WGz1aiHM6B2SNWw5vOmrOROn_uLpZkrC/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1WoTxDJBfj9HKCdI5eXCI0sUUgAtcK2Je/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1md3KKzBWzFuTtiquc4a01vn1t1hX-ias/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/19Q_ZHRVEQ3e3xEMNTvlbDVHi_UAZaQEi/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1AqQLQeB1XjntbF7g0Ij2TlQmK9PmHsR3/view?usp=drivesdk"
                    }
                },
                "Oct 2022": {
                    "paper": {
                        "paper 5": "https://drive.google.com/file/d/1WGz1aiHM6B2SNWw5vOmrOROn_uLpZkrC/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1WoTxDJBfj9HKCdI5eXCI0sUUgAtcK2Je/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1md3KKzBWzFuTtiquc4a01vn1t1hX-ias/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/19Q_ZHRVEQ3e3xEMNTvlbDVHi_UAZaQEi/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1AqQLQeB1XjntbF7g0Ij2TlQmK9PmHsR3/view?usp=drivesdk"
                    }
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 2": "https://drive.google.com/file/d/17nt0LxktlpUrnA1J4npjvghAHMH562ca/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/17ZbiSzgxuNPD6_fLoDG_pfVyoe_ZZ-xa/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1G6j7KKrGlaSMVZ1_GG7eYBlwMiSxivSO/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1PLh9LcUBhgRA5Yp6zDz4j5wlUQp3ZPbV/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 2": "https://drive.google.com/file/d/17nt0LxktlpUrnA1J4npjvghAHMH562ca/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/17ZbiSzgxuNPD6_fLoDG_pfVyoe_ZZ-xa/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1G6j7KKrGlaSMVZ1_GG7eYBlwMiSxivSO/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1PLh9LcUBhgRA5Yp6zDz4j5wlUQp3ZPbV/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "Dec 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1xkmvm_wvZzMK-yU-3kmneBICSst240RX/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1gScW30hxPUwkVSTeNUxYjBVRXiU_NF4L/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1jt8PP1BII3x8W8ceIn0gIyWIaMLIGjHs/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1kH-pbKAmY7X7uBUkm9BUyqvui6iYgxSW/view?usp=drivesdk"
                    }
                }
            }
        },
        "hs1001": {
            "quiz-1": {
                "Feb 2023": {
                    "paper": {
                        "paper 5": "https://drive.google.com/file/d/1NzAONEOOruUDf-wURLDR8w5WYgV_QVir/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1imGvAQnI4Evm_EKXGM5d1330-Jxb_Fyx/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1psrGDHqT-30ZdwtPqmuQ4Ii3A7CzBvva/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1G1DgDScoAxpeWJaTgzhoMhYm_qNvCg29/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1z7hejYr5HqIAXfj4hNNDqUZM3aOFG3wO/view?usp=drivesdk"
                    }
                },
                "Oct 2022": {
                    "paper": {
                        "paper 5": "https://drive.google.com/file/d/1NzAONEOOruUDf-wURLDR8w5WYgV_QVir/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1imGvAQnI4Evm_EKXGM5d1330-Jxb_Fyx/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1psrGDHqT-30ZdwtPqmuQ4Ii3A7CzBvva/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1G1DgDScoAxpeWJaTgzhoMhYm_qNvCg29/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1z7hejYr5HqIAXfj4hNNDqUZM3aOFG3wO/view?usp=drivesdk"
                    }
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 1": "https://drive.google.com/file/d/19sQJllYUh0JTMjiD3Kvn-I7vPhAkfk0l/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1ApBxWmNXsefrhY1L9LXZCbaVrHpOWgDA/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1KUzeD5DI5vTaBbLdhg8zuk3Bz2SdUFCE/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1ZcQYNnngToREO-aF_1gYs43KKvmOMgyO/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 1": "https://drive.google.com/file/d/19sQJllYUh0JTMjiD3Kvn-I7vPhAkfk0l/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1ApBxWmNXsefrhY1L9LXZCbaVrHpOWgDA/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1KUzeD5DI5vTaBbLdhg8zuk3Bz2SdUFCE/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1ZcQYNnngToREO-aF_1gYs43KKvmOMgyO/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "Dec 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1smgpIfE_6aq5pC0UokIdXo5zbW58A9q-/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/10O8xmHuiBIhXvwgAdrsXOVrz3s0JZWRa/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1iwRAI1ezAmN9C7fsRlm9yKLxM4XndPy_/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/16urHBu3Tpe0ZWRGgpgFnFsrdHbPFry2g/view?usp=drivesdk"
                    }
                }
            }
        },
        "ma1001": {
            "quiz-1": {
                "Feb 2023": {
                    "paper": {
                        "paper 5": "https://drive.google.com/file/d/12EgWEtQYNO2LfYEpgdOgSKdeYo3FWWID/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1GNsQhlVv9dHl1uolcJkENgWDAWHj3grr/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/11UfPr-Z5p98AFGXibru1T1ExGyjeUFjh/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1owoEFFKZi6CJ4Yu1lC6Zi9_qAL6QfT1u/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/10WqQIqHdKco6rXbJQ0mRA6I644EPn_cW/view?usp=drivesdk"
                    }
                },
                "Oct 2022": {
                    "paper": {
                        "paper 5": "https://drive.google.com/file/d/12EgWEtQYNO2LfYEpgdOgSKdeYo3FWWID/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1GNsQhlVv9dHl1uolcJkENgWDAWHj3grr/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/11UfPr-Z5p98AFGXibru1T1ExGyjeUFjh/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1owoEFFKZi6CJ4Yu1lC6Zi9_qAL6QfT1u/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/10WqQIqHdKco6rXbJQ0mRA6I644EPn_cW/view?usp=drivesdk"
                    }
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 1": "https://drive.google.com/file/d/1mPFU9R0FTjmF5x57qe7yqYYYxgOuHArg/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1PU9vyToPcPQ_ygDI9pWhymjQfa5ILdoZ/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/15QHJf8_I5IfQs3KqteiGDBdt8eyo0YrA/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1DykccO3F6ZNU5LJd0N5pcVqNzAXypY-z/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 1": "https://drive.google.com/file/d/1mPFU9R0FTjmF5x57qe7yqYYYxgOuHArg/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1PU9vyToPcPQ_ygDI9pWhymjQfa5ILdoZ/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/15QHJf8_I5IfQs3KqteiGDBdt8eyo0YrA/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1DykccO3F6ZNU5LJd0N5pcVqNzAXypY-z/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "Dec 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/10ioJsLg3YaDrw9VCnIo_cFm36nnbjiba/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1qvRGzpB6ZLTIC-cDrtSI05q7DoTuzzdK/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1gOVUbH4WXXXH5S1sAMTwfSOx8taEp8Nd/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/19s8vjoDudX06EUOdpkqABtk9wu3yKuqW/view?usp=drivesdk"
                    }
                }
            }
        },
        "ma1002": {
            "quiz-1": {
                "Feb 2023": {
                    "paper": {
                        "paper 5": "https://drive.google.com/file/d/14QW97GCb__mtyT0v_87lOQa790M1Wyp1/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1Uo1oSBsLY0gXnML2gIiJJa8hq3-7G6MC/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1AXkHHA5QNRu2wQPQbJmahS-zodWkljMV/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1pQSTooOIMueLmChSCfOq59gmNtz1KOU8/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1P6iIv8g05XarzfcM_Mer9SHgFuNcfX7o/view?usp=drivesdk"
                    }
                },
                "Oct 2022": {
                    "paper": {
                        "paper 5": "https://drive.google.com/file/d/14QW97GCb__mtyT0v_87lOQa790M1Wyp1/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1Uo1oSBsLY0gXnML2gIiJJa8hq3-7G6MC/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1AXkHHA5QNRu2wQPQbJmahS-zodWkljMV/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1pQSTooOIMueLmChSCfOq59gmNtz1KOU8/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1P6iIv8g05XarzfcM_Mer9SHgFuNcfX7o/view?usp=drivesdk"
                    }
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 1": "https://drive.google.com/file/d/1iAXAXzCJyhYcn8L9rgVjqT4qra7tEb7S/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1U1KiPhULl9EWu5mZGnLdHgVPxd9FY22a/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1ZZhIkn3mYGI-SHEWn4-1H_k9cfdPxOyz/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1whiemJE119EUXWmHYdGpL7ZEzV7OIS7p/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 1": "https://drive.google.com/file/d/1iAXAXzCJyhYcn8L9rgVjqT4qra7tEb7S/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1U1KiPhULl9EWu5mZGnLdHgVPxd9FY22a/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1ZZhIkn3mYGI-SHEWn4-1H_k9cfdPxOyz/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1whiemJE119EUXWmHYdGpL7ZEzV7OIS7p/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "Dec 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1SESUNKu_xD0MellLUQGKipwF_6_jRA5c/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1wQizdhMOyND321mlPncqeRsvrt33Rrr-/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1RYml6lq1e3fyT34I4JnWckXawkTHu6qX/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1j-hzKhwMyHncllGqRTG-Cp63k6ZEryW0/view?usp=drivesdk"
                    }
                }
            }
        },
        "hs1002": {
            "quiz-1": {
                "Feb 2023": {
                    "paper": {
                        "paper 5": "https://drive.google.com/file/d/15uKQ5NgoyhQCytuhjsYyfbYO0jW6CHJe/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1J0A2GhAdkiVxyMl2wzGBn8dXWkiFfiyg/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1IMqjKPr3_cYhh34UtHvMe6VM7jZ_pxff/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1t7mbGFFbh3kKOZqNqwBRzRkPvjy-Fbn2/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1vMLVdk3995kbWdEgTXsA2RyCrNhDzrfC/view?usp=drivesdk"
                    }
                },
                "Oct 2022": {
                    "paper": {
                        "paper 5": "https://drive.google.com/file/d/15uKQ5NgoyhQCytuhjsYyfbYO0jW6CHJe/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1J0A2GhAdkiVxyMl2wzGBn8dXWkiFfiyg/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1IMqjKPr3_cYhh34UtHvMe6VM7jZ_pxff/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1t7mbGFFbh3kKOZqNqwBRzRkPvjy-Fbn2/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1vMLVdk3995kbWdEgTXsA2RyCrNhDzrfC/view?usp=drivesdk"
                    }
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 1": "https://drive.google.com/file/d/1rydIfh_2jL2VcNxCTzjqH_KmxbsiXUw6/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1RQixMuPci9_dmDtQMwolJ2wWb1KW8ABQ/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1mCVEQlKdmyvTsfy-G34MDYyCBHAWLPco/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1jHa3CpQon1LUhwg37Z2z7bJN43dtekcH/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 1": "https://drive.google.com/file/d/1rydIfh_2jL2VcNxCTzjqH_KmxbsiXUw6/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1RQixMuPci9_dmDtQMwolJ2wWb1KW8ABQ/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1mCVEQlKdmyvTsfy-G34MDYyCBHAWLPco/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1jHa3CpQon1LUhwg37Z2z7bJN43dtekcH/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "Dec 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1z_uiWVl0pdge-BwTvM1P0srrLZHhqVoa/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1yUiWdYsu7Wj7L9d9luvueVMGBgAm0nNt/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1Pu75LbeG9W79yU8EhIHeq69J7iSqayvc/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1-4Ko1ICLzpFn59ysQoeTWhBLGbulfDtP/view?usp=drivesdk"
                    }
                }
            }
        },
        "ma1004": {
            "quiz-1": {
                "Feb 2023": {
                    "paper": {
                        "paper 5": "https://drive.google.com/file/d/1O_zIFJkYU4Qd_lIAjMadMlialHSfrEc2/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1djLf_qq6YEYnlMHgn0-aqmHANqp9O2qe/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1_JjnFIJtRdbC-ZT-iCii3SK_dmipW5eU/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/18wprx0pvzCgmlc1V5CQ8h2EmPqpNrzIn/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/16tPRcHLf2kY5XFMy2qyLih_V3ZCzkBIR/view?usp=drivesdk"
                    }
                },
                "Oct 2022": {
                    "paper": {
                        "paper 5": "https://drive.google.com/file/d/1O_zIFJkYU4Qd_lIAjMadMlialHSfrEc2/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1djLf_qq6YEYnlMHgn0-aqmHANqp9O2qe/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1_JjnFIJtRdbC-ZT-iCii3SK_dmipW5eU/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/18wprx0pvzCgmlc1V5CQ8h2EmPqpNrzIn/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/16tPRcHLf2kY5XFMy2qyLih_V3ZCzkBIR/view?usp=drivesdk"
                    }
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 1": "https://drive.google.com/file/d/1qF-cL8rjYWlZjVnFzrkbOYiiyfHgtwj2/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1l8zF-nlimE1lzvINL7i3nbADBg4ngULU/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/16hwM7gSFP4FnoM71dzrMTtLQKMz6Xr9w/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1wAGbtF7pw6k5--yEHxz2Wl2UcDiPNCF6/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 1": "https://drive.google.com/file/d/1qF-cL8rjYWlZjVnFzrkbOYiiyfHgtwj2/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1l8zF-nlimE1lzvINL7i3nbADBg4ngULU/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/16hwM7gSFP4FnoM71dzrMTtLQKMz6Xr9w/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1wAGbtF7pw6k5--yEHxz2Wl2UcDiPNCF6/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "Dec 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/19NQmXIYQK1p_M2jbbVx_68V3oAWKIhFn/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1LZsaYlhyA37rm6AGxkyR9BWb30FjhCfJ/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1TN7VF4Exzi2P2d8sYW1J8Evomum-AXj4/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1Vt-lcNh17TIqLkSqDoaqjezHTfCiMUWx/view?usp=drivesdk"
                    }
                }
            }
        },
        "ma1003": {
            "quiz-1": {
                "Feb 2023": {
                    "paper": {
                        "paper 5": "https://drive.google.com/file/d/1hJI5g_uK1gMCCxI6TUBGRHGkr7tQKN_f/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/192lzuEoepH3AHO6D9bTvDuFOge4pDPrR/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/15q-gpFSOs0yUTA6J24gA62kDTyBF_Hv8/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1z-f8wZa3nhhKln5i7vzlDIMLPFvcVVRo/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1WQC-tukolXuIIC1w6Yoc6S_8x11gSOAc/view?usp=drivesdk"
                    }
                },
                "Oct 2022": {
                    "paper": {
                        "paper 5": "https://drive.google.com/file/d/1hJI5g_uK1gMCCxI6TUBGRHGkr7tQKN_f/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/192lzuEoepH3AHO6D9bTvDuFOge4pDPrR/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/15q-gpFSOs0yUTA6J24gA62kDTyBF_Hv8/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1z-f8wZa3nhhKln5i7vzlDIMLPFvcVVRo/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1WQC-tukolXuIIC1w6Yoc6S_8x11gSOAc/view?usp=drivesdk"
                    }
                }
            },
            "quiz-2": {
                "Apr 2023": {
                    "paper": {
                        "paper 1": "https://drive.google.com/file/d/1rwHS2ySvHUnPGRZSv8JXaSZxa0rtj0rT/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1UFdrtsFoMu2Lf80_o8IWt0lFPmP-HCC5/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/19bZ_s55gDUGY0vrLva09dnMsqo01QDmX/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1QN3N-B_Y8uqpPZMI0NYBU6S5aXmbR0xQ/view?usp=drivesdk"
                    }
                },
                "Nov 2022": {
                    "paper": {
                        "paper 1": "https://drive.google.com/file/d/1rwHS2ySvHUnPGRZSv8JXaSZxa0rtj0rT/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1UFdrtsFoMu2Lf80_o8IWt0lFPmP-HCC5/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/19bZ_s55gDUGY0vrLva09dnMsqo01QDmX/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1QN3N-B_Y8uqpPZMI0NYBU6S5aXmbR0xQ/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "Dec 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1gEcajjB9Y5zDRMfVzFss6w3dbWwDyD6o/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1AMFRnoz9DZ7ldEGlwqpCDb0aG8FSxcNW/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1_6ahzFPiB9muFknXOrqhwlUZPpzWmEbn/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1KxDGic6OLCh4odDeWvw8Smkh3SDboaQZ/view?usp=drivesdk"
                    }
                }
            }
        },
        "cs1002": {
            "quiz-1": {
                "Feb 2023": {
                    "paper": {
                        "paper 5": "https://drive.google.com/file/d/1HAzfqqyjMnmOiFLg53M2synTSyzijl_y/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1MN_al6qDxD581CwFD8z_gMeG5C6qzj1m/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1E6q-cGswEfmcZL--dQ2MKk8iDOuJawt7/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1NmqPwhFqJMyoCNs5yDW9QM7_VvQVIogN/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1WGIe40sf-B7bpZRbI6KZELnO0s2_8d_z/view?usp=drivesdk"
                    }
                },
                "Oct 2022": {
                    "paper": {
                        "paper 5": "https://drive.google.com/file/d/1HAzfqqyjMnmOiFLg53M2synTSyzijl_y/view?usp=drivesdk",
                        "paper 4": "https://drive.google.com/file/d/1MN_al6qDxD581CwFD8z_gMeG5C6qzj1m/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1E6q-cGswEfmcZL--dQ2MKk8iDOuJawt7/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1NmqPwhFqJMyoCNs5yDW9QM7_VvQVIogN/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1WGIe40sf-B7bpZRbI6KZELnO0s2_8d_z/view?usp=drivesdk"
                    }
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
                "Dec 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1v1hB6hrSe4SyW0hB14e9D2Y2IEtySUtw/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1nuhEl0WBZ1bT5mXagMqxuTlKtu_jJBt3/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1jLXBfrq8chTckaGs-JvbEv2guV1fx6Fc/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1bSHkVeX1-pGilz7iUr8slpQTtDztZFHI/view?usp=drivesdk"
                    }
                }
            }
        }
    },
    {
        "level": "diploma",
        "cs2001": {
            "quiz-1": {
                "Jun 2022": {
                    "paper": {
                        "paper 3": "https://drive.google.com/file/d/1b8BQMsX-tR4MG3k9hhX2Qyo7aLeM5_Zk/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/14lDI4J8FBWsNbvSeA4zHLWlIPt8uZYnv/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1vT8xL9OU9eGKGwvsBNulrN_mO1RjhHoL/view?usp=drivesdk"
                    }
                }
            },
            "quiz-2": {
                "Mar 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1kkbKW22-Up1ZFwWNF7NPwTDqro_gsu-6/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1UEXgWqIms-I1FJLhXp3hEXvWWuMgMNzN/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1cPiH7E3-MkLUOFAB1hwppgbgrjrFgUO3/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/15SxhCd2fZ6-gUX8wfNNUrvlBoqKsuDxk/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "Apr 2022": {
                    "paper": {
                        "paper 2": "https://drive.google.com/file/d/1EzIntXwCJ4cJQJ7_AFVVmIPT_OMaZfrI/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/16vlYWTYhdLnRFhGPsuVvuh1B_O9CoCMA/view?usp=drivesdk"
                    }
                }
            }
        },
        "cs2002": {
            "quiz-1": {
                "Jun 2022": {
                    "paper": {
                        "paper 3": "https://drive.google.com/file/d/1XK6b59Xu6BCTc_dvj2_rt3Dvp7KqOnKd/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1wa5OFJdvqHdDElLII_9TmrkS3k0_Hi13/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1TxY4-GYULBpzDVXHXWg6uEpBcfAovxQR/view?usp=drivesdk"
                    }
                }
            },
            "quiz-2": {
                "Mar 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1z0WPtUo16TIaUV2vPS8ryHd3kSPVVJoj/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1zejLxoqnLMIzJghRh7INpYjbKQkb_r1K/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1UpJDg8gOabYcPS5Xm-9PlZ2SRQhEizM5/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1OOT4SbwHtQ4ED9Hgo-gI_V7KNW-Ybfr9/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "Apr 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1WdJPOhtwjrpbP0Dpg4whFs7XmzgNQnv2/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/18LROPxYuuoPSBwXEp9azMY-nSftJscFz/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1bmoytImbLOkeIH3HcmwhCPp4UshaV6Nt/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1Hi_qAAuRSGl-u0vVTBPO1BOAtvUojpQO/view?usp=drivesdk"
                    }
                }
            }
        },
        "cs2003": {
            "quiz-1": {
                "Jun 2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Mar 2022": {
                    "paper": {}
                }
            },
            "endterm": {
                "Apr 2022": {
                    "paper": {}
                }
            }
        },
        "cs2004": {
            "quiz-1": {
                "Jun 2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Mar 2022": {
                    "paper": {}
                }
            },
            "endterm": {
                "Apr 2022": {
                    "paper": {}
                }
            }
        },
        "cs2005": {
            "quiz-1": {
                "Jun 2022": {
                    "paper": {
                        "paper 3": "https://drive.google.com/file/d/1pXgnP5vG1cTgoUKcE2RCUssVVUBl-aTj/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1Wb1TaqHp2rAH8KNsW_Zke6adZKkIoDPa/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1Fwr4KW27kWI5gqKdhsodg0BAUxup_p9O/view?usp=drivesdk"
                    }
                }
            },
            "quiz-2": {
                "Mar 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1M92jBDeE-aIRP81kUG3tGBAE0AS9ZZAH/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1VEd-Pdp5JtR7zbuA7_l9pqhNw_9KPnPb/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1iILGD1iGGvHJxN09vwjHiynngoddGq7w/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1BpNNlPQQzjQg6Iv8ExHaFtmZjzJCmA54/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "Apr 2022": {
                    "paper": {
                        "paper 2": "https://drive.google.com/file/d/1Fy2h5Qj7IzqrCnEwd2iai-15BOloj6C3/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1HpGgvykEvqZ2VoAwmVUE2mPyvJaISfy5/view?usp=drivesdk"
                    }
                }
            }
        },
        "cs2006": {
            "quiz-1": {
                "Jun 2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Mar 2022": {
                    "paper": {}
                }
            },
            "endterm": {
                "Apr 2022": {
                    "paper": {}
                }
            }
        },
        "cs2007": {
            "quiz-1": {
                "Jun 2022": {
                    "paper": {
                        "paper 3": "https://drive.google.com/file/d/1BT7Quewhja9p7xjvUfVqVs9c2d8rp8BI/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/18a9Pxi_aUk830-FeLJ2R6LRy4X4mSja8/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1JWDYxm_XtREI7yqJ5REekLyrqZYDe313/view?usp=drivesdk"
                    }
                }
            },
            "quiz-2": {
                "Mar 2022": {
                    "paper": {}
                }
            },
            "endterm": {
                "Apr 2022": {
                    "paper": {
                        "paper 2": "https://drive.google.com/file/d/1s3oGjU3p4Qh5YEs0qbUcC8L37OSkSdA3/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1-39lnzY9rpZ6ZnRY9-xjzWMHX7CjV9F3/view?usp=drivesdk"
                    }
                }
            }
        },
        "cs2008": {
            "quiz-1": {
                "Jun 2022": {
                    "paper": {
                        "paper 3": "https://drive.google.com/file/d/16j7luW6HtDIZFxep5kDKE7UOhOxgJnFz/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/132Z9EkOHwJOpT0OjcCUyGJYVRmriNQTF/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1z4uGAhR_y6wRCGD7NQb8ht0yHdiU0nGw/view?usp=drivesdk"
                    }
                }
            },
            "quiz-2": {
                "Mar 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1ZuBG7SjeAuSEQIUWfZFPtMDkB8GpuSaP/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1k2JIlf3Qai0Bhy7GwdsOnQlG2ag-r3Da/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1lLDPXeI8AFNldJdlQtVPcZPqPht4WAIP/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1pi6FUJT6fs0wf-Pco0TQvXI8R0XxkbW5/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "Apr 2022": {
                    "paper": {}
                }
            }
        },
        "ms2001": {
            "quiz-1": {
                "Jun 2022": {
                    "paper": {
                        "paper 3": "https://drive.google.com/file/d/1CTxUhJwn2V4Ckkl3uiU2WNqePKNKYh8L/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1VSBiXKxL2F27_cFdKNsKJHZUorn53Dq6/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1gx3peVo_47WQWWjPRZr2NgME4xJ06-Nl/view?usp=drivesdk"
                    }
                }
            },
            "quiz-2": {
                "Mar 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/14r30fXPTOysjYazggdwY2pBXHMlJOgZW/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1N74RUPOs_Nl9_l9G08TMWG9FL1jLMRRn/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/192r3DfOHC39TW1zPs3j6CdKOZjSLz9k5/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1qqBd4dW6hmsr5aO8Cj-uvzU1l0ZcoglG/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "Apr 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1LQ9CKYhnUjszi2FcB2_6YSyAHhjr7sLP/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1UWTSJ3uHoOs-xZ9cx11o8nR0JXN3EitM/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1LOqwNNgM4LIZ_hJ5DKIjH-u6VxyqHXsT/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1C4xlYpdJ4z22wNgiDSKAEgYn1vS3E7W4/view?usp=drivesdk"
                    }
                }
            }
        },
        "ms2002": {
            "quiz-1": {
                "Jun 2022": {
                    "paper": {
                        "paper 3": "https://drive.google.com/file/d/12CbeCXdGm-tUHdf6Rig9PsB7WFc0RCgj/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1WnT2k2OIZULJd-ieNqHhZmDZ8C5AScjI/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1_1RCRUUOT8G-80FQ7q22T3aEHEnsMdII/view?usp=drivesdk"
                    }
                }
            },
            "quiz-2": {
                "Mar 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1hwaYJ6F9kiglENqzWL_uVN4lRRq5U2eI/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1BB_S35XUarkFbqDH96f9niOsvmrhbymh/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1HbJRuzSpkefw0YCV3XkooTCtEBnn9TXM/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1ofxg5JLGyQntt0p0mIng2Q-Fa_PppFot/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "Apr 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/107_kmMYzclaiyLB5WHUL0mEC_4iyxxxx/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1_lLs_Vmi379bqZKG_VxSET1TaFTDd_2O/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1QmRIn2YDmG4VIkHJDC6RZOaeAE6mH1lI/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/143pZc80drN0QM_tFsX0CAYN5Nhb2k2yL/view?usp=drivesdk"
                    }
                }
            }
        },
        "se2001": {
            "quiz-1": {
                "Jun 2022": {
                    "paper": {
                        "paper 3": "https://drive.google.com/file/d/11l26fkiudg9JaNlldDfxf8XA1cvsNQZo/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1t3eUteFJSGpaFC8ZvVgHXw_HCI-5Enqv/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1hGlfgk-uHO0RmQEiGX0pXNy0O2DOn5gP/view?usp=drivesdk"
                    }
                }
            },
            "quiz-2": {
                "Mar 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/1rhtWzKptKO2m511nUbLS-tjqfC8XesQl/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1b4kcnv9HDv3GcXgSMFnVH6bK15LutHaE/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1uUI2RUC7lx8Aj4ELn8tSNYwYPpoxycLk/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1QE-C_mYmtIWcLAo7VZTKOtOWoD5ilA2y/view?usp=drivesdk"
                    }
                }
            },
            "endterm": {
                "Apr 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/17LyA3XlbzBZLfqluWxrqdVaaAXsitbBq/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1rFVWmJLvJOmecPL6ObGB48mFwL2pbvF3/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/12VNJy_HeToEhXkiEU1HOS_O81GGwPK3K/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/14M6J2BPkyZuizXftZhul2brxZmBsQWeo/view?usp=drivesdk"
                    }
                }
            }
        },
        "se2002": {
            "quiz-1": {
                "Jun 2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Mar 2022": {
                    "paper": {}
                }
            },
            "endterm": {
                "Apr 2022": {
                    "paper": {
                        "paper 4": "https://drive.google.com/file/d/16Bv137cDERov3GQAg-aCAif0RmQavj-F/view?usp=drivesdk",
                        "paper 3": "https://drive.google.com/file/d/1wa6PXWsNXqH7eY1z2yuSYQ-C-KS1ayXq/view?usp=drivesdk",
                        "paper 2": "https://drive.google.com/file/d/1NXR1NPgls069mCm50vxwAhYfRHKUYZy7/view?usp=drivesdk",
                        "paper 1": "https://drive.google.com/file/d/1So_hFA9lrNOo-VSbOX2Gybob2bJladUM/view?usp=drivesdk"
                    }
                }
            }
        },
        "cs2003p": {
            "quiz-1": {
                "Jun 2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Mar 2022": {
                    "paper": {}
                }
            },
            "endterm": {
                "Apr 2022": {
                    "paper": {}
                }
            }
        },
        "cs2006p": {
            "quiz-1": {
                "Jun 2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Mar 2022": {
                    "paper": {}
                }
            },
            "endterm": {
                "Apr 2022": {
                    "paper": {}
                }
            }
        },
        "MS2001P": {
            "quiz-1": {
                "Jun 2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Mar 2022": {
                    "paper": {}
                }
            },
            "endterm": {
                "Apr 2022": {
                    "paper": {}
                }
            }
        },
        "CS2008P": {
            "quiz-1": {
                "Jun 2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "Mar 2022": {
                    "paper": {}
                }
            },
            "endterm": {
                "Apr 2022": {
                    "paper": {}
                }
            }
        }
    },
    {
        "level": "degree",
        "subject 1": {
            "quiz-1": {
                "Dec 2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "quiz_2_date_d": {
                    "paper": {}
                },
                "Nov 2022": {
                    "paper": {}
                }
            },
            "endterm": {
                "Dec 2022": {
                    "paper": {}
                }
            }
        },
        "subject 2": {
            "quiz-1": {
                "Dec 2022": {
                    "paper": {}
                }
            },
            "quiz-2": {
                "quiz_2_date_d": {
                    "paper": {}
                },
                "Nov 2022": {
                    "paper": {}
                }
            },
            "endterm": {
                "Dec 2022": {
                    "paper": {}
                }
            }
        }
    }
]

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
