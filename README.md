# Collaborative Manipulation Corpus
A Corpus of Natural Language Instructions for Collaborative Manipulation

# Overview 
This site presents a dataset of natural language instructions for object specification in manipulation scenarios. It is comprised of 1582 individual written instructions which were collected via online crowdsourcing. Each of these instructions was elicited from one of 28 included scenario images. This dataset is particularly useful for researchers who work in natural language processing, human-robot interaction, and robotic manipulation. In addition to serving as a rich corpus of domain-specific language, it provides a benchmark of image/instruction pairs to be used in system evaluations as well as uncovers inherent challenges in tabletop object specification. Example code is provided for easy access via Python.  



<p>Primary Dataset: Natural Language Instructions Corpus</p>

<ul>
<li><p><a href="./data/NLICorpusData.csv" target="_blank">Data in CSV</a></p></li>
<li><p><a href="./data/NLICorpusData_1400.csv" target="_blank">Downsampled Data in CSV</a></p>
<p>(We downsampled the data from 1582 to 1400 and use the 1400 instructions in the evaluation study)</p></li>
<li><p><a href="./code/access_NLICorpusData_CSV.py" target="_blank">Accessing code in Python</a></p></li>
<li><p>Example of one row from the table:</p></li>
<br>
<table style="height:100px; width:750px; overflow-x:scroll ; overflow-y:hidden ; padding-bottom:10px;">
  <tr>
    <th>Instruction</th>
    <th>Index</th>
    <th>Scenario</th>
    <th>AgentType</th>
    <th>Difficulty</th>
    <th>TimeToComplete</th>
    <th>Strategy</th>
    <th>Challenging</th>
    <th>GeneralComments</th>
    <th>Age</th>
    <th>Gender</th>
    <th>Occupation</th>
    <th>ComputerUsage</th>
    <th>DominantHand</th>
    <th>EnglishFirst</th>
    <th>ExpWithRobots</th>
    <th>ExpWithRCCars</th>
    <th>ExpWithFPS</th>
    <th>ExpWithRTS</th>
    <th>ExpWithRobotComments</th>
  </tr>
  <tr>
    <td>Pick up the yellow cube.</td>
    <td>1341</td>
    <td>Configuration_1_v1.png</td>
    <td>human</td>
    <td>1</td>
    <td>00:00:16</td>
    <td>Tried to find something that would differ the specific cube from others</td>
    <td>Moderately challenging at the beginning but it get's easier with practice.</td>
    <td> </td>
    <td>28</td>
    <td>female</td>
    <td>Engineer</td>
    <td>15-20</td>
    <td>Right</td>
    <td>1</td>
    <td>3</td>
    <td>1</td>
    <td>5</td>
    <td>3</td>
    <td>Yes, I had to build one in one of my classes </td>
    <td>3.593606</td>
  </tr>
</table>
<br>
<ul>
  <li><p>Instruction: When prompted with the scenario stimulus image, the participant generated this instruction.</p></li>
  <li><p>Index: This is Instruction ID #1341 - it is consistent across all data files</p></li>
  <li><p>Scenario: The corresponding stimulus image used to elicit the instruction. <a href="./study1_images_with_red_arrows/Configuration_01_v1.png" target="_blank">Configuration_01_v1.png</a></p></li>
  <li><p>AgentType: The participant was told they were instructing a <i>human</i> rather than a <i>robot</i>.</p></li>
  <li><p>Difficulty: The participant rated this scenario as 5 (most difficult).</p></li>
  <li><p>TimeToComplete: The participant spent 16 seconds generating their instruction.</p></li>
  <li><p>Demographics: Please refer to Table 2 in the <a href="./docs/ijrr_2016.pdf" target="_blank">IJRR Data Paper</a> for further details.</p></li>
</ul>
</ul>
</li>
<li>
<p>Supplementary Dataset: Instruction Evaluation</p>

