def newball():
	mass = 1.5
	radius = 10.3
	moment = pm.moment_for_circle(mass, radius, 0.0, (0,0))
	ballbody = pm.Body(mass, moment)
	ballform = pm.Circle(ballbody, radius, (0,0))
	ballform.elasticity = 0.5
	ballform.color = THECOLORS["white"]
	space.add(ballbody, ballform)
	global ballbody
	global ballform
	return ballform

def newgate():
	gate = pymunk.Segment(space.static_body, (870,560), (900,612), 1)
	gate.elasticity = 2.5
	gate.color = pygame.color.THECOLORS["white"]
	space.add(gate)
	return gate
def deletegate(gates):
	for pinna in gates:
		space.remove(pinna)
	gates = []
	return gates

def changey(position):
	return int(position.x), int(-position.y+720)

def draw():
	for ball in balls:
		disegnapalla(ball)
	for bumper in bumpers:
		disegnabumper(bumper)
def disegnapalla(ball):
	body = ball.body
	position = body.position + ball.offset.cpvrotate(body.rotation_vector)
	coordinates = changey(position)
	r = ball.radius
	pygame.draw.circle(window, THECOLORS["white"], coordinates, int(r), 0)
def disegnabumper(ball):
	body = ball.body
	position = body.position + ball.offset.cpvrotate(body.rotation_vector)
	coordinates = changey(position)
	r = ball.radius
	pygame.draw.circle(window, THECOLORS["white"], coordinates, int(r), 0)

def punteggiodesign():
		#Rettangoli punteggio 
		pygame.draw.rect(window,pygame.color.THECOLORS["white"] ,[30, 50, 270, 52], 2)
		pygame.draw.rect(window,pygame.color.THECOLORS["white"] ,[30, 162, 270, 52], 2)
		pygame.draw.rect(window,pygame.color.THECOLORS["white"] ,[30, 274, 270, 52], 2)
		pygame.draw.rect(window,pygame.color.THECOLORS["white"] ,[30, 386, 270, 52], 2)
		
		#Numeri
		NUMEROUNO= fontsuino.render(("1"),True,THECOLORS["white"])
		NUMERODUE= fontsuino.render(("2"),True,THECOLORS["white"])
		NUMEROTRE= fontsuino.render(("3"),True,THECOLORS["white"])
		NUMEROQUATTRO= fontsuino.render(("4"),True,THECOLORS["white"])
		window.blit(NUMEROUNO,(150,15))
		window.blit(NUMERODUE,(150,125))
		window.blit(NUMEROTRE,(150,235))
		window.blit(NUMEROQUATTRO,(150,345))
def printscore(letters,scores):
	printscore = fontsuino.render(("%s"%scores),True,THECOLORS["white"])
	window.blit(printscore,(40,55))

def printletters():
	lettera_N = fontsmall.render(("N"),True,THECOLORS["white"])
	lettera_I = fontsmall.render(("I"),True,THECOLORS["white"])
	lettera_G = fontsmall.render(("G"),True,THECOLORS["white"])
	lettera_H = fontsmall.render(("H"),True,THECOLORS["white"])
	lettera_T = fontsmall.render(("T"),True,THECOLORS["white"])

	lettera_D = fontsmall.render(("D"),True,THECOLORS["white"])
	lettera_R = fontsmall.render(("R"),True,THECOLORS["white"])
	lettera_O = fontsmall.render(("O"),True,THECOLORS["white"])
	lettera_P = fontsmall.render(("P"),True,THECOLORS["white"])

	lettera_A = fontsmall.render(("A"),True,THECOLORS["white"])
	lettera_B = fontsmall.render(("B"),True,THECOLORS["white"])
	lettera_C = fontsmallest.render(("C"),True,THECOLORS["white"])
	lettera_D2 = fontsmallest.render(("D"),True,THECOLORS["white"])

	if letters["n"] == True:
		window.blit(lettera_N,(620,140))
	if letters["i"] == True:
		window.blit(lettera_I,(659,135))
	if letters["g"] == True:
		window.blit(lettera_G,(698,132))
	if letters["h"] == True:
		window.blit(lettera_H,(736,135))
	if letters["t"] == True:
		window.blit(lettera_T,(776,140))
	if letters["d"] == True:
		window.blit(lettera_D,(340,460))
	if letters["r"] == True:
		window.blit(lettera_R,(366,460))
	if letters["o"] == True:
		window.blit(lettera_O,(392,460))
	if letters["p"] == True:
		window.blit(lettera_P,(417,460))
	if letters["a"] == True:
		window.blit(lettera_A,(795,325))
	if letters["b"] == True:
		window.blit(lettera_B,(818,347))
	if letters["c"] == True:
		window.blit(lettera_C,(492,38))
	if letters["d2"] == True:		
		window.blit(lettera_D2,(517,44))

