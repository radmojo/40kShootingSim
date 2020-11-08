import random
import numpy as N

dump = list()
dump2 = list()
averageROI = list()

# dice parsing substrings
substringd6 = "d6"
substringd3 = "d3"
substringPlus = "+"

#d6 function
def roll6():
	d6 = random.randrange(1,6,1)
	return d6


# d3 function
def roll3():
	d3 = random.randrange(1,3,1)
	return d3

# shooting function
def shooting():
	global shots
	global bSkill
	global strength
	global armorPierce
	global damage
	global rerollHits
	global rerollWounds
	shotsRolled = 0
	shotsConstant = 0
	shotsVarFinal = 0
	if substringPlus in shots:
		if substringd6 in shots:
			shotsParse = shots.split("+")
			shotsConstant = shotsParse[0]
			shotsVariable = shotsParse[1]
			shotsConstant = int(shotsConstant)
			shotsVarSplit = shotsVariable.split("d")
			shotsVarInt = shotsVarSplit[0]
			shotsVarInt = int(shotsVarInt)
			while (shotsRolled < shotsVarInt):
				shotsVarFinal += roll6()
				shotsRolled += 1
		elif substringd3 in shots:
			shotsParse = shots.split("+")
			shotsConstant = shotsParse[0]
			shotsVariable = shotsParse[1]
			shotsConstant = int(shotsConstant)
			shotsVarSplit = shotsVariable.split("d")
			shotsVarInt = shotsVarSplit[0]
			shotsVarInt = int(shotsVarInt)
			while (shotsRolled < shotsVarInt):
				shotsVarFinal += roll3()
				shotsRolled += 1
	elif substringd6 in shots:
		shotsVariable = shots.split("d")
		shotsVarInt = shotsVariable[0]
		shotsVarInt = int(shotsVarInt)
		while (shotsRolled < shotsVarInt):
			shotsVarFinal += roll6()
			shotsRolled += 1
	elif substringd3 in shots:
		shotsVariable = shots.split("d")
		shotsVarInt = shotsVariable[0]
		shotsVarInt = int(shotsVarInt)
		while (shotsRolled < shotsVarInt):
			shotsVarFinal += roll3()
			shotsRolled += 1
	else:
		shotsConstant = int(shots)

	shotsFinal = shotsConstant + shotsVarFinal

# to hit sim
	hitsAttempt = 0
	hitsMade = 0
	hitRolls = N.random.randint(1,7,shotsFinal)
	if rerollHits == "1s":
		rerollHitsQuant = N.count_nonzero(hitRolls == 1)
		rerolledHits = N.random.randint(1,7,rerollHitsQuant)
		hitRolls = hitRolls[hitRolls != 1]
		hitRolls = N.concatenate((hitRolls,rerolledHits), axis=None)
	if rerollHits == "all":
		rerollHitsQuant = N.count_nonzero(hitRolls < bSkill)
		rerolledHits = N.random.randint(1,7,rerollHitsQuant)
		hitRolls = hitRolls[hitRolls >= bSkill]
		hitRolls = N.concatenate((hitRolls,rerolledHits), axis=None)
	hitRolls = hitRolls[hitRolls >= bSkill]

# to wound sim
	woundsAttempt = 0
	woundsMade = 0
	if strength >= 2 * toughness:
		woundCheck = 2
	elif strength > toughness and strength < 2 * toughness:
		woundCheck = 3
	elif strength == toughness:
		woundCheck = 4
	elif toughness > strength and toughness < 2 * strength:
		woundCheck = 5
	else:
		woundCheck = 6
	woundRolls = N.random.randint(1,7,hitRolls.size)
	if rerollWounds == "1s":
		rerollWoundsQuant = N.count_nonzero(woundRolls == 1)
		rerolledWounds = N.random.randint(1,7,rerollWoundsQuant)
		woundRolls = woundRolls[woundRolls != 1]
		woundRolls = N.concatenate((woundRolls,rerolledWounds), axis=None)
	if rerollWounds == "all":
		rerollWoundsQuant = N.count_nonzero(woundRolls < woundCheck)
		rerolledWounds = N.random.randint(1,7,rerollWoundsQuant)
		woundRolls = woundRolls[woundRolls >= woundRolls]
		woundRolls = N.concatenate((woundRolls,rerolledWounds), axis=None)
	woundRolls = woundRolls[woundRolls >= woundCheck]

