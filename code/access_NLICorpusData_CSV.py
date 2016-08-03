import csv
from collections import defaultdict

source = '../data/NLICorpusData.csv'
numEntries = 1583
table_LoD = [None for i in range(numEntries)]
table_DoL = defaultdict(lambda: [None] * numEntries)

def initDataStructs():
    """
    Opens and parses CSV, creates two data structures, and populates them.
    Creates 'List of Dictionaries' and 'Dictionary of Lists' for ease of access.

    Example for LoD: table_LoD[77] will access the dictionary of fields for the instruction which corresponds to Index field 77.

    Examples for DoL: table_DoL['Description'] will access a list of all descriptions.
                      table_DoL['Description'][77] will access the Description which corresponds to Index field 77.


    keys available:
        Instruction:            Given by participant as response to prompt
        Index:                  Corresponds to individual instruction
        Scenario:               Configuration by image and variation
        AgentType:              Agent participant is instructing
        Difficulty:             Rating for a scenario given by participant
        TimeToComplete:         Duration participant took to create instruction
        Strategy:               Comments on strategy for used
        Challenging:            Comments on overall study difficulty
        GeneralComments:        Comments on general on overall study
        Age:                    Age of participant
        Gender:                 Gender of participant
        Occupation:             Occupation of participant
        ComputerUsage:          Duration participant uses a computer per week
        DominantHand:           Dominant hand of participant
        EnglishAsFirst:         Participant's first language
        ExpWithRobots:          Participant experience with robots
        ExpWithRCCars:          Participant experience with RC cars
        ExpWithFPS:             Participant experience with first-person shooter video games
        ExpWithRTS:             Participant experience with real-time strategy video games
        ExpWithRobotComments:   Comments on experience with robots
        InternalUserID:         Particpant ID in study 1 unaffiliated with Amazon ID
    """

    with open(source) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            table_LoD[int(row['Index'])] = row
            for k in row.keys():
                table_DoL[k][int(row['Index'])] = row[k]

initDataStructs()

print len(table_DoL['Index'])
print len(table_LoD)

print table_LoD[77]

# entire data entry from 77 to 79
print table_LoD[77:80]
print table_LoD[77]['Instruction']
print table_DoL['Instruction']
print table_DoL['Instruction'][77]

# description from entry 77 to 79
print table_DoL['Instruction'][77:80]

