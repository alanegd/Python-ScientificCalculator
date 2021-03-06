import turtle

window = turtle.Screen()
window.title("Calculator")
window.bgcolor("gray")
window.setup(width=500, height=700)
window.tracer(0)

# Outputs
too_long = False
already_comma = False
number = ""
answer = ""

# Numbers_GUI
text = turtle.Turtle()
text.color("black")
text.penup()
text.hideturtle()
text.goto(0, 260)

one = turtle.Turtle()
one.color("black")
one.penup()
one.hideturtle()
one.goto(-180, 130)
one.write(1, align="center", font=("Courier", 24, "normal"))

two = one.clone()
two.goto(-60, 130)
two.write(2, align="center", font=("Courier", 24, "normal"))

three = one.clone()
three.goto(60, 130)
three.write(3, align="center", font=("Courier", 24, "normal"))

plus = one.clone()
plus.goto(178, 130)
plus.write("+", align="center", font=("Courier", 24, "normal"))

four = one.clone()
four.goto(-180, 30)
four.write(4, align="center", font=("Courier", 24, "normal"))

five = one.clone()
five.goto(-60, 30)
five.write(5, align="center", font=("Courier", 24, "normal"))

six = one.clone()
six.goto(60, 30)
six.write(6, align="center", font=("Courier", 24, "normal"))

minus = one.clone()
minus.goto(178, 30)
minus.write("-", align="center", font=("Courier", 24, "normal"))

seven = one.clone()
seven.goto(-180, -70)
seven.write(7, align="center", font=("Courier", 24, "normal"))

eight = one.clone()
eight.goto(-60, -70)
eight.write(8, align="center", font=("Courier", 24, "normal"))

nine = one.clone()
nine.goto(60, -70)
nine.write(9, align="center", font=("Courier", 24, "normal"))

times = one.clone()
times.goto(178, -70)
times.write("*", align="center", font=("Courier", 24, "normal"))

zero = one.clone()
zero.goto(-180, -170)
zero.write(0, align="center", font=("Courier", 24, "normal"))

decimal = one.clone()
decimal.goto(-60, -170)
decimal.write(".", align="center", font=("Courier", 24, "normal"))

enter = one.clone()
enter.color("blue")
enter.goto(60, -170)
enter.write("EXE", align="center", font=("Courier", 24, "normal"))

divided_by = one.clone()
divided_by.goto(178, -170)
divided_by.write("/", align="center", font=("Courier", 24, "normal"))

delete_all = one.clone()
delete_all.goto(0, -270)
delete_all.write("DELETE ALL", align="center", font=("Courier", 24, "normal"))

mid1 = turtle.Turtle()
mid1.shape("square")
mid1.color("black")
mid1.shapesize(stretch_wid=0.9, stretch_len=100)
mid1.penup()
mid1.goto(0, 100)

mid2 = mid1.clone()
mid2.goto(0, 0)

mid3 = mid1.clone()
mid3.goto(0, -100)

upbar1 = mid1.clone()
upbar1.goto(0, 340)

upbar = mid1.clone()
upbar.shapesize(stretch_wid=1.5, stretch_len=100)
upbar.goto(0, 216)

downbar = mid1.clone()
downbar.goto(0, -200)

downbar1 = mid1.clone()
downbar1.shapesize(stretch_wid=4.6, stretch_len=100)
downbar1.goto(0, -340)

ver1 = turtle.Turtle()
ver1.shape("square")
ver1.color("black")
ver1.shapesize(stretch_wid=20, stretch_len=0.9)
ver1.penup()
ver1.goto(0, 0)

ver2 = ver1.clone()
ver2.goto(120, 0)

ver3 = ver1.clone()
ver3.shapesize(stretch_wid=50, stretch_len=0.9)
ver3.goto(236, 0)

ver4 = ver1.clone()
ver4.goto(-120, 0)

ver5 = ver1.clone()
ver5.shapesize(stretch_wid=50, stretch_len=0.9)
ver5.goto(-239, 0)


