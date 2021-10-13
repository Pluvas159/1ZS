import turtle, math


turtle.speed(0)

def arc(t, r, angle = 45, left = True):
    #makes a curved line from a part of the circle
    #turtle needs to be headed to the direction wanted
    
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 10) 
    step_length = arc_length / n
    step_angle = float(angle) / n

    polyline(t, n, step_length, step_angle, left)

def polyline(t, n, length, angle, left):
    for i in range(n):
        t.fd(length)
        t.lt(angle) if left else t.rt(angle)

def turtle_moveto(t, pos):
    t.penup()
    t.goto(pos)
    t.pendown()




class Kvietok:
    def __init__(self, **kwargs):
        #get props for leaves
        self.initial_angle = kwargs['initial_angle']
        self.leaf_length = kwargs['leaf_length']
        self.leaf_angle = kwargs['leaf_angle']
        
        #props for stem
        self.stem_length = kwargs['stem_length']
        self.stem_angle = kwargs['stem_angle']

        #props for kvet
        self.kvet_n = kwargs['kvet_n']
        self.kvet_length = kwargs['kvet_length']
        self.kvet_angle = kwargs['kvet_angle']


    def leaf(self, length, angle):
        start_heading = turtle.heading()

        #first turn to make the leaf in the heading
        turtle.right(angle/2)

        #two arcs for a leaf
        for i in range(2):
            arc(turtle, length, angle)
            #left turn for next arc
            turtle.left(180 - angle)
        
        #set to previous heading
        turtle.setheading(start_heading)


    def leaves(self):
        #draws two leaves with intial_angle from ground

        turtle.left(self.initial_angle)
        self.leaf(self.leaf_length, self.leaf_angle)
        turtle.left(180-self.initial_angle*2)
        self.leaf(self.leaf_length, self.leaf_angle)


    def stonka(self):
        #set the heading to 90, because stem is upright
        turtle.setheading(90)

        turtle.left(self.stem_angle/2)
        #make the curve
        arc(turtle, self.stem_length, self.stem_angle, left = False)
        turtle.setheading(90)


    def kvet(self):
        for i in range(self.kvet_n):
            self.leaf(self.kvet_length, self.kvet_angle)
            turtle.right(360 / self.kvet_n)


    def draw(self):
        #draws the kvietok and returns to starting position&heading
        start_pos = turtle.position()
        start_heading = turtle.heading()

        #call drawing functions
        self.leaves()
        self.stonka()
        self.kvet()

        #return to starting position, penup to avoid drawing
        turtle_moveto(turtle, start_pos)
        turtle.setheading(start_heading)

            



kvietky = []
kvietky.append(Kvietok(initial_angle = 25, leaf_length = 150, leaf_angle = 30, 
                stem_length = 150, stem_angle = 90,
                kvet_n = 6, kvet_length = 100, kvet_angle = 50))

kvietky.append(Kvietok(initial_angle = 70, leaf_length = 250, leaf_angle = 30, 
                stem_length = 650, stem_angle = 30,
                kvet_n = 10, kvet_length = 65, kvet_angle = 70))

kvietky.append(Kvietok(initial_angle = 45, leaf_length = 150, leaf_angle = 70, 
                stem_length = 300, stem_angle = 40,
                kvet_n = 20, kvet_length = 200, kvet_angle = 20))

turtle_moveto(turtle, (-300, -100))
kvietky[0].draw()

turtle_moveto(turtle, (0, -250))
kvietky[1].draw()

turtle_moveto(turtle, (300, -100))
kvietky[2].draw()


turtle.done()



