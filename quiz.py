import json
print ("Welcome to movie quiz")
print("Enter your name, please: ")
x = input()
print("Welcome, " + x) 
print("You will be presented with 20 Questions. Enter your choice to get the points. Good luck!")
score = 0
name = ""

   
def questions(all_questions):
    global score
    
    print(all_questions["Question"])
    print("1", all_questions["1"])
    print("2", all_questions["2"])
    print("3", all_questions["3"])
    print("4", all_questions["4"])

    guest_answer = input('Your answer:')
   

    if guest_answer == all_questions["right_answer"]:
        score += 1
        print("Great! You've earned a point. You've got:", score, "points")
           
    else:
        print("Sorry, this is wrong answer")
        print("The right answer is", all_questions["right_answer"])

def only_num(guest_answer):
    while True:
     try:
        userInput = int(input()) 
     except ValueError:
            print("Enter anumber. Please")
     else:
         return 
         guest_answer
         break

            



        

with open("quiz_main.json") as que_s:
    all_questions = json.load(que_s)
    
    for i in range(0, len(all_questions)):
        questions(all_questions[i])

print("This is the end of quiz. You've got", score, "points. Congratulations")       