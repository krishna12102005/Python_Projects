questions = ("How many elements are in the periodic tabel ?" ,
             "Which animal lays the largest eggs ?" ,
             "What is the most abudant gas in the earth atmosphere ?" ,
             "How many bones are there in the human body ?" ,
             "Which planet in the solar system is hottest ?")

options = (("A.309" , "B.234" , "C.118" , "D.89") ,
           ("A.Hen" , "B.Oggy" , "C.Elephant" , "D.Ostrich") ,
           ("A.Nitrogen" , "B.Oxygen" , "C.Carbonmonoxide" , "D.Carbondioxide") ,
           ("A.206" , "B.207" , "C.208" , "D.209") ,
           ("A.Mercury" , "B.Venus" , "C.Sun" , "D.Jupiter"))

answers = ("C" , "D" , "A" , "A" , "B")

score = 0

question_num = 0

for question in questions:
    print("----------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter the option ")
    if guess == answers[question_num]:
        print("Correct!")
        score+=1
    else:
        print("Wrong!")

    question_num += 1


print("Thank you for participating in quizz")
print(f"Your score is {score} / {len(questions)}")
