import sys #acabar com o jogo
import time #frases mais lentas

Game = print("Welcome to my game! Lets start with the basics")

count = 2

time.sleep(3)
Name = input("What is your name?:") #nome
time.sleep(2)
print("Welcome", Name, "I hope you enjoy my game!") 
time.sleep(3)
age = input("What is your age?:") #idade
time.sleep(3)
username = input("Please input your username:") #nome do jogo
time.sleep(3)
password = input("Now type the password:") #password? xd

if password == "1234":
  print("Welcome back!") #O jogo continua
  count += 1
else:
  print("Wrong password!") #Password incorreta
  count -= 1

if count == 1:
  sys.exit()
else:
  print("Just a minute, the game is loading.")



for i in range(1,100):
  time.sleep(0.3)
  print(i,"%")

"""
time.sleep(1)
print("20%")
time.sleep(1)
print("30%")
time.sleep(1)
print("40%")
time.sleep(1)
print("50%")
time.sleep(1)
print("60%")
time.sleep(1)
print("70%")
time.sleep(1)
print("80%")
time.sleep(1)
print("90%")
time.sleep(1)
print("100% done!")
"""

time.sleep(2)
print("So the game we will play is , guess the number!")
time.sleep(2)
print("I will choose a number and you will say wich number you think it is")
time.sleep(2)
print("I will help you by saying if its higher or lower, good luck!")
time.sleep(5)
print("You have 3 lives!")
print("Guess the number!")


while True:
    guess = int(input())
    
    if guess > 150:
        print("Lower")
    else:
        print("Higher!")

    if guess == 150:
        print("Congratulations, I hope you enjoyed my game! Bye now!")
        time.sleep(10)
        sys.exit()