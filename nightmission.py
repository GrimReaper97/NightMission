def newball():
	mass = 1
	radius = 10
	inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
	ballbody = pymunk.Body(mass, inertia)
	ballform = pymunk.Circle(ballbody, radius, (0,0))
	ballform.elasticity = 0.7
	ballform.color = pygame.color.THECOLORS["white"]
	ballbody.position = 890, 300
	global ballbody
	global ballform
	space.add(ballbody, ballform)
	ball.append(ballform)
	

def speed(springs):
	if springs == 584:
		power = 700
	elif springs == 614:
		power = 500
	elif springs == 644:
		power = 400
	elif springs == 674:
		power = 320
	elif springs == 704:
		power = 200
	return (power)

import random,pygame,sys
from pygame.locals import *
from pygame.color import *
import pymunk
from pymunk import Vec2d
import pymunk.pygame_util

pygame.init()
window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Night Mission")
time1 = pygame.time.Clock()

### Physics stuff
space = pymunk.Space()
space.gravity = (0.0, -200.0)
OptionsDraw = pymunk.pygame_util.DrawOptions(window)

staticwalls = [pymunk.Segment(space.static_body, (875, 136), (905, 136), 1.0)
				,pymunk.Segment(space.static_body, (873, 136), (873, 560), 1.0)
				,pymunk.Segment(space.static_body, (906, 136), (906, 610), 2)
				,pymunk.Segment(space.static_body, (889,653), (905,610), 2)
				,pymunk.Segment(space.static_body, (878,665), (888,653), 2)
				,pymunk.Segment(space.static_body, (855,680), (878,665), 2)
				,pymunk.Segment(space.static_body, (840,690), (855,680), 2)
				,pymunk.Segment(space.static_body, (818,700), (840,690), 2)
				,pymunk.Segment(space.static_body, (780,710), (818,700), 2)
				,pymunk.Segment(space.static_body, (765,711), (780,710), 2)
				,pymunk.Segment(space.static_body, (578,711), (765,711), 1)
				,pymunk.Segment(space.static_body, (510,691), (578,711), 2)
				,pymunk.Segment(space.static_body, (376,691), (510,691), 2)
				,pymunk.Segment(space.static_body, (342,667), (376,691), 2)
				,pymunk.Segment(space.static_body, (342,457), (342,667), 2)
				,pymunk.Segment(space.static_body, (407,351), (342,457), 2)
				,pymunk.Segment(space.static_body, (333,318), (407,352), 2)
				,pymunk.Segment(space.static_body, (333,12), (333,318), 2)
				
#~ ***************************** BARRETTE "N I G H T" *********************
				,pymunk.Segment(space.static_body, (606.5,554), (606.5,609), 3)
				,pymunk.Segment(space.static_body, (647,558), (647,621), 3)
				,pymunk.Segment(space.static_body, (686,564), (686,630), 3)
				,pymunk.Segment(space.static_body, (723,564), (723,631), 3)
				,pymunk.Segment(space.static_body, (763,557), (763,619), 3)
				,pymunk.Segment(space.static_body, (803,554), (803,609), 3)
				
#~ ************************** LATO "D R O P" **********************************
				,pymunk.Segment(space.static_body, (376.8,86), (376.8,165), 1)
				,pymunk.Segment(space.static_body, (359,164), (359,257), 1)
				,pymunk.Segment(space.static_body, (382,165), (359,165), 1)
				,pymunk.Segment(space.static_body, (375,165), (359,178), 1)
				,pymunk.Segment(space.static_body, (483,86), (376.8,86), 1)
				,pymunk.Segment(space.static_body, (409,125), (382,166), 1)
				,pymunk.Segment(space.static_body, (484,91), (409,125), 1)
				,pymunk.Segment(space.static_body, (385,219), (385,257), 1)
				,pymunk.Segment(space.static_body, (411,219), (411,257), 1)
				
#~ *************************** LATO MOLLA BONUS ****************************
				,pymunk.Segment(space.static_body, (815,130), (724,91), 1)
				,pymunk.Segment(space.static_body, (831,86), (728,86), 1)
				,pymunk.Segment(space.static_body, (831,86), (831,12), 1)
				,pymunk.Segment(space.static_body, (816,130), (816,199), 1)
				,pymunk.Segment(space.static_body, (825,135), (825,199), 1)
				,pymunk.Segment(space.static_body, (816,199), (825,199), 1)
				,pymunk.Segment(space.static_body, (875,136), (825,136), 1)
				,pymunk.Segment(space.static_body, (868, 484), (868, 560), 1.0)
				,pymunk.Segment(space.static_body, (868, 484), (806, 405), 1.0)
				,pymunk.Segment(space.static_body, (860, 362), (806, 405), 1.0)
				,pymunk.Segment(space.static_body, (860, 360), (840, 340), 1.0)
				,pymunk.Segment(space.static_body, (870, 258), (840, 340), 1.0)
				,pymunk.Segment(space.static_body, (825, 278), (813, 318), 1.0)
				,pymunk.Segment(space.static_body, (825, 230), (825, 278), 1.0)
				,pymunk.Segment(space.static_body, (825, 230), (793, 290), 1.0)
				,pymunk.Segment(space.static_body, (812, 320), (793, 290), 1.0)
				
				#~ ************ BUMPER SINISTRO ***********
				,pymunk.Segment(space.static_body, (484,117), (436,142), 1)
				,pymunk.Segment(space.static_body, (436,257), (436,142), 1)
				,pymunk.Segment(space.static_body, (484,117), (497,124), 1)
]