# save sim
	savesAttempt = 0
	savesFail = 0
	saveReal = save + armorPierce
	if invuln > 1 and invuln < 7 and invuln <= saveReal:
		saveRolls = N.random.randint(1,7,woundRolls.size)
		saveRolls = saveRolls[saveRolls < invuln]
	elif saveReal < 7:
		saveRolls = N.random.randint(1,7,woundRolls.size)
		saveRolls = saveRolls[saveRolls < saveReal]
	else:
		saveRolls = woundRolls
	savesFail = saveRolls.size

# damage module
	deadModels = 0
	damageRolled = 0
	if substringPlus in damage:
		if substringd6 in damage:
			damageParse = damage.split("+")
			damageConstant = damageParse[0]
			damageConstant = int(damageConstant)
			damageVarFinal = roll6()
		elif substringd3 in damage:
			damageParse = damage.split("+")
			damageConstant = damageParse[0]
			damageConstant = int(damageConstant)
			damageVarFinal = roll3()
	elif substringd6 in damage:
		damageSplit = damage.split("d")
		if len(damageSplit[0]) == 0:
			damageVarFinal = roll6()
			damageConstant = 0
		else:
			damageVar = int(damageSplit[0])
			while (damageRolled < damageVar):
				damageVarFinal += roll6()
				damageRolled += 1
	elif substringd3 in damage:
		damageSplit = damage.split("d")
		if len(damageSplit[0]) == 0:
			damageVarFinal = roll3()
			damageConstant = 0
		else:
			damageVar = int(damageSplit[0])
			while (damageRolled < damageVar):
				damageVarFinal += roll3()
				damageRolled += 1
	else:
		damageConstant = int(damage)
		damageVarFinal = 0
	damage = damageConstant + damageVarFinal
	while (savesFail > 0):
		currentModel = wounds
		while currentModel > 0:
			damageLeft = damage
			if FNPBool == True and damageLeft > 0:
				if FNP > roll6():
					currentModel -= 1
					damageLeft -= 1
			else:
				currentModel -= damage
		savesFail -= 1
		deadModels += 1

	return deadModels


# weapon init
weapon0 = [0,1,2,3,4]
weapon1 = [0,1,2,3,4]
weapon2 = [0,1,2,3,4]
weapon3 = [0,1,2,3,4]
weapon4 = [0,1,2,3,4]
weapon5 = [0,1,2,3,4]
weapon6 = [0,1,2,3,4]
weapon7 = [0,1,2,3,4]
weapon8 = [0,1,2,3,4]
weapon9 = [0,1,2,3,4]

totalIterations = 0
weapons = int(input("Number of weapon profiles (Max 10): "))
atkPoints = int(input("Attacker Unit Points: "))



weapon0[0] = input("Number of attacks: ")
weapon0[1] = input("BS: ")
weapon0[2] = input("Strength: ")
weapon0[3] = input("AP absolute value: ")
weapon0[4] = input("Damage: ")
weapon0RerollHits = input("Reroll hits? (n/1s/all)")
weapon0RerollWounds = input("Reroll wounds? (n/1s/all)")

if weapons >= 2:
	weapon1[0] = input("Number of attacks for weapon 2: ")
	weapon1[1] = input("BS: ")
	weapon1[2] = input("Strength: ")
	weapon1[3] = input("AP absolute value: ")
	weapon1[4] = input("Damage: ")
	weapon1RerollHits = input("Reroll hits? (n/1s/all)")
	weapon1RerollWounds = input("Reroll wounds? (n/1s/all)")
