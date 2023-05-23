questions = ['What does CPU Stand For? ',"second","third","hello world",5]
answers_list = ["central Processing Unit","2","3","4","5"]
score = 0

if input('Would you like to play (y/n) ').lower() == 'y':
    print ("lets start the game")
    for i in range(len(questions)):
        print (f"{i+1}. {questions[i]}")
        answers = input('Enter your answer: ').lower()
        if i == 0:
            answers == answers_list[i].lower() or answers == "CPU".lower() or answers == "computer".lower()
            print ("Correct")
            score += 1
            print (f"your score is : {score} our of {len(questions)}")
            print (f"{score/len(questions)* 100} %")
        elif answers == answers_list[i].lower():
            print ("Correct")
            score += 1
            print (f"your score is : {score} our of {len(questions)}")
            print (f"{score/len(questions)* 100} %")
        else:
            print ("Wrong")
            print(f'The correct answer is {answers_list[i]}')
            print ("The correct answer is", answers_list[i])
            print (f"your score is : {score} our of {len(questions)}")
            print (f"{score/len(questions)* 100} %")


else:
    print ('Thanks for playing!')