def speed(springs):
	if springs == 584:
		power = 300
	elif springs == 614:
		power = 500
	elif springs == 644:
		power = 630
	elif springs == 674:
		power = 950
	elif springs == 704:
		power = 1550
	return (power)
def drawsprings():
	pygame.draw.line(window, pygame.color.THECOLORS["white"], (890,707), (890,584), 30)

def drawall():
	punteggiodesign()
	printscore(letters,scores)
	printletters()
	draw()

def drawroll(x,y): 
	riga1 = pygame.draw.line(window, pygame.color.THECOLORS["red"], (550,255), (550,227), 1)
	riga2 = pygame.draw.line(window, pygame.color.THECOLORS["red"], (557,255), (557,227), 1)
	riga3 = pygame.draw.line(window, pygame.color.THECOLORS["red"], (565,255), (565,227), 1)
	pygame.draw.line(window, pygame.color.THECOLORS["red"], (542,242), (572,242), 1)
	pygame.draw.line(window, pygame.color.THECOLORS["red"], (384,155), (418,155), 1)
	riga4 = pygame.draw.line(window, pygame.color.THECOLORS["red"], (396,163), (396,149), 1)
	riga5 = pygame.draw.line(window, pygame.color.THECOLORS["red"], (401,163), (401,149), 1)
	riga6 = pygame.draw.line(window, pygame.color.THECOLORS["red"], (406,163), (406,149), 1)
	if 540 <= x <= 570 and 480 < y < 500:
		print("suca")
		yup = 0
		ydown = 0
		for x in range(1,15):
			yup += 1.5
			ydown += 1.5
			riga1 = pygame.draw.line(window, pygame.color.THECOLORS["red"], (550,255+yup), (550,227-ydown), 1)
			riga2 = pygame.draw.line(window, pygame.color.THECOLORS["red"], (557,255+yup), (557,227-ydown), 1)
			riga3 = pygame.draw.line(window, pygame.color.THECOLORS["red"], (565,255+yup), (565,227-ydown), 1)
			pygame.display.flip()
	elif 384 <= x <= 414 and 560 < y < 570:
			yup = 0
			ydown = 0
			for x in range(1,15):
				yup += 1
				ydown += 1
				riga4 = pygame.draw.line(window, pygame.color.THECOLORS["red"], (396,163+yup), (396,149-ydown), 1)
				riga5 = pygame.draw.line(window, pygame.color.THECOLORS["red"], (401,163+yup), (401,149-ydown), 1)
				riga6 = pygame.draw.line(window, pygame.color.THECOLORS["red"], (406,163+yup), (406,149-ydown), 1)
				pygame.display.flip()

def printcredit(credit):
	printcredit=fontsuino.render(("%s"%credit),True,THECOLORS["white"])
	window.blit(printcredit,(1020,550))

import pygame,sys,pymunk,score
from pygame.locals import *
from pygame.color import *
import pymunk as pm
from pymunk import Vec2d
import pymunk.pygame_util

pygame.init()
window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Night Mission")
time = pygame.time.Clock()

