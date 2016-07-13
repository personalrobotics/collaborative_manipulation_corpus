import json

"""
Opens and parses JSON, creates a dictionary

Example for data: table_LoD[77] will access the dictionary of fields for the instruction which corresponds to Index field 77.

keys available:
    description:            Given by participant in study 1 as response to prompt
    sentence_index:         Corresponds to individual instruction
    configuration:          Configuration by image and variation
    r_num_of_words:         In study 2, number of words in the instruction
    r_correctness:          In study 2, whether this participant in study 2 has correctly identified the target block or not
    r_user_id:              In study 2, the user index number in study 2
    r_num_blocks_clicked:   In study 2, how many times has the participant in study 2 clicked on a block
    r_num_blocks_hovered:   In study 2, how many times has the participant in study 2 hovered above a block
    r_time/sec:             In study 2, duration participant took to choose the target block
    r_target_block_index:   In study 2, corresponds to the target block
    c_perspective:          Based on data manual coding result, the instruction is using
                                partner, participant, neither or unknown perspective
    c_ambiguity:            The number of of blocks which could be potentially identified based on the instruction

"""


source = '../data/reverse_study_per_sentence_user.json'
with open(source) as data_file:
    data = json.load(data_file)

print len(data)
# this is the data entry from study 2
#   whose id of the user in study 2 is 1 and sentence index is 282
print data['U1@S282']
print data['U1@S282']['sentence_index']

