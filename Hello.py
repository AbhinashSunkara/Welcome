import turtle
import time

#check background image

s=turtle.Screen()
s.bgcolor("white")
s.bgpic("ex.gif")
s.title("Maize Stealer")
s.tracer(0)
s.setup(width=700,height=700)


score=turtle.Turtle()
score.penup()
score.speed(50)
score.color("black")
score.pensize(0)
score.goto(0,-150)
hs=0
life=0
while(True):
    for i in range(1,7):
        s.bgpic("ex.gif")

        score.clear()
        if(i==1):
            score.write("Hey there..!",align="center",font=("Courie",16,"italic"))
        elif(i==2):
            score.write("Happy to interact with you  ",align="center",font=("Courie",16,"italic"))
        elif(i==3):
            score.write("I am glad that you are interested ",align="center",font=("Courie",16,"italic"))
        elif(i==4):
            score.write("You will find some interesting programs here ", align="center",font=("Courie",16,"italic"))
        elif(i==5):
            score.write("And Finally I want to say one thing.....Welcome to the Family buddyyy",align="center",font=("Courie",16,"italic"))
        elif(i==6):
            s.bgpic("join.gif")
            score.write("Never mind those words and Go Ahead..",align="center",font=("Courie",16,"italic"))
        time.sleep(3.097)
        
score.hideturtle()
score.penup()