for wall in staticwalls:
	wall.elasticity = 0.7
	wall.group = 1
	wall.color = pygame.color.THECOLORS["red"]
space.add(staticwalls)



##bumpers
for p in [(790,500), (650,320),(700,450)]:
    body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    body.position = p
    shape = pymunk.Circle(body, 14)
    shape.elasticity = 2
    shape.color = pygame.color.THECOLORS["white"]
    space.add(shape)
    
for q in [(630,500),(550,350)]:
    body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    body.position = q
    shape = pymunk.Circle(body, 9)
    shape.elasticity = 2
    shape.color = pygame.color.THECOLORS["white"]
    space.add(shape)


##Flipper
rbar = [(20,-15), (-85, 0), (15,10)]
lbar = [(-20,-15), (85, 0), (-4,10)]
mass = 100
mo = pymunk.moment_for_poly(mass, rbar)

# right flipper
r_bar_body = pymunk.Body(mass, mo)
r_bar_body.position = 710, 78
r_bar_form = pymunk.Poly(r_bar_body, rbar)
r_bar_form.color = pygame.color.THECOLORS["white"]
space.add(r_bar_body, r_bar_form)

r_bar_union_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
r_bar_union_body.position = r_bar_body.position 
a = pymunk.PinJoint(r_bar_body, r_bar_union_body, (0,0), (0,0))
#todo: tweak values of spring better
l = pymunk.DampedRotarySpring(r_bar_body, r_bar_union_body, 0.15, 20000000,900000)
space.add(a, l)

# left flipper
l_bar_body = pymunk.Body(mass, mo)
l_bar_body.position = 490, 78
l_bar_form = pymunk.Poly(l_bar_body, lbar)
l_bar_form.color = pygame.color.THECOLORS["white"]
space.add(l_bar_body, l_bar_form)

l_bar_union_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
l_bar_union_body.position = l_bar_body.position 
a = pymunk.PinJoint(l_bar_body, l_bar_union_body, (0,0), (0,0))
l = pymunk.DampedRotarySpring(l_bar_body, l_bar_union_body, -0.15, 20000000, 900000)
space.add(a, l)

#Font
font = pygame.font.Font('FONT/ARCADECLASSIC.TTF',60)
fontsmall = pygame.font.Font('FONT/ARCADECLASSIC.TTF',30)


