import requests, json
from datetime import datetime

def getGenders(names):
	url = ""
	cnt = 0
	if not isinstance(names,list):
		names = [names,]

	for name in names:
		if url == "":
			url = "name[0]=" + name
		else:
			cnt += 1
			url = url + "&name[" + str(cnt) + "]=" + name


	req = requests.get("https://api.genderize.io?" + url)
	results = json.loads(req.text)

	retrn = []
	for result in results:
		if result["gender"] is not None:
			retrn.append((result["gender"], result["probability"], result["count"]))
		else:
			retrn.append((u'None',u'0.0',0.0))
	return retrn

sessionfilename = "gender_output_" + str(datetime.today()) + ".csv"

with open('names.csv', 'r') as f:
    imported_names = list(f)

#clean up the names
for i in range(len(imported_names)):
    temp = imported_names[i]
    imported_names[i] = temp.strip('\n')
print("Imported names successfully.")


for i in range(len(imported_names)):
	temp = imported_names[i]
	gender_data = getGenders(temp)
	# print(gender_data)

	print(str(temp + ", " + str(gender_data[0][0]) + ", " + str(gender_data[0][1])))
	print(str(i) + " out of " + str(len(imported_names)))

	with open(sessionfilename, 'a') as f:
		f.write(str(temp + ", " + str(gender_data[0][0]) + ", " + str(gender_data[0][1]) + "\n"))



print('All names assessed and saved.')
# print(getGenders(imported_names))
