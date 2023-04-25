import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Initialize a new Firebase app with your service account credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)

# Access your Firestore database
db = firestore.client()


# import json
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

# # Use a service account to authenticate with Firestore
# cred = credentials.Certificate("firebase.json")
# firebase_admin.initialize_app(cred)

# # Access Firestore
# db = firestore.client()

data = {
    "foundation": {
        "hs1001": {
            "endterm": {
                "Dec 2022": [
                    "https://drive.google.com/file/d/1JYkkXBojAdKyBsW8aBeNTF_x4qTrUjbN/view?usp=drivesdk",
                    "https://drive.google.com/file/d/10n064zK2Ow9THM3fCT80zXfpexrLdC8E/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1CfTKHWz3wcfMghLX71U-ebOC8my9Sp6T/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1DiDvQAxXj3UvuOGT4WdbcWRqpRhDJJE9/view?usp=drivesdk"
                ]
            },
            "quiz-2": {
                "Nov 2022": [
                    "https://drive.google.com/file/d/1h9FoWovsjKzzXei7s8CR6NXnY3-V0uzB/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1xn6fDrpWQlqeUuO29q71P2Hu88rbxBEF/view?usp=drivesdk",
                    "https://drive.google.com/file/d/18dmq02soewWB2cmFiZBT3vLh7NYyykZi/view?usp=drivesdk"
                ],
                "Apr 2023": [
                    "https://drive.google.com/file/d/1drUFjBQWjW_aEC3gLruX1ARagylCKCx_/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1EOAdrE1f1R8gOJHkcm6bS2g-sun7PjUm/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1yjJjw98xjGUxqYLW_jLUOd3w20PzqaXs/view?usp=drivesdk"
                ]
            },
            "quiz-1": {
                "Oct 2022": [
                    "https://drive.google.com/file/d/1vg10VE5rKnp-ktYsoiOxik46nAAFdUnJ/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1fpgFaNFW902gDZlRwNFsJ3KL8Zmqkvo0/view?usp=drivesdk"
                ],
                "Feb 2023": [
                    "https://drive.google.com/file/d/1vW2uaNCCrmegyQaJFSu5tF-qwCMOSMMo/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1VcJkjL09Yft-YTKiI4l0tLkqM-fejjAH/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1c46oK1vL4Lj6mjFGomTih1Ekxj_73R1e/view?usp=drivesdk"
                ]
            }
        },
        "cs1001": {
            "endterm": {
                "Dec 2022": [
                    "https://drive.google.com/file/d/1uKwSz3AmARmxcwLJDod5wnKjGy-gEq-G/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1JcR3sta0VijseearUe7Xvr_V5LasXWCT/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1V6ZzBa7VgnPjiO811c0UVrHB7XkzrhVM/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1_2HBXu2i9zGUGCjPMF9NiUeDDxbHrZmZ/view?usp=drivesdk"
                ]
            },
            "quiz-2": {
                "Nov 2022": [
                    "https://drive.google.com/file/d/1JcOUHBpNED1x_TgHTDXk10TZPCldh2d2/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1Wl6of1IxzW2jwQubNK1QtvjhHlXw_3Vj/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1mL_dl3u5msi6uhZqjvEt2pDLIehXEHie/view?usp=drivesdk"
                ],
                "Apr 2023": [
                    "https://drive.google.com/file/d/1zm2YSrR84n0TQEUzn0jlXzUjdsDhqUjd/view?usp=drivesdk",
                    "https://drive.google.com/file/d/10AdvBmW-rf8BEpkvNvq-7x2_ioWQFkQr/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1JI7j3BRMMLIhZ-P7lExxCAkutCKcuEwb/view?usp=drivesdk"
                ]
            },
            "quiz-1": {
                "Oct 2022": [
                    "https://drive.google.com/file/d/1P2O51283pm6ERTWmBSglJujr18t-6wWL/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1uGnvfc30GXELbvUXD4f5CwZekiD2SkMI/view?usp=drivesdk"
                ],
                "Feb 2023": [
                    "https://drive.google.com/file/d/1Kh8B7FpbC1tmZBcrkFgYRVNYjlKOog1R/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1g5cEvITSCm03ejNUoK45MxxdzHHXLLMZ/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1-Zar-WDul_mvQ1zKuPl8_QVG9XQzNQcN/view?usp=drivesdk"
                ]
            }
        },
        "ma1002": {
            "endterm": {
                "Dec 2022": [
                    "https://drive.google.com/file/d/1lfqNR2TIAGpsQGqWA9PaFBC0bChbvSX4/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1xAW1BP7txHpQc7288EpR4CNzWU1KeVgm/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1tBxMPRNvbqRr1_9VbfRQJRBcjfxESvpG/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1i3tlHXAF3SaDgq-tAoj6NnL3S0bD62Ir/view?usp=drivesdk"
                ]
            },
            "quiz-2": {
                "Nov 2022": [
                    "https://drive.google.com/file/d/19r3M7uzbsLJ9I8YG3evecSEZtyFQ3x3z/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1PgBYEflLEtVIOdU2wJt7R33DVdURTRJE/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1Fkej_dggrreH6lwj9DQt6kTH3a4oB0w2/view?usp=drivesdk"
                ],
                "Apr 2023": [
                    "https://drive.google.com/file/d/1ODjO0cyZfilmMg6IrUUpKDqM_mSjj6bV/view?usp=drivesdk",
                    "https://drive.google.com/file/d/19l06KXpRXTHKYut60xggLLGQ97JqVGw-/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1eO9vBesG0F6ANC2bVhLtxMgYeUHQyBUR/view?usp=drivesdk"
                ]
            },
            "quiz-1": {
                "Oct 2022": [
                    "https://drive.google.com/file/d/1ZhSHlpKrKGJN_h7HD_cmGByfAy-xO-Th/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1OAdQOEdZRJ8y1p3G4fAchegb_09isEGs/view?usp=drivesdk"
                ],
                "Feb 2023": [
                    "https://drive.google.com/file/d/1t61t4N_DYxbkxg-5cOnig_vzMWaStvqv/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1j7jFiRmdAPjfpBRvlDvr4_0OBqKJhcbO/view?usp=drivesdk",
                    "https://drive.google.com/file/d/10ftZBITzn36MgaLT-1XOOnlKtd8Xb0oi/view?usp=drivesdk"
                ]
            }
        },
        "hs1002": {
            "endterm": {
                "Dec 2022": [
                    "https://drive.google.com/file/d/1c9vQ3slvZHujOkEqeOKE6j2dNVWFoOPQ/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1RYt998wcPcJQwmyBsIjGh7EQtGhsUjku/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1oZ4MBSX4EOdL34SpzCuPzWBuARa8oU8P/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1G40mKZe-UBzlsIzpVhWA9u_T7Jsudpj_/view?usp=drivesdk"
                ]
            },
            "quiz-2": {
                "Nov 2022": [
                    "https://drive.google.com/file/d/1z13Sq-FtG_TJsHidjNheRp2c7J6JkEAv/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1RVTbMA8oSxiZeGNnhWME1-28MB8mkzyP/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1pJKS3bEjzOSEe2vg9i1NeYR1ONeUl7rf/view?usp=drivesdk"
                ],
                "Apr 2023": [
                    "https://drive.google.com/file/d/1rU8hgbEJJcfi6kGL6L09SLVvLeiujcfZ/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1s5Uon4cFOiyFO0fWCHsAm2vNPc2dd1KY/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1CgBNEoIGPYAfUo4hzfySIutIPYhGzJ3o/view?usp=drivesdk"
                ]
            },
            "quiz-1": {
                "Oct 2022": [
                    "https://drive.google.com/file/d/1qmNoAzCsC2J42tGPvyQlUrrVd2BMgO4k/view?usp=drivesdk",
                    "https://drive.google.com/file/d/15O-Zfi9vdhnM20iozZ62xabMxqihfq96/view?usp=drivesdk"
                ],
                "Feb 2023": [
                    "https://drive.google.com/file/d/1Y4ANJYm_t92EcMEIsweuVLAHCMq7kvCV/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1ywUZQPc0y3wNK2RmWIP4W2IWad6bHVCD/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1bfb42uBQ19bw-zbYmrrDk0LjBZ9yUGLN/view?usp=drivesdk"
                ]
            }
        },
        "cs1002": {
            "endterm": {
                "Dec 2022": [
                    "https://drive.google.com/file/d/1pDfhYIvCC8x3mWPX_7TGHpSIN7NLIEOS/view?usp=drivesdk",
                    "https://drive.google.com/file/d/18DLRxiUab0LxX43H4mnAcqYEz-nJ3Od8/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1wlanZJaCSU6gM4KmqY5659kt2AcXirSr/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1slkIvE9JXhc_Jy7CElMJubjkldkV6Q-x/view?usp=drivesdk"
                ]
            },
            "quiz-1": {
                "Oct 2022": [
                    "https://drive.google.com/file/d/1Nz1gBVtCfWgpyt0sB1efot95pcAwWKVJ/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1pjlLRQuqDQlIbdRuOAuElorN95b7MfwA/view?usp=drivesdk"
                ],
                "Feb 2023": [
                    "https://drive.google.com/file/d/1WxWUHgq_UbpBaTmNGs-Oz3AOV36ZfrLu/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1Yvd79KvJKOrOdEUa6Bv-whpLBwZiaNp8/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1NGc7_frj1x643KpN5yIp1NXveC8A23hd/view?usp=drivesdk"
                ]
            }
        },
        "ma1004": {
            "endterm": {
                "Dec 2022": [
                    "https://drive.google.com/file/d/1iz9fUzyfyBH733pwu0NWuSq-ylWGqZiw/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1U-Fdq6c55d6IRYSQ9RGZyN0_DdwdV8CY/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1AhfhQAut4xTo5-UoC8xXKxDrRMDAn_fk/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1RDaL-gaCYyfOHKBd9F9EQETbRtbbMFvZ/view?usp=drivesdk"
                ]
            },
            "quiz-2": {
                "Nov 2022": [
                    "https://drive.google.com/file/d/1sZ8plhVMr2VhRB7HgLQ0HCHNJnp8lEOG/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1IQ9-BGwvKxRxUXTQ5x6U_2kyUKlr0sfa/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1TP39xTi5bjRR7_fzhmeb4Sla2OsWa8OK/view?usp=drivesdk"
                ],
                "Apr 2023": [
                    "https://drive.google.com/file/d/1PpODe3t-UQzFqg31z0rVSX0avtE08_4E/view?usp=drivesdk",
                    "https://drive.google.com/file/d/19bOBoCzJKS7avkUEijHeGUfyHVahDsNI/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1Qto4scT5ney6RwfktgDTLtL7MQsr_kXk/view?usp=drivesdk"
                ]
            },
            "quiz-1": {
                "Oct 2022": [
                    "https://drive.google.com/file/d/1lp69dHQ-QE6OqucHUiYbcr_fQvjB97nw/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1TsjWyxn76KHj0c09mCxFoTao6JCEB4SM/view?usp=drivesdk"
                ],
                "Feb 2023": [
                    "https://drive.google.com/file/d/1t9g6w_pltZ8Y2QFdzHvyft6chTbFu10_/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1PfY7qt3Aaqe87myl6t2Elg4A2Zj_BIAI/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1_3FSUU4relNx72FfH8FRwVT0fDvpcnpE/view?usp=drivesdk"
                ]
            }
        },
        "ma1003": {
            "endterm": {
                "Dec 2022": [
                    "https://drive.google.com/file/d/16JSOj1RSGF5j3bIq20NlOc4O5xXDtcfh/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1lFqsgXHOU5BVQx5VnrMhZFiLZFW70d-J/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1GlLudIljlB7h-tWeP7a7Ag3nxhUVKMYJ/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1GkvllwxsjofKIA-YXXCtcEqorluhLFtB/view?usp=drivesdk"
                ]
            },
            "quiz-2": {
                "Nov 2022": [
                    "https://drive.google.com/file/d/1NsVNZXtOvOyP-kpEk7U5eOAhtVAzgSWp/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1jvYNCqhzFmJegI3TGfHgl8_k5ZL_WEGc/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1luyI8Bv1Df2_aezuFKV2FwidLgFBxf6v/view?usp=drivesdk"
                ],
                "Apr 2023": [
                    "https://drive.google.com/file/d/1LRo-wN0Y9iDSEsIcfaY9L4URW238q8-e/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1E1EI6A5LEHqN97we1MgHRGwlfsy_79j4/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1VutdDF1QHWUXrhbWlTBGcZF6735Gp6CV/view?usp=drivesdk"
                ]
            },
            "quiz-1": {
                "Oct 2022": [
                    "https://drive.google.com/file/d/14ejlz1PEZl_6WTy2sYNrNXmPoTFnKMJt/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1vxX1efFFABQ_ZObaM4AxmCGNE6p6CBeB/view?usp=drivesdk"
                ],
                "Feb 2023": [
                    "https://drive.google.com/file/d/1shrfYEO6P-jQjF5Ypge6LHtYempPVe9M/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1foNDfZuyumXnFFQiRVu7kDHzt5ntxcOH/view?usp=drivesdk",
                    "https://drive.google.com/file/d/196D-c7thIRiXddcYtU_uhVKDNwy4zBOc/view?usp=drivesdk"
                ]
            }
        },
        "ma1001": {
            "endterm": {
                "Dec 2022": [
                    "https://drive.google.com/file/d/1oP8OHieQz__dUKk9ebb0K7OlIoyH8kpN/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1JSl_qF52B4pG-cS-COkhHqznUFWQ6gol/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1hxbr-P0hpLerpQQ0A1Hz9_1jynwNvOv7/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1P1dKpNyfrWvgasGU00hCSsIHtLu1Yl4l/view?usp=drivesdk"
                ]
            },
            "quiz-2": {
                "Nov 2022": [
                    "https://drive.google.com/file/d/14lDY_i1A3FP3GG15asvYZORME2w7nMai/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1HNaRxgB05H3Kjg3sfn_k3nipU-DC5YQx/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1UinAcJC9xxeBMysoPGFgxji1mf8Hzddn/view?usp=drivesdk"
                ],
                "Apr 2023": [
                    "https://drive.google.com/file/d/1KQNfQ7Dzaw0DF0bYszk3Em7IDuX80Bs5/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1-ul13C-lmM9iifH5nHIrZ_W_kihdTozh/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1Ks2YAS9xQG1nH3hWcO2rnR8X1h962Lc3/view?usp=drivesdk"
                ]
            },
            "quiz-1": {
                "Oct 2022": [
                    "https://drive.google.com/file/d/10HS7BZPR26R1f6A5wIfcG_e8wJJg8iLO/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1FFEpu5IrzMMpp1H36xUXBNRsr-29A83o/view?usp=drivesdk"
                ],
                "Feb 2023": [
                    "https://drive.google.com/file/d/1Spq3vsr2Klqph4dLgexJ6KPLJVGSqujW/view?usp=drivesdk",
                    "https://drive.google.com/file/d/13SkLa_fBALT7CsGAOQkCQyTocigQrvve/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1S3tPpR6Ea8-b7dC3A8fqNHALmuhxjIlR/view?usp=drivesdk"
                ]
            }
        }
    },
    "diploma": {
        "se2002": {
            "endterm": {
                "Apr 2022": [
                    "https://drive.google.com/file/d/1HPxB-3fjOiC2CZLhWv4C5kCH67h1PdkD/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1KQV5NJOat8f4zlbC7LRn5Dhap1pzk4yC/view?usp=drivesdk",
                    "https://drive.google.com/file/d/135zM2j40i6sHxxHUaSA_KXCtblsy0JWI/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1qWwrPCx7YpR_s9pUrKnaGh_4ZjhUIgX2/view?usp=drivesdk"
                ]
            }
        },
        "se2001": {
            "endterm": {
                "Apr 2022": [
                    "https://drive.google.com/file/d/1UVFx9CKGX_93iEZ-tyBOaaBMV2YSvn2V/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1BjAH7imIiU7YqGkQr2HQMjUKRBYAu7SV/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1Wdx3b6R3kZ_b608cnHf9fvmSVl_7okgp/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1dqznyc5X36XZW0a-gxlY9vGLpR2FX4kH/view?usp=drivesdk"
                ]
            },
            "quiz-2": {
                "Mar 2022": [
                    "https://drive.google.com/file/d/1FfYk6JxbWNxCaVi6mwUQBeKMa2PuUUPN/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1wqjmxv5xGeLil52iCAm_MyZAGY_aRB6z/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1C6Jb8rbUVxKYgOEWoMVdgPCmWIhlzAit/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1dyCkz_SGv2pQyK9mETdJHv00jQFAX1G-/view?usp=drivesdk"
                ]
            },
            "quiz-1": {
                "Jun 2022": [
                    "https://drive.google.com/file/d/1VPPJR3R43qwHtG1EKOy3QCFxP5k_vnf1/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1nly9j2FaaGGHUgmYV0pkcsLesa-yBJuQ/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1szdYW8wSBdQp-i3sk9DWrOOS0zdIyur9/view?usp=drivesdk"
                ]
            }
        },
        "cs2002": {
            "endterm": {
                "Apr 2022": [
                    "https://drive.google.com/file/d/15mgoRgQkhHrKvTgcOzVDp37YXGDZ9p27/view?usp=drivesdk",
                    "https://drive.google.com/file/d/11ew3AXHjP_d5Klp7DpVAuzHzEg9HsRRf/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1fxD0NRlrPm0v-KyJXz6agoeWR6Fjnn-E/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1GYCY9paT2zpfHmrythosWmmk4puVptOY/view?usp=drivesdk"
                ]
            },
            "quiz-2": {
                "Mar 2022": [
                    "https://drive.google.com/file/d/1gQzL6FP83MG_ETGVzZ_-H3D3vAxThTok/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1Ewtx-pfp7EYgJ4Q5qFx3a_D_3REJa0MK/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1yaJkuTUMFtN29q_uXtHcG4gVoGOYGoST/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1RK3uazwkLoyofVhId07szS5OcUXjNgC5/view?usp=drivesdk"
                ]
            },
            "quiz-1": {
                "Jun 2022": [
                    "https://drive.google.com/file/d/1zyoRME6VRUPZnF3dRB_3W9gB5JlKoGDq/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1S9vFxyah5GfVVlfsHSGsUw3kgsv88JsP/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1dwrDOs7N8rXh29w6fZ-CBCD9lK1H7chZ/view?usp=drivesdk"
                ]
            }
        },
        "ms2002": {
            "endterm": {
                "Apr 2022": [
                    "https://drive.google.com/file/d/1pLNmxUplN1nozNtHANKEq8sNaVCNrnXU/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1wgFGxEUf4NZ3wGvsqbqrLHLksQXEkTZj/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1qD2T-aNGf7kKVD8wDDHL5Bq2KLWIRhTh/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1hH25gZVuFtMGS3DqM9xcsNyjs3Cha_iV/view?usp=drivesdk"
                ]
            },
            "quiz-2": {
                "Mar 2022": [
                    "https://drive.google.com/file/d/1UA5-CJ_D5ktkDBEDEUiCDvkaXHmv1_30/view?usp=drivesdk",
                    "https://drive.google.com/file/d/15M2gfsubXj9x35WZTdRpD9WX-Mqpwe26/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1oLtHpCUtEb1RsQ2-z2MdMEmT0UvuG9R-/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1rrkt5oHmr4AsxKVNBaUMS5ghQcsVAM5l/view?usp=drivesdk"
                ]
            },
            "quiz-1": {
                "Jun 2022": [
                    "https://drive.google.com/file/d/1irq15FYtZszm2ewFxhCP5f-o7w6ZhS3o/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1JGH7PqexYivwiDlgprNT8rVI_3S4fvLS/view?usp=drivesdk",
                    "https://drive.google.com/file/d/11f1e7Hq3WIoqisaBcmuObXKmRWCqMqvy/view?usp=drivesdk"
                ]
            }
        },
        "ms2001": {
            "endterm": {
                "Apr 2022": [
                    "https://drive.google.com/file/d/1GzhvWESw46B2xxw-aeVK2tLOHaOUB0ug/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1MK1yLcI9XEBSpwdMDmZyL79aSAMGqAC2/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1uZRX13CSfBIXjxBz4FMgrpkN6-dhsFsL/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1yZAHOp2wCNhskcE7DfTRelUHZxwS4uOL/view?usp=drivesdk"
                ]
            },
            "quiz-2": {
                "Mar 2022": [
                    "https://drive.google.com/file/d/15GnRP2AaKBdfOnq6pAgGgiQlhSILYsAx/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1CCD4c_L759lcGdB6mlPIgyKjp8_VVrg_/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1NOJfjinOPMwaR8HeLnMEhHfbecOLbTEl/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1qM8AANC1EmBK2cAqvFksR8HC34ccaOxa/view?usp=drivesdk"
                ]
            },
            "quiz-1": {
                "Jun 2022": [
                    "https://drive.google.com/file/d/1hYivuoAiVM69C_bhlfM0706BGeK-qNme/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1MxzXXseHi3fS0pIlblUbKCkKuDFFYoUH/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1fQdzq_byMYo-HrrVxgEXpIOLXVcAIk64/view?usp=drivesdk"
                ]
            }
        },
        "cs2007": {
            "endterm": {
                "Apr 2022": [
                    "https://drive.google.com/file/d/1BLRvQxJGXFI23Lhc2rdZjiMM5k8uAGlw/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1P-Nky1gGjsAMzA818MXna4VkuFXn63-n/view?usp=drivesdk"
                ]
            },
            "quiz-2": {
                "Mar 2022": [
                    "https://drive.google.com/file/d/1wc75FB-jhWElKNKH2Xh2QL2-r96JpgrG/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1rt9tssYP2Pdk9SCFtERULR1LzVtbVHGv/view?usp=drivesdk",
                    "https://drive.google.com/file/d/15cG7obpQbm79qnDbwMhzNJGE2BGITKL1/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1U4OSyGEJTvGgTzGVmufr-jFWT2prhLJR/view?usp=drivesdk"
                ]
            },
            "quiz-1": {
                "Jun 2022": [
                    "https://drive.google.com/file/d/107ucHoL19VoeZo-Q_pMETBALnuxjdaJl/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1nilnoCbGjBTQloJ0TDWL8y-fVlmH-557/view?usp=drivesdk",
                    "https://drive.google.com/file/d/17F2Oa0QqqDKQJmfgWCWUwS3awAZVfluR/view?usp=drivesdk"
                ]
            }
        },
        "cs2004": {
            "endterm": {
                "Apr 2022": [
                    "https://drive.google.com/file/d/1Y_XlaPPPmq1D3gApMkGJudhRaMptAmzV/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1cML-Un7m_TvPknI287CaG-wxYhIxGvzA/view?usp=drivesdk"
                ]
            },
            "quiz-2": {
                "Mar 2022": [
                    "https://drive.google.com/file/d/1U2NpBvewMO5cSlxh6bXZ4FP0hv1PE-rM/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1SzvfSYE7w_uX0izjdZXUxjfZ8G7c6uRQ/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1HH9XxfCYj1cRJHILpT3Prh_XyAo_jMu0/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1o7mJd4EjWMKz12fiLrxFErHW7UGaUDSM/view?usp=drivesdk"
                ]
            },
            "quiz-1": {
                "Jun 2022": [
                    "https://drive.google.com/file/d/1nDQ3CMpL98et_1sGMoZYHTYMP8vr_6Ge/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1BjMfzbX_9i7LmNW6nvgkr6UgX8-iLMpq/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1UngX0ILvfxdUPzpzw1Pba5l4bhda-GGD/view?usp=drivesdk"
                ]
            }
        },
        "cs2005": {
            "endterm": {
                "Apr 2022": [
                    "https://drive.google.com/file/d/1jczk_r8UthFPj0Tw-2SEgbM6_8fxnGK5/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1-w7GKRBXSjGZ0K6vt1gpg-KV-Is1CFf7/view?usp=drivesdk"
                ]
            },
            "quiz-2": {
                "Mar 2022": [
                    "https://drive.google.com/file/d/1G-yz-mAwGLIyuIDN-jaxyFKS1hRArcQe/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1SG51upGdKXfGowUZee3-I1Vg4itaxDUp/view?usp=drivesdk",
                    "https://drive.google.com/file/d/17GP9nBuVB7hy1Nrh5efUUNFYkPvCgcTn/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1uPnF-omUqv6MnofPpp3EV6t-boCup2ju/view?usp=drivesdk"
                ]
            },
            "quiz-1": {
                "Jun 2022": [
                    "https://drive.google.com/file/d/1lNbb5_UyJQXUMwh6D-DR0jWn-jwAWL1s/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1SKCtpgDG89aY_v_v5E2G2cEtUdtYcsZ2/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1NfXq-TztMgV6qrrGzkL4YFzjyy8oPYCv/view?usp=drivesdk"
                ]
            }
        },
        "cs2001": {
            "endterm": {
                "Apr 2022": [
                    "https://drive.google.com/file/d/1PdCuGslv0dC65KoGC9wCi5S9-7zR30EZ/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1fjMeXsJcxu5V5bU1D49m13lOhogAWEK1/view?usp=drivesdk"
                ]
            },
            "quiz-2": {
                "Mar 2022": [
                    "https://drive.google.com/file/d/1izjfYM7JE6yF41y-adWEiyT1UWdPsa10/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1RLNxVC4K15-vETLN7qoywacPvm7FCs8n/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1MT-54MrLoFV_WObGfAf0sHg8pmhKJBm9/view?usp=drivesdk",
                    "https://drive.google.com/file/d/12fwvLc08ALgxydOtN_wI6GQCMJdILVjc/view?usp=drivesdk"
                ]
            },
            "quiz-1": {
                "Jun 2022": [
                    "https://drive.google.com/file/d/1IGe24OlwBbVM2udBuog-9N3-pszLgKzy/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1zRtwCEK4qKpCJmD6AK2jhxlaAm5a8v78/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1NST9NLckTfNZZ2c21SNtjSWvmKxAhP2o/view?usp=drivesdk"
                ]
            }
        },
        "cs2006": {
            "quiz-2": {
                "Mar 2022": [
                    "https://drive.google.com/file/d/1nfESd8oncAjft5cULdDcRcfLWITnn8dF/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1n81W9BsZblnEf54xkKjDGFRgOpXJOqxY/view?usp=drivesdk",
                    "https://drive.google.com/file/d/179kAts4yOYrbesngRrQd0teO_MfyYqSb/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1Qwqny5Q8KwFeo2hJ7HbpQEEgj3yjY742/view?usp=drivesdk"
                ]
            }
        },
        "cs2003": {
            "quiz-2": {
                "Mar 2022": [
                    "https://drive.google.com/file/d/1XxrYbkew0jPZTzKELNk9aghfAqYhntZl/view?usp=drivesdk",
                    "https://drive.google.com/file/d/191e3SN3BBaVZUoAWn4ipgUq7MHKvLeBp/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1-CbtTWOImc2SdN_LGwfnIOKW88hJfZjM/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1NIJoMtYAfYkMCTrnKqUxBQIaLD4ZCpjK/view?usp=drivesdk"
                ]
            }
        },
        "cs2008": {
            "quiz-2": {
                "Mar 2022": [
                    "https://drive.google.com/file/d/1SO-t7nSLgBEAuWOZ2dMRWi07vJ9WLM03/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1sdwQ9JED-l2s9Gh8fbaxnDYX8da90nnw/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1Rf74ALA2bSmD_PCTy3U1HAaMKXZbOTTD/view?usp=drivesdk",
                    "https://drive.google.com/file/d/16lSmP9iE-Jh5Bn2IkvSi9XeUUQefTckk/view?usp=drivesdk"
                ]
            },
            "quiz-1": {
                "Jun 2022": [
                    "https://drive.google.com/file/d/1u8wq5-ZylrMcbq7TC0GLvnJ7V8q3aRaR/view?usp=drivesdk",
                    "https://drive.google.com/file/d/1y3Dya2bg7TconSnqdBWXc5mChTxrJ_pV/view?usp=drivesdk",
                    "https://drive.google.com/file/d/14oWdrmPc4tXw7ylnmZuZmFo2AScOByO_/view?usp=drivesdk"
                ]
            }
        }
    },
    "degree": {}
}

