# Section 1 - Helper functions
import turtle, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite = turtle.Turtle()
	sprite.shape(image_file)
	sprite.penup()
	sprite.goto(x,y)
	return sprite


# Section 2 - Variables
x1 = -100
y1 = 100
x2 = -100
y2 = 50
x3 = -100
y3 = 0
x4 = -100
y4 = -50
# Section 3 - Setup
set_background("summer")
t1 = create_sprite("basketball",x1,y1)
t2 = create_sprite("flower",x2,y2)
t3 = create_sprite("kitten",x3,y3)
t4 = create_sprite("sodacan",x4,y4)


# # Section 4 - Racing
# # x3, is the fastest and will always win because it always goes to 10, x1 is the second fastest and x2 is third and x4 is the slowest
for i in range(30):
	x1 += 8
	x2 += 6
	x3 +=10
	x4 +=5
	t1.goto(x1, y1)
	t2.goto(x2, y2)
	t3.goto(x3, y3)
	t4.goto(x4, y4)
	time.sleep(0.1)


# # Section 5 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
	print("basketball wins!")
elif x2>=x3 and x2>=x4:
	print("flower wins!")
elif x3>=x4:
	print("cat wins!")
else:
	print("sodacan wins!")


turtle.exitonclick()