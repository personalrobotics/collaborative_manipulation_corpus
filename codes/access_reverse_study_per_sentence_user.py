import csv
from collections import defaultdict

source = '../data/forward_study_per_sentence_user.csv' 
numEntries = 1583
table_LoD = [None for i in range(numEntries)]
table_DoL = defaultdict(lambda: [None] * numEntries) 

def initDataStructs():
    """ 
    Opens and parses CSV, creates two data structures, and populates them.
    Creates List of Dictionaries and Dictionary of Lists for ease of access.

    Example for LoD: table_LoD[77] will access the dictionary of fields for the instruction which corresponds to Index field 77.

    Examples for DoL: table_DoL['Description'] will access a list of all descriptions.
                      table_DoL['Description'][77] will access the Description which corresponds to Index field 77. 
    
    
    keys available: 
        Description, Index, Scenario, AgentType, Difficulty, 
        TimeToComplete, Strategy, Challenging, GeneralComments, Age, Gender, 
        Occupation, ComputerUsage, DominantHand, EnglishAsFirst, ExpWithRobots, 
        ExpWithRCCars, ExpWithFPS, ExpWithRTS, ExpWithRobotComments, InternalUserID
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
print table_LoD[77]['Description']
print table_DoL['Description']
print table_DoL['Description'][77]
# description from entry 77 to 79
print table_DoL['Description'][77:80]