if weapons >= 3:
	weapon2[0] = input("Number of attacks for weapon 3: ")
	weapon2[1] = input("BS: ")
	weapon2[2] = input("Strength: ")
	weapon2[3] = input("AP absolute value: ")
	weapon2[4] = input("Damage: ")
	weapon2RerollHits = input("Reroll hits? (n/1s/all)")
	weapon2RerollWounds = input("Reroll wounds? (n/1s/all)")
if weapons >= 4:
	weapon3[0] = input("Number of attacks for weapon 4: ")
	weapon3[1] = input("BS: ")
	weapon3[2] = input("Strength: ")
	weapon3[3] = input("AP absolute value: ")
	weapon3[4] = input("Damage: ")
	weapon3RerollHits = input("Reroll hits? (n/1s/all)")
	weapon3RerollWounds = input("Reroll wounds? (n/1s/all)")
if weapons >= 5:
	weapon4[0] = input("Number of attacks for weapon 5: ")
	weapon4[1] = input("BS: ")
	weapon4[2] = input("Strength: ")
	weapon4[3] = input("AP absolute value: ")
	weapon4[4] = input("Damage: ")
	weapon4[5] = input("Reroll hits? (n/1s/all)")
	weapon4RerollWounds = input("Reroll wounds? (n/1s/all)")
if weapons >= 6:
	weapon5[0] = input("Number of attacks for weapon 6: ")
	weapon5[1] = input("BS: ")
	weapon5[2] = input("Strength: ")
	weapon5[3] = input("AP absolute value: ")
	weapon5[4] = input("Damage: ")
	weapon5RerollHits = input("Reroll hits? (n/1s/all)")
	weapon5RerollWounds = input("Reroll wounds? (n/1s/all)")
if weapons >= 7:
	weapon6[0] = input("Number of attacks for weapon 7: ")
	weapon6[1] = input("BS: ")
	weapon6[2] = input("Strength: ")
	weapon6[3] = input("AP absolute value: ")
	weapon6[4] = input("Damage: ")
	weapon6RerollHits = input("Reroll hits? (n/1s/all)")
	weapon6RerollWounds = input("Reroll wounds? (n/1s/all)")
if weapons >= 8:
	weapon7[0] = input("Number of attacks for weapon 8: ")
	weapon7[1] = input("BS: ")
	weapon7[2] = input("Strength: ")
	weapon7[3] = input("AP absolute value: ")
	weapon7[4] = input("Damage: ")
	weapon7RerollHits = input("Reroll hits? (n/1s/all)")
	weapon7RerollWounds = input("Reroll wounds? (n/1s/all)")
if weapons >= 9:
	weapon8[0] = input("Number of attacks for weapon 9: ")
	weapon8[1] = input("BS: ")
	weapon8[2] = input("Strength: ")
	weapon8[3] = input("AP absolute value: ")
	weapon8[4] = input("Damage: ")
	weapon8RerollHits = input("Reroll hits? (n/1s/all)")
	weapon8RerollWounds = input("Reroll wounds? (n/1s/all)")
if weapons == 10:
	weapon9[0] = input("Number of attacks for weapon 10: ")
	weapon9[1] = input("BS: ")
	weapon9[2] = input("Strength: ")
	weapon9[3] = input("AP absolute value: ")
	weapon9[4] = input("Damage: ")
	weapon9RerollHits = input("Reroll hits? (n/1s/all)")
	weapon9RerollWounds = input("Reroll wounds? (n/1s/all)")

weaponTicker = 1
totalDeadModels = 0

toughness = int(input("Toughness: "))
wounds = int(input("Wounds: "))
save = int(input("Armor Save: "))
invuln = int(input("Invuln Save or 0: "))
FNP = int(input("FNP or 0: "))
defPoints = int(input("Defender Model Points: "))
iteration = int(input("Amount of iterations: "))

if FNP > 1 and FNP < 7:
	FNPBool = True
