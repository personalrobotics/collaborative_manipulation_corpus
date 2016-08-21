import json

# Opens and parses JSON, creates a dictionary

"""
1. In evaluationData
Keys Available:
Per Instruction:
    Instruction             Taken from Instruction Corpus and to be evaluated by participant
    Index                   Corresponds to individual instruction
    Scenario                Configuration by image and variation
    NumOfWords              The number of words contained in an instruction
    TargetBlockId           Corresponds to the target block of an instruction
    ClickedBlockId          Corresponds to the block participant eventu- ally selected
    Correctness             Whether participant chose the target block
    TimeToComplete          Duration participant took to evaluate an instruction
Per Participant:
    DiffcultyComm           Comment on the general difficulty of overall task.
    ObsHardComm             Observation on instructions difficult to interpret
    ObsEasyComm             Observation on instructions easy to interpret
    AddiComm                Comment in general on overall study
"""
source = '../data/evaluationData.json'
with open(source) as data_file:
    data = json.load(data_file)

print len(data)
# this is the data entry from study 2

# this data is orgnaized by 'userID@instructionIndex' being the first key
# to see a list of valid user/index permutations 
print data.keys()

# then access either one users input table or a particular field in this table
# here we access userID 1 evaluating instruction index #282
print data['U1@S282']
print data['U1@S282']['Instruction']

"""
2. In evaluationDataAvg
Keys Available:
Per Instruction:
    Instruction             Instruction being evaluated
    Index                   Corresponds to individual instruction
    Scenario:               Configuration by image and variation 
    ClickedBlockIdList      Corresponds to the blocks multiple participants respectively selected
    TargetBlockID           Corresponds to the target block of an instruction
    NumOfWords              The number of words contained in an instruction
    AccuracyAvg             Averaget correctness among multiple participants
    TimeToCompleteAvg       Average duration among multiple participants
    InternalUserIDList      Multiple participant IDs unaffiliated with Amazon ID
    Ambiguity               Manually coded data corresponding to the number of possible target blocks an instruction could reference given the stimulus scenario
    Perspective             Manually coded data corresponding to the perspective an instruction uses 

"""
source = '../data/evaluationDataAvg.json'
with open(source) as data_file:
    data = json.load(data_file)

print len(data)

# this data is orgnaized with instruction Index as first key 
# to see a list of valid keys 
print data.keys()

# access instruction @ Index #282 data
print data['282']
print data['282']['Instruction']






