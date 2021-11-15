import json
print ("Welcome to movie quiz")
print("Enter your name, please: ")
x = input()
print("Welcome, " + x, "You will be presented with 20 Questions. Enter your choice to get the points. Good luck!")
score = 0
name =""



def quest_answer(all_questions):
    print()
    
    

with open("quiz.json") as que_s:
    all_questions = json.load(que_s)

    
    for i in range(0, len(all_questions)):
        print(all_questions[i]["Question"])
