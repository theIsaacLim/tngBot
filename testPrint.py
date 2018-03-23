from json import loads

file = open("dumped.json")
loaded = loads(file.read())
file.close()

for thing in loaded:
    if thing['type'] == 'stageDir':
        print(thing['line'])
        print("\n")
    if thing['type'] == 'charLine':
        print(thing['speaker'] + ":  " + thing['line'])
