import csv
from collections import defaultdict

numEntries = 1583
table_LoD = [None for i in range(numEntries)]
table_DoL = defaultdict(lambda: [None] * numEntries)

def initDataStructs():
    """
    Opens and parses CSV, creates two data structures, and populates them.
    Creates 'List of Dictionaries' and 'Dictionary of Lists' for ease of access.

    Example for LoD: table_LoD[277] will access the dictionary of fields for the instruction which corresponds to Index field 277.

    Examples for DoL: table_DoL['Instruction'] will access a list of all descriptions.
                      table_DoL['Instruction'][77] will access the Description which corresponds to Index field 77.
    """

    with open(source) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            table_LoD[int(row['Index'])] = row
            for k in row.keys():
                table_DoL[k][int(row['Index'])] = row[k]


"""
1. In evaluationData
Keys Available:
Per Instruction:
    Instruction             Taken from NLI Corpus for evaluation by separate participant
    Index                   Corresponds to individual instruction
    Scenario                Configuration by image and image variant 
    NumOfWords              The number of words contained in an instruction
    TargetBlockId           Corresponds to the target block of an instruction
    ClickedBlockId          Corresponds to the block participant finally selected
    Correctness             Whether participant chose the correct target block 
    TimeToComplete          Duration participant took to evaluate an instruction
Per Particpant:
    DiffcultyComm           Comment on the general difficulty of overall task.
    ObsHardComm             Observation on instructions difficult to interpret
    ObsEasyComm             Observation on instructions easy to interpret
    AddiComm                Comment in general on overall study
"""
source = '../data/evaluationData.csv'
initDataStructs()

# note these lengths are the number of NLI from the original corpus and should be equivalent
# there will be 'holes' in these data structures where no evaluation data was collected due to downsampling from the original set to a cleaner less noisy subset
print len(table_DoL['Index'])
print len(table_LoD)

# an example of an entry with no evaluation data
print table_LoD[133]

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



"""
2. In evaluationDataAvg
Keys Available:
Per Instruction:
    ClickedBlockIdList      Corresponds to the blocks multiple participants respectively selected
    AccuracyAvg             Average correctness among multiple participants
    TimeToCompleteAvg       Average duration among multiple participants
    InternalUserIDList      Multiple participant IDs unaffiliated with Amazon ID
"""
source = '../data/evaluationDataAvg.csv'
initDataStructs()


print len(table_DoL['Index'])
print len(table_LoD)

# an example of an entry with no evaluation data
print table_LoD[133]

print table_LoD[277]

print table_LoD[277:280]

print table_LoD[277]['Instruction']
print table_DoL['Instruction'][277]

print table_DoL['Instruction']

print table_DoL['Instruction'][277:280]





