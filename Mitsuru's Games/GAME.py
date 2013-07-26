import random
import sys
import time
e_monster_art = None
can = True
canuse = 1
player_monster_name = None
ascii_voldemort = """

 O_o
/ ----------------------------
| BLAAAAAAAAAAAA AAAAAAARGH!!!
\_----------------------------

"""
ascii_fire = """
|         _____  |
|        /     \ |
|       /   O O_\|
|      /      _\ |
|     /  \\\\   /  |
|    /    o  /   |
| __/       /    |
|/         /     |
|-----\/-\/      |
"""
ascii_water = """
|          ____  |
|     ____/    \ |
|    /   /  O O_\|
|   /   /     _\ |
|  /   /  \\\\ |   |
| |   /    O |   |
| |  /      /    |
| \ /      /     |
|  \--\/-\/      |
"""
ascii_earth = """
|   _________    |
|  |___   ___|   |
|      | |       |
|    __|_|__     |
|   /       \_   |
|  /         O\  |
| /           _| |
||  ___   ____\  |
||_|   |_|       |
"""
doText = False
hasattack = False
pattack = ["Tackle"]
attackchosen = None
attacktracker = 0
fireattack = ["0","1","2","Flamethrower","4","Fireball","6","Meteor","8","Volcano","Sun"]
waterattack = ["0","1","2","Watershot","4","Waterball","6","Waterbomb","8","Tsunami","Ocean"]
earthattack = ["0","1","2","Mudshot","4","Mudball","6","Mudbomb","8","Earthquake","Earth"]
explist = [10,100,150,200,250,300,350,400,450,500]
exp = 0 #10,100,150,200,250,300,350,400,450,500
LAZARBEAM = 250
Tackle = 5 #level 1
Scratch = 10 #level 2
Flamethrower = 30 #level 3
Fireball = 40 #level 5
Meteor = 100 #level 7
Volcano = 200 #level 9
Sun = 300 #level 10 (max)
Watershot = 30
Waterball = 40
Waterbomb = 100
Tsunami = 200
Ocean = 300
Mudshot = 30
Mudball = 40
Mudbomb = 100
Earthquake = 200
Earth = 300
used = False
attacktype = None
maxhealth = [100,200,300,400,500,600,700,800,900,1000]
health = 100
level = 1
defense = 5
attack = 25
luck = 1
Gmaxhealth = maxhealth
Ghealth = 100
Glevel = 1
Gdefense = 1
Gattack = 10
Gluck = 1
maxdefense = [5,10,15,20,25,30,35,40,45,50]
maxattack = [25,50,75,100,125,150,175,200,250,500]
ptype = None
gary_monster = None
gary_monster_name = None
Gtype = None
mindchange = None
selectingmonster = None
ehealth = None
e_defense = None
e_attack = None
e_luck = None
etype = None
e_monster = None
e_monster_name = None
attackdone = None
wascritical = None
def enemyhealthafterhit(attackdone,attack,ptype,luck,e_defense,etype,ehealth):
	critical = random.randint(1,30)
	global damage
	wascritical = None
	global effectiveness
	global wascritical
	attackdamage = random.randint(1,attack)
	secondattackdamage = random.randint(1,attackdone)
	finalattack = (attackdamage + secondattackdamage)/2
	attackdefended = random.randint(1, e_defense)
	damage = finalattack - attackdefended
	attackdefended = attackdefended - 1
	if critical <= luck:
		damage = damage * 2
		wascritical = "You hit the enemy's weak spot!"
	if ptype == "fire" and etype == "earth" or ptype == "water" and etype == "fire" or ptype == "earth" and etype == "water":
		damage = int(damage * 1.5)
		effectiveness = "IT'S SUPER EFFECTIVE!"
	elif ptype == etype or ptype == "fire" and etype == "water" or ptype == "water" and etype == "earth" or ptype == "earth" and etype == "fire":
		damage = int(damage * .75)
		effectiveness = "It hardly did any damage..."
	if damage <= 0:
		damage = 1
	ehealth = ehealth - damage
	if ehealth < 0:
		ehealth = 0
	return ehealth