#Physics Stuff
space = pm.Space()
space.gravity = (0.0, -180.0)
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
				,pymunk.Segment(space.static_body, (480,86), (376.8,86), 1)
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
#~ ******************************** BUMPER SINISTRO ****************************
				,pymunk.Segment(space.static_body, (484,117), (436,142), 1)
				,pymunk.Segment(space.static_body, (436,257), (436,142), 1)
				,pymunk.Segment(space.static_body, (484,117), (497,124), 1)
#~ ******************************* BUMPER DESTRO ****************************
				,pymunk.Segment(space.static_body, (724,120), (782,145), 1)
				,pymunk.Segment(space.static_body, (782,145), (782,243), 1)
				,pymunk.Segment(space.static_body, (768,264), (782,243), 1)
				,pymunk.Segment(space.static_body, (724,120), (710,133), 1)
#~ ********************************* AEROPORTO DI BIRGI **************************
				,pymunk.Segment(space.static_body, (375,467), (375,640), 1)
				,pymunk.Segment(space.static_body, (375,467), (438,390), 1)
				,pymunk.Segment(space.static_body, (438,390), (540,432), 1)
				,pymunk.Segment(space.static_body, (540,432), (540,532), 1)
				,pymunk.Segment(space.static_body, (540,532), (556,563), 1)
				,pymunk.Segment(space.static_body, (556,563), (556,625), 1)
				
				,pymunk.Segment(space.static_body, (382,477), (382,640), 1)
				,pymunk.Segment(space.static_body, (375,640), (382,640), 2)
				,pymunk.Segment(space.static_body, (382,477), (399,457), 1)
				,pymunk.Segment(space.static_body, (527,457), (399,457), 1)
				,pymunk.Segment(space.static_body, (529,457), (529,607), 1)
				,pymunk.Segment(space.static_body, (552,626), (529,607), 1)
				,pymunk.Segment(space.static_body, (552,626), (556,626), 1)
#~ *******************************AEROPORTO DI BIRGI INTERNO**********************
				,pymunk.Segment(space.static_body, (420,620), (420,484), 1)
				,pymunk.Segment(space.static_body, (426,480), (495,480), 1)
				,pymunk.Segment(space.static_body, (426,480), (420,484), 1)
				,pymunk.Segment(space.static_body, (499,611), (499,484), 1)
				,pymunk.Segment(space.static_body, (495,480), (499,484), 1)
				,pymunk.Segment(space.static_body, (420,620), (462,655), 1)
				,pymunk.Segment(space.static_body, (505,655), (462,655), 1)
				,pymunk.Segment(space.static_body, (505,655), (525.5,648), 1)
				,pymunk.Segment(space.static_body, (526,635), (526,647), 1)
				,pymunk.Segment(space.static_body, (526,635), (499,611), 1)
				
#~ *********************************ROLLINO***************************************
				,pymunk.Segment(space.static_body, (574,500), (574,460), 2)
]

for wall in staticwalls:
	wall.elasticity = 0.7
	wall.group = 1
	wall.friction = 1
	wall.color = pygame.color.THECOLORS["white"]
space.add(staticwalls)

##Bumpers
bumpers = []
for p in [(790,500), (650,320),(700,450)]:
	body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
	body.position = p
	shape = pymunk.Circle(body, 14)
	shape.elasticity = 3
	shape.friction = 1
	shape.color = pygame.color.THECOLORS["white"]
	space.add(shape)
	bumpers.append(shape)
for q in [(630,500),(550,350)]:
	body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
	body.position = q
	shape = pymunk.Circle(body, 9)
	shape.elasticity = 2
	shape.color = pygame.color.THECOLORS["white"]
	space.add(shape)
	bumpers.append(shape)

bumperleft = pymunk.Segment(space.static_body, (438,257), (498,123), 1)
bumperleft.elasticity = 2.5
bumperleft.group = 1
bumperleft.friction = 1
bumperleft.color = pygame.color.THECOLORS["white"]
bumperight = pymunk.Segment(space.static_body, (768,264), (709,133), 1)
bumperight.elasticity = 2.5
bumperight.group = 1
bumperight.friction = 1
bumperight.color = pygame.color.THECOLORS["white"]
space.add(bumperleft,bumperight)

