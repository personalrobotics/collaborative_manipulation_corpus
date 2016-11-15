# Collaborative Manipulation Corpus
A Corpus of Natural Language Instructions for Collaborative Manipulation

# Overview 
This site presents a dataset of natural language instructions for object specification in manipulation scenarios. It is comprised of 1582 individual written instructions which were collected via online crowdsourcing. Each of these instructions was elicited from one of 28 included scenario images. This dataset is particularly useful for researchers who work in natural language processing, human-robot interaction, and robotic manipulation. In addition to serving as a rich corpus of domain-specific language, it provides a benchmark of image/instruction pairs to be used in system evaluations as well as uncovers inherent challenges in tabletop object specification. Example code is provided for easy access via Python.  



# 1. Primary Dataset: Natural Language Instructions Corpus
## Sample data

| Description | Index | Scenario | ... |
|--------------------------|-------|------------------------|
| Pick up the yellow cube. | 1341 | Configuration\_1\_v1.png | ... |

| AgentType | Difficulty | TimeToComplete | ... |
|--------------------------|-------|------------------------|---|
| human | 5 | 0:00:16 | ... |

- Description or Instruction: The participant gave it to describe the indicated block
- Index: This is the No. 1341 description
- Scenario: In study 1, we show people either Configuration\_01\_v1.png or Configuration\_01\_v2.png. Here it is Configuration\_01\_v1.png, which you can access at [Configuration\_01\_v1.png](./study1_images_with_red_arrows/Configuration_01_v1.png)
- AgentType: The participant is instructing a human instead of a robot
- Difficulty: The participant rated this scenario as 5 (most difficult)
- TimeToComplete: The participant spent 16 seconds to generate this description



# 2. Supplementary Dataset: Instruction Evaluation
## Sample data

| Instruction | Index | Scenario |
|--------------------------|-------|------------------------|
| Pick up the yellow cube. | 1341 | Configuration\_1\_v1.png |

| NumOfWords | TargetBlockId | ClickedBlockId |
|--------------------------|-------|------------------------|
| human | 5 | 0:00:16 |

| Correctness | TimeToComplete | ... |
|--------------------------|-------|------------------------|
| 1 | 3.593606 | ... |

- Description or Instruction: The participant looked for the indicated block based on this instruction
- Index: This is the No. 1341 description
- Scenario: In study 2, we don't distinguish Configuration\_01\_v1.png or Configuration\_01\_v2.png. So you can access this image at Configuration_01.png [Configuration\_01.png](./study2_images_without_red_arrows/Configuration_01.png)
- NumOfWords: Number of words within this instruction
- TargetBlockId: You can find out the target block by referring to [images_code.pdf](./docs/images_code.pdf) Page 1. You can find the block indicated by '1'
- ClickedBlockId: You can find out the block selected by the participant by referring to images_code.pdf Page 1. You can find the block indicated by '1'
- Correctness: The participant successfully select the target block (1 if right, 0 if wrong)
- TimeToComplete: The participant spent 3.593606 seconds to generate this description

