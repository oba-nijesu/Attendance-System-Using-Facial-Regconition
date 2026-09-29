import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://smartfacialrecogattendance-default-rtdb.firebaseio.com/"
})

# Reference to the "Students" node in Firebase
ref = db.reference('Students')

# Student data
data = {
    "2101944": {
        "name": "Obanijesu Adeyemo",
        "major": "Physics",
        "starting_year": 2021,
        "reg_number": 2101944,
        "total_attendance": 11,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "2100023": {
        "name": "Adegoke Boluwatife",
        "major": "Accounting",
        "starting_year": 2021,
        "reg_number": 2100023,
        "total_attendance": 10,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "2203145": {
        "name": "Triumph-Igurube Oreva",
        "major": "Economics",
        "starting_year": 2022,
        "reg_number": 2203145,
        "total_attendance": 7,
        "level": 300,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "2100971": {
        "name": "Chukwunenye Somto",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2100971,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
     "2101980": {
        "name": "Chimezie Prince Ozioma",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2101980,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
     "2102945": {
        "name": "Ejidoh Rhema Kosisochukwu",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2102945,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
     "2100732": {
        "name": "Nwobia David Uchechi",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2100732,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
     "2100857": {
        "name": "Olajide Olatokunbo",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2100857,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
     "2100562": {
        "name": "Agunlana Lotachukwu Emmanuel",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2100562,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
      "2101869": {
        "name": "Morodolu Christopher",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2101869,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
     "2100414": {
        "name": "Achebe Malobi",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2100414,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
     "2101817": {
        "name": "Innocent David",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2101817,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
     "2100809": {
        "name": "Harry Bernard",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2100809,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
     "2103356": {
        "name": "Anagu Seth",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2103356,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
     "2101620": {
        "name": "Chukwudulue Chiderah",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2101620,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
     "2002708": {
        "name": "Ugo Chidiebere",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2002708,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
     "2100305": {
        "name": "Okanlawon Micheal",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2100305,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
     "2002553": {
        "name": "Tamunotonye Dumo",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2002553,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
     "2101682": {
        "name": "Anyanwu Ugo",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2101682,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
     "2101606": {
        "name": "Obasuyi Imade",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2101606,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
     "2100890": {
        "name": "King Wisdom-Praise Oluwakorede",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2100890,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
     "2100361": {
        "name": "Ovotoroi Clement",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2100361,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
     "2200513": {
        "name": "Akpan Jedidiah",
        "major": "International Relations",
        "starting_year": "2022",
        "reg_number": 2200513,
        "total_attendance": 0,
        "level": 300,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "2101825": {
        "name": "Chris Peniel",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2101825,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "2101787": {
        "name": "Ebong Favor",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2101787,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    }
}

# Insert data into Firebase
for key, value in data.items():
    ref.child(key).set(value)

