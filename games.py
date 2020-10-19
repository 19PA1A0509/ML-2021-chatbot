import random
from datetime import datetime
import calendar
def welcome():
    intro=["Hello my name is mimi. Are you bored? I think I can cure your boredom...wanna try??","Hey you wanna play with me? by the way I am cricki :) so..are you ready?"]
    print(random.choice(intro))
    name=input("May i know your name please:")
    current_time=datetime.now().hour
    if current_time<12:
        print("Heyy! goodmorning..",name)
        print("now shall we play the game?")
    elif current_time>=12 and current_time<16:
        print("Hello...goodafternoon",name)
        print("so..a game after lunch? Ok let's start")
    elif current_time>=16 and current_time<21:
        print("Haha good evening",name)
        print("So shall we play an evening game?")
    else:
        print("Woo...",name,"wanna refresh after a tired day? Let's play :)")

    print("As I've already said my name is mimi and I can help you cure your boredom")
    print("I can do the following things for you")
    print("1.I can say how many days old are you..it's fun right?")
    print("2.You know your birthday date..but do you know the day")
    print("I can do that for you")
    print("And if you really want to play some intresting game,you can play")
    print("3.Hand cricket")
    print("4.If you think I've cured your boredom..you may quit this chat")
def games():
    try:
        return int(input("So..what do you want to do CHOOSE FROM 1 - 4 : "))
    except:
        print("I'm a small bot and i don't have somany options so CHOOSE FROM 1,2,3 AND 4 ")
def day():
    import datetime
    print("hello there..could you please enter ur input as per instructuons (yyyy,mm,dd")
    year=int(input("enter your year : "))
    month = int(input("enter your month : "))
    day=int(input("enter your day : "))
    bday=datetime.date(year,month,day)
    td=datetime.date.today()
    td1= td - bday
    print(td1)
def finddays():
    import datetime
    import calendar 
    print("hello there..could you please enter ur input as per instructuons (yyyy,mm,dd")
    year=int(input("enter your year.."))
    month= int(input("enter your month.."))
    day=int(input("enter your day.."))
    date=datetime.date(year,month,day)
    print("YOU ARE BORN ON",date.strftime("%A"))
def handcricket():
    print("Okay first I'm gonna say the rules(Incase you don't know.. ")
    print("As we all know handcricket... it is played by 2 members")
    print("Here your opponent is cricki..and that's me")
    print("And you have to choose between 1(batting) and 2(bowling)")
    print("you will be given 10 chances and you have to chose from 1 to 6(runs)")
    print("And it's an out if we both got the same")
    print("who has the highest score at the last will be the winner")
    print("so..shall we start the game?? choose from 1 or 2")
    your_choice=int(input())
    if your_choice == 1:
        print("okay you chose to bat!!!")
        your_score=0
        my_score=0
        count=0
        while (count<10):
            count+=1
            bat=int(input("your score for this ball:"))
            if bat>0 and bat<7:
                bowl=random.randint(1,6)
                if bat!=bowl:
                    your_score+=bat
                    my_score+=bowl
                else:
                    print("you are out!!! as our scores coincided")
                    return 0
            else:
                print("you can get a score only between 1 and 6")
        print("your score is :",your_score)
        print("my score is:",my_score)
        if your_score>my_score:
            print("congrats!! you won.....the next time I'll win upon you for sure")
        elif your_score<my_score:
            print("Haha I won..don't feel bad..try in the next one")
        else:
            print("We're equal..wanna play another one??If you want we can start again:)")
    elif your_choice == 2:
        print("okay you chose to bowl!!!")
        your_score1=0
        my_score=0
        count=0
        while (count<10):
            count+=1
            bowl=int(input("your score for this ball:"))
            if bowl>0 and bowl<7:
                bat=random.randint(1,6)
                if bat!=bowl:
                    your_score1+=bowl
                    my_score+=bat
                else:
                    print("I am out!! and I lost the game >_< as our scores coincided")
                    return 0
            else:
                print("you can get a score only between 1 and 6")
        print("your score is :",your_score1)
        print("my score is:",my_score)
        if your_score1>my_score:
            print("congrats!! you won.....the next time I'll win upon you for sure")
        elif your_score1<my_score:
            print("Haha I won..don't feel bad..try in the next one")
        else:
            print("We're equal..wanna play another one??If you want we can start again:)")
    else:
        print("you can choose only between batting and bowling: 1 or 2")
def mimi():
    welcome()
    choice=games()
    while choice!=4:
        if choice==1:
            day()
        elif choice==2:
            finddays()
        elif choice==3:
            handcricket()
        else:
            print("Sorry..I have only 1 to 4 options. So please choose from 1 to 4")
        choice=games()

mimi()