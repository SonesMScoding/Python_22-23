
class Question:  
    def _init_(self):
        self.qvalue = input("Enter the true or false question.")
        self.avalue = input("Enter T or F for the correct answer.")
        self.pvalue = int(input("How many points is this question worth?"))
        
questionsArray = []
def Test():
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
