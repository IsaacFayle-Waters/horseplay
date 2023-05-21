import json

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

#jsstring ='<script>\n        window.horseData = {"raceId":"838455","raceTypeCode":"C","items":[{"outcomeCode":"1","accumLengthNative":null,"wgtStNative":165,"wgtAllowance":0,"wfaAdjustment":0,"runnerInfo":{"horseId":2346169}},{"outcomeCode":"2","accumLengthNative":0.3,"wgtStNative":157,"wgtAllowance":0,"wfaAdjustment":0,"runnerInfo":{"horseId":2548199}},{"outcomeCode":"3","accumLengthNative":24.3,"wgtStNative":166,"wgtAllowance":0,"wfaAdjustment":0,"runnerInfo":{"horseId":2653173}},{"outcomeCode":"4","accumLengthNative":26.3,"wgtStNative":164,"wgtAllowance":0,"wfaAdjustment":0,"runnerInfo":{"horseId":903220}},{"outcomeCode":"5","accumLengthNative":27.8,"wgtStNative":156,"wgtAllowance":0,"wfaAdjustment":0,"runnerInfo":{"horseId":1965936}},{"outcomeCode":"PU","accumLengthNative":null,"wgtStNative":167,"wgtAllowance":0,"wfaAdjustment":0,"runnerInfo":{"horseId":1967593}}],"generalInfo":{"length":1}};\n    </script>'


#awnser =  jsStripper(jsstring,"wgtStNative",'items',0)
#awnser2 = jsStripper(jsstring,'raceId')
#print(awnser)
#rint(awnser2)



