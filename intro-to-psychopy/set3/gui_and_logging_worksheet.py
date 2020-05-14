"""
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
setDir = rootDir + '/set3'
stimDir = rootDir + '/stimuli'

# Experiment Parameter
#-----------------------------------------------------------------------#
trueKey = 'period'
falseKey = 'slash'
fullscreen = True
dur_blank = 30

# 1. Adding Simple Graphic User Interface for Experimenter
#-----------------------------------------------------------------------#
# PsychoPy includes gui, a set of functions that lets us create a box pop-up
# which can be used to enter in experiment/subject info
# Whenever you ran our experiments before, you probably noticed how you entered subject ID and so on
# It is the gui function that lets you do it.

# GUI to enter subj & experiment details
gui = gui.Dlg(title="Sample Code Parameter")  # this line creates a box frame named the given title
# now we can add however many fields we want using .addField, .addFixedField
# .addFixedField adds a text field that cannot be modified in the box
# then why add a fixed field? It's useful to specify details of experiment/subject
# ie. if you know that the experiment is purely behavioral, you could add something like 'beh' tag
gui.addFixedField("exp:", 'sample')
# Q1. Add two fields named 'SubjID' and 'type' being behavioral

# ---YOUR CODE START---


# ---YOUR CODE END---

gui.show()
if not gui.OK:
    print('Cancelled')
    core.quit()

# Now whatever input is entered in the gui can be accessed by gui.data[index]
exp_name = gui.data[0]  # this will return sample

# Q1-2. Now create variables named 'subj_id' and 'exp_type' to retrieve the SubjID and type information from the gui you created above:

# ---YOUR CODE START---


# ---YOUR CODE END---

# if you did the above correctly, exp_summary should print 'sample001beh'
exp_summary = exp_name + '_' + exp_type + '_'  + subj_id
print('exp summary: ' + str(exp_summary))


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


# helper functions
#-----------------------------------------------------------------------#
def show_blank_screen(frameN):
    # show blank screen in between words
    stimText.text = " "
    for frameN in range(0, frameN):
        stimText.draw()
        win.flip()


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


# Building DataFrame
#-----------------------------------------------------------------------#
# dataFrame is used to keep track of all the data from the experiment
# Pandas is a useful package in Python that helps you efficiently manage data
# we specify the data columns as below
data_columns = ['item','resp','rt','globaltime']
data = pd.DataFrame(columns=data_columns)


# setup a variable 'globalClock' to keep track of time
globalClock = core.Clock()


# 2. Creating a log file
#-----------------------------------------------------------------------#
# log file can be saved everytime a script is run
# log file is useful in a sense that it is a safe-keeper for saving whatever is going on
# in case of data loss, you can refer to the log of what happened
logging.setDefaultClock(globalClock)  # logging needs a timer to base on

# there are different levels of log levels
# (ie. DEBUG is the most low-level, details that prints out almost everything that goes on with the script)
# however, we don't want all the small details, like setting next word is set as 'pepper'
# so intead, in the console level of the logging, we specify logging.ERROR
# which will only print stuff that would cause error, or important data
logging.console.setLevel(logging.ERROR)

# then we have a seperate logDat file that will save out all the details. Notice we set the save out directory and the logging level as DEBUG
logDat = logging.LogFile(setDir + '/' + str(exp_summary) + '.log', filemode='w',  # if you set this to 'a' it will append instead of overwriting
    level=logging.DEBUG)


#-----------------------------------------------------------------------#
for i in range(0, len(stim)):
    # Before beginning each stimuli, it's useful for experimenter to see what's being presented
    print('Showing sentence ' + str(i) + ': ' + stim_concept[i] + ' ' + stim_stopword[i] + ' ' + stim_target[i])

    show_blank_screen(dur_blank)

    # now show concept word
    stimText.text = stim_concept[i]
    for frameN in range(0, 60):
        stimText.draw()
        # Now that we added logging to the code,
        # we want to log all the start of each event that is happening
        # ie. when the frame is the very first frame:
        # Q2. Example of logging the start of concept word is shown below
        # Now for all the events happening in the script, add the logging like below
        # when the frame == 0
        if frameN == 0:
            win.logOnFlip('start concept word: ' + stim_concept[i], level=logging.DATA)
        win.flip()

    show_blank_screen(dur_blank)

    current_stopword = stim_stopword[i].split()
    for j in range(0, len(current_stopword)):
        # show each word one at a time
        stimText.text = current_stopword[j]
        for frameN in range(0, 60):
            stimText.draw()
            # ---YOUR CODE START---


            # ---YOUR CODE END---
            win.flip()
        show_blank_screen(dur_blank)

    # show last target word
    stimText.text = stim_target[i]
    for frameN in range(0, 60):
        stimText.draw()
        # ---YOUR CODE START---


        # ---YOUR CODE END---
        win.flip()

    # any keypresses that are made are saved in events keyboard buffer
    # for example, if I pressed any keys before my response period starts,
    # we don't want the previous keypress to interfere with any of the actual response period.
    # thus, it is a good practice to clear out the keyboard events buffer just in case like below
    event.clearEvents('keyboard')


    # Get keyboard response
    #-----------------------------------------------------------------------#
    # after showing the last word in a sentence, display a text to get a keyboard response
    # we first specify a text to display
    stimText.text = 'True or False?'

    keypress_rt = core.Clock()

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

    show_blank_screen(dur_blank)

    # if the keypress has not been made, record the following data as below
    # also display a warning message for not pressing anything
    if not keyPressed:
        data.at[i, 'resp'] = '[]'
        data.at[i, 'rt'] = '[]'
        stimText.text = 'TIME OUT!'
        for frameN in range(0, 30):
            stimText.draw()
            # ---YOUR CODE START---


            # ---YOUR CODE END---
            win.flip()

        show_blank_screen(dur_blank)

    # we need this line that will be saving all the log records and then spit it all out
    # ie. its like flushing toilet
    logging.flush()

    # save to dataframe
    data.at[i, 'item'] =  stim_concept[i] + ' ' + stim_stopword[i] + ' ' + stim_target[i]
    data.at[i, 'globaltime'] = globalClock.getTime()


# End the experiment
#-----------------------------------------------------------------------#
IntstructionText.text = endingText
IntstructionText.draw()
win.flip()

# reindex the dataframe just in case, and save out by specifying directory
data = data.reindex(columns=data_columns)
data.to_csv(setDir + '/' + str(exp_summary) + '.csv', index=False)

# wait for 2 seconds and then quit out of PsychoPy
core.wait(2)
print('end of experiment!')
core.quit()
