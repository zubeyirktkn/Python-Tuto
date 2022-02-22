import random
#soru havuzunu artır ve soruyu havuzdan random seçip seçileni tekrar sorma
#şık sistemi yaparak cevapları şıklara göre değerlendir hepsini baştan yaz
#Question
class Question:
    def __init__(self,text,choices,answer):
        self.text=text 
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer== answer
#-----------------------------------------
#Quiz
class Quiz:
    def __init__(self,questions):
        random.shuffle(questions)#sorular listesini karıştırır
        self.questions = questions
        self.score = 0
        self.questionIndex = 0 #random.randint(0,len(questions)-1)
    #----------------------------------------------------------
    def getQuestion(self):
        return self.questions[self.questionIndex]
    #-------------------------------------------------------------
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Question {self.questionIndex+1}:{question.text}")
    
        for q in question.choices:
            print("-"+ q)
        
        answer=input("Answer:")
        self.guess(answer)
        self.loadQuestion()
    #----------------------------------------------------------------
    def guess(self,answer):
        question = self.getQuestion()
        answer = answer.upper()#büyük harf yap
        if question.checkAnswer(answer):
            quiz.score+=1
        self.questionIndex+=1
    #----------------------------------------------------------------
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    #------------------------------------------------------------------
    def showScore(self):
        print(f"Score:{self.score}")
    #-------------------------------------------------------------------
    def displayProgress(self):
        totalQuestion =len(self.questions)
        questionNumber = self.questionIndex+1

        if(questionNumber>totalQuestion):
            print("Quiz over.")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(50,"*"))
#--------------------------------------------------------------------------
q1=Question("Kuantum fiziğinin başlangıcı kabul edebileceğimiz deney hangisidir?",["A:Çift Yarak Deneyi","B:Çift Yarık Deneyi","C:Çift Tarak Deneyi","D:Çift Kürek Deneyi"],"B")
q2=Question("Kuantum belirsizliği denilince akla gelen hayvan hangisidir.",["A:Heisenberg'in kedisi.","B:Schrodingerin Köpeği","C:Schrodinger'in kedisi.","D:Heisenberg'in köpeği."],"C")
q3=Question("İkizler paradoksu hangi bilim insanının düşünce deneyidir.",["A:Einstein.","B:Heisenberg","C:Schrodinger.","D:Newton."],"A")
q4=Question("Paralel evrenler teorisi kuantum fiziğine hangi yaklaşımdır.",["A:Severet Yorumu.","B:Deveret Yorumu","C:Genelev Yorumu.","D:Everet Yorumu."],"D")

questions=[q1,q2,q3]

quiz=Quiz(questions)
quiz.loadQuestion()

