#Make a program in which the computer randomly
#chooses a number between 1 to 10, 1 to 100, or any range.
#Then give users a hint to guess the number. Every time the user guesses wrong, he gets another clue, and his score gets reduced.
#The clue can be multiples, divisible, greater or smaller, or a combination of all.

import random as r
import math
print(" **********     NUMBER GUESSING GAME  ************          ")
print(""" ********           HI WLECOME TO PYTHONVERSE!!!      ************
          ********   This is a number guessing game. ***********        """)

print("************ You have 7 chances to guess the number    **************")
print("************ If you cannot guess the number in 7 guesses then you will lose the game ***********")
print("************          Maximum score is 7    ***********")
print("**********  Please enter your bound for the game to start  *********     ")
print("***************************************************************************")

a=int(input("Enter lower bound of the range in which you want to play the game : "))
b=int(input("Enter upper bound of the range in which you want to play the game : "))
random_number = r.randint(a,b)
guess=int(input("Enter the guessed number between " + str(a) +" and "+str(b)+": "))
score=7
if(guess==random_number):
    print("*********   CONGRATULATIONS YOU HAVE WON   ***************")
    print("*********   It is a correct guess    ******************")
    print("*********   Your final score is "+str(score)+"   *******")
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
else:
    q= (a+b)//2
    if(random_number<q):
        if(math.isclose(random_number,guess,abs_tol=3)):
            print("You are very very very close to the number")
        print("The number is less than "+str(q))
        print("Your score becomes "+str(score-1))
        print("You have "+str(score-1)+" guesses left now ")
        print("**********************************************************")
    elif(random_number>q):
        if(math.isclose(random_number,guess,abs_tol=3)):
            print("You are very very very close to the number")
        print("The number is greater than "+str(q))
        print("Your score becomes "+str(score-1))
        print("You have "+str(score-1)+" guesses left now ")
        print("**********************************************************")
    score=score-1
    guess=int(input("Enter new guess: "))
    if(guess==random_number):
        print("*********   CONGRATULATIONS YOU HAVE WON   ***************")
        print("*********   It is a correct guess    ******************")
        print("*********   Your final score is "+str(score)+"   *******")
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    else:
        if(math.isclose(random_number,guess,abs_tol=3)):
            print("You are very very very close to the number")
            print("Your score becomes "+str(score-1))
            print("You have "+str(score-1)+" guesses left now ")
            print("**********************************************************")
        else:
            print("You are not even close to the number ")
            print("Your score becomes "+str(score-1))
            print("You have "+str(score-1)+" guesses left now ")
            print("**********************************************************")

        score=score-1
        guess=int(input("Enter new guess: "))
        if(guess==random_number):
            print("*********   CONGRATULATIONS YOU HAVE WON   ***************")
            print("*********   It is a correct guess    ******************")
            print("*********   Your final score is "+str(score)+"   *******")
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        else:
            if(random_number%2==0):
                print("It is an even number")
            else:
                print("It is an odd number")
            if(math.isclose(random_number,guess,abs_tol=3)):
                print("You are very very very close to the number")
            print("Your score becomes "+str(score-1))
            print("You have "+str(score-1)+" guesses left now ")
            print("**********************************************************")
            score=score-1
            guess=int(input("Enter new guess"))
            if(guess==random_number):
                print("*********   CONGRATULATIONS YOU HAVE WON   ***************")
                print("*********   It is a correct guess    ******************")
                print("*********   Your final score is "+str(score)+"   *******")
                print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            else:
                for i in range(2,random_number+1):
                    if random_number%i==0:
                        div=i
                        break
                if(math.isclose(random_number,guess,abs_tol=3)):
                    print("You are very very very close to the number")
                print("The number is divisible by "+str(div))

                print("Your score becomes "+str(score-1))
                print("You have "+str(score-1)+" guesses left now ")
                print("**********************************************************")
                score=score-1
                guess=int(input("Enter new guess: "))
                if(guess==random_number):
                    print("*********   CONGRATULATIONS YOU HAVE WON   ***************")
                    print("*********   It is a correct guess    ******************")
                    print("*********   Your final score is "+str(score)+"   *******")
                    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                else:
                    count=0
                    for j in range(2,random_number):
                        if random_number%j==0:
                            count+=1
                    if count>=1:
                        print("It is  a Composite Number")
                    else:
                        print("It is a Prime Number")
                    
                    if(math.isclose(random_number,guess,abs_tol=3)):
                        print("You are very very very close to the number")

                    print("Your score becomes "+str(score-1))
                    print("You have "+str(score-1)+" guesses left now ")
                    print("**********************************************************")
                    score=score-1

                    guess=int(input("Enter new guess : "))
                    if(guess==random_number):
                        print("*********   CONGRATULATIONS YOU HAVE WON   ***************")
                        print("*********   It is a correct guess    ******************")
                        print("*********   Your final score is "+str(score)+"   *******")
                        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                    else:
                        for k in range(2,random_number+1):
                            if(random_number%k==0):
                                print("The number is a multiple of "+str(k))
                                break
                        if(math.isclose(random_number,guess,abs_tol=3)):
                            print("You are very very very close to the number")
                        print("Your score becomes "+str(score-1))
                        print("You have "+str(score-1)+" guesses left now ")
                        print("**********************************************************")
                        score=score-1
                        print("It is your last chance to guess the number otherwise you will lose the game")
                        guess=int(input("Enter new guess: "))
                        if(guess==random_number):
                            print("*********   CONGRATULATIONS YOU HAVE WON   ***************")
                            print("*********   It is a correct guess    ******************")
                            print("*********   Your final score is "+str(score)+"   *******")
                            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                        else:
                            print("***********   SORRY YOU LOST THE GAME ***********************")
                            score=score-1
                            print("***********   The number was : "+str(random_number)+"**********")
                            print("***********  Your final score is "+str(score)+"***********")
                            print("**********************************************************")