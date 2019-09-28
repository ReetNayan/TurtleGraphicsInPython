import turtle as t
import random

# this sets the number of pixels to print along x-axis
length = int(input("Enter length of image:"))
# this sets the number of pixels to print aling y-axis
breadth = int(input("Enter breadth of image:"))
pixelLength = int(input("Set pixel length to:"))  # this sets length of a pixel
# smaller pixel length can create large image in small space

# this sets the singleton's moving speed
speed = int(input("Enter the printing speed:"))
t.speed(speed)
t.bgcolor("black")  # the background colour
color = ["red", "black", "white", "green", "blue", "violet", "yellow"]
# above is a list of colours which is randomly filled in the pixel frame created

c = pixelLength*length
# the above variable takes the total length of the line on x-axis


def printer():  # this function creates one pixel
    # sets a random color for pen and for filling in pixel frame
    paint = color[random.randint(0, 6)]
    t.colormode(255)
    t.pencolor(paint)
    # fillcolor will fill the color with color name in variable 'paint'
    t.fillcolor(paint)
    t.begin_fill()  # below is creation of a pixel frame and filling of color
    t.fd(pixelLength)
    t.rt(90)
    t.fd(pixelLength)
    t.rt(90)
    t.fd(pixelLength)
    t.lt(180)
    t.end_fill()


numOfpixels = 0  # this variable will tell how many pixels have been generated in a line

t.penup()
t.setpos(-500, 250)  # sets the position of singleton for better view
t.pendown()

for i in range(1, (length*breadth)+1):
    if i == 1:
        t.lt(90)  # because singleton is facing +ve x-axis by default
    printer()  # create one pixel
    numOfpixels += 1  # add 1 when 1 pixel is created
    if i >= 50 and i <= 57:
        t.speed(2)
    else:
        t.speed(speed)
    if numOfpixels == length:  # if num of created pixels equals length assgined
        t.penup()  # lift the pen up
        t.lt(90)
        t.fd(c)  # move back to the initial(default) position after tutning
        t.lt(90)
        t.fd(pixelLength)  # move back by pixel length
        # turn 180 degrees(just oppsite as it is currently 180 degree in wrong dirn)
        t.rt(180)
        t.pendown()  # move the pen down
        numOfpixels = 0  # and reset the pixel generated in a line
# if the pixels are created length*breadth times,
# the image will be generated
print("Bye!")