def yourhealthafterhit(attackdone,e_attack,etype,e_luck,defense,ptype,health):
	global wascritical
	wascritical = None
	critical = random.randint(1,30)
	global damage
	global effectiveness
	attackdamage = random.randint(1,e_attack)
	secondattackdamage = random.randint(1,attackdone)
	finalattack = (attackdamage + secondattackdamage)/2
	attackdefended = random.randint(1, defense)
	damage = finalattack - attackdefended
	attackdefended = attackdefended - 1
	if critical <= luck:
		damage = damage * 2
		wascritical = "It hit your monster's weak spot!"
	if ptype == "fire" and etype == "water" or ptype == "water" and etype == "earth" or ptype == "earth" and etype == "fire":
		damage = int(damage * 1.5)
		effectiveness = "IT'S SUPER EFFECTIVE!"
	elif ptype == etype or ptype == "fire" and etype == "earth" or ptype == "water" and etype == "fire" or ptype == "earth" and etype == "water":
		damage = int(damage * .75)
		effectiveness = "It hardly did any damage..."
	if damage <= 0:
		damage = 1
	health = health - damage
	if health < 0:
		health = 0
	return health
def attackgary(attackdone,attack,ptype,luck,Gdefense,Gtype,Ghealth):
	critical = random.randint(1,30)
	wascritical = None
	attackdamage = random.randint(1,attack)
	global damage
	global wascritical
	global effectiveness
	secondattackdamage = random.randint(1,attackdone)
	finalattack = (attackdamage + secondattackdamage)/2
	attackdefended = random.randint(1, Gdefense)
	damage = finalattack - attackdefended
	attackdefended = attackdefended - 1
	if critical <= luck:
		damage = damage * 2
		wascritical = "You hit the enemy's weak spot!"
	effectiveness = "It hardly did any damage..."
	damage = int(damage * .75)
	if damage <= 0:
		damage = 1
	Ghealth = Ghealth - damage
	if Ghealth < 0:
		Ghealth = 0
	return Ghealth
def garyattack(attackdone,Gattack,Gtype,Gluck,defense,ptype,health):
	critical = random.randint(1,30)
	global damage
	wascritical = None
	global wascritical
	global effectiveness
	attackdamage = random.randint(1,Gattack)
	secondattackdamage = random.randint(1,attackdone)
	finalattack = (attackdamage + secondattackdamage)/2
	attackdefended = random.randint(1, defense)
	damage = finalattack - attackdefended
	attackdefended = attackdefended - 1
	if critical <= luck:
		damage = damage * 2
		wascritical = "It his your monster's weak spot!"
	damage = int(damage * 1.5)
	effectiveness = "IT'S SUPER EFFECTIVE!"
	if damage <= 0:
		damage = 1
	health = health - damage
	if health < 0:
		health = 0
	return health
print "\n" * 1000
print "This game would not be possible by..."
print "The CS Club teachers - For teaching me programming."
print "And..."
print "Andrew Wang - For teaching me Python and debugging my code."
time.sleep(3)
response = raw_input("Press enter to continue.")
print "\n" * 1000
print "Quick tip: When battling, don't retype the same attack over and over.\nInstead, press up to go back to the previous attack and just hit enter!"
time.sleep(1.5)
response = raw_input("Press enter to continue.")
name = True
cheat = False
while name:
	print "\n"*1000
	name = False
	if doText:
		print "Error, please type in a name."
	print "Professor Ork: Welcome to the monster training game! Our world has been taken over by the evil king VOLDEMORT. I presume you are here to defeat him and his mosnter and save all mankind. Would you be so nice to tell me your name?"
	player_name = raw_input("Name: ")
	if player_name.replace(" ","") == "":
		doText = True
		name = True
	elif player_name == "Voldemort's Husband":
		cheat = True
		player_name = "Cheater"
		pattack = ["LAZARBEAM"]
