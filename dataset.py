import csv
from json import dumps

outPath = "dumped.json"
writeLs = []
lastSpeaker = "NA"
"""
lineTemplate = {"type": "charLine",
                "line": "linee",
                "speaker": "speker",
                "prevLine": "previousLine"}

stageTemplate = {"type": "charLine",
                 "line": "linee",
                 "prevLine": "previousLine"}
"""


def convertLine(originLineDict, prevLineDict):
    global lastSpeaker
    rVal = {}
    rVal['type'] = 'charLine'
    rVal["line"] = originLineDict["text"]
    if originLineDict["who"] == "NA":
        return convertStageDir(originLineDict, prevLineDict)
    else:
        rVal["speaker"] = originLineDict["who"]

    if lastRow is not None:
        rVal["prevLine"] = prevLineDict["text"]
    else:
        rVal["prevLine"] = None
    lastSpeaker = rVal["speaker"]
    return rVal


def convertStageDir(originStageDict, prevLineDict):
    rVal = {}
    rVal['type'] = 'stageDir'
    rVal["line"] = originStageDict["text"]
    if lastRow is not None:
        rVal["prevLine"] = prevLineDict["text"]
    else:
        rVal["prevLine"] = None
    return rVal

lastRow = None
with open("TNG.csv", 'r', encoding='utf-8', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        if row['type'] == "speech":
            writeLs.append(convertLine(row, lastRow))

        if row['type'] == 'description':
            writeLs.append(convertLine(row, lastRow))
        lastRow = row

file = open(outPath, "w")
file.write(dumps(writeLs))
file.close()
