import pymunk
def countscore(x,y,letters,scores,scorebonus,special):
	if 335 <= x <= 360 and y <= 246 and letters["d"] == True: #D
		scores += 2000 + scorebonus
		letters["d"] = False
		if letters["r"] == False and letters["o"] == False and letters["p"] == False:#ROP+D BONUS
			if letters["d"] == False:
				special = False
				scores+=30000
				letters["d"] = None
	elif 360 <= x <= 385 and 235 <= y <= 258 and letters["r"] == True:#R
		scores += 2000 + scorebonus
		letters["r"] = False
	elif 380 <= x <= 410 and 235 <= y <= 258 and letters["o"] == True:#O
		scores += 2000 + scorebonus
		letters["o"] = False
	elif 410 <= x <= 437 and 235 <= y <= 258 and letters["p"] == True:#P
		scores += 2000 + scorebonus
		letters["p"] = False

	elif 605 <= x <= 645 and 554 <= y <= 579 and letters["n"] == True:#N
		scores += 1500 + scorebonus
		letters["n"] = False
	elif 648 <= x <= 685 and 563 <= y <= 580 and letters["i"] == True:#I
		scores += 1500 + scorebonus
		letters["i"] = False
	elif 686 <= x <= 720 and 564 <= y <= 580 and letters["g"] == True:#G
		scores += 1500 + scorebonus
		letters["g"] = False
	elif 724 <= x <= 760 and 562 <= y <= 582 and letters["h"] == True:#H
		scores += 1500 + scorebonus
		letters["h"] = False
	elif 762 <= x <= 800 and 554 <= y <= 579 and letters["t"] == True:#T
		scores += 1500 + scorebonus
		letters["t"] = False

	elif 805 <= x <= 884 and 382 <= y <= 398 and letters["a"] == True:#A
		scores += 1000 + scorebonus
		letters["a"] = False
	elif 830 <= x <= 848 and 362 <= y <= 377 and letters["b"] == True:#B
		scores += 1000 + scorebonus
		letters["b"] = False
	elif 830 <= x <= 854 and 447 <= y <= 482 and letters["c"] == True:#C
		scores += 1000
		letters["c"] = False
	elif 801 <= x <= 829 and 419 <= y <= 445 and letters["d2"] == True:#D
		scores += 1000
		letters["d2"] = False

	elif 438 <= x <= 478 and 384 <= y <= 405 and letters["f"] == True:#F
		scores += 1000 + scorebonus
		letters["f"] = False
	elif 475 <= x <= 514 and 401 <= y <= 418 and letters["l"] == True:#L
		scores += 1000
		letters["l"] = False
	elif 508 <= x <= 544 and 409 <= y <= 433 and letters["y"] == True:#Y
		scores += 1000
		letters["y"] = False

	elif 825 <= x <= 860 and 295 <= y <= 300:#PERCORSO MOLLA BONUS
		scores += 100
	elif 785 <= x <= 820 and 220 <= y <= 225:#PERCORSO FLIPPER DESTRO
		scores += 300
	elif 385 <= x <= 420 and 205 <= y <= 210:#PERCORSO FLIPPER SINISTRO
		scores += 300
	elif 380 <= x <= 410 and 405 <= y <= 410:#SCIVOLO 5000
		scores += 5000
	elif 540 <= x <= 570 and 480 < y < 490: #ROLLOVER GRANDE
		scores += 100
	elif 390 <= x <= 420 and 555 < y < 565:#ROLLOVER PICCOLO
		scores += 200


#BONUSES
	if letters["a"] == False and letters["b"] == False and letters["c"] == False and letters["d2"] == False and letters["bonusabcd"] == True:#ABCD BONUS
		scores += 8000
		letters["bonusabcd"] = False
	if letters["n"] == False and letters["i"] == False and letters["g"] == False and letters["h"] == False and letters["t"] == False and letters["bonusnight"] == True:#NIGHT BONUS
		scores += 10000
		letters["bonusnight"] = False
	if letters["d"] == False and letters["r"] == False and letters["o"] == False and letters["p"] == False and letters["special"] == True:#DROP BONUS
		scores+=10000
		letters["special"] =  False
	if letters["f"] == False and letters["l"] == False and letters["y"] and letters["bonusfly"] == True:#FLY BONUS
		scores+=5000
		letters["bonusfly"] = False
	if letters["bonusabcd"] == False and letters["bonusfly"] == False:#SEQ ABCD+FLY
		pass
	if letters["bonusabcd"] == False and letters["bonusnight"] == False and letters["multiball"] == True:#SEQ ABCD+NIGHT 
		letters["multiball"] = False
	if special == False:
		scorebonus += 3000
		if special == True:
			scorebonus = 0
	return scores,scorebonus