if not cheat:
	print "\n" * 1000
	mindchange = True
	while mindchange:
		print "\n" * 1000
		mindchange = False
		selectingmonster = True
		while selectingmonster:
			print "\n" * 1000
			selectingmonster = False
			print ascii_fire,"Firemon", ascii_water,"Watermon", ascii_earth,"Earthmon"
			if doText:
				print "Error, invalid monster name."
				doText = False
			print("Well {player}, select a monster!".format(player = player_name))
			player_monster = raw_input("Monster name: ")
			player_monster = player_monster.lower()
			if player_monster == "firemon":
				player_monster = ascii_fire
				player_monster_name = "Firemon"
				ptype = "fire"
				gary_monster = ascii_water
				gary_monster_name = "Blastoise"
				Gtype = "water"
			elif player_monster == "watermon":
				player_monster = ascii_water
				player_monster_name = "Watermon"
				ptype = "water"
				gary_monster = ascii_earth
				gary_monster_name = "Venasaur"
				Gtype = "earth"
			elif player_monster == "earthmon":
				player_monster_name = "Earthmon"
				player_monster = ascii_earth
				ptype = "earth"
				gary_monster = ascii_fire
				gary_monster_name = "Charzard"
				Gtype = "fire"
			else:
				selectingmonster = True
				doText = True
		textinput = True
		while textinput:
			textinput = False
			print "\n" * 1000
			print player_monster
			if doText:
				print "Error, invalid response."
				doText = False
			print "Professor Ork: Are you sure you would like this monster?"
			YN = raw_input("Yes or No: ")
			YN = YN.lower()
			if YN == "no":
				mindchange = True
			elif YN != "yes":
				doText = True
				textinput = True
	rename = True
	already = False
if not cheat:
	while rename:
		rename = False
		print "\n" *1000
		print player_monster
		if doText:
			print "Error, invalid resonse."
			doText = False
		print "Professor Ork: you like to rename your mosnter: "
		YN = raw_input ("Yes or No: ")
		YN = YN.lower()
		if YN == "yes":
			rename = True
			while rename:
				rename = False
				monstername = True
				while monstername:
					monstername = False
					print "\n" * 1000
					print player_monster
					if doText:
						print "Error, please input your monster's name."
						doText = False
					player_monster_name = raw_input("Type in desired monster name: ")
					if player_monster_name.replace(" ","") == "":
						doText = True
						monstername = True
				print "\n" * 1000
				print player_monster
				print "Professor Ork: Would you like your monster to be called {name}?".format(name = player_monster_name)
				response = True
				while response:
					response = False
					if doText:
						print "\n" * 1000
						print player_monster
						print "Error, invalid response."
						print "Professor Ork: Would you like your monster to be called {name}?".format(name = player_monster_name)
						doText = False
					YN = raw_input("Yes or No: ")
					YN = YN.lower()
					if YN == "no":
						rename = True
					elif YN != "yes":
						doText = True
						response = True
		elif YN != "no":
			doText = True
			rename = True
print "\n"*1000
print "Gary: Hey! My name is Gary. I'm going to be your rival!"
response = raw_input("Press enter to continue.")
print "\n"*1000
print "Gary: My monster and I just finished defeating 10 other noob trainers!"
response = raw_input("Press enter to continue.")
print "\n"*1000
if not cheat:
	print "Gary: I see you chose a {ptype} monster. Well I choes a {gtype} monster just to kick your ass!".format(ptype = ptype, gtype = Gtype)
	response = raw_input("Press enter to continue.")
	print "\n"*1000
print "Gary: Prepare to be beaten!"
response = raw_input("Press enter to continue.")
nametext = True
alreadyattack = False
yourattack = 0
Gattacklist = ["Tackle"]
if cheat:
	level = 9999
	health = 9999
	defense = 9999
	attack = 9999
	luck = 9999
	player_monster_name = "Shoop Da Whoop"
	ptype = "water"
	player_monster = ascii_voldemort
	gmonster = ascii_fire
	gtype = "fire"
	gary_monster = ascii_fire
	gary_monster_name = "Charzard"
