import random
import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()

hd = turtle.textinput("","가위, 바위, 보 중에 하나를 입력하세요:")

rsp = random.choice(["가위","바위","보"])

screen = turtle.Screen()
imager = "rock.gif"
images = "scissors.gif"
imagep = "paper.gif"
screen.addshape(imager)
screen.addshape(images)
screen.addshape(imagep)

t1.penup()
t2.penup()

if rsp == "가위":
    t1.goto(200,0)
    t1.shape(images)
    t1.stamp()
    t1.write("컴퓨터의 선택")
    if hd == "가위":
        t2.goto(-200,0)
        t2.shape(images)
        t2.stamp()
        t2.write("당신의 선택")
        t2.hideturtle()
        t2.goto(0,200)
        t2.write("비겼습니다",font=("Arial",40,"normal"))
    elif hd == "바위":
        t2.goto(-200,0)
        t2.shape(imager)
        t2.stamp()
        t2.write("당신의 선택")
        t2.hideturtle()
        t2.goto(0,200)
        t2.write("당신이 이겼습니다",font=("Arial",40,"normal"))
    elif hd == "보":
        t2.goto(-200,0)
        t2.shape(imagep)
        t2.stamp()
        t2.write("당신의 선택")
        t2.hideturtle()
        t2.goto(0,200)
        t2.write("당신이 졌습니다",font=("Arial",40,"normal"))
    else:
        t1.write("잘못 입력하셨습니다")
elif rsp == "바위":
    t1.goto(200,0)
    t1.shape(imager)
    t1.stamp()
    t1.write("컴퓨터의 선택")
    if hd == "가위":
        t2.goto(-200,0)
        t2.shape(images)
        t2.stamp()
        t2.write("당신의 선택")
        t2.hideturtle()
        t2.goto(0,200)
        t2.write("당신이 졌습니다",font=("Arial",40,"normal"))
    elif hd == "바위":
        t2.goto(-200,0)
        t2.shape(imager)
        t2.stamp()
        t2.write("당신의 선택")
        t2.hideturtle()
        t2.goto(0,200)
        t2.write("비겼습니다",font=("Arial",40,"normal"))
    elif hd == "보":
        t2.goto(-200,0)
        t2.shape(imagep)
        t2.stamp()
        t2.write("당신의 선택")
        t2.hideturtle()
        t2.goto(0,200)
        t2.write("당신이 이겼습니다",font=("Arial",40,"normal"))
    else:
        t1.write("잘못 입력하셨습니다")
elif rsp == "보":
    t1.goto(200,0)
    t1.shape(imagep)
    t1.stamp()
    t1.write("컴퓨터의 선택")
    if hd == "가위":
        t2.goto(-200,0)
        t2.shape(images)
        t2.stamp()
        t2.write("당신의 선택")
        t2.hideturtle()
        t2.goto(0,200)
        t2.write("당신이 이겼습니다",font=("Arial",40,"normal"))
    elif hd == "바위":
        t2.goto(-200,0)
        t2.shape(imager)
        t2.stamp()
        t2.write("당신의 선택")
        t2.hideturtle()
        t2.goto(0,200)
        t2.write("당신이 졌습니다",font=("Arial",40,"normal"))
    elif hd == "보":
        t2.goto(-200,0)
        t2.shape(imagep)
        t2.stamp()
        t2.write("당신의 선택")
        t2.hideturtle()
        t2.goto(0,200)
        t2.write("비겼습니다",font=("Arial",40,"normal"))
    else:
        t1.write("잘못 입력하셨습니다")
else:
    t1.write("잘못 입력하셨습니다")
