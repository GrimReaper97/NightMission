def newball():
	mass = 1
	radius = 10.3
	moment = pm.moment_for_circle(mass, radius, 0.0, (0,0))
	ballbody = pm.Body(mass, moment)
	ballform = pm.Circle(ballbody, radius, (0,0))
	ballform.elasticity = 0.7
	ballform.group = 1
	ballform.collision_type = 1
	ballbody.position = (890,300)
	ballform.color = THECOLORS["white"]
	space.add(ballbody, ballform)
	global ballbody,ballform
	return ballform

def newgate():
	gate = pymunk.Segment(space.static_body, (870,560), (900,612), 1)
	gate.elasticity = 0.7
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
def flipy(y): ##
	return -y+720 ##

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
		CREDIT = fontsuino.render(("Credits"),True,THECOLORS["white"])
		BALLS = fontsuino.render(("Balls"),True,THECOLORS["white"])
		window.blit(NUMEROUNO,(150,15))
		window.blit(NUMERODUE,(150,125))
		window.blit(NUMEROTRE,(150,235))
		window.blit(NUMEROQUATTRO,(150,345))
		window.blit(CREDIT,(10,605))
		window.blit(BALLS,(190,605))
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
	lettera_C = fontsmall.render(("C"),True,THECOLORS["white"])
	lettera_D2 = fontsmall.render(("D"),True,THECOLORS["white"])

	lettera_F = fontsmallest.render(("F"),True,THECOLORS["white"])
	lettera_L = fontsmallest.render(("L"),True,THECOLORS["white"])
	lettera_Y = fontsmall.render(("Y"),True,THECOLORS["white"])

	starimg = pygame.image.load("star.png")

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
		pygame.draw.line(window, pygame.color.THECOLORS["white"], (804,323), (827,342), 3)
	if letters["b"] == True:
		window.blit(lettera_B,(818,347))
		pygame.draw.line(window, pygame.color.THECOLORS["white"], (852,361), (831,344), 3)
	if letters["c"] == True:
		window.blit(lettera_C,(828,233))
		pygame.draw.line(window, pygame.color.THECOLORS["white"], (833,274), (857,244), 3)
	if letters["d2"] == True:		
		window.blit(lettera_D2,(802,265))
		pygame.draw.line(window, pygame.color.THECOLORS["white"], (807,303), (829,277), 3)
	if letters["f"] == True:
		window.blit(lettera_F,(461,327))
		pygame.draw.line(window, pygame.color.THECOLORS["white"], (448,333), (475,323), 3)
	if letters["l"] == True:
		window.blit(lettera_L,(495,314))
		pygame.draw.line(window, pygame.color.THECOLORS["white"], (483,319), (508,309.5), 3)
	if letters["y"] == True:
		window.blit(lettera_Y,(524,301))
		pygame.draw.line(window, pygame.color.THECOLORS["white"], (515,305), (541,295), 3)
	if star == True:
		window.blit(star,(31,28))

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

def printcredit(credit):
	printcredit=fontsuino.render(("%s"%credit),True,THECOLORS["white"])
	window.blit(printcredit,(70,655))
	printballs=fontsuino.render(("%s"%nball),True,THECOLORS["white"])
	window.blit(printballs,(230,655))

def setletters():
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
	"t": True,
	"bonusabcd" : True,
	"bonusnight" : True,
	"bonusfly" : True,
	"special" : True,
	"multiball": True,
	"bonusbumper": True
	}
	return letters

def bumpersmall(arbiter, space, data):
	ballform.group = 2
def bumperbig(arbiter, space, data):
	ballform.group = 3

def multiball():
	mass = 1
	radius = 10.3
	inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
	ballbody = pymunk.Body(mass, inertia,body_type=pymunk.Body.DYNAMIC)

	ballform = pymunk.Circle(ballbody, radius, (0,0))
	ballform.elasticity = 0.7
	ballform.group = 1
	ballform.color = pygame.color.THECOLORS["white"]
	ballform.collision_type = 1
	ballbody.position = 852, 154
	space.add(ballbody, ballform)
	balls.append(ballform)
	global ballbody
	global ballform
	ballbody.apply_impulse_at_local_point((Vec2d((0,500))))

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

#Bumpers
bumpers = []
for b in [(790,500), (650,320),(700,450)]:
	body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
	body.position = b
	shape = pymunk.Circle(body, 14)
	shape.elasticity = 3
	shape.collision_type = 3
	shape.friction = 1
	shape.color = pygame.color.THECOLORS["white"]
	space.add(shape)
	bumpers.append(shape)
