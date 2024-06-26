from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

budget_property_map = {
    "40-60 Lakhs": ["Whitefield", "Sarjapur", "Electronic City", "K.R Puram "],
    "60-80 Lakhs": ["Whitefield", "Electronic City", "K.R Puram", "Akshaya Nagar", "Varthur Hobli", "RR Nagar"],
    "80-1 Cr": ["RR Nagar", "JP Nagar", "Nagarbhavi", "Begur Road", "K.R Puram", "Whitefield"],
    "1 Cr - 1.5 Cr": ["Whitefield", "Begur Road", "Kengeri", "RR Nagar"],
    "1.5 - 2 Cr": ["RR Nagar", "Sarjapur"],
    "2 - 2.5 Cr": ["RR Nagar", "Sarjapur"],
    "4.45Cr": ["RR Nagar"],
}

PROPERTIES = [
    {
        "project_name": "DS Max SkySamurai",
        "property_type": ["apartment"],
        "budget_range": ["40-60Lakhs", "60-80Lakhs", "80-1Cr"],
        "property_area": "Whitefield",
        "address": "Whitefield",
        "floor_plans": [
            {"floor": "2BHK", "price": "45.63L - 58.35L"},
            {"floor": "3BHK", "price": "64.04L - 1Cr"}
        ],
        "map_url": "https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d3887.8156493815745!2d77.82312837507665!3d12.983639987332868!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zMTLCsDU5JzAxLjEiTiA3N8KwNDknMzIuNSJF!5e0!3m2!1sen!2sin!4v1719383207365!5m2!1sen!2sin",
        "image_src": "https://lh3.googleusercontent.com/pw/AP1GczOvf3QLNn4TOdIR0hS5NNHGkDC9r2g8rwwgeYXcV34XCfvevxEmniA40x4G7bfkrBz2h_HwdvuCXDvfKOxZDLqEPZaUDFk8HWtSzVOHrSdR2kxyrl_W7yjyuC51McBUHYL4mpAeG8mrWXMTwVUXe-7ZzAehVWSLOqGYgdP7KoVgGzGdL-6yzT3UmZpyI8zAzQmcX5UeT40HSPbFRqGJ56h3Kz-R6pJM_gUBolkWnzCOP6KMPj-9HGQGPcww70aUab5KPgpH6FVpIcSy3UjvBlv-Jb3uOVQxk0q9C1x7uEfScFMt5i4nDDR6xOWJ5vCnCISoU225lGWEIN74FOtEmiboqvnQNrk4oe-4oDWp6kTK50z_wlCsKLbUO9w-1sovV-HAmNYp8q-tR2zhd2bsalQD3PBIQNbacwERcfNVFBzQecs6yNQyLkXHdsWkTdbePoYF7sUUkbof7LLkybRw_Y2tIkyiaVqWyDGm3gIMSxwOGYuZipsqbKVQdm7IukgmBqngf0qPfco5PEqx3uWm47NC4rjbdShezUv2ezFrZ8tTrFLOFAK3mbQ1BOHtzqvQZp2_uNLHoHKK6E5tZ4SwjrSKMT-L1pVsC7Z-nyb3d06BFPvC2opKZ-lgtT5_e1xlUqGNxBAk9MIcc6RuDSQRTCzz4E7pa3jvOWjhQ5LtMGZOvctWwgYl1t67uCX-NPgs_oJIN4PaRQtIOWQvm3ovLT6yWglQd406qGHsDQOMK7K6SamXCSJrrse3Ll81sz-GrY9DaHIUFTYFNrHNHWe5Hc4rEGyCXmfHhWifo0N-PJwxDEMahgKbo6UhhXn1Xc2YC-I2U9RuG4at4xv3R8gud9C__nL-A8f7HqXO7Qpb8eX1gPAqs0WyZ17qX_Sfeo9_qhBbzzvLVD1qACUK9i3ZMUA=w913-h913-s-no-gm?authuser=0",
        "brochure_link": "18aAvrARhOA3q7CUcIIxpxcr2xQwRGzHD",
    },
    {
        "project_name": "Ds Max Spoorthi",
        "property_type": ["apartment"],
        "budget_range": ["40-60Lakhs"],
        "property_area": "Sarjapur",
        "address": "Sarjapur",
        "floor_plans": [
            {"floor": "2BHK", "price": "38.72L - 44.12L"},
            {"floor": "3BHK", "price": "46..84L - 49.80L"}
        ],
        "map_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3890.405261429205!2d77.77302277483861!3d12.817068387484236!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae73e1e4fd6405%3A0x236d1346632b1185!2sDS%20MAX%20Spoorthi!5e0!3m2!1sen!2sin!4v1719381475072!5m2!1sen!2sin",
        "image_src": "",
        "brochure_link": "1zThaQH9su4rS-Rm1ICgPTPNmeoI2V5EM",
    },
    {
        "project_name": "Ds Max Sahara Grand",
        "property_type": ["apartment"],
        "budget_range": ["40-60Lakhs", "60-80Lakhs", "80-1Cr"],
        "property_area": "ElectronicCity",
        "address": "ElectronicCity",
        "floor_plans": [
            {"floor": "2BHK", "price": "54.10L - 63.55L"},
            {"floor": "3BHK", "price": "69.45L - 99.12L"}
        ],
        "map_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3889.6596344514796!2d77.69034907483946!3d12.865246687440386!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae6d003f8b752b%3A0x87e2f999d68c6259!2sDS-MAX%20Sahara%20Grand!5e0!3m2!1sen!2sin!4v1719381553929!5m2!1sen!2sin",
        "image_src": "",
        "brochure_link": "1geyNg7RWW7ti8kVw5Z4hSAWoy-ipOY0y",
    },
    {
        "project_name": "Ds Max Skyblossom",
        "property_type": ["apartment"],
        "budget_range": ["60-80Lakhs", "80-1Cr", "1-1.5Cr"],
        "property_area": "BegurRoad",
        "address": "BegurRoad",
        "floor_plans": [
            {"floor": "2BHK", "price": "71.34L - 80.25L"},
            {"floor": "3BHK", "price": "85.50L - 1.16Cr"}
        ],
        "map_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3889.5867853202744!2d77.63218367483952!3d12.869944287436176!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae6b335ef2be13%3A0xdd22ed0384cf51e5!2sDS-MAX%20SkyBlossom!5e0!3m2!1sen!2sin!4v1719381602416!5m2!1sen!2sin",
        "image_src": "https://lh3.googleusercontent.com/pw/AP1GczP1ONS76OJYqG3ohRTU-HxoMEP4Bw70PpVdWT7r9iuBgbRH7v9gNz7thgqhnJpiiINy_hTXlUaORBvnzvPPaNlSk3CAHof_6iCnRkHtMRByDDXiY6YeuiAFC_lsCD2Bs8hxv3s6f605GXva32JTi7I=w913-h913-s-no-gm?authuser=0",
        "brochure_link": "1B3a-E8iSQF3X5fyXhYZt5NXSl7fG9K8Z",
    },
    {
        "project_name": "Ds Max Skyshubham",
        "property_type": ["apartment"],
        "budget_range": ["40-60Lakhs", "60-80Lakhs", "80-1Cr"],
        "property_area": "K.RPuram",
        "address": "K.RPuram",
        "floor_plans": [
            {"floor": "2BHK", "price": "53.70L - 68.94L"},
            {"floor": "3BHK", "price": "73.13L - 87.72L"}
        ],
        "map_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d124424.94413527833!2d77.58612415243472!3d12.953958254994914!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae11cc88e603a5%3A0xdf7db18f662aa4a3!2sDS-MAX%20SKYSHUBHAM!5e0!3m2!1sen!2sin!4v1719381664330!5m2!1sen!2sin",
        "image_src": "",
        "brochure_link": "186I5M7J4jt2RgyMd9f8CSHxdiqHqjUPW",
    },
    {
        "project_name": "Suraksha Spring",
        "property_type": ["apartment"],
        "budget_range": ["80-1Cr", "1-1.5Cr"],
        "property_area": "BegurRoad",
        "address": "BegurRoad",
        "floor_plans": [
            {"floor": "2BHK", "price": "90L"},
            {"floor": "3BHK", "price": "1.1Cr"}
        ],
        "map_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3889.7068384340027!2d77.61206097483947!3d12.862201887443268!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae6b0e8ca572d1%3A0x193a99119463a09b!2sSuraksha%20Springs!5e0!3m2!1sen!2sin!4v1719381711384!5m2!1sen!2sin",
        "image_src": "https://lh3.googleusercontent.com/pw/AP1GczPlOp4hSgbeXLwPAI8WRsvU4lQ5dpnofqdLjoHa3lqR_hbBwjLJOFKzWxmdoFeqmUuVGCNSLN-321hPgYqQEhq1dXgUeaTxxkB2noAV0vQXZQHnJEGwCdZLHuzpNRemD3uIPud_Q-zLYMKUCe9TQIQ=w913-h913-s-no-gm?authuser=0",
        "brochure_link": "1C3bISs4rUcBrRQaXJZHCfdWPEGihyf6A",
    },
    {
        "project_name": "Suraksha Heritage Park",
        "property_type": ["apartment"],
        "budget_range": ["80-1Cr", "1-1.5Cr"],
        "property_area": "BegurRoad",
        "address": "BegurRoad",
        "floor_plans": [
            {"floor": "2BHK", "price": "93L"},
            {"floor": "3BHK", "price": "1.20Cr"}
        ],
        "map_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3889.5941185602514!2d77.61985087483957!3d12.869471487436627!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae6b7949b28b51%3A0xff5ae85bfd350ebe!2sSuraksha%20Heritage%20Park!5e0!3m2!1sen!2sin!4v1719381774140!5m2!1sen!2sin",
        "image_src": "https://photos.fife.usercontent.google.com/pw/AP1GczOCL7ei3xKvTxhjs7NHpB3ui1xZOXJfQEK3zyoGbMxJgE6Fq5eeRrn6lcYh_GMSkW8yAFY8y3UmjWxx-ddIPSWC9bxi=w913-h913-s-no-gm?authuser=0",
        "brochure_link": "",
    },
    {
        "project_name": "Vaaradhi Blossom",
        "property_type": ["apartment"],
        "budget_range": ["60-80Lakhs"],
        "property_area": "AkshayaNagar",
        "address": "AkshayaNagar",
        "floor_plans": [
            {"floor": "2BHK", "price": "61 lakh"},
            {"floor": "3BHK", "price": "79 lakh"}
        ],
        "map_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3889.5638160477306!2d77.6187223748396!3d12.87142508743472!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae6b003c49cc99%3A0x8a94abea2cf3268e!2sVAARADHI%20BLOSSOM!5e0!3m2!1sen!2sin!4v1719381872514!5m2!1sen!2sin",
        "image_src": "",
        "brochure_link": "1CO1dN6zWUGfO6M0UzXpG2ccHOqeg9q5Q",
    },
    {
        "project_name": "Vaaradhi Aquila",
        "property_type": ["apartment"],
        "budget_range": ["60-80Lakhs"],
        "property_area": "VarthurHobli",
        "address": "VarthurHobli",
        "floor_plans": [
            {"floor": "3BHK", "price": "75 Lakhs"}
        ],
        "map_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3889.068524157705!2d77.68173957484015!3d12.903315287405793!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae13001c5350b7%3A0x2fffc2ec009e5fcf!2sVAARADHI%20AQUILA!5e0!3m2!1sen!2sin!4v1719381921645!5m2!1sen!2sin",
        "image_src": "",
        "brochure_link": "1BrTskOIZcOxm-q8IPfwRhbwXP7sit--v",
    },
    {
        "project_name": "Durga Devi",
        "property_type": ["individual house"],
        "budget_range": ["80-1Cr"],
        "property_area": "Nagarbhavi",
        "address": "Nagarbhavi",
        "floor_plans": [
            {"floor": "3BHK", "price": "90 lakhs"}
        ],
        "map_url": "",
        "image_src": "",
        "brochure_link": "",
    },
    {
        "project_name": "Ganesh Enclave",
        "budget_range": ["1-1.5Cr"],
        "property_type": ["individual house"],
        "property_area": "Kengeri",
        "address": "Kengeri",
        "floor_plans": [
            {"floor": "3BHK", "price": "1.40Cr"}
        ],
        "map_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3886.5422590630287!2d77.48055067484306!3d13.064782587259266!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae23456a84e247%3A0xa9e568206244099c!2sGanesh%20enclave%2C%20Thotada%20Guddadhalli%20Village%2C%20Bengaluru%2C%20Karnataka%20562123!5e0!3m2!1sen!2sin!4v1719382331298!5m2!1sen!2sin",
        "image_src": "",
        "brochure_link": "",
    }, {
        "project_name": "ABM Homes",
        "property_type": ["apartment"],
        "budget_range": ["80-1Cr"],
        "property_area": "JPNagar",
        "address": "JPNagar",
        "floor_plans": [
            {"floor": "3BHK", "price": "90 lakhs"}
        ],
        "map_url": "https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d2459.163668224437!2d77.57441434142383!3d12.872110632686915!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zMTLCsDUyJzE5LjYiTiA3N8KwMzQnMzIuNyJF!5e0!3m2!1sen!2sin!4v1719382128329!5m2!1sen!2sin",
        "image_src": "",
        "brochure_link": "1gVfr1KNErJd_svEwvFFUJWAGOgx0M6Db",
    }, {
        "project_name": "NY home",
        "property_type": ["individual house"],
        "budget_range": ["4.45Cr"],
        "property_area": "RRNagar",
        "address": "RRNagar",
        "floor_plans": [
            {"floor": "5BHK", "price": "4.45Cr"}
        ],
        "map_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3888.737284326374!2d77.6026706779325!3d12.924599554863219!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae1565dda42255%3A0xcafec21282283ad1!2sN%20Y%20homes!5e0!3m2!1sen!2sin!4v1719382443231!5m2!1sen!2sin",
        "image_src": "",
        "brochure_link": "",
    },
    {
        "project_name": "Elegant Hermitage",
        "property_type": ["apartment"],
        "budget_range": ["1-1.5Cr", "2-2.5Cr"],
        "property_area": "RRNagar",
        "address": "RRNagar",
        "floor_plans": [
            {"floor": "2BHK", "price": "1,06 Cr - 1.17 Cr"},
            {"floor": "3BHK", "price": "1.34 Cr - 1.5 Cr"},
            {"floor": "4BHK", "price": "2.10 Cr"},
        ],
        "map_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3889.1400454832615!2d77.50737897792935!3d12.898715054947473!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae3fba8319e2d3%3A0xdaa4ed2382f22976!2sElegant%20Hermitage!5e0!3m2!1sen!2sin!4v1719382207883!5m2!1sen!2sin",
        "image_src": "https://lh3.googleusercontent.com/pw/AP1GczOuOGKvPGs96tRIUoD9-rHp16f-athebc3yzyBPdOOsZRouqGQt72NQ6lXwZOnvX-5HLNcD4Pro5jTKfKOCAvNxPSFE8ZC8pecpPoIO52WBY3ldLknTGVCCUxzeUW2dJ5cX25TZT_btcIpKBy5oZ2C4Fx40ITAy329Q-XCI-ZJO0mrgHy6bdKJnWel_Z087suzl4rpN4sCjyFZFc0HF61bKeYgGybMuZcHEUvWPCzR9GE060DLOgAkpIUuduHttKMYg6UG9pQdA-3-Ao0GQ7vazYesSwuddbqFf9G9EUBslJ1UG3Edog430n9kZOXBH0t7o9SFwl48b-NJiNCwW2k_AK0yIAvaeN6AcPuhjr0GdSmdXSTHnYBwSGZAXVrmK-bEyBbWPmUfryJOxEM4V8Ngw1gs-1CcBjKIFNIupKZVfaaE8gSVxZZSBzj24D8BVdgsF-4mngkAlKvTeyM9AO5qmEssZe_8FYA5_i72xYwzNnRpEy-xA0REDSrjvd4EcTugOXhmn-R4dFWHvpgDjIxu93ZcDkFSE6a4ezC87b-NelJ4kGGBPIX4mXbAT9Xfdk42P9jrhvDmVcGkdwmkHwQ4vWY_Vi5osN_RLiI0ckZEatEmvS_mI-NhRGDCd5Zsj8ZiFM0wd-A3vFi6Cy68y1_x_uh9jpuEQ-F5eSA_3PHlyIg1PltDURsm4f59SPKtVSQ3RMcwkwKzdqGtyYBOge17kyQGijsIXbXVxdb-Aw4g6mJyWv6u0AWrjzKdo-vJk6BV07f2nW95B7i6-TjHukvNOj6P81V5iulYMtXhftW1itzM5EBfQudTtbxtKeEZWFWmqhkoqiWaNWVxrxZzyNADOn32rEIkSA70m_WHT25mENypitPiUGq4YCcqsiJLdSTn5nRlKDU9X3xCtlk7XFg=w913-h913-s-no-gm?authuser=0",
        "brochure_link": "1MqTKBNEvKhzCeyiCzCqs2CwW8iJjtb1P",
    },
    {
        "project_name": "Garudadri Gardens",
        "property_type": ["apartment"],
        "budget_range": ["60-80Lakhs", "80-1Cr"],
        "property_area": "RRNagar",
        "address": "RRNagar",
        "floor_plans": [
            {"floor": "2BHK", "price": "71.03 L - 77 L"},
            {"floor": "3BHK", "price": "93.5 L - 96.02 L"}
        ],
        "map_url": "https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d3889.0514339335064!2d77.4914157750753!3d12.904414287404778!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zMTLCsDU0JzE1LjkiTiA3N8KwMjknMzguNCJF!5e0!3m2!1sen!2sin!4v1719383070329!5m2!1sen!2sin",
        "image_src": "https://lh3.googleusercontent.com/pw/AP1GczOwZWZA8Rop0qflDzOPIELKd553YbOZj3TYgEVPOy1qa4UySPtpxp9EdwlEl-fBCf_0FB9On2EB555LFUu2VjDTu-aiE2tbBPQ4Gp7W4ENcDlgiOzTi-4le4FkSPYYwxvnZXnhnf7MZrhLAMMsYSKlUJbNZqsg42YvFC8EZdvf9z57HENNdpmBVDRcDOiISN2eqRP_SX8D8ayyqZKYs9QQ9BAyH2__9yShLMNVmcSJdmvBB9eLy4d6rTwjGPwomgDUAZFj5ghQOtgrqAfoZ1gOTDujezDT-ov2lKEW5rprWxFJvkkfZ5I5Au77QPHZjhV5mVpBaLIhxWWIM0SZuLRdZP0NKVvr2i9JnGxyz4S5FmaZkSSdGq61aprFJFlnPh_f-etXdql-BvHOaJOd1gdk76TGHSsWiufo6MTfhEsR7fwRUAwU-4HL-t6eychnZsgfN_Hr5oKgBpIDcQmMGLARJxpGGBJ0rPzxyuJ5kgvztSyBndTtq6fddjGY-vjzJoex1X2Ewv85olP5EzhPPSfwptdCPm_9QdKe8ApBf2S6GGlbCT1bRrv1uSAR3NWCRS0kVCV9er-glseyAErjjH-eaT-4GWHxLVtaEGAKmnX50EbeOS-_DFBMWCw7I-Ju6G2U_gaRWngMMJDMhZlTBGnwqjjWb9Uxc1WHVeOHpLXCABC5qVL3-Tx7cK8gzld1e7se9Yp8O9vLgLKA9Y4lJR90rCLIsyKPZKAO-m1Eg_Z9mla3KXczLgY-HHOTBjjsUNa-VHO_gs6HXopTImsyFD3eRvctGGGAOYbicDsVxhOUyiyUebyH6LhP3mfLtTo24HK0UZWyxN8WloYmBMrat6r8nWPX6Gl3YkFRpuvdwi6PH5tKBWzsRBWj35_noIvjev0MGtgtc9H9mtMFYZ897J2Q=w913-h913-s-no-gm?authuser=0",
        "brochure_link": "1V1RxDkpVdUDJG4FfYhuvNoWmJEVp39NS",
    },
    {
        "project_name": "Samaya Sunshine",
        "property_type": ["apartment"],
        "budget_range": ["80-1Cr"],
        "property_area": "RRNagar",
        "address": "RRNagar",
        "floor_plans": [
            {"floor": "2BHK", "price": "84 L"},
            {"floor": "3BHK", "price": "85 L -   90 L"}
        ],
        "map_url": "https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d3889.0418120831578!2d77.49629707507536!3d12.905032987404212!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zMTLCsDU0JzE4LjEiTiA3N8KwMjknNTUuOSJF!5e0!3m2!1sen!2sin!4v1719383112890!5m2!1sen!2sin",
        "image_src": "https://lh3.googleusercontent.com/pw/AP1GczP4NdEEoTuubwwEB-jB4sHnPXGa89mMa3fvXltgPiEON1ULPDzV1NbfC-4b-kpVgsrD_8tJa8NHzLvXA3ZSuV16IUCb0DS-IlvHOnEJnfAM2guXwu3DSwGwzg8v8uzoezwoKNz-5RLITaDfU-VyGlM=w913-h913-s-no-gm?authuser=0",
        "brochure_link": "1xjgzEcEdw4GKXs5_BgSmRz8QE2KTi5n_",
    },
    {
        "project_name": "Sonin Park South",
        "property_type": ["apartment"],
        "budget_range": ["1-1.5Cr", "1.5-2Cr"],
        "property_area": "JPNagar",
        "address": "JPNagar",
        "floor_plans": [
            {"floor": "2BHK", "price": "1.11 Cr - 1.19 Cr"},
            {"floor": "3BHK", "price": "1.46 Cr - 1.52 Cr"}
        ],
        "map_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3889.4040254325937!2d77.58540187792731!3d12.881721955002762!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae15007b3fde11%3A0x81f664abcf29ca45!2sSonin%20Park%20South!5e0!3m2!1sen!2sin!4v1719382899294!5m2!1sen!2sin",
        "image_src": "https://lh3.googleusercontent.com/pw/AP1GczPiVZfFwEwFMIunRDG4a1FJOFvbk5QBI0wfNVzsOy_DgYTSriK7t3wBU0GrtdhL6O4OgAXLqeR2Hr9vA5gryjiN8K_MHKwgqMwnaZSXFh3vytmee0k1ASVI2e2deXvrwTGYof08q-PKKc7bG3POQpc=w913-h913-s-no-gm?authuser=0",
        "brochure_link": "1hR9H6SqPTw_ssENxbuHt14RDiRet6y9L",
    },
    {
        "project_name": "La Vivante",
        "property_type": ["villa", "villament"],
        "budget_range": ["1-1.5Cr", "1.5-2Cr", "2-2.5Cr"],
        "property_area": "Sarjapur",
        "address": "Sarjapur",
        "floor_plans": [
            {"floor": "2BHK", "price": "1.22 - 1.36 Cr"},
            {"floor": "3BHK", "price": "1.87 - 2.45 Cr"}
        ],
        "map_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15561.354030764496!2d77.75179518715818!3d12.82138889999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae73d7f5952d81%3A0xc95c3f0256311975!2sATCO%20LA%20VIVANT!5e0!3m2!1sen!2sin!4v1719383007708!5m2!1sen!2sin",
        "image_src": "https://lh3.googleusercontent.com/pw/AP1GczMcwIxqoq2RsmPwrFdTTeArvcA-jTF7cgFa-kW2EmucI_1T7IfoOL0HFz7BKmkw5nYvei4fqD6Sv_vYwu6ROzaoF6YeIgShJczayL4rXUHX1csIWFee0TC2KuYOhU4Du-SiGkoqvu811QGx3ehgiDI=w913-h913-s-no-gm?authuser=0",
        "brochure_link": "1hrwWfQdoEvykAxrzrCncoELcSe3BOWuy",
    },

]


