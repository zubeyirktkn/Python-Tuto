import random

print("*"*20+"Welcome to Guessing Game!"+"*"*20)

number=random.randint(0,100)

#gereken değişkenler
point=100 #total puan tek seferde bilirse kazanır
chance=0 #kullanıcıdan girdi olarak alınacak

chance=int(input("How many chance do you need to guess the number:"))
wrong_guess=point//chance #wrong guess yanlış tahminde point-wrong_guess yapılır ve chance-1 

while chance>0:
    guess=int(input("Guess the number:"))

    if(guess==number):
        print(f"Congratulations!The number is {number}.Your point is {point}.")
        break
    else:
        chance-=1
        point-=wrong_guess
        if(chance==0):
            print(f"You lost!The number is {number}.")
            break
        if(guess<number):
            print(f"Wrong guess.The number is greater than your guess.You have {chance} more chance to guess.")
        elif(guess>number):
            print(f"Wrong guess.The number is smaller than your guess.You have {chance} more chance to guess.")
        