while health > 0 and Ghealth > 0:
	yourattack = 0
	while yourattack < 2:
		print "\n" *1000
		print gary_monster
		print "Health : {}".format(Ghealth)
		print player_monster
		print "Health : {}".format(health)
		if used:
			print "\n" * 1000
			Ghealth = 0
			print gary_monster
			print "Health : {}".format(Ghealth)
			print player_monster
			print "Health : {}".format(health)
			print "CHEATER'S monster used LAZARBEAM!"
			print "IT'S SUPER EFFECTIVE!"
			response = raw_input("Press enter to continue.")
			used = False
			can = False
		if yourattack == 1:
			if wascritical != None:
				print wascritical
			print "{yourmonster} did {damage} damage to {gmonster}! {effectiveness}".format(yourmonster = player_monster_name,damage = damage,gmonster = gary_monster_name, effectiveness = effectiveness)
			yourattack += 1
		if nametext:
			print "Gary chose {gmonster}. I choose you {pmonster}!".format(gmonster = gary_monster_name,pmonster = player_monster_name)
			nametext = False
		if doText:
			print "Error, invalid response."
			doText = False
			yourattack = 0
		if yourattack == 0 and can == True:
			print pattack
			attackchosen = raw_input("\nSelect an attack: ")
			attackchosen = attackchosen.lower()
			attacktracker = 0
			notattack = True
			while notattack:
				notattack = False
				if attackchosen != pattack[attacktracker].lower():
					if attacktracker < len(pattack)-1:
						attacktracker += 1
						notattack = True
					else:
						doText = True
				else:
					if cheat:
						used = True
						continue
					attackdone = eval(pattack[attacktracker])
					Ghealth = attackgary(attackdone,attack,ptype,luck,Gdefense,Gtype,Ghealth)
					yourattack = yourattack + 1
		if Ghealth <= 0 and used == False:
			can = True
			print "\n" * 1000
			print player_monster
			print "{gmonster} fainted.".format(gmonster = gary_monster_name)
			print "You won the fight!!!"
			response = raw_input("Press enter to continue.")
			time.sleep(1)
			print"."
			time.sleep(1)
			print"."
			time.sleep(1)
			print"."
			time.sleep(1)
			finishhim = True
			display = True
			while finishhim:
				print "\n" * 1000
				print"But would you like to finish him off?"
				finishhim = False
				if doText:
					print "Error, invalid response."
					doText = False
				YN = raw_input("Yes or No: ")
				YN = YN.lower()
				print "\n" * 1000
				if YN == "yes":
					kill = True
					print "You have killed your rival's monster..."
				elif YN == "no":
					print "You left without killing your rival's monster..."
					kill = False
				else:
					doText = True
					finishhim = True
			response = raw_input("Press enter to continue.")
			break
	display = True
	alreadygaryattack = False
	while yourattack == 2 and health > 0 and Ghealth > 0:
		if display:
			response = raw_input("Press enter to continue.")
			display = False
		print "\n" *1000
		print gary_monster
		print "Health : {}".format(Ghealth)
		print player_monster
		print "Health : {}".format(health)
		if alreadygaryattack:
			print "Gary uses tackle!"
			if wascritical != None:
				print wascritical
			print "{gmonster} did {damage} damage to {yourmonster}! {effectiveness}".format(gmonster = gary_monster_name, damage = damage, yourmonster = player_monster_name, effectiveness = effectiveness)
			response = raw_input("Press enter to continue.")
			yourattack = 0
		attackdone = eval(Gattacklist[0])
		if not alreadygaryattack:
			health = garyattack(attackdone,Gattack,Gtype,Gluck,defense,ptype,health)
			if health <= 0:
				print "\n" * 1000
				print gary_monster
				print "{yourmonster} fainted!".format(yourmonster = player_monster_name)
				print "You lost the fight!!!"
				response = raw_input("Press enter to continue.")
				print "\n" * 1000
				print "So {playername}, are you serious about defeating the evil king? You wouldn't last a second. See you later loser!".format(playername = player_name)
				response = raw_input("Press enter to continue.")
		alreadygaryattack = True
used = False
if health > 0 and not cheat:
	print "\n" * 1000
	print player_monster
	print "{yourmonster} gained 10 EXP!".format(yourmonster = player_monster_name)
	response = raw_input("Press enter to continue.")
	print "\n" * 1000
	print player_monster
	print "{yourmonster} leveled up!".format(yourmonster = player_monster_name)
	response = raw_input("Press enter to continue.")
	print "\n" * 1000
	print player_monster
	print "STATS"
	exp += 10
	level = 2
	print "Level : {level}\nHealth : {hi}\nAttack : {bye}\nDefense : {hi2}\nLuck : {bye2}\nEXP : {asdf}".format(level = 2,hi = maxhealth[1],bye = maxattack[1],hi2 = maxdefense[1],bye2 = level,asdf = exp)
	health = maxhealth[level - 1]
	attack = maxattack[level - 1]
	defense = maxdefense[level - 1]
	luck = level
	response = raw_input("Press enter to continue.")
	print "\n" * 1000
	print player_monster
	print "{yourmonster} learned \"scratch\"!".format(yourmonster = player_monster_name)
	pattack.append("Scratch")
