import requests
import datetime as dt

WORKOUT_ID = "xxxxxxxxxxx"
WORKOUT_API = "xxxxxxxxxxx"

header = {
    "x-app-id": WORKOUT_ID,
    "x-app-key": WORKOUT_API
}

my_exercise_param = {
    "query": input("How's your workout: "),
    "gender": "male",
    "weight_kg": 74,
    "height_cm": 180.34,
    "age": 20
}
response1 = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", headers=header,
                          json=my_exercise_param)
exercises = response1.json()['exercises']
print(exercises)
x = dt.datetime.now()
for exercise in exercises:
    my_sheet_param = {
        "workout": {
            "date": x.strftime("%d/%m/%Y"),
            "time": x.strftime("%X"),
            "exercise": exercise['name'].title(),
            "duration": str(exercise["duration_min"]),
            "calories": exercise["nf_calories"]
        }
    }
    response2 = requests.post(url="https://api.sheety.co/xxxxxxxxxxx/myWorkouts/workouts",
                              json=my_sheet_param, auth=('username', 'xxxxxxxxxxx'))
    print(response2.text)