else:
	FNPBool = False
# parse shots


while (totalIterations < iteration):
	while (weaponTicker <= weapons):
		if weaponTicker == 1:
			shots = weapon0[0]
			bSkill = int(weapon0[1])
			strength = int(weapon0[2])
			armorPierce = int(weapon0[3])
			damage = weapon0[4]
			rerollHits = weapon0RerollHits
			rerollWounds = weapon0RerollWounds

		elif weaponTicker == 2:
			shots = weapon1[0]
			bSkill = int(weapon1[1])
			strength = int(weapon1[2])
			armorPierce = int(weapon1[3])
			damage = weapon1[4]
			rerollHits = weapon1RerollHits
			rerollWounds = weapon1RerollWounds
		elif weaponTicker == 3:
			shots = weapon2[0]
			bSkill = int(weapon2[1])
			strength = int(weapon2[2])
			armorPierce = int(weapon2[3])
			damage = weapon2[4]
			rerollHits = weapon2RerollHits
			rerollWounds = weapon2RerollWounds
		elif weaponTicker == 4:
			shots = weapon3[0]
			bSkill = int(weapon3[1])
			strength = int(weapon3[2])
			armorPierce = int(weapon3[3])
			damage = weapon3[4]
			rerollHits = weapon3RerollHits
			rerollWounds = weapon3RerollWounds
		elif weaponTicker == 5:
			shots = weapon4[0]
			bSkill = int(weapon4[1])
			strength = int(weapon4[2])
			armorPierce = int(weapon4[3])
			damage = weapon4[4]
			rerollHits = weapon4RerollHits
			rerollWounds = weapon4RerollWounds
		elif weaponTicker == 6:
			shots = weapon5[0]
			bSkill = int(weapon5[1])
			strength = int(weapon5[2])
			armorPierce = int(weapon5[3])
			damage = weapon5[4]
			rerollHits = weapon5RerollHits
			rerollWounds = weapon5RerollWounds
		elif weaponTicker == 7:
			shots = weapon6[0]
			bSkill = int(weapon6[1])
			strength = int(weapon6[2])
			armorPierce = int(weapon6[3])
			damage = weapon6[4]
			rerollHits = weapon6RerollHits
			rerollWounds = weapon6RerollWounds
		elif weaponTicker == 8:
			shots = weapon7[0]
			bSkill = int(weapon7[1])
			strength = int(weapon7[2])
			armorPierce = int(weapon7[3])
			damage = weapon7[4]
			rerollHits = weapon7RerollHits
			rerollWounds = weapon7RerollWounds
		elif weaponTicker == 9:
			shots = weapon8[0]
			bSkill = int(weapon8[1])
			strength = int(weapon8[2])
			armorPierce = int(weapon8[3])
			damage = weapon8[4]
			rerollHits = weapon8RerollHits
			rerollWounds = weapon8RerollWounds
		elif weaponTicker == 10:
			shots = weapon9[0]
			bSkill = int(weapon9[1])
			strength = int(weapon9[2])
			armorPierce = int(weapon9[3])
			damage = weapon9[4]
			rerollHits = weapon9RerollHits
			rerollWounds = weapon9RerollWounds
		totalDeadModels += shooting()
		weaponTicker += 1
	weaponTicker = 1
	pointsKilled = totalDeadModels * defPoints
	ROI = pointsKilled / atkPoints
	averageROI.append(ROI)
	ROI = "{:.2f}".format(ROI)
	dump.append(ROI)
	totalIterations += 1
	totalDeadModels = 0

meanROI = sum(averageROI) / len(averageROI)

devArr = N.array(averageROI)
devArr = devArr - meanROI
devArr = devArr * devArr
dev = iteration - 1
stDev = N.sum(devArr) / dev
stDev = N.sqrt(stDev)
print(stDev)


simResults=open('simResults.txt','w')

for element in dump:
     simResults.write(element)
     simResults.write('\n')
simResults.close()
