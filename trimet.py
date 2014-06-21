import json, xmltodict

# PROBLEM: We are reading in a large KML (XML-based) file. We need to retrieve the stop ID and names, with no repeats

def outputThings(_, data):
	stopid = int(data['ExtendedData']['Data'][6]['value'])
	stopname = data['ExtendedData']['Data'][7]['value']
	stopdirection = data['ExtendedData']['Data'][3]['value']

	if stopid not in stopinfo.keys():
		stopinfo[stopid] = ( stopname, stopdirection )
		
	return True

f = open('tm_route_stops.kml')
stopinfo = {}

xmltodict.parse(f.read(), item_depth=3, item_callback=outputThings)

print json.dumps(stopinfo, sort_keys=True, indent=2)

f.close()