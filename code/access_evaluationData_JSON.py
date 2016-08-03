import json

# Opens and parses JSON, creates a dictionary
# Example for data: table_LoD[77] will access the dictionary of fields for the instruction which corresponds to Index field 77.

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
source = '../data/evaluationData.json'
with open(source) as data_file:
    data = json.load(data_file)
print len(data)
# this is the data entry from study 2
#   where the id of the user in study 2 is 1 and the instruction index is 282
print data['U1@S282']
print data['U1@S282']['Instruction']


"""
2. In evaluationDataAvg
keys available:
    ClickedBlockIdList      Corresponds to the blocks multiple participants respectively selected
    AccuracyAvg             Averaget correctness among multiple participants
    TimeToCompleteAvg       Average duration among multiple participants
    InternalUserIDList      Multiple participant IDs unaffiliated with Amazon ID
"""
source = '../data/evaluationDataAvg.json'
with open(source) as data_file:
    data = json.load(data_file)
print len(data)
# this is the data entry from study 2
#   where the instruction index is 282
print data['282']
print data['282']['Instruction']






