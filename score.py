import pymunk
def countscore(x,y,letters,scores):
	if 335 <= x <= 360 and y <= 246 and letters["d"] == True: #D
		scores += 100
		letters["d"] = False
	elif 360 <= x <= 385 and 235 <= y <= 258 and letters["r"] == True:#R
		scores += 100
		letters["r"] = False
	elif 380 <= x <= 410 and 235 <= y <= 258 and letters["o"] == True:#O
		scores += 100
		letters["o"] = False
	elif 410 <= x <= 437 and 235 <= y <= 258 and letters["p"] == True:#P
		scores += 100
		letters["p"] = False



	elif 605 <= x <= 645 and 554 <= y <= 579 and letters["n"] == True:#N
		scores += 100
		letters["n"] = False
	elif 648 <= x <= 685 and 563 <= y <= 580 and letters["i"] == True:#I
		scores += 100
		letters["i"] = False
	elif 686 <= x <= 720 and 564 <= y <= 580 and letters["g"] == True:#G
		scores += 100
		letters["g"] = False
	elif 724 <= x <= 760 and 562 <= y <= 582 and letters["h"] == True:#H
		scores += 100
		letters["h"] = False
	elif 762 <= x <= 800 and 554 <= y <= 579 and letters["t"] == True:#T
		scores += 100
		letters["t"] = False


	elif 805 <= x <= 884 and 382 <= y <= 398 and letters["a"] == True:#A
		scores += 100
		letters["a"] = False
	elif 830 <= x <= 848 and 362 <= y <= 377 and letters["b"] == True:#B
		scores += 100
		letters["b"] = False
	elif x and y: #C
		pass
	elif x and y: #D2
		pass
	return scores
