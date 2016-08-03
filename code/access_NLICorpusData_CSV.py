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

    Example for LoD: table_LoD[277] will access the dictionary of fields for the instruction which corresponds to Index field 277.

    Examples for DoL: table_DoL['Instruction'] will access a list of all instructions.
                      table_DoL['Instruction'][277] will access the instruction which corresponds to Index field 277.


    Keys Available:
    Per Instruction:
        Instruction:            Given by participant as response to prompt
        Index:                  Corresponds to individual instruction
        Scenario:               Configuration by image and variant of image
        AgentType:              Agent participant is instructing
        Difficulty:             Rating for a scenario given by participant
        TimeToComplete:         Duration participant took to create instruction
    Per Particpant (multiple instructions will have same entries for these fields):
        Strategy:               Participant comments on strategy used in answering prompt
        Challenging:            Participant comments on overall study difficulty
        GeneralComments:        Participant comments in general on overall study
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
        ExpWithRobotComments:   Participant comments on experience with robots
        InternalUserID:         Particpant ID in study 1 unaffiliated with Amazon ID
    """

    with open(source) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            table_LoD[int(row['Index'])] = row
            for k in row.keys():
                table_DoL[k][int(row['Index'])] = row[k]

initDataStructs()

# note these lengths are the number of Instructions and should be equivalent
print len(table_DoL['Index'])
print len(table_LoD)

# table entry for instruction @ Index #277
print table_LoD[277]

# table entries for instructions from Index #277 to #279
print table_LoD[277:280]

# just the instruction @ Index #277
print table_LoD[277]['Instruction']
print table_DoL['Instruction'][277]

# all entries in the Instruction field 
print table_DoL['Instruction']

# instructions from Index #277 to #279 
print table_DoL['Instruction'][277:280]

