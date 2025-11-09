# SIMPLE PYTHON  QUIZ GAME
#AUTHOR : MAEHI SAO

score = 0

print("welcome to the python quiz game!")
print("================================")

#question 1
answer = input("Q1. What is the keyword to define a function in python?\n(a)func\n(b)define\n(c)def\n(d)function\n ANSWER:")
if answer.lower() == "c" or answer.lower == "def":
    print("correct!\n")
    score += 1
else:
        print("wrong! the correct answer is (c) def\n")

#question 2
answer = input("Q2. whta is the correct file extension for python files?\n(a).py \n(b).pyt \n(c).pt \n(d).pyth\n ANSWER:")
if answer .lower() == "a" or answer.lower() == ".py":
    print("correct!\n")
    score += 1
else:
    print("wrong! the correct answer is (a) .py\n")

#question3
answer = input("Q3. which operator is used for multipicationin python?\n(a)x\n(b)*\n(c)X\n(d)**\n ANSWER:")
if answer. lower() == "b" or answer.lower == "*":
    print("correct!\n")
    score+=1
else:
    print("wrong! the correct answer is (b) *\n")

#question4
answer = input("Q4. what data type is used to store true or false values?\n(a)string\n(b)bool \n(c)int \n(d)float\nanswer:")
if answer.lower() == "b" or  answer.lower == "bool":
     print("correct\n")
     score+=1
else:
         print("wrong! \n the correct answer is (b) bool")

#qusetion5
answer = input("Q5. what function is used to get user input in pyhton?\n(a)enter()\n(b)\nscan()\n(c)input() n\(d) type()\nAnswer:")
if answer.lower() == "c" or answer.lower == "input()":
        print("correct\n")
        score+=1
else:
            print("wrong! \n the correct answer is (c) input")
#FINAL SCORE
print("=================================")
print(" your final score")