<ul>
<li><p><a href="./data/evaluationData.json" target="_blank">Full Data in JSON</a></p></li>
<li><p><a href="./data/evaluationData.csv" target="_blank">Full Data in CSV</a></p></li>
<li><p><a href="./data/evaluationDataAvg.json" target="_blank">Averaged Data in JSON</a></p></li>
<li><p><a href="./data/evaluationDataAvg.csv" target="_blank">Averaged Data in CSV</a></p></li>
<li><p><a href="./code/access_evaluationData_JSON.py" target="_blank">Python code to access JSON data</a></p></li>
<li><p><a href="./code/access_evaluationData_CSV.py" target="_blank">Python code to access CSV data</a></p></li>
<ul>
<li>Note: in accessing code of study 2, <code>r_target_block_index</code> is referring to the index of the target block. The index of all the blocks and the indices of target blocks in both versions of each scenario on the tabletop are annotated in <a href="./docs/images_code.pdf" target="_blank">images_code.pdf</a>
</li>
</ul>
<br>
<table style="height:100px; width:750px; overflow-x:scroll ; overflow-y:hidden ; padding-bottom:10px; n-th">
  <tr>
    <th>Instruction</th>
    <th>Index</th>
    <th>Scenario</th>
    <th>NumOfWords</th>
    <th>TargetBlockId</th>
    <th>ClickedBlockId</th>
    <th>Correctness</th> 
    <th>TimeToComplete</th>
    <th>DifficultyComm</th>
    <th>ObsHardComm</th>
    <th>ObsEasyComm</th>
    <th>AddiComm</th>
    <th>Age</th>
    <th>Gender</th>
    <th>Occupation</th>
    <th>ComputerUsage</th>
    <th>DominantHand</th>
    <th>EnglishFirst</th>
    <th>ExpWithRobots</th>
    <th>ExpWithRCCars</th>
    <th>ExpWithFPS</th>
    <th>ExpWithRTS</th>
    <th>ExpWithRobotComments</th>
    <th>InternalUserID</th>
  </tr>
  <tr>
    <td>Pick up the yellow cube.</td>
    <td>1341</td>
    <td>Configuration_1_v1.png</td>
    <td>5</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>3.593606</td>
    <td>Nice Game and Fun</td>
    <td>Nothing</td>
    <td>Nothing</td>
    <td> </td>
    <td>37</td>
    <td>female</td>
    <td>SEO</td>
    <td>>20</td>
    <td>Right</td>
    <td>1</td>
    <td>6</td>
    <td>6</td>
    <td>6</td>
    <td>6</td>
    <td>No Idea</td>
    <td>165</td>
  </tr>
</table>
<br>
<ul>
  <li><p>Instruction: The instruction a participant was prompted with when searching for the block from the source stimulus image.</p></li>
  <li><p>Index: This is Instruction ID #1341 - it is consistent across all data files</p></li>
  <li><p>Scenario: In the evaluation study, there was no distinction between versions of stimulus images e.g. 'v0 or v1'. Configuration_01_v1.png or Configuration_01_v2.png would both correspond to <a href="./study2_images_without_red_arrows/Configuration_01.png" target="_blank">Configuration_01.png</a> as they are the same when the red indication arrow is removed.</p></li>
  <li><p>NumOfWords: Number of words within this instruction</p></li>
  <li><p>TargetBlockId: A number assigned to each block within an image as defined in<a href="./docs/images_code.pdf" target="_blank">images_code.pdf</a> Page 1. The real target block in the original source images was block '1'.</p></li>
  <li><p>ClickedBlockId: A number which comes from the same definition as the TargetBlockId. This number refers to the block that was selected by the evaluating participant.</p></li>
  <li><p>Correctness: This participant successfully selected the target block (1 if correct, 0 if wrong).</p></li>
  <li><p>TimeToComplete: The participant spent ~3.6 seconds evaluating this instruction.</p></li>
  <li><p>Demographics: Please refer to Table 3 in the <a href="./docs/ijrr_2016.pdf" target="_blank">IJRR Data Paper</a> for further details.</p></li>
</ul>
</li>
</ul>
</li>
</ol>
