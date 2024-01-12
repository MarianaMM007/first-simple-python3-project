questions = ['should you subscribe?', 'is coding cool?', 'does 1+1=3?', 'is java a fun language?', 'did you like the video?']

answers = ['yes', 'yes', 'no', 'no', 'no']

def quizGame():
  score = 0
  for i in range(len(questions)):
    print(questions[i])
    ans = input('please answer \n')
    if ans == answers[i]:
       print('Correct!!')
       score = score + 1
    else:
       print('sorry!!')

  print(f'Final score: {score}')


quizGame()
