import turtle as t
import random
import time

d = 0.1 # delay
s = 0 # score
hs = 0 # high score

# screen
sc = t.Screen()
sc.title("Snake Game")
sc.bgcolor("blue")
sc.setup(width=600, height=600)
sc.tracer(0)

# snake head
h = t.Turtle()
h.shape("square")
h.color("white")
h.penup()
h.goto(0, 0)
h.direction = "Stop"

# food
f = t.Turtle()
f.speed(0)
f.shape(random.choice(['square', 'triangle', 'circle']))
f.color(random.choice(['red', 'green', 'black']))
f.penup()
f.goto(0, 100)

# score display
p = t.Turtle()
p.speed(0)
p.shape("square")
p.color("white")
p.penup()
p.hideturtle()
p.goto(0, 250)
p.write("Score : 0  High Score : 0", align="center", font=("candara", 24, "bold"))

# Direction functions
def up():
    if h.direction != "down":
        h.direction = "up"

def down():
    if h.direction != "up":
        h.direction = "down"

def left():
    if h.direction != "right":
        h.direction = "left"

def right():
    if h.direction != "left":
        h.direction = "right"

# Movement function
def move():
    if h.direction == "up":
        h.sety(h.ycor() + 20)
    if h.direction == "down":
        h.sety(h.ycor() - 20)
    if h.direction == "left":
        h.setx(h.xcor() - 20)
    if h.direction == "right":
        h.setx(h.xcor() + 20)

# Key bindings
sc.listen()
sc.onkeypress(up, "Up")
sc.onkeypress(down, "Down")
sc.onkeypress(left, "Left")
sc.onkeypress(right, "Right")

# Snake body segments
seg = []
# Main Gameplay
while True:
    sc.update()
    
    # Boundary check
    if h.xcor() > 290 or h.xcor() < -290 or h.ycor() > 290 or h.ycor() < -290:
        time.sleep(1)
        h.goto(0, 0)
        h.direction = "Stop"
        f.goto(random.randint(-270, 270), random.randint(-270, 270))
        for seg in seg:
            seg.goto(1000, 1000)
        seg.clear()
        s = 0
        d = 0.1
        p.clear()
        p.write(f"Score : {s} High Score : {hs}", align="center", font=("candara", 24, "bold"))
    
    # Food collision
    if h.distance(f) < 20:
        f.goto(random.randint(-270, 270), random.randint(-270, 270))

        # Adding segment
        n_seg = t.Turtle()
        n_seg.speed(0)
        n_seg.shape("square")
        n_seg.color("orange")
        n_seg.penup()
        seg.append(n_seg)
        d -= 0.001
        s += 10
        if s > hs:
            hs = s
        p.clear()
        p.write(f"Score : {s} High Score : {hs}", align="center", font=("candara", 24, "bold"))
    
    # Move segments
    for i in range(len(seg)-1, 0, -1):
        x, y = seg[i-1].xcor(), seg[i-1].ycor()
        seg[i].goto(x, y)
    
    if len(seg) > 0:
        x, y = h.xcor(), h.ycor()
        seg[0].goto(x, y)
    
    # Move head
    move()

    # Checking for self-collision
    for segment in seg:
        if segment.distance(h) < 20:
            time.sleep(1)
            h.goto(0, 0)
            h.direction = "Stop"
            f.goto(random.randint(-270, 270), random.randint(-270, 270))
            for seg in seg:
                seg.goto(1000, 1000)
            seg.clear()
            s = 0
            d = 0.1
            p.clear()
            p.write(f"Score : {s} High Score : {hs}", align="center", font=("candara", 24, "bold"))
    
    time.sleep(d)