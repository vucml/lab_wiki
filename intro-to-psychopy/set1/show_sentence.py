"""
This is a simple script to read in a csv file and display each sentence one word at a time on the screen. There will be blanks in between each word.
By experimental design, each sentence is broken down into three types:
concept words, stopwords, and target words.
Concept words are the very first noun in the sentence
Stopwords are meaningless articles, etc (ie. is a, has an, ...)
Target words are the final noun in the sentence

You can open the sample_stimuli.csv file to have a better look at the structure

* The order of presentation will be:
concept word > blank > stop word > blank > target word > blank

Set 1:
This script will go over:
1. creating windows
2. setting project path
3. setting text instructions as string
4. building visual stimuli components
5. a brief experiment code to loop each sentence
6. closing out
"""
from __future__ import absolute_import, division, print_function
import os
import sys
import random
import pandas as pd
from builtins import range
from psychopy import visual, event, gui, core, logging
import numpy as np

# avoid getting .pyc files
sys.dont_write_bytecode = True

weeklyDir = os.getcwd()
# recursively find the root cdcatmr dir
while os.path.basename(weeklyDir) != 'intro-to-psychopy':
    os.chdir('..')
    weeklyDir = os.getcwd()

# setup the project path (Do not change)
# this will assign rootDir as the root of your cloned project
rootDir = os.getcwd()
stimDir = rootDir + '/stimuli'


# 1. Creating Windows
#-----------------------------------------------------------------------#
# create a window to display
# Q1: Make the win below to show in full screen:
win = visual.Window([800,800], fullscr=True, monitor='testMonitor', color=[0,0,0], colorSpace='rgb')


# 2. Setting visual components
#-----------------------------------------------------------------------#
# text/visual component properties
IntstructionText = visual.TextStim(
    win=win, text="", font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0,units='cm')

# Q2. Write a new stimText component with its position at center with text size being 1.2cm
stimText = visual.TextStim(win=win,text="",font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, units='cm')


# 3. Setting text instructions
#-----------------------------------------------------------------------#
# set text instructions as variables
# \n is for printing empty space
IntroText = "In this study, you will be seeing a sentence or a phrase, presented word by word. \n\nPress the spacebar to begin."

# Q3. Write up a simple sentence to thank the subject for participating
endingText = "Your thank you text here"


# 4. Read in stimuli file
#-----------------------------------------------------------------------#
# Q4. Specify the variable for stim_file below so that the script can locate sample_stimuli.csv file in /stimuli folder
stim_file = stimDir + '/sample_stimuli.csv'
stim = pd.read_csv(stim_file, None, engine='python')

# assign each column values as variables
stim_concept = stim['concept']
stim_stopword = stim['stopword']
stim_target = stim['target']
# stim_concept will contain all the concept column from sample csv
# to get the nth item within the specified column above, you use the method called 'indexing'
# in indexing, you use brackets [] and a number inside to basically say nth item of that column
# for example:
# stim_concept[0] will print the first concept word in the column
# stim_stopword[2] will contain the third stopword

# Q4-1. How would you print the fifth concept word in the column?
print(stim_concept[4])
print(stim_concept[-1:])

# [Advanced] Q4-2. How would you print just all the target words?
# *Hint: ':' colon means all
print(stim_target[:])


# 4. Actual experiment code
#-----------------------------------------------------------------------#
# 4A. Showing instructions
# You set the IntroText variable as instuction text to display.
# Then, you need to draw the text, and then flip to actually display it on the screen
IntstructionText.text = IntroText
IntstructionText.draw()
win.flip()
# then the event.waitKeys lets the script wait until the certain key is pressed to proceed to the next line of the script
inst_key = event.waitKeys(keyList=['space'])


#-----------------------------------------------------------------------#
# 4B. Looping each stimuli line by line in stimuli
# the line below basically tells to check i starting from 0 upto length of stimuli file
for i in range(0, len(stim)):

    # Before beginning each stimuli, it's useful for experimenter to see what's being presented
    # we ue the print statement to print what's being shown

    # Q4B-1. Make a print('string') statement to show which sentence is being shown
    # *Hint: print(stim_concept[0] + stim_stopword[0] + stim_target[0]) will print first item of each column
    print('Showing sentence: ' + stim_concept[i] + ' ' + stim_stopword[i] + ' ' + stim_target[i])


    # first show blank screen for 30 frames
    # [Advanced] Q4B-2: Write a for loop to display blank screen for 30 frames
    # blank can be depiccted as  empty string ie. ' '
    # make sure to add .text, .draw(), and win.flip()
    stimText.text = " "
    for frameN in range(0, 30):
        stimText.draw()
        win.flip()

    # now show concept word
    # Q4B-3: Assign the stimText.text as the ith item in concept column
    # *Hint: refer to target word code later in the code
    stimText.text = stim_concept[i]
    for frameN in range(0, 60):
        stimText.draw()
        win.flip()

    stimText.text = " "
    # show blank screen in between words
    for frameN in range(0, 30):
        stimText.draw()
        win.flip()

    current_stopword = stim_stopword[i].split()
    for j in range(0, len(current_stopword)):
        # show each word one at a time
        stimText.text = current_stopword[j]
        for frameN in range(0, 60):
            stimText.draw()
            win.flip()
        # show blank screen in between words
        stimText.text = " "
        for frameN in range(0, 30):
            stimText.draw()
            win.flip()

    # show last target word
    stimText.text = stim_target[i]
    for frameN in range(0, 60):
        stimText.draw()
        win.flip()

    # show blank screen at the end
    stimText.text = " "
    for frameN in range(0, 30):
        stimText.draw()
        win.flip()


# 5. End the experiment
#-----------------------------------------------------------------------#
IntstructionText.text = endingText
IntstructionText.draw()
win.flip()
# wait for 2 seconds and then quit out of PsychoPy
core.wait(2)
print('end of experiment!')
core.quit()
