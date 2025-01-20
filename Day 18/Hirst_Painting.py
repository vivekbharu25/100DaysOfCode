import colorgram
import turtle as t
import random

# colors = colorgram.extract('200430102527-01-damien-hirst-severed-spots.jpg',30
#                            )
# color_combo = []
#
# for i in range(30):
#     color = colors[i]
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     t = (r,g,b)
#     color_combo.append(t)
#
# print(color_combo)

color_list =  [(199, 12, 32), (249, 236, 25), (40, 77, 187), (239, 229, 4), (38, 217, 69), (227, 160, 50), (29, 40, 156), (213, 75, 14), (17, 153, 17), (242, 35, 160), (196, 16, 11), (68, 10, 31), (223, 21, 120), (61, 15, 8), (223, 141, 207), (11, 97, 62), (221, 159, 9), (53, 210, 230), (19, 21, 48), (75, 72, 218), (238, 156, 218), (10, 228, 239), (75, 211, 167), (89, 234, 199), (224, 84, 45), (59, 233, 242)]

jim = t.Turtle()
t.colormode(255)


for i in range(1,11):
    for j in range (1,11):
        jim.color(random.choice(color_list))
        jim.dot(5)
        jim.penup()
        jim.forward(20)
        jim.pendown()
    jim.teleport(0,i*20)


screen = t.Screen()
screen.exitonclick()