class ActionShowFloorPlans(Action):
    def name(self) -> Text:
        return "action_show_floor_plans"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        property_type = tracker.get_slot('property_type')

        floor_plan_options = set()

        for project in PROPERTIES:
            if property_type in project.get("property_type"):
                for floor_plan in project.get("floor_plans"):
                    floor_plan_options.add(floor_plan.get("floor"))

        if not floor_plan_options:
            floor_plan_options = ["2BHK", "3BHK", "4BHK", "5BHK"]

        custom_payload = {
            "type": "budget_options",
            "options": list(floor_plan_options),  # Convert set to list for the payload
        }

        dispatcher.utter_message(text="Here are the floor plan options:", json_message=custom_payload)
        return []


class ActionShowBudget(Action):
    def name(self) -> Text:
        return "action_show_budget"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        property_type = tracker.get_slot('property_type')
        floor_plan = tracker.get_slot('floor_plan')

        budget_options = set()

        for project in PROPERTIES:
            if property_type in project.get("property_type"):
                for floor_plans in project.get("floor_plans"):
                    if floor_plan == floor_plans.get("floor"):
                        for budget_range in project.get("budget_range"):
                            budget_options.add(budget_range)

        if not budget_options:
            budget_options = ["40-60Lakhs", "60-80Lakhs", "80-1Cr", "1-1.5Cr", "1.5-2Cr", "2-2.5Cr"]

        custom_payload = {
            "type": "budget_options",
            "options": list(budget_options)
        }

        dispatcher.utter_message(text="Here are the budget options:", json_message=custom_payload)
        return []