#FLIPPER

rbar = [(27,-16), (-90, 0), (15,10)]
lbar = [(-27,-16), (90, 0), (-15,10)]
mass = 100
mo = pymunk.moment_for_poly(mass, rbar)

#Flipper Right
r_bar_body = pymunk.Body(mass, mo)
r_bar_body.position = 710, 74
r_bar_form = pymunk.Poly(r_bar_body, rbar)
r_bar_form.color = pygame.color.THECOLORS["white"]
space.add(r_bar_body, r_bar_form)

r_bar_union_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
r_bar_union_body.position = r_bar_body.position 
union = pymunk.PinJoint(r_bar_body, r_bar_union_body, (0,0), (0,0))
rotary = pymunk.DampedRotarySpring(r_bar_body, r_bar_union_body, 0.35, 9000000,999999)
space.add(union, rotary)

#Flipper Left
l_bar_body = pymunk.Body(mass, mo)
l_bar_body.position = 502, 74
l_bar_form = pymunk.Poly(l_bar_body, lbar)
l_bar_form.color = pygame.color.THECOLORS["white"]
space.add(l_bar_body, l_bar_form)

l_bar_union_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
l_bar_union_body.position = l_bar_body.position 
union = pymunk.PinJoint(l_bar_body, l_bar_union_body, (0,0), (0,0))
rotary = pymunk.DampedRotarySpring(l_bar_body, l_bar_union_body, -0.35, 9000000,999999)
space.add(union, rotary)

r_bar_form.group = l_bar_form.group = 1
r_bar_form.elasticity = l_bar_form.elasticity = 0.7

#Font
font = pygame.font.Font('FONT/ARCADECLASSIC.TTF',60)
fontsmall = pygame.font.Font('FONT/ARCADECLASSIC.TTF',30)
fontsuino = pygame.font.Font('FONT/ARCADECLASSIC.TTF',40)
fontsmallest = pygame.font.Font('FONT/ARCADECLASSIC.TTF',25)

#Event
MOVEEVENT,t = pygame.USEREVENT+1,3000
pygame.time.set_timer(MOVEEVENT, t)
porco,ti = pygame.USEREVENT+2,500
pygame.time.set_timer(porco, ti)
chiave = False

