#Write a program that solves the following:

#They would like to be able to create questions and answers as objects. 
# They also want these objects to be comparable based on points that the questions are worth. /assigned value I assume
#They want the students to take the tests in the terminal. (100 pts)
#The teacher also requests a terminal interface that allows them to give the tests to students. (25 pts)
#Include a test class for this program that shows the user how to use it (25 pts)


#Write a GUI version of the previous program. 
# The teacher got tired of using the terminal to give the tests and wants to use a graphical component to do it instead. (125)

from Question import Question

questionsArray = []
class Test:
    number = int(input("How many questions do you want in your test?\n"))
    for i in range(number):
        questionsArray.append(Question())
            
        score = 0
        earnedpoints = 0
        totalpoints = 0
        correct = 0
    
        for i in range(len(questionsArray)):
            studentanswer = input(Question.qvalue)
            totalpoints += int(Question.pvalue)
        
            if studentanswer == Question.avalue:
                earnedpoints += Question.pvalue
                correct += 1
    
        score = ((earnedpoints / totalpoints) * 100)
           
           
Test()
