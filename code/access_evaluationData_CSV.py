import csv
from collections import defaultdict

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
    """

    with open(source) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            table_LoD[int(row['Index'])] = row
            for k in row.keys():
                table_DoL[k][int(row['Index'])] = row[k]


"""
1. In evaluationData
keys available:
    Instruction             Taken from Instruction Corpus and to be evaluated by participant
    Index                   Corresponds to individual instruction
    Scenario                Configuration by image and variation
    NumOfWords              The number of words contained in an instruction
    TargetBlockId           Corresponds to the target block of an instruction
    ClickedBlockId          Corresponds to the block participant eventu- ally selected
    Correctness             Whether participant chose the target block
    TimeToComplete          Duration participant took to evaluate an instruction
    DiffcultyComm           Comment on the general difficulty of overall task.
    ObsHardComm             Observation on instructions difficult to interpret
    ObsEasyComm             Observation on instructions easy to interpret
    AddiComm                Comment in general on overall study
"""
source = '../data/evaluationData.csv'
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



"""
2. In evaluationDataAvg
keys available:
    ClickedBlockIdList      Corresponds to the blocks multiple participants respectively selected
    AccuracyAvg             Averaget correctness among multiple participants
    TimeToCompleteAvg       Average duration among multiple participants
    InternalUserIDList      Multiple participant IDs unaffiliated with Amazon ID
"""
source = '../data/evaluationDataAvg.csv'
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