#Game
MOVEEVENT,t = pygame.USEREVENT+1,2000
pygame.time.set_timer(MOVEEVENT, t)
ball = []
start = True
while 1:
	while start:		
		#Menu start
		window.fill(THECOLORS["black"])
		namegame = font.render(("Night Mission"),True,THECOLORS["white"])
		quitgame = fontsmall.render(("Press q for quit the game"),True,THECOLORS["white"])
		startgame = fontsmall.render(("Press a for start the game"),True,THECOLORS["white"])
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN and event.key == K_q: #Quit
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN and event.key == K_a: #Restart
				#Create the ball
				newball()
				
				#Power of spring
				springs = 584
				
				running = True
				pause = True
				start = False
		window.blit(namegame,(473,70))
		window.blit(quitgame,(490,230))
		window.blit(startgame,(485,280))
		pygame.display.update()
	while running:
		sfondo = pygame.image.load("suca.jpg")
		window.blit(sfondo,(0,0))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN:
				x,y = event.pos
				print(x,y)
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				pause = True
				running = False
			elif event.type == KEYDOWN and event.key == K_RIGHT:
				r_bar_body.apply_impulse_at_local_point(Vec2d.unit() * 15000, (-100, 0))
			elif event.type == KEYDOWN and event.key == K_LEFT:
				l_bar_body.apply_impulse_at_local_point(Vec2d.unit() * -15000, (-100, 0))
			elif event.type == KEYDOWN and event.key == K_DOWN:
				if springs != 704:
					springs += 30
			elif event.type == KEYDOWN and event.key == K_UP:
				if springs != 584:
					springs -= 30
			elif event.type == KEYDOWN and event.key == K_SPACE: #and 146 <= ballbody.position[1] <= 147 and ballbody.position[0] == 890.0:
				power = speed(springs)
				ballbody.apply_impulse_at_local_point((Vec2d((0,power))))		

		### Springs
		pygame.draw.line(window, pygame.color.THECOLORS["white"], (890,707), (890,springs), 30)
		
		## Animazione molla bonus
		if 825 <= ballbody.position[0] <= 875 and ballbody.position[1] < 154:
			space.remove(ballbody, ballform)
			ball.remove(ballform)
			
			mass = 1
			radius = 10
			inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
			ballbody = pymunk.Body(mass, inertia, body_type=pymunk.Body.STATIC)

			ballform = pymunk.Circle(ballbody, radius, (0,0))
			ballform.elasticity = 0.7
			ballform.color = pygame.color.THECOLORS["white"]
			ballbody.position = 852, 154
			space.add(ballbody, ballform)
			ball.append(ballform)
			space.debug_draw(OptionsDraw)
			pygame.display.update()
			go = True
			while go:
				for event in pygame.event.get():
					if event.type == MOVEEVENT:
						space.remove(ballbody, ballform)
						ball.remove(ballform)
						
						mass = 1
						radius = 10
						inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
						ballbody = pymunk.Body(mass, inertia,body_type=pymunk.Body.DYNAMIC)

						ballform = pymunk.Circle(ballbody, radius, (0,0))
						ballform.elasticity = 0.7
						ballform.color = pygame.color.THECOLORS["white"]
						ballbody.position = 852, 154
						space.add(ballbody, ballform)
						ball.append(ballform)
						
						
						ballbody.apply_impulse_at_local_point((Vec2d((0,700))))
						go = False
		### Draw stuff
		space.debug_draw(OptionsDraw)

		r_bar_body.position = 710, 78
		l_bar_body.position = 490, 78
		r_bar_body.velocity = l_bar_body.velocity = 0,0
		
		#Respawn balls
		if ballbody.position[1] <= 12 and 333 <= ballbody.position[0] <= 830:
			space.remove(ballbody, ballform)
			ball.remove(ballform)
			
			#Create new ball
			newball()

		### Update physics
		dt = 2/60.0/5.5
		for x in range(9):
			space.step(dt)

		### Flip screen
		pygame.display.update()
		time1.tick(60)
	while pause:
		window.fill(THECOLORS["black"])
		font = pygame.font.Font('FONT/ARCADECLASSIC.TTF',60)
		fontsmall = pygame.font.Font('FONT/ARCADECLASSIC.TTF',30)
		written = font.render(("Pause"),True,THECOLORS["white"])
		writtensmall = fontsmall.render(("Press q for quit the game"),True,THECOLORS["white"])
		resume = fontsmall.render(("Press esc for resume the game"),True,THECOLORS["white"])
		restart = fontsmall.render(("Press r for restart the game"),True,THECOLORS["white"])
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN and event.key == K_q: #Quit
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN and event.key == K_r: #Restart
				space.remove(ballbody, ballform)
				ball.remove(ballform)
				running = False
				pause = False
				start = True
			elif event.type == KEYDOWN and event.key == K_ESCAPE: #Resume
				running = True
				pause = False
		window.blit(written,(580,70))
		window.blit(writtensmall,(480,230))
		window.blit(resume,(450,280))
		window.blit(restart,(460,330))
		pygame.display.update()