elif health == 0:
	print "\n" * 1000
	print "Gary humiliates you horribly."
	killhim = True
	while killhim:
		killhim = False
		print "You have a knife in your pocket. Do you want to use your knife on {enemy}?".format(enemy = gary_monster_name)
		if doText:
			print "Error, invalid response."
			doText = False
		YN = raw_input("Yes or No: ")
		YN = YN.lower()
		print "\n" * 1000
		if YN == "yes":
			kill = True
			print "You backstabbed {garymonster} and it died.".format(garymonster = gary_monster_name)
		elif YN == "no":
			kill = False
			print "You left ashamed of yourself..."
		else:
			killhim = True
			doText = True
print "\n" * 1000
print "Professor Ork: Well how was your first battle? "
response = raw_input("Press enter to continue.")
print "\n" * 1000
print "Professor Ork: It must have been intense."
response = raw_input("Press enter to continue.")
print "\n" * 1000
print "Professor Ork: Just keep on training against other monsters, gain EXP, level up, and become powerful enough to defeat Voldemort!"
response = raw_input("Press enter to continue.")
print "\n" * 1000
print "Professor Ork: Once you become level 10, you will be given the chance to fight Voldemort."
response = raw_input("Press enter to continue.")
print "\n" * 1000
print "Professor Ork: I wish you good luck!!!"
response = raw_input("Press enter to continue.")
playing = True
notattack = False
while playing:
	menu = True
	voldemort = False
	train = False
	while menu:
		menu = False
		print "\n" * 1000
		print player_monster
		if not cheat:
			print "Level : {qwer}\nHealth : {hi}\nAttack : {bye}\nDefense : {hi2}\nLuck : {bye2}\nEXP : {asdf}".format(qwer = level,hi = maxhealth[1],bye = maxattack[1],hi2 = maxdefense[1],bye2 = level,asdf = exp)
		else:
			print "Level : 9999\nHealth : 9999\nAttack : 9999\n Defense : 9999\nLuck : 9999\nEXP : 9999"
		if doText:
			print "Error, invalid response."
		print "\n"
		if level >= 10:
			print "Type in \"Voldemort\" if you would like to battle him."
		print "Type in \"Train\" in order to train your monster against wild monsters!"
		print "Type in \"Quit\" in order to quit the game. WARNING: This game will NOT save your progress."
		nextaction = raw_input("Pick an action: ")
		nextaction = nextaction.lower()
		if nextaction == "quit":
			print "\n" *1000
			print "Thank you for playing my game!"
			response = raw_input("Press enter to continue.")
			sys.exit()
		if nextaction == "voldemort":
			voldemort = True
		elif nextaction == "train":
			train = True
		else:
			menu = True
			doText = True
	while train:
		if not cheat:
			health = maxhealth[level-1]
			e_health = health
		else:
			e_health = maxhealth[9]
		train = False
		hasselected = True
		if not cheat:
			if level >= 2:
				e_attack = maxattack[level-2]
				e_defense = maxdefense[level - 1]
				e_luck = level - 1
			else:
				e_attack = 10
				e_luck = 1
				e_defense = 1
		e_monster = random.sample(["firemon","watermon","earthmon"], 1)
		if e_monster[0] == "firemon":
			e_monster_art = ascii_fire
			e_monster_name = "Firemon"
			e_attacklist = ["Tackle","Scratch","Flamethrower","Fireball","Meteor","Volcano","Sun"]
			etype = "fire"
			if cheat:
				ptype = "water"
		elif e_monster[0] == "watermon":
			e_monster_art = ascii_water
			e_monster_name = "Watermon"
			e_attacklist = ["Tackle","Scratch","Watershot","Waterball","Waterbomb","Tsunami","Ocean"]
			etype = "water"
			if cheat:
				ptype = "earth"
		elif e_monster[0] == "earthmon":
			e_monster_art = ascii_earth
			e_monster_name = "Earthmon"
			e_attacklist = ["Tackle","Scratch","Mudshot","Mudball","Mudbomb","Earthquake","Earth"]
			etype = "earth"
			if cheat:
				ptype = "fire"
		nametext = True
		while health > 0 and e_health > 0:
			yourattack = 0
			while yourattack < 2:
				print "\n" *1000
				print e_monster_art
				print "Health : {}".format(e_health)
				print player_monster
				print "Health : {}".format(health)
				if used:
					print "\n" * 1000
					e_health = 0
					print e_monster_art
					print "Health : {}".format(e_health)
					print player_monster
					print "Health : {}".format(health)
					print "CHEATER'S monster used LAZARBEAM!"
					print "IT'S SUPER EFFECTIVE!"
					response = raw_input("Press enter to continue.")
					can = False
					used = False
				if yourattack == 1:
					if wascritical != None:
						print wascritical
					print "{yourmonster} did {damage} damage to {gmonster}! {effectiveness}".format(yourmonster = player_monster_name,damage = damage,gmonster = e_monster_name, effectiveness = effectiveness)
					yourattack += 1
				if nametext:
					print "A wild {gmonster} appeard! I choose you {pmonster}!".format(gmonster = e_monster_name,pmonster = player_monster_name)
					nametext = False
				if doText:
					print "Error, invalid response."
					yourattack = 0
					doText = False
				if yourattack == 0 and can == True:
					print pattack
					attackchosen = raw_input("\nSelect an attack: ")
					attackchosen = attackchosen.lower()
					attacktracker = 0
					notattack = True
					while notattack:
						notattack = False
						if attackchosen != pattack[attacktracker].lower():
							if attacktracker < len(pattack)-1:
								attacktracker += 1
								notattack = True
							else:
								doText = True
						else:
							if cheat:
								used = True
								continue
							attackdone = eval(pattack[attacktracker])
							e_health = enemyhealthafterhit(attackdone,attack,ptype,luck,e_defense,etype,e_health)
							yourattack += 1
				if e_health <= 0 and used == False:
					can = True
					print "\n" * 1000
					print player_monster
					print "{gmonster} fainted.".format(gmonster = e_monster_name)
					print "You won the fight!!!"
					response = raw_input("Press enter to continue.")
					break
			display = True
			alreadygaryattack = False
			while yourattack == 2 and health > 0 and e_health > 0:
				if display:
					response = raw_input("Press enter to continue.")
					display = False
				print "\n" *1000
				print e_monster_art
				print "Health : {}".format(e_health)
				print player_monster
				print "Health : {}".format(health)
				if alreadygaryattack:
					print "The wild {a} uses {b}!".format(a = e_monster_name, b = attackdone)
					if wascritical != None:
						print wascritical
					print "The wild {gmonster} did {damage} damage to {yourmonster}! {effectiveness}".format(gmonster = e_monster_name, damage = damage, yourmonster = player_monster_name, effectiveness = effectiveness)
					response = raw_input("Press enter to continue.")
					yourattack = 0
				number = random.randint(0,canuse)
				attackdone = e_attacklist[number]
				if not alreadygaryattack:
					health = yourhealthafterhit(eval(attackdone),e_attack,etype,e_luck,defense,ptype,health)
				alreadygaryattack = True
			if health <= 0:
				print "\n" * 1000
				print e_monster_art
				print "{yourmonster} fainted!".format(yourmonster = player_monster_name)
				print "You lost the fight!!!"
				response = raw_input("Press enter to continue.")
				print "\n" * 1000
				print "You fainted of humiliation..."
				response = raw_input("Press enter to continue.")
	if health > 0 and level < 10:
		print "\n" * 1000
		print player_monster
		print "{yourmonster} gained {hi} EXP!".format(yourmonster = player_monster_name,hi = level * 10)
		response = raw_input("Press enter to continue.")
		exp += level * 10
		if exp >= explist[level-1]:
			if exp > explist[9]:
				exp = "MAX"
			print "\n" * 1000
			print player_monster
			print "{yourmonster} leveled up!".format(yourmonster = player_monster_name)
			response = raw_input("Press enter to continue.")
			print "\n" * 1000
			print player_monster
			level += 1
			health = maxhealth[level-1]
			attack = maxattack[level-1]
			defense = maxdefense[level-1]
			luck = level
			print "STATS"
			print "Level : {level}\nHealth : {hi}\nAttack : {bye}\nDefense : {hi2}\nLuck : {bye2}".format(level = level,hi = maxhealth[1],bye = maxattack[1],hi2 = maxdefense[1],bye2 = level)
			response = raw_input("Press enter to continue.")
			print "\n" * 1000
			print player_monster
			if level == 2:
				print "{yourmonster} learned \"Scratch\"!".format(yourmonster = player_monster_name)
				pattack.append("Scratch")
			if level == 3 or level == 5 or level == 7 or level == 9 or level == 10:
				canuse += 1
				if ptype == "fire":
					print "{yourmonster} learned \"{attack}\"!".format(yourmonster = player_monster_name,attack = fireattack[level-4])
					pattack.append(fireattack[level])
				elif ptype == "water":
					print "{yourmonster} learned \"{attack}\"!".format(yourmonster = player_monster_name,attack = waterattack[level-4])
					pattack.append(waterattack[level])
				elif ptype == "earth":
					print "{yourmonster} learned \"{attack}\"!".format(yourmonster = player_monster_name,attack = earthattack[level-4])
					pattack.append(earthattack[level])
	while voldemort:
		voldemort = False
		if not cheat:
			if ptype == "fire":
				voldemort_type = "water"
			elif ptype == "water":
				voldemort_type = "earth"
			elif ptype == "earth":
				voldemort_type = "fire"
		else:
			ptype = "water"
			voldemort_type = "fire"
		print "\n" * 1000
		print "Voldemort: Hello {player}.".format(player = player_name)
		response = raw_input("Press enter to continue.")
		print "\n" * 1000
		print "Voldemort: I see you are here to try and defeat me..."
		response = raw_input("Press enter to continue.")
		print "\n" * 1000
		print "Voldemort: You don't know what you're getting yourself into..."
		response = raw_input("Press enter to continue.")
		print "\n" * 1000
		print "Voldemort: Prepare to DIE!"
		response = raw_input("Press enter to continue.")
		print "\n" * 1000
		if not cheat:
			health = maxhealth[level-1]
			voldemort_health = health
			voldemort_attack = maxattack[level - 1]
			voldemort_luck = level
			voldemort_defense = maxdefense[level - 2]
		else:
			voldemort_health = 1000
			voldemort_attack = maxattack[9]
			voldemort_luck = 10
			voldemort_defense = maxdefense[9]
		while health > 0 and voldemort_health > 0:
			yourattack = 0
			if not kill:
				print "\n" * 1000
				print "Gary rushes in through the door!!!"
				response = raw_input("Press enter to continue.")
				print "\n" * 1000
				print "Gary: Hey {player}!".format(player = player_name)
				response = raw_input("Press enter to continue.")
				print "\n" * 1000
				print "Gary: I remember that time when we fought, and you decided not to kill my monster!"
				response = raw_input("Press enter to continue.")
				print "\n" * 1000
				print "Gary: As a thank you, I'm going to help you defeat Voldemort!!!"
				response = raw_input("Press enter to continue.")
				print "\n" * 1000
				Ghealth = 50
				print ascii_voldemort
				print "Health : {}".format(voldemort_health)
				print gary_monster
				print "Health : {}".format(Ghealth)
				print "Voldemort chose Voldemon!"
				print "Gary chose {monster}!".format(monster = gary_monster_name)
				print "{monster} used sacrifice!".format(monster = gary_monster_name)
				if not cheat:
					print "It hit Voldemon's weakpoint!"
				else:
					print "It healed Voldemon by accident!!!"
				response = raw_input("Press enter to continue.")
				if not cheat:
					voldemort_attack = maxattack[level - 2]
					voldemort_luck = level - 2
					voldemort_defense = maxdefense[level - 4]
					voldemort_health = 750
				else:
					voldemort_health = 1000000000000
					voldemort_attack = 9999
					voldemort_luck = 30
					voldemort_defense = 9999
				print "\n" * 1000
				Ghealth = 0
				print ascii_voldemort
				print "Health : {}".format(voldemort_health)
				print gary_monster
				print "Health : {}".format(Ghealth)
				print "Voldemon used LAZARBEAM!"
				print "{gary} was killed!".format(gary = gary_monster_name)
				response = raw_input("Press enter to continue.")
				print "\n" * 1000
				if not cheat:
					print "Gary: {player}! You better not let my monster's death be wasted!"
				else:
					print "Gary: Whoopsie! Good luck fighting Voldemort Cheater."
				response = raw_input("Press enter to continue.")
			while yourattack < 2:	
				print "\n" *1000
				print ascii_voldemort
				print "Health : {}".format(voldemort_health)
				print player_monster
				print "Health : {}".format(health)
				if used:
					print "\n" * 1000
					voldemort_health = 0
					print ascii_voldemort
					print "Health : {}".format(voldemort_health)
					print player_monster
					print "Health : {}".format(health)
					print "CHEATER'S monster used LAZARBEAM!"
					print "IT'S SUPER EFFECTIVE!"
					response = raw_input("Press enter to continue.")
					can = False
					used = False
				if yourattack == 1:
					if wascritical != None:
						print wascritical
					print "{yourmonster} did {damage} damage to Voldemon! {effectiveness}".format(yourmonster = player_monster_name,damage = damage, effectiveness = effectiveness)
					yourattack += 1
				if nametext:
					print "Voldemort chose Voldemon! I choose you {pmonster}!".format(pmonster = player_monster_name)
					nametext = False
				if doText:
					print "Error, invalid response."
					yourattack = 0
					doText = False
				if yourattack == 0 and can == True:
					print pattack
					attackchosen = raw_input("\nSelect an attack: ")
					attackchosen = attackchosen.lower()
					attacktracker = 0
					notattack = True
					while notattack:
						notattack = False
						if attackchosen != pattack[attacktracker].lower() and attackdone != None:
							if attacktracker < len(pattack)-1:
								attacktracker += 1
								notattack = True
							else:
								doText = True
						else:
							if cheat:
								used = True
								continue
							attackdone = eval(pattack[attacktracker])
							voldemort_health = enemyhealthafterhit(attackdone,attack,ptype,luck,voldemort_defense,voldemort_type,voldemort_health)
							yourattack += 1
							attackdone = None
				if voldemort_health <= 0 and used == False:
					can = True
					print "\n" * 1000
					print player_monster
					print "Voldemon fainted."
					print "You won the fight!!!"
					response = raw_input("Press enter to continue.")
					break
			display = True
			alreadygaryattack = False
			while yourattack == 2 and health > 0 and voldemort_health > 0:
				if display:
					response = raw_input("Press enter to continue.")
					display = False
				print "\n" *1000
				print ascii_voldemort
				print "Health : {}".format(voldemort_health)
				print player_monster
				print "Health : {}".format(health)
				if alreadygaryattack:
					print "Voldemon uses LAZARBEAM!"
					if wascritical != None:
						print wascritical
					print "Voldemon did {damage} damage to {yourmonster}! {effectiveness}".format(damage = damage, yourmonster = player_monster_name, effectiveness = effectiveness)
					response = raw_input("Press enter to continue.")
					yourattack = 0
				attackdone = "LAZAR_BEAM"
				if not alreadygaryattack:
					health = yourhealthafterhit(eval(attackdone),voldemort_attack,voldemort_type,voldemort_luck,defense,ptype,health)
				alreadygaryattack = True
			if health <= 0:
				print "\n" * 1000
				print ascii_voldemort
				print "{yourmonster} fainted!".format(yourmonster = player_monster_name)
				print "You lost the fight!!!"
				response = raw_input("Press enter to continue.")
				print "\n" * 1000
				print "VOLDEMORT IS ABOUT TO KILL YOU"
				response = raw_input("Press enter to continue.")
				rewind = True
				while rewind:
					rewind = False
					print "\n" * 1000
					if doText == True:
						print "Error, invalid response."
						doText = False
					print "Would you like to rewind time before the battle?"
					YN = raw_input("Yes or No: ")
					YN = YN.lower()
					print "\n" * 1000
					if YN == "yes":
						voldemort = True
					elif YN == "no":
						print "Voldemort killed you and your monster."
						response = raw_input("Press enter to continue.")
						print "\n" * 1000
						print "Thank you for playing my game!"
						sys.exit()
					else:
						doText = True
						rewind = True
		if not voldemort:
			print "\n" * 1000
			print "Professor Ork: Wow {player}! You were able to defeat Voldemort!".format(player = player_name)
			response = raw_input("Press enter to continue.")
			print "\n" * 1000
			print "Professor Ork: Thank you so much for saving the world!"
			response = raw_input("Press enter to continue.")
			print "\n" * 1000
			print "Professor Ork: You will now be given the title \"Ruler of the World\"!"
			response = raw_input("Press enter to continue.")
			print "\n" * 1000
			print "Congratulations, you beat the monster training game!"
			response = raw_input("Press enter to continue.")
			print "\n" * 1000
			print "You will now be given the cheat code to unlock a powerful monster!"
			response = raw_input("Press enter to continue.")
			print "\n" * 1000
			print "When prompted your name, type in \"Voldemort's Husband\"."
			response = raw_input("Press enter to continue.")
			print "\n" * 1000
			print "Thank you so much for playing my game!"
			response = raw_input("Press enter to continue.")
			sys.exit()
		else:
			print "\n" * 1000
			print "Congratulations. You simply cheated."
			print "PLAY THE GAME LEGIT :P"
			sys.exit()