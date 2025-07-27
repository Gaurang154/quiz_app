import json
import random
import sys
import time 
score = 0
print("Hi Hope You Will Enjoy My Game \n")
name = input("Please Enter Your Name \n")
print("Lets Begin! ")
with open('questions.json' , 'r') as file:
    questions = json.load(file)
random.shuffle(questions)
start_time = time.time()
for q in questions:
    print("\n" , q["question"])
    for key , value in q["options"].items():
        print(f"{key}:{value}")
    while True:
        a = input("Choose correct answer \n")
        if a.upper()==q["answer"]:
            score = score+1
            print ("Correct Answer ✅")
            break
        elif a.upper() in ["A" ,"B" , "C" , "D"]:
            print("Incorrect " ,q["answer"] , "is correct answer")
            break
        else:
            print("Please choose between A , B , C , D")
end_time=time.time()
total_time=end_time-start_time
print ("Mr." , name.capitalize() , "Scored" , score , "out of" , len(questions)) 
percentage = (score/len(questions))*100
print(f"Your scored {percentage:.2f}%")
minutes = int(total_time // 60)
seconds = int(total_time % 60)
print(f"You completed the quiz in {minutes} minute(s) and {seconds} second(s).")

b =input("Do you want to save your score (yes/y):") .strip().lower()
if b in ["yes", "y"]:
    try:
        with open ('leaderboard.json' , 'r') as file :
            leaderboard_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        leaderboard_data = []
    leaderboard_data.append({
    "name": name,
    "score": score,
    "percentage": percentage,
    "time_taken": f"{minutes}m {seconds}s"
})
    leaderboard_data.sort(key = lambda x: x["score"] , reverse = True)
    with open ('leaderboard.json' , 'w') as file:
        json.dump(leaderboard_data , file , indent=4)
else:
    print ("Score is not scored \n")
    sys.exit()