# Define the collection names
collections = {
    "foundation": "pyq/foundation",
    "diploma": "pyq/diploma",
    "degree": "pyq/degree"
}

# for level, courses in data.items():
#     print(courses, '\n')
#     for course, quiz in courses.items():
#         print(course, '\n\n\n\n', quiz)
#         doc_ref = db.collection(f"ds_courses/23t1/{course}").document('pyq')
#         doc_ref.set(quiz)


data = {
    "foundation": {
        "hs1001": {
            "course_name": " English1"
        },
        "cs1001": {
            "course_name": " CT"
        },
        "ma1002": {
            "course_name": " Statistics1"
        },
        "hs1002": {
            "course_name": " English2"
        },
        "cs1002": {
            "course_name": " Intro to Python"
        },
        "ma1004": {
            "course_name": " Statistics2"
        },
        "ma1003": {
            "course_name": " Maths2"
        },
        "ma1001": {
            "course_name": " Maths1"
        }
    },
    "diploma": {
        "se2002": {
            "course_name": "TDS"
        },
        "se2001": {
            "course_name": "System Commands"
        },
        "cs2002": {
            "course_name": "PDSA"
        },
        "ms2002": {
            "course_name": "Business Analytics"
        },
        "ms2001": {
            "course_name": "BDM"
        },
        "cs2007": {
            "course_name": "MLT"
        },
        "cs2004": {
            "course_name": "MLF"
        },
        "cs2005": {
            "course_name": "Java"
        },
        "cs2001": {
            "course_name": "DBMS"
        },
        "cs2006": {
            "course_name": "AppDev 2"
        },
        "cs2003": {
            "course_name": "AppDev 1"
        },
        "cs2008": {
            "course_name": "MLP"
        }
    },
    "degree": {}
}


courses = {}

for level, courses_dict in data.items():
    level_courses = {}
    for course_id, course_data in courses_dict.items():
        level_courses[course_id] = course_data['course_name']
    courses[level] = level_courses

doc_ref = db.collection('pyq').document('meta_data')
doc_ref.set(courses)

print(courses)

cs = {'foundation': {'hs1001': ' English1', 'cs1001': ' CT', 'ma1002': ' Statistics1', 'hs1002': ' English2', 'cs1002': ' Intro to Python', 'ma1004': ' Statistics2', 'ma1003': ' Maths2', 'ma1001': ' Maths1'}, 'diploma': {'se2002': 'TDS',
                                                                                                                                                                                                                             'se2001': 'System Commands', 'cs2002': 'PDSA', 'ms2002': 'Business Analytics', 'ms2001': 'BDM', 'cs2007': 'MLT', 'cs2004': 'MLF', 'cs2005': 'Java', 'cs2001': 'DBMS', 'cs2006': 'AppDev 2', 'cs2003': 'AppDev 1', 'cs2008': 'MLP'}}
