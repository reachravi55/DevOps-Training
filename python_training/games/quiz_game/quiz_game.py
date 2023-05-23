''' let's create a game of quiz. 
This is a simple quiz game where the user inputs an answer and the correct answer is stored in a variable. 
Let's get started.'''

print('Welcome to the quiz game!')

# let's create a variable to store the score
questionOne = 'What does CPU Stand For? '
questionTwo = 'What is the capital of India? '
questionThree = 'What is the capital of USA? '
questionFour = "what does GPU Stand For? "
questionFive = 'What element does "O" represent on the periodic table? '

list = [questionOne, questionTwo, questionThree, questionFour, questionFive]

answer_list = ['Central Processing Unit', 'Delhi','Washington', 'Graphics Processing Unit','Oxygen']

score = 0
 
print('Let\'s play a quiz!')
print('Are you really ready to play?')
if input('Type "yes" to continue or "no" to quit: ').lower() == 'yes':
    print('Let\'s start!')
    for i in range(len(list)):
        print(f'{i+1}. {list[i]}')
        answer = input('Enter your answer: ')
        if i == 3:
                answer.lower() == "graphical processing unit" or answer.lower() == "graphics processing unit" or answer.lower() == "graphic processing unit"
                print('Correct!')
                score += 1
        if i == 2:
                answer.lower() == "Washington" or answer.lower() == "Washington D.C" or answer.lower() == "DC" or answer.lower() == "D.C" or answer.lower() == "Washington DC"
                print('Correct!')
                score += 1
        elif answer.lower() == answer_list[i].lower():
            print('Correct!')
            score += 1
        else:
            print('Wrong!')
            print(f'The correct answer is {answer_list[i]}')

        print(f'Your score is {score} out of {len(list)}')
        total_score = (score/len(list))*100
        print(f'Your score is {total_score}%')