"""Week 6 quiz"""

score = 0

questions = ["What is 2+2?", "What is the capital of France?", "What keyword defines a function?"]
answers = ["4", "Paris", "def"]

for i in range(len(questions)):
    user_answer = input(questions[i])
    if user_answer == answers[i]:
        print("CORRECT!")
        score = score + 1    
    else:
        print("Wrong")

        
print(score)