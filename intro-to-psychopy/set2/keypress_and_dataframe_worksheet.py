dur_blank"""
This is a simple script to read in a csv file and display each sentence one word at a time on the screen. There will be blanks in between each word.
By experimental design, each sentence is broken down into three types:
concept words, stopwords, and target words.
Concept words are the very first noun in the sentence
Stopwords are meaningless articles, etc (ie. is a, has an, ...)
Target words are the final noun in the sentence

Set 2:
This script will go over:
1. specifying experiment parameters and variables on top of the script
2. writing a function
3. setting up a clock to check timing
4. reading in a keypress
5. saving a sample data as csv file
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

# setup the project path (Do not change)
# this will assign rootDir as the root of your cloned project
rootDir = os.getcwd()
while os.path.basename(rootDir) != 'intro-to-psychopy':
    os.chdir('..')
    rootDir = os.getcwd()
rootDir = os.getcwd()
setDir = rootDir + '/set2'
stimDir = rootDir + '/stimuli'

# 1. Specify Experiment Parameter On Start
#-----------------------------------------------------------------------#
# Q1. We set important variables on top of the script
# this helps us manage experiment parameter in one place here
# below, we specified true keypress as 'period' button on the keyboard and so on
# create a variable named 'dur_blank' that specifies the duration of blank screen
trueKey = 'period'
falseKey = 'slash'
fullscreen = True
# ---YOUR CODE START---

# ---YOUR CODE END---


# Creating Windows
#-----------------------------------------------------------------------#
# create a window to display
win = visual.Window([800,800], fullscr=fullscreen, monitor='testMonitor', color=[0,0,0], colorSpace='rgb')


# Setting text/visual components
#-----------------------------------------------------------------------#
# text/visual component properties
IntstructionText = visual.TextStim(win=win, text="", font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, depth=0.0, units='cm')

stimText = visual.TextStim(win=win,text="",font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, units='cm')


# 2. Writing helper functions
#-----------------------------------------------------------------------#
# Q2. Helper functions are sub functions that can be used repetitively throughout the script
# For example, showing a blank screen is used in the code throughout
# by having a function that simply shows blank screen, we can replace those repetitive blank screen code to a single line of code
# Write a function 'show_blank_screen' that takes in 'frameN' as an argument which basically shows blank screen for frameN frames:
def show_blank_screen(frameN):
    # ---YOUR CODE START---




    # ---YOUR CODE END---


# Setting text instructions
#-----------------------------------------------------------------------#
# set text instructions as variables
# \n is for printing empty line space
IntroText = "In this study, you will be seeing a sentence or a phrase, presented word by word. \n\nPress the spacebar to begin."

endingText = "You are done with the experiment!"


# Read in stimuli file
#-----------------------------------------------------------------------#
stim_file = stimDir + '/sample_stimuli.csv'
stim = pd.read_csv(stim_file, None, engine='python')

# assign each column values as variables
stim_concept = stim['concept']
stim_stopword = stim['stopword']
stim_target = stim['target']


# Actual experiment code
#-----------------------------------------------------------------------#
# You set the IntroText variable as instuction text to display
# Then, you need to draw the text, and then flip to actually display it on the screen
IntstructionText.text = IntroText
IntstructionText.draw()
win.flip()
# then the event.waitKeys lets the script wait until the certain key is pressed to proceed to the next line of the script
inst_key = event.waitKeys(keyList=['space'])


# 3. Building DataFrame
#-----------------------------------------------------------------------#
# dataFrame is used to keep track of all the data from the experiment
# Pandas is a useful package in Python that helps you efficiently manage data
# we specify the data columns as below
data_columns = ['item','resp','rt','globaltime']
# Q3: Specify the column names in the data below
# here, we initialize variable 'data' as a new dataFrame with columns specified as data_columns. Specify the columns below.
data = pd.DataFrame(columns=)


# setup a variable 'globalClock' to keep track of time
globalClock = core.Clock()

for i in range(0, len(stim)):
    # Before beginning each stimuli, it's useful for experimenter to see what's being presented
    print('Showing sentence ' + str(i) + ': ' + stim_concept[i] + ' ' + stim_stopword[i] + ' ' + stim_target[i])

    # Q2A. replace the blank screen to helper function
    # ---YOUR CODE START---

    # ---YOUR CODE END---

    # now show concept word
    stimText.text = stim_concept[i]
    for frameN in range(0, 60):
        stimText.draw()
        win.flip()

    # Q2A. replace the blank screen to helper function
    # ---YOUR CODE START---

    # ---YOUR CODE END---

    current_stopword = stim_stopword[i].split()
    for j in range(0, len(current_stopword)):
        # show each word one at a time
        stimText.text = current_stopword[j]
        for frameN in range(0, 60):
            stimText.draw()
            win.flip()
        # Q2A. replace the blank screen to helper function
        # ---YOUR CODE START---

        # ---YOUR CODE END---

    # show last target word
    stimText.text = stim_target[i]
    for frameN in range(0, 60):
        stimText.draw()
        win.flip()

    # any keypresses that are made are saved in events keyboard buffer
    # for example, if I pressed any keys before my response period starts,
    # we don't want the previous keypress to interfere with any of the actual response period.
    # thus, it is a good practice to clear out the keyboard events buffer just in case like below
    event.clearEvents('keyboard')


    # 4. Get keyboard response
    #-----------------------------------------------------------------------#
    # after showing the last word in a sentence, display a text to get a keyboard response
    # we first specify a text to display
    stimText.text = 'True or False?'

    # Q4A. create a variable named 'keypressed_rt' that initializes a clock
    # ---YOUR CODE START---

    # ---YOUR CODE END---

    # we will now write a for loop that shows the 'True or False?' text above for certain amount of time to get the keyboard response
    keyPressed = False
    for frameN in range(0, 60):
        stimText.draw()
        win.flip()
        # event.getKeys is the function that commands PsychoPy to record any keys that are being pressed
        # because we have this in the for loop above, it will try to record any keypresses being made for that period of time
        respKey = event.getKeys(keyList=[trueKey,falseKey], modifiers=False, timeStamped=keypress_rt)

        # if the keypress has been made, record the following data as below
        if respKey and not keyPressed:
            data.at[i, 'resp'] = respKey[0][0]
            data.at[i, 'rt'] = respKey[0][1]
            print('Pressed: ' + str(respKey[0][0]) + '\nRT: ' + str(respKey[0][1]))
            keyPressed = True

    # Q2A. replace the blank screen to helper function
    # ---YOUR CODE START---

    # ---YOUR CODE END---

    # if the keypress has not been made, record the following data as below
    # also display a warning message for not pressing anything
    if not keyPressed:
        data.at[i, 'resp'] = '[]'
        data.at[i, 'rt'] = '[]'
        stimText.text = 'TIME OUT!'
        for frameN in range(0, 30):
            stimText.draw()
            win.flip()

        # Q2A. replace the blank screen to helper function
        # ---YOUR CODE START---

        # ---YOUR CODE END---

    # save to dataframe
    # Q4B. Above, we recorded 'resp' and 'rt' in the dataframe
    # now record values for 'item' and 'globaltime' for the dataframe, in which item simply means the entire sentence that was shown. 'globaltime' means the entire time of the experiment that we specified earlier as globalClock = core.Clock()
    # hint: globalClock.getTime() returns you the time since the start

    # ---YOUR CODE START--


    # ---YOUR CODE END---


# 5. End the experiment
#-----------------------------------------------------------------------#
IntstructionText.text = endingText
IntstructionText.draw()
win.flip()

# reindex the dataframe just in case, and save out by specifying directory
data = data.reindex(columns=data_columns)
data.to_csv(setDir + '/sample_data.csv', index=False)

# wait for 2 seconds and then quit out of PsychoPy
core.wait(2)
print('end of experiment!')
core.quit()
