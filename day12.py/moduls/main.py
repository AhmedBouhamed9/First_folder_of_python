from pyjokes import get_joke
from calcul import add
from calcul import multi
from art import text2art
# x=int(input("give me numbre :  "))
# y=int(input("give me numbre :  "))
# # result=add(x,y)
# result=multi(x,y)
# print(f"{x} x {y}= {result}")
# from greeting import greeting
# name=input("give me your name :  ")

# greeting(name)
joke=get_joke()
print(joke)
art=text2art("Ahmed")
print(art)