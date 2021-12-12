import turtle
import math

#house walls

turtle.begin_fill()
turtle.color("black","brown")

house_height = 100
house_width = 130

for sides in range(2):
    turtle.forward(house_width)
    turtle.right(90)
    turtle.forward(house_height)
    turtle.right(90)

turtle.end_fill()

#house roof



turtle.color("dark red","red")
turtle.begin_fill()

roof_angle=120
roof_corner=(180-roof_angle)/2

roof_overhang=20
roof_base=house_width+(2*roof_overhang)
roof_slope=math.sqrt((roof_base**2)/2)


turtle.left(180)

turtle.forward(roof_overhang)
turtle.right(180-roof_corner)
turtle.forward(roof_slope)
turtle.right(180-roof_angle)
turtle.forward(roof_slope)
turtle.right(180-roof_corner)
turtle.forward(roof_base)

turtle.end_fill()