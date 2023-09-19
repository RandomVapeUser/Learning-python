import sys #acabar com o jogo
import time #frases mais lentas

Game = print("Welcome to my game! Lets start with the basics")

count = 2

time.sleep(3)
Name = input("What is your name?:") #nome
time.sleep(2)
print("Welcome", Name, "I hope you enjoy my game!") 
time.sleep(3)
age = int(input("What is your age?:")) #idade
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


time.sleep(2)
print("10%")
time.sleep(2)
print("20%")
time.sleep(2)
print("30%")
time.sleep(2)
print("40%")
time.sleep(2)
print("50%")
time.sleep(2)
print("60%")
time.sleep(2)
print("70%")
time.sleep(2)
print("90%")
time.sleep(2)
print("100% done!")
time.sleep(2)