class ActionShowAreas(Action):
    def name(self) -> Text:
        return "action_show_area"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        property_type = tracker.get_slot('property_type')
        floor_plan = tracker.get_slot('floor_plan')
        budget_range = tracker.get_slot("budget_range")
        area_options = set()

        for project in PROPERTIES:
            if property_type in project.get("property_type"):
                for floor_plans in project.get("floor_plans"):
                    if floor_plan == floor_plans.get("floor"):
                        if budget_range in project.get("budget_range"):
                            area_options.add(project.get('property_area'))

        print("area: {}", area_options)
        if not area_options:
            area_options = ["Whitefield", "JP Nagar", "Nagarbhavi", "Begur Road", "Kengeri", "Sarjapur",
                            "Electronic City", "K.R Puram", "Akshaya Nagar", "Varthur Hobli", "RR Nagar"],

        custom_payload = {
            "type": "area_options",
            "options": list(area_options),
            "apartment": [property_type, floor_plan, budget_range]
        }

        dispatcher.utter_message(text="Here are the area options:", json_message=custom_payload)
        return []


class ActionShowProperties(Action):
    def name(self) -> Text:
        return "action_show_properties"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        budget_range = tracker.get_slot('budget_range')
        property_type = tracker.get_slot('property_type')
        property_area = tracker.get_slot('property_area')
        floor_plan = tracker.get_slot('floor_plan')

        projects = []
        for project in PROPERTIES:
            if (property_area == project.get('property_area') and
                    budget_range in project.get("budget_range") and
                    property_type in project.get("property_type") and
                    any(fp["floor"] == floor_plan for fp in project.get("floor_plans", []))):
                # Create a tuple of (key, value) tuples for the project attributes
                project_data = tuple((key, value) for key, value in project.items())
                projects.append(project_data)  # Add the tuple to the set

        if not projects:
            projects = PROPERTIES

        custom_payload = {
            "type": "project_options",
            "options": list(projects)
        }

        dispatcher.utter_message(text="Here are the property options:", json_message=custom_payload)
        return []



