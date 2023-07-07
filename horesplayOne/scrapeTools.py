import json
import random
#Strip down js string/window data, convert it to json to then return a value from a particular key
#Section references a key with an array and index is used to acess that array.
def jsStripper (jscript, key,section=0,index=0):
	start = jscript.find('= ')
	end = jscript.find('}};')

	scriptStripped = jscript[start + 2:end + 2]

	hdjson = json.loads(scriptStripped)

	if section == 0:
		return hdjson[key]
	else:
		section = hdjson[section]		
		return section[index][key] 

"""USAGE EXAMPLE
#jsstring ='<script>\n        window.horseData = {"raceId":"838455","raceTypeCode":"C","items":[{"outcomeCode":"1","accumLengthNative":null,"wgtStNative":165,"wgtAllowance":0,"wfaAdjustment":0,"runnerInfo":{"horseId":2346169}},{"outcomeCode":"2","accumLengthNative":0.3,"wgtStNative":157,"wgtAllowance":0,"wfaAdjustment":0,"runnerInfo":{"horseId":2548199}},{"outcomeCode":"3","accumLengthNative":24.3,"wgtStNative":166,"wgtAllowance":0,"wfaAdjustment":0,"runnerInfo":{"horseId":2653173}},{"outcomeCode":"4","accumLengthNative":26.3,"wgtStNative":164,"wgtAllowance":0,"wfaAdjustment":0,"runnerInfo":{"horseId":903220}},{"outcomeCode":"5","accumLengthNative":27.8,"wgtStNative":156,"wgtAllowance":0,"wfaAdjustment":0,"runnerInfo":{"horseId":1965936}},{"outcomeCode":"PU","accumLengthNative":null,"wgtStNative":167,"wgtAllowance":0,"wfaAdjustment":0,"runnerInfo":{"horseId":1967593}}],"generalInfo":{"length":1}};\n    </script>'

#awnser =  jsStripper(jsstring,"wgtStNative",'items',1)
#awnser2 = jsStripper(jsstring,'raceId')
#print(awnser)
#Print(awnser2)
"""
def wgtStripper(wgtString):
	start = wgtString.find('wgt="')
	end = wgtString.find('">\n')
	return wgtString[start + 5:end]

def randomJsonSample(jsonFile):
	with open(jsonFile,'r') as f:
		data = json.load(f)

	for i in range(10):
		print(random.choice(data))
		print('')

def quickJson(jsonFile):
	with open(jsonFile,'r') as f:
		data = json.load(f)
	return data

def raceTypeGet(title):
	B = ["inh flat", "national hunt flat","bumper"]
	C = []
	H = []
	U = []
	X = []
	if title.lower() in B: 
		return 'B'
	elif title.lower() in C:
		return 'C'
	elif title.lower() in H:
		return 'H'
	elif title.lower() in U:
		return 'U'
	elif title.lower() in X:
		return 'X'
	else:
		return 'F'