# Click_events
def get_mouse_click_coor(x, y):
    global already_comma, number, answer, too_long
    try:
        # One
        if -130 >= x >= -230 and 110 <= y <= 193 and not too_long:
            number += "1"
            print(number)
            text.clear()
            text.write(number, align="center", font=("Courier", 24, "normal"))

        # Two
        if -11 >= x >= -111 and 110 <= y <= 193 and not too_long:
            number += "2"
            print(number)
            text.clear()
            text.write(number, align="center", font=("Courier", 24, "normal"))

        # Three
        if 10 <= x <= 110 <= y <= 193 and not too_long:
            number += "3"
            print(number)
            text.clear()
            text.write(number, align="center", font=("Courier", 24, "normal"))

        # Sum
        if 230 >= x >= 128 and 110 <= y <= 193 and not too_long:
            number += "+"
            already_comma = False
            print(number)
            text.clear()
            text.write(number, align="center", font=("Courier", 24, "normal"))

        # Four
        if -130 >= x >= -230 and 9 <= y <= 91 and not too_long:
            number += "4"
            print(number)
            text.clear()
            text.write(number, align="center", font=("Courier", 24, "normal"))

        # Five
        if -11 >= x >= -111 and 9 <= y <= 91 and not too_long:
            number += "5"
            print(number)
            text.clear()
            text.write(number, align="center", font=("Courier", 24, "normal"))

        # Six
        if 110 >= x >= 10 and 9 <= y <= 91 and not too_long:
            number += "6"
            print(number)
            text.clear()
            text.write(number, align="center", font=("Courier", 24, "normal"))

        # Subtraction
        if 230 >= x >= 128 and 9 <= y <= 91 and not too_long:
            number += "-"
            already_comma = False
            print(number)
            text.clear()
            text.write(number, align="center", font=("Courier", 24, "normal"))

        # Seven
        if -130 >= x >= -230 and -90 <= y <= -10 and not too_long:
            number += "7"
            print(number)
            text.clear()
            text.write(number, align="center", font=("Courier", 24, "normal"))

        # Eight
        if -11 >= x >= -111 and -90 <= y <= -10 and not too_long:
            number += "8"
            print(number)
            text.clear()
            text.write(number, align="center", font=("Courier", 24, "normal"))

        # Nine
        if 110 >= x >= 10 and -90 <= y <= -10 and not too_long:
            number += "9"
            print(number)
            text.clear()
            text.write(number, align="center", font=("Courier", 24, "normal"))

        # Multiplication
        if 230 >= x >= 128 and -90 <= y <= -10 and not too_long:
            number += "*"
            already_comma = False
            print(number)
            text.clear()
            text.write(number, align="center", font=("Courier", 24, "normal"))

        # Zero
        if -130 >= x >= -230 and -191 <= y <= -109 and not too_long:
            number += "0"
            print(number)
            text.clear()
            text.write(number, align="center", font=("Courier", 24, "normal"))

        # Decimal
        if -11 >= x >= -111 and -191 <= y <= -109 and not already_comma and not too_long:
            number += "."
            already_comma = True
            print(number)
            text.clear()
            text.write(number, align="center", font=("Courier", 24, "normal"))

        # Answer
        if 110 >= x >= 10 and -191 <= y <= -109:
            answer = str(eval(number))
            print(answer)
            text.clear()
            text.write(answer, align="center", font=("Courier", 24, "normal"))
            number = ""
            too_long = False

        # Division
        if 230 >= x >= 128 and -191 <= y <= -109 and not too_long:
            number += "/"
            already_comma = False
            print(number)
            text.clear()
            text.write(number, align="center", font=("Courier", 24, "normal"))

        # Restart
        if 230 >= x >= -230 and -290 <= y <= -209:
            already_comma = False
            too_long = False
            number = ""
            answer = ""
            print("Everything was deleted")
            text.clear()

        if len(number) >= 24:
            print("Error, too long")
            too_long = True
    except:
        print("Error")
        text.clear()
        text.write("Invalid, try again", align="center", font=("Courier", 24, "normal"))


turtle.onscreenclick(get_mouse_click_coor)

# Main loop
while True:
    window.update()
