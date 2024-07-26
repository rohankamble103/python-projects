print('''
Welcome to my Quize !
    ''')

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print('''
Okay! Let's play :) 
    ''')
score = 0
total = 0

question = input('''Q1. Who is known as the father of modern computers ?                
A) Charles Babbage
B) Alan Turing
C) John von Neumann
D) Bill Gates
select one of the above from ( A,B,C,D ) :- ''')
if question.lower() == "a":
    print('''
You are abosolutely Correct
          ''')
    score += 1
    total += 1
else:
    print('''
You are abosolutely Incorrect
          ''')
    total += 1


question = input('''Q2. What is the capital of Australia ?                 
A) Sydney
B) Melbourne
C) Canberra
D) Brisbane
select one of the above from ( A,B,C,D ) :- ''')
if question.lower() == "c":
    print('''
You are abosolutely Correct
          ''')
    score += 1
    total += 1
else:
    print('''
You are abosolutely Incorrect
          ''')
    total += 1


question = input('''Q3. What is the chemical symbol for gold?                
A) Au
B) Ag
C) Go
D) Fe
select one of the above from ( A,B,C,D ) :- ''')
if question.lower() == "a":
    print('''
You are absolutely Correct
          ''')
    score += 1
    total += 1
else:
    print('''
You are absolutely Incorrect
          ''')
    total += 1


question = input('''Q4. Which planet is known as the Red Planet?                
A) Venus
B) Mars
C) Jupiter
D) Saturn
select one of the above from ( A,B,C,D ) :- ''')
if question.lower() == "b":
    print('''
You are absolutely Correct
          ''')
    score += 1
    total += 1
else:
    print('''
You are absolutely Incorrect
          ''')
    total += 1


question = input('''Q5. What is the value of π (pi) up to two decimal places?                
A) 3.12
B) 3.14
C) 3.16
D) 3.18
select one of the above from ( A,B,C,D ) :- ''')
if question.lower() == "b":
    print('''
You are absolutely Correct
          ''')
    score += 1
    total += 1
else:
    print('''
You are absolutely Incorrect
          ''')
    total += 1


print("You got " + str(score) + " questions correct of " + str(total) + " And got " + str((score / total ) * 100) + ''' % 
    ''')
