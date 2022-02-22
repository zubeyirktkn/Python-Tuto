import random
#soru havuzunu artır ve soruyu havuzdan random seçip seçileni tekrar sorma
#şık sistemi yaparak cevapları şıklara göre değerlendir hepsini baştan yaz
#Question
class Question:
    def __init__(self,text,choices,answer):
        self.text=text 
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):#uppercase yapılan cevabı kıyasla
        return self.answer == answer
#-----------------------------------------
#Quiz
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.tempQuestions=questions#temp üzerinden random alındıkça eksiltme yapılacak
        self.score = 0
        #self.randQuestion = random.randint(0,len(questions)-1)#random index aldım ancak random alınan indexi ayrıyeten tutup question listesinden eksiltmek gerekebilir veya question listesini kopyalayıp temp bi listeden yapılabilir main listeyle oynamamak için
    
    #----------------------------------------------------------
    def getQuestion(self):
        self.randQuestion = random.randint(0,len(self.tempQuestions)-1)
        return self.randQuestion
    #-------------------------------------------------------------
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Question {self.questionIndex+1}:{question.text}")
    
        for q in question.choices:
            print("-"+ q)
        
        answer=input("Answer:")#burada answeri upper yapıp vereceğiz
        answer=answer.upper()#upper yapmayı denedim
        self.guess(answer)
        self.loadQuestion()
    #----------------------------------------------------------------
    def guess(self,answer):
        question = self.getQuestion()
        
        if question.checkAnswer(answer):
            quiz.score+=1
        self.questionIndex+=1#bu kısıma gerek kalmadı çünkü indexi random alacağız
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

