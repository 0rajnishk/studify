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
        "subject 1": {
            "quiz-1": {
                "Dec 2022": {
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
                "Apr 2023": {
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
    },
    {
        "level": "degre",
        "subject 1": {
            "quiz-1": {
                "Dec 2022": {
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
                "Apr 2023": {
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
