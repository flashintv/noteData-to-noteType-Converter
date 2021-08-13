import re
import json
import math
import sys
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def greenConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'color 2'
    os.system(command)

clearConsole()
greenConsole()
print('Welcome to \'vs. Tricky\' chart converter!')
input('Press ENTER to begin!')
clearConsole()
    
jsonName = input('What\'s the name of the json (without .json): ')
clearConsole()
noteType = input('What do you want to turn the above 7 noteData to? (basically note type): ')

infile = f'json/{jsonName}.json'
chart_jsons = []

with open(infile, "r") as chartfile:
	chart_json = json.loads(chartfile.read().strip('\0'))
	chart_jsons.append(chart_json)

for chart_json in chart_jsons:
    song_notes = chart_json["song"]["notes"]
    num_sections = len(song_notes)

def convertSections(noteType):
    for i in range(num_sections):
        section = song_notes[i]
        section_notes = section["sectionNotes"]
        for section_note in section_notes:
            note = section_note[1]
            if section["mustHitSection"]:
                    note = (note + 4) % 8
            length = section_note[2]
            if note > 7:
                note -= 8
                section_note[1] = note
                section_note.append(noteType)

convertSections(noteType)

global value
global valueAdder
value = 0
valueAdder = '(0)';

def recheckValue():
    global value
    global valueAdder
    valueAdder = f'({value})';
    if os.path.isfile(f"./outputs/{jsonName}-output" + valueAdder + '.json'):
        value += 1
        recheckValue()

recheckValue()
a_file = open(f"outputs/{jsonName}-output" + valueAdder + '.json', "w")
json.dump(chart_json, a_file)
a_file.close()

clearConsole()
fileName = f"{jsonName}-output" + valueAdder + '.json'
print('The JSON has been successfully converted!')
print(f'The JSON has been saved under a name \'{fileName}\' in the in the \'output\' folder!')
input('Press ENTER to exit the program...')