#Game
balls = []
gates = []
letters = {
	"d": True,
	"r": True,
	"o": True,
	"p": True,
	"f": True,
	"l": True,
	"y": True,
	"a": True,
	"b": True,
	"c": True,
	"d2": True,
	"n": True,
	"i": True,
	"g": True,
	"h": True,
	"t": True
}
scores = 0
credit = 0
nball = 0
start = True
while 1:
	while start:
		#Menu Start
		window.fill(THECOLORS["black"])
		namegame = font.render(("Night Mission"),True,THECOLORS["white"])
		quitgame = fontsmall.render(("Press q to quit the game"),True,THECOLORS["white"])
		startgame = fontsmall.render(("Press a to start the game"),True,THECOLORS["white"])
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN and event.key == K_q: #Quit
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN and event.key == K_a: #Start
				#Create the ball
				balls.append(newball())

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
		sfondo = pygame.image.load("prova1.jpg")
		window.blit(sfondo,(0,0))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN:
				x,y = event.pos #
				print(x,y) #
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				pause = True
				running = False
			elif event.type == KEYDOWN and event.key == K_c:
				if credit != 25:
					credit+=1
			elif event.type == KEYDOWN and event.key == K_LSHIFT:
				if credit != 0:
					ballbody.position = Vec2d(890,300) 
					springs = 584
					credit -= 1
					nball += 3
					print(nball)
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
				drawsprings()
				springs = 584
			elif event.type == porco and chiave == True:
				print("evento")
				pygame.draw.line(window,THECOLORS["white"],(550,230-up),(550,250+up),3)
				pygame.draw.line(window,THECOLORS["white"],(557,230-up),(557,250+up),3)
				pygame.draw.line(window,THECOLORS["white"],(564,230-up),(564,250+up),3)
				up += 0.2

		#Animazione Molla Bonus
		if 825 <= ballbody.position.x <= 875 and ballbody.position.y < 154:
			space.remove(ballbody, ballform)
			balls.remove(ballform)

			go = True
			while go:
				sfondo = pygame.image.load("prova1.jpg")
				window.blit(sfondo,(0,0))
				pygame.draw.circle(window, THECOLORS["white"], (852,566), 10, 0)
				scores += 2
				printscore(letters,scores)
				drawall()
				draw()
				drawroll()
				drawsprings()
				space.debug_draw(OptionsDraw)
				pygame.display.update()
				for event in pygame.event.get():
					if event.type == MOVEEVENT:
						mass = 1
						radius = 10
						inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
						ballbody = pymunk.Body(mass, inertia,body_type=pymunk.Body.DYNAMIC)

						ballform = pymunk.Circle(ballbody, radius, (0,0))
						ballform.elasticity = 0.7
						ballform.color = pygame.color.THECOLORS["white"]
						ballbody.position = 852, 154
						space.add(ballbody, ballform)
						balls.append(ballform)

						ballbody.apply_impulse_at_local_point((Vec2d((0,500))))
						go = False

		#*** MOLLA AEROPORTO DI BIRGI****
		if 500 <= ballbody.position.x <= 550 and 450 < ballbody.position.y < 500:
			space.remove(ballbody, ballform)
			balls.remove(ballform)
			mass = 1.5
			radius = 10.3
			inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
			ballbody = pymunk.Body(mass, inertia,body_type=pymunk.Body.DYNAMIC)
			ballform = pymunk.Circle(ballbody, radius, (0,0))
			ballform.elasticity = 0.7
			ballform.color = pygame.color.THECOLORS["white"]
			ballbody.position = 510, 480
			space.add(ballbody, ballform)
			balls.append(ballform)
			ballbody.apply_impulse_at_local_point((Vec2d((0,800))))

		#Springs
		pygame.draw.line(window, pygame.color.THECOLORS["white"], (890,707), (890,springs), 30)

		#Gate
		if ballbody.position.y > 598 and 860 <= ballbody.position.x <= 890: ## modificare condizione
			gates.append(newgate())

		#Respawn Ball
		if ballbody.position.y <= 12 and 333 <= ballbody.position.x <= 830:
			gates = deletegate(gates)
			balls.remove(ballform)
			space.remove(ballbody,ballform)
			if nball != 0:
				#Create new ball
				balls.append(newball())
				ballbody.position = Vec2d(890,260)
				nball -= 1
				print(nball)
			else:
				print(nball)
				pass

		#Draw Stuff
		space.debug_draw(OptionsDraw)

		r_bar_body.position = 710, 74
		l_bar_body.position = 502, 74
		r_bar_body.velocity = l_bar_body.velocity = 0,0

		scores = score.countscore(ballbody.position.x,ballbody.position.y,letters,scores)
		drawall()

		drawroll(ballbody.position.x,ballbody.position.y)
		printcredit(credit)

		#Update Physics
		dt = 1/50.0/3
		for x in range(9):
			space.step(dt)

		#Flip Screen
		time.tick()
		pygame.display.flip()
	while pause:
		window.fill(THECOLORS["black"])
		written = font.render(("Pause"),True,THECOLORS["white"])
		writtensmall = fontsmall.render(("Press q to quit the game"),True,THECOLORS["white"])
		resume = fontsmall.render(("Press esc to resume the game"),True,THECOLORS["white"])
		restart = fontsmall.render(("Press r to restart the game"),True,THECOLORS["white"])
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN and event.key == K_q: #Quit
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN and event.key == K_r: #Restart
				space.remove(ballbody, ballform)
				balls.remove(ballform)
				gates = deletegate(gates)
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