for s in [(630,500),(550,350)]:
	body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
	body.position = s
	shape = pymunk.Circle(body, 9)
	shape.elasticity = 2
	shape.collision_type = 2
	shape.color = pygame.color.THECOLORS["white"]
	space.add(shape)
	bumpers.append(shape)

bumperleft = pymunk.Segment(space.static_body, (438,257), (498,123), 1)
bumperleft.elasticity = 2
bumperleft.group = 1
bumperleft.friction = 1
bumperleft.color = pygame.color.THECOLORS["white"]
bumperight = pymunk.Segment(space.static_body, (768,264), (709,133), 1)
bumperight.elasticity = 2
bumperight.group = 1
bumperight.friction = 1
bumperight.color = pygame.color.THECOLORS["white"]
space.add(bumperleft,bumperight)

#FLIPPER

rbar = [(27,-16), (-90, 0), (15,10)]
lbar = [(-27,-16), (90, 0), (-15,10)]
mass = 100
mo = pymunk.moment_for_poly(mass, rbar)

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
TILTS,t1 = pygame.USEREVENT+2,2000
pygame.time.set_timer(MOVEEVENT, t)
pygame.time.set_timer(TILTS, t1)

#Game
balls = []
gates = []
letters = setletters()
scores = 0
scorebonus = 0
bumperbonus = 0
credit = 1
nball = 0
tilt = 0
#~ record = 0
star = False
animazione = 1
animazionep = 1
special = True
suca = True
start = True
tilted = False
hard = False
startcredit = False
select = True
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
				balls.remove(ballform)
				space.remove(ballbody,ballform)

				#Power of spring
				springs = 584

				running = True
				pause = False
				start = False
		window.blit(namegame,(473,70))
		window.blit(quitgame,(490,230))
		window.blit(startgame,(485,280))
		pygame.display.update()
	while select:
			window.fill(THECOLORS["black"])
			selectd = font.render(("Select difficulty"),True,THECOLORS["white"])
			ez = fontsmall.render(("E               Easy level"),True,THECOLORS["white"])
			md = fontsmall.render(("M               Medium level"),True,THECOLORS["white"])
			hd = fontsmall.render(("H               Hard level"),True,THECOLORS["white"])
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == KEYDOWN and event.key == K_e:
					running = True
					select = False
					body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
					body.position = (605,20)
					shape = pymunk.Circle(body, 5)
					shape.friction = 1
					shape.color = pygame.color.THECOLORS["white"]
					space.add(shape)
					bumpers.append(shape)
					shape.elasticity = 0.8
				elif event.type == KEYDOWN and event.key == K_m:
					running = True
					select = False
				elif event.type == KEYDOWN and event.key == K_h:
					hard = True
					running = True
					select = False
			window.blit(selectd,(400,70))
			window.blit(ez,(470,300))
			window.blit(md,(470,350))
			window.blit(hd,(470,400))
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
			elif event.type == KEYDOWN and event.key == K_c and startcredit == False:
				if hard == True:
					if credit != 5:
						credit+=1
						sound = pygame.mixer.Sound("credit.ogg")
						sound.play()
				else:
					if credit != 25:
						credit+=1
						sound = pygame.mixer.Sound("credit.ogg")
						sound.play()
			elif event.type == KEYDOWN and event.key == K_LSHIFT:
				startcredit = True
				if credit != 0:
					if balls == []:
						balls.append(newball())
						credit -= 1
						if hard == True:
							nball += 2
						else:
							nball += 5
			elif event.type == KEYDOWN and event.key == K_RIGHT and tilted == False:
				r_bar_body.apply_impulse_at_local_point(Vec2d.unit() * 15000, (-100, 0))
			elif event.type == KEYDOWN and event.key == K_LEFT and tilted == False:
				l_bar_body.apply_impulse_at_local_point(Vec2d.unit() * -15000, (-100, 0))
			elif event.type == KEYDOWN and event.key == K_DOWN:
				if springs != 704:
					springs += 30
			elif event.type == KEYDOWN and event.key == K_UP:
				if springs != 584:
					springs -= 30
			elif event.type == KEYDOWN and event.key == K_z:
				if balls != []:
					tilt += 1
					ballbody.apply_impulse_at_local_point((Vec2d((100,0))))
			elif event.type == KEYDOWN and event.key == K_x:
				if balls != []:
					tilt += 1
					ballbody.apply_impulse_at_local_point((Vec2d((-100,0))))
			elif event.type == KEYDOWN and event.key == K_SPACE and 147 <= ballbody.position.y <= 148 and ballbody.position.x == 890.0:
				power = speed(springs)
				ballbody.apply_impulse_at_local_point((Vec2d((0,power))))
				drawsprings()
				springs = 584
			elif event.type == TILTS and tilt != 0:
				tilt = 0
			elif event.type == MOUSEBUTTONUP: ##
				puntisuca = Vec2d(event.pos[0], flipy(event.pos[1]))
				mass = 1
				radius = 10.3
				moment = pm.moment_for_circle(mass, radius, 0.0, (0,0))
				ballbody = pm.Body(mass, moment)
				ballform = pm.Circle(ballbody, radius, (0,0))
				ballform.elasticity = 0.7
				ballform.group = 1
				ballform.collision_type = 1
				ballbody.position = puntisuca
				ballform.color = THECOLORS["white"]
				global ballform,ballbody
				space.add(ballbody, ballform)
				balls.append(ballform)

		#Tilt animation
		if tilt >= 3:
			tilted = True
		if tilted == True:
			tiltext = font.render(("TILT"),True,THECOLORS["white"])
			window.blit(tiltext,(975,115))
			setletters()
			special = True

		#Animazione Molla Bonus
		if 825 <= ballbody.position.x <= 875 and ballbody.position.y < 154:
			space.remove(ballform,ballbody)
			balls.remove(ballform)
			sound = pygame.mixer.Sound("mollabonus.ogg")
			sound.play()

			go = True
			while go:
				sfondo = pygame.image.load("prova1.jpg")
				window.blit(sfondo,(0,0))
				pygame.draw.circle(window, THECOLORS["white"], (852,566), 10, 0)
				scores += 2
				printscore(letters,scores)
				drawall()
				draw()
				drawsprings()
				space.debug_draw(OptionsDraw)
				pygame.display.update()
				for event in pygame.event.get():
					if event.type == MOVEEVENT:
						multiball()
						go = False

		#*** MOLLA AEROPORTO DI BIRGI****
		if 500 <= ballbody.position.x <= 550 and 450 < ballbody.position.y < 500:
			sound = pygame.mixer.Sound("birgi.ogg")
			sound.play()
			space.remove(ballbody, ballform)
			balls.remove(ballform)
			mass = 1
			radius = 10.3
			inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
			ballbody = pymunk.Body(mass, inertia,body_type=pymunk.Body.DYNAMIC)
			ballform = pymunk.Circle(ballbody, radius, (0,0))
			ballform.elasticity = 0.7
			ballform.group = 1
			ballform.color = pygame.color.THECOLORS["white"]
			ballform.collision_type = 1
			ballbody.position = 510, 480
			space.add(ballbody, ballform)
			balls.append(ballform)
			ballbody.apply_impulse_at_local_point((Vec2d((0,1200))))

		#Springs
		pygame.draw.line(window, pygame.color.THECOLORS["white"], (890,707), (890,springs), 30)

		#Gate
		if ballbody.position.y > 598 and 860 <= ballbody.position.x <= 890: ## modificare condizione
			gates.append(newgate())

		#Respawn Ball
		if ballbody.position.y <= 12 and 333 <= ballbody.position.x <= 830:
			tilted = False
			tilt = 0
			if balls != []:
				space.remove(ballbody, ballform)
				balls.remove(ballform)
			if gates != []:
				gates = deletegate(gates)
			letters = setletters()
			if balls == []:
				if nball > 1:
					#Create new ball
					balls.append(newball())
					nball -= 1
				elif nball == 1:
					nball -= 1

		space.debug_draw(OptionsDraw)
		pygame.draw.circle(window,THECOLORS["white"],(710,646),6,0)
		pygame.draw.circle(window,THECOLORS["white"],(502,646),6,0)
		r_bar_body.position = 710, 74
		l_bar_body.position = 502, 74
		r_bar_body.velocity = l_bar_body.velocity = 0,0

		#Animation rollover
		rollo = pygame.draw.rect(window, THECOLORS["white"], (548,235,19,7))
		if 540 <= ballbody.position.x <= 570 and 480 < ballbody.position.y < 500:
			if animazione == 1:
				rollo = pygame.draw.rect(window, THECOLORS["white"], (548,230,19,18))
			if animazione == 2:
				rollo = pygame.draw.rect(window, THECOLORS["white"], (548,233,19,11))
			if animazione == 3:
				rollo = pygame.draw.rect(window, THECOLORS["white"], (548,235,19,7))
			if animazione == 4:
				rollo = pygame.draw.rect(window, THECOLORS["white"], (548,235,19,7))
			if animazione == 5:
				rollo = pygame.draw.rect(window, THECOLORS["white"], (548,235,19,11))
			if animazione == 6:
				rollo = pygame.draw.rect(window, THECOLORS["white"], (548,233,19,7))
			if animazione == 7:
				rollo = pygame.draw.rect(window, THECOLORS["white"], (548,233,19,18))
			if animazione == 8:
				rollo = pygame.draw.rect(window, THECOLORS["white"], (548,233,19,7))
			if animazione == 9:
				rollo = pygame.draw.rect(window, THECOLORS["white"], (548,233,19,11))
			if animazione == 10:
				rollo = pygame.draw.rect(window, THECOLORS["white"], (548,233,19,18))
				animazione = 1
			else:
				animazione += 1
		#ROLLOVER PICCOLO
		rollop = pygame.draw.rect(window, THECOLORS["white"], (392,170,19,7))
		if 390 <= ballbody.position.x <= 420 and 540 < ballbody.position.y < 560:
			if animazionep == 1:
				rollop = pygame.draw.rect(window, THECOLORS["white"], (392,170,19,18))
			if animazionep == 2:
				rollop = pygame.draw.rect(window, THECOLORS["white"], (392,170,19,11))
			if animazionep == 3:
				rollop = pygame.draw.rect(window, THECOLORS["white"], (392,170,19,7))
			if animazionep == 4:
				rollop = pygame.draw.rect(window, THECOLORS["white"], (392,170,19,7))
			if animazionep == 5:
				rollop = pygame.draw.rect(window, THECOLORS["white"], (392,170,19,11))
			if animazionep == 6:
				rollop = pygame.draw.rect(window, THECOLORS["white"], (392,170,19,18))
			if animazionep == 7:
				rollop = pygame.draw.rect(window, THECOLORS["white"], (392,170,19,18))
			if animazionep == 8:
				rollop = pygame.draw.rect(window, THECOLORS["white"], (392,170,19,18))
			if animazionep == 9:
				rollop = pygame.draw.rect(window, THECOLORS["white"], (392,170,19,18))
			if animazionep == 10:
				rollop = pygame.draw.rect(window, THECOLORS["white"], (392,170,19,18))
				animazionep = 1
			else:
				animazionep += 1

		#Punteggio for bumper
		h = space.add_collision_handler(1,2)
		h.post_solve = bumpersmall
		p = space.add_collision_handler(1,3)
		p.post_solve = bumperbig
		if ballform.group == 2:
			scores += 50 + bumperbonus
			ballform.group = 1
		elif ballform.group == 3:
			scores += 90 + bumperbonus
			ballform.group = 1
		if letters["bonusbumper"] == False:
			bumperbonus = 150

		#Multiball
		if letters["multiball"] == False:
			multiball()
			letters["multiball"] = None
		if scorebonus >= 3000: #Special
			if suca == True:
				multiball()
				suca = False

		#To start a game
		if nball == 0:
			startgame = fontsmall.render(("Press LEFT SHIFT"),True,THECOLORS["white"])
			respawnball = fontsmall.render(("To start a game"),True,THECOLORS["white"])
			window.blit(startgame,(995,90))
			window.blit(respawnball,(999,123))
			scores = 0
			setletters()

		#Loser
		loser = False
		if nball == 0 and credit == 0:
			loser = True
			while loser:
				#~ space.remove(ballbody, ballform)
				#~ balls.remove(ballform)
				sfondo = pygame.image.load("prova1.jpg")
				window.blit(sfondo,(0,0))
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
					elif event.type == KEYDOWN and event.key == K_ESCAPE:
						pause = True
						running = False
						loser = False

		printcredit(credit)
		scores,scorebonus = score.countscore(ballbody.position.x,ballbody.position.y,letters,scores,scorebonus,special)
		drawall()

		if scores >= 10000000:
			star = True
			credit += 1

		#~ if scores > record:
			#~ record = scores
			#~ credit += 3

		#Update Physics
		dt = 1/60.0/6
		for x in range(12):
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
				if balls != []:
					space.remove(ballbody, ballform)
					balls.remove(ballform)
				if gates != []:
					gates = deletegate(gates)
				nball = 0
				tilt = 0
				credit = 0
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
