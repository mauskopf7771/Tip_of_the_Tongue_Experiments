#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Mon Jun 20 14:41:08 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'ToT_2_v2'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jackcrosby/Desktop/ToT_Study_1/ToT_Picure_Naming/ToT_2_v1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1512, 982], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Introduction"
IntroductionClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Thank you for taking part in this on-line picture naming study,   All you have to do is to have a go at retrieving the name/word, in English, for each  object/picture, and then type it in.    Here are the instructions - please do read, especially so you are clear about what a Tip of the Tongue (ToT) experience is.\n\n\n\nThe pictures of objects will be presented in the centre of the screen one by one  (there will be a central fixation cross on the screen, just before each picture).\n\n\n\nBelow each picture are 3 response boxes, and you are asked to press one of these  (the picture is on for a maximum of 5 seconds).    \n\n\nPress ‘space’ to continue…\n\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Intro_Slider"
Intro_SliderClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='Here are the 3 response options:\n\nKNOW  If you know the name of the object (in the English language), then click on the KNOW box as soon as you have retrieved its name.  This will be followed by a text box, for you to type in the name (don’t worry at all about spelling accuracy or typos).\n\nPress ‘space’ to continue…',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "Intro_3"
Intro_3Clock = core.Clock()
text_15 = visual.TextStim(win=win, name='text_15',
    text='ToT – i.e. Tip of the Tongue experience.   If, on the other hand, you know you know the name of the object (in the English language), and have a specific word in mind , but cannot quite retrieve it at this moment, then please click the ToT box.  This will also be followed by a text box, and if you remember anything about the name (e.g., the first letter/sound, or any other letters/sounds, or the  number of syllables), you can type this in.   Or else you can briefly type anything you do know about the object.  Otherwise you can leave the text box blank.\n\nPress ‘Space’ to continue…',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_12 = keyboard.Keyboard()

# Initialize components for Routine "Intro_4"
Intro_4Clock = core.Clock()
text_16 = visual.TextStim(win=win, name='text_16',
    text="DK –   click on the DK box if either the object is unfamiliar to you and you don't know what it is, or else you don’t know the name in English (e.g., you may have forgotten it).  This is not the same as a ToT -  remember a ToT is when you know you know the name, and have a specific word in mind, but just can’t quite retrieve it there and then.     Again, the text box will appear in case you want to type anything you do know about the object.  Otherwise you can leave the text box blank.\n\nAfter this, you press the return key, for the next picture trial.\n\nWe expect the study to take about 10 to 15 minutes, and thank you again for taking part. \n\nPress ‘Space’ to continue…",
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_13 = keyboard.Keyboard()

# Initialize components for Routine "Test_Routine"
Test_RoutineClock = core.Clock()
FC_1 = visual.TextStim(win=win, name='FC_1',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Stimulus = visual.ImageStim(
    win=win,
    name='Stimulus', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
knowbutton = visual.ButtonStim(win, 
    text='', font='Arvo',
    pos=(-0.5, -0.35),
    letterHeight=0.05,
    size=(0.35, 0.1), borderWidth=0.0,
    fillColor='black', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='knowbutton'
)
knowbutton.buttonClock = core.Clock()
ToTButton = visual.ButtonStim(win, 
    text='', font='Arvo',
    pos=(0, -0.35),
    letterHeight=0.05,
    size=(0.25, 0.1), borderWidth=0.0,
    fillColor='black', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='ToTButton'
)
ToTButton.buttonClock = core.Clock()
Dontknowbutton = visual.ButtonStim(win, 
    text='', font='Arvo',
    pos=(0.5, -0.35),
    letterHeight=0.05,
    size=(0.45, 0.1), borderWidth=0.0,
    fillColor='black', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Dontknowbutton'
)
Dontknowbutton.buttonClock = core.Clock()

# Initialize components for Routine "text_entry"
text_entryClock = core.Clock()
jhonny_davidson = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False,
     editable=True,
     name='jhonny_davidson',
     autoLog=True,
)
key_resp_11 = keyboard.Keyboard()
Instruction = visual.TextStim(win=win, name='Instruction',
    text='Please type the name if you clicked Know.  If you clicked ToT or DK, you can type anything you do know about the object or its name e.g., for ToT, you may know some letters.    ',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_13 = visual.TextStim(win=win, name='text_13',
    text='Press the ‘return’ or ‘enter’ key to continnue.',
    font='Open Sans',
    pos=(0, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "End"
EndClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Thank you for compleing this experiment. \n\nPlease close this tab to return the Qualtrics survey.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Introduction"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
IntroductionComponents = [text, key_resp]
for thisComponent in IntroductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Introduction"-------
while continueRoutine:
    # get current time
    t = IntroductionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroductionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Introduction"-------
for thisComponent in IntroductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Intro_Slider"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
Intro_SliderComponents = [text_9, key_resp_7]
for thisComponent in Intro_SliderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Intro_SliderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro_Slider"-------
while continueRoutine:
    # get current time
    t = Intro_SliderClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Intro_SliderClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro_SliderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro_Slider"-------
for thisComponent in Intro_SliderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
# the Routine "Intro_Slider" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Intro_3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
Intro_3Components = [text_15, key_resp_12]
for thisComponent in Intro_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Intro_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro_3"-------
while continueRoutine:
    # get current time
    t = Intro_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Intro_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_15* updates
    if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_15.frameNStart = frameN  # exact frame index
        text_15.tStart = t  # local t and not account for scr refresh
        text_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
        text_15.setAutoDraw(True)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro_3"-------
for thisComponent in Intro_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_15.started', text_15.tStartRefresh)
thisExp.addData('text_15.stopped', text_15.tStopRefresh)
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys = None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.addData('key_resp_12.started', key_resp_12.tStartRefresh)
thisExp.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
thisExp.nextEntry()
# the Routine "Intro_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Intro_4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_13.keys = []
key_resp_13.rt = []
_key_resp_13_allKeys = []
# keep track of which components have finished
Intro_4Components = [text_16, key_resp_13]
for thisComponent in Intro_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Intro_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro_4"-------
while continueRoutine:
    # get current time
    t = Intro_4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Intro_4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_16* updates
    if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_16.frameNStart = frameN  # exact frame index
        text_16.tStart = t  # local t and not account for scr refresh
        text_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
        text_16.setAutoDraw(True)
    
    # *key_resp_13* updates
    waitOnFlip = False
    if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.tStart = t  # local t and not account for scr refresh
        key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_13.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_13.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _key_resp_13_allKeys.extend(theseKeys)
        if len(_key_resp_13_allKeys):
            key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
            key_resp_13.rt = _key_resp_13_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro_4"-------
for thisComponent in Intro_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_16.started', text_16.tStartRefresh)
thisExp.addData('text_16.stopped', text_16.tStopRefresh)
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys = None
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.addData('key_resp_13.started', key_resp_13.tStartRefresh)
thisExp.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
thisExp.nextEntry()
# the Routine "Intro_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ToT_2_conditions_master.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Test_Routine"-------
    continueRoutine = True
    routineTimer.add(5.500000)
    # update component parameters for each repeat
    Stimulus.setImage(Img)
    knowbutton.setText('KNOW')
    ToTButton.setText('ToT')
    Dontknowbutton.setText("Don't Know")
    # keep track of which components have finished
    Test_RoutineComponents = [FC_1, Stimulus, knowbutton, ToTButton, Dontknowbutton]
    for thisComponent in Test_RoutineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Test_RoutineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Test_Routine"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Test_RoutineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Test_RoutineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FC_1* updates
        if FC_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FC_1.frameNStart = frameN  # exact frame index
            FC_1.tStart = t  # local t and not account for scr refresh
            FC_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FC_1, 'tStartRefresh')  # time at next scr refresh
            FC_1.setAutoDraw(True)
        if FC_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FC_1.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                FC_1.tStop = t  # not accounting for scr refresh
                FC_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FC_1, 'tStopRefresh')  # time at next scr refresh
                FC_1.setAutoDraw(False)
        
        # *Stimulus* updates
        if Stimulus.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Stimulus.frameNStart = frameN  # exact frame index
            Stimulus.tStart = t  # local t and not account for scr refresh
            Stimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stimulus, 'tStartRefresh')  # time at next scr refresh
            Stimulus.setAutoDraw(True)
        if Stimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stimulus.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                Stimulus.tStop = t  # not accounting for scr refresh
                Stimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stimulus, 'tStopRefresh')  # time at next scr refresh
                Stimulus.setAutoDraw(False)
        
        # *knowbutton* updates
        if knowbutton.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            knowbutton.frameNStart = frameN  # exact frame index
            knowbutton.tStart = t  # local t and not account for scr refresh
            knowbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(knowbutton, 'tStartRefresh')  # time at next scr refresh
            knowbutton.setAutoDraw(True)
        if knowbutton.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > knowbutton.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                knowbutton.tStop = t  # not accounting for scr refresh
                knowbutton.frameNStop = frameN  # exact frame index
                win.timeOnFlip(knowbutton, 'tStopRefresh')  # time at next scr refresh
                knowbutton.setAutoDraw(False)
        if knowbutton.status == STARTED:
            # check whether knowbutton has been pressed
            if knowbutton.isClicked:
                if not knowbutton.wasClicked:
                    knowbutton.timesOn.append(knowbutton.buttonClock.getTime()) # store time of first click
                    knowbutton.timesOff.append(knowbutton.buttonClock.getTime()) # store time clicked until
                else:
                    knowbutton.timesOff[-1] = knowbutton.buttonClock.getTime() # update time clicked until
                if not knowbutton.wasClicked:
                    continueRoutine = False  # end routine when knowbutton is clicked
                    None
                knowbutton.wasClicked = True  # if knowbutton is still clicked next frame, it is not a new click
            else:
                knowbutton.wasClicked = False  # if knowbutton is clicked next frame, it is a new click
        else:
            knowbutton.wasClicked = False  # if knowbutton is clicked next frame, it is a new click
        
        # *ToTButton* updates
        if ToTButton.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            ToTButton.frameNStart = frameN  # exact frame index
            ToTButton.tStart = t  # local t and not account for scr refresh
            ToTButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ToTButton, 'tStartRefresh')  # time at next scr refresh
            ToTButton.setAutoDraw(True)
        if ToTButton.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ToTButton.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                ToTButton.tStop = t  # not accounting for scr refresh
                ToTButton.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ToTButton, 'tStopRefresh')  # time at next scr refresh
                ToTButton.setAutoDraw(False)
        if ToTButton.status == STARTED:
            # check whether ToTButton has been pressed
            if ToTButton.isClicked:
                if not ToTButton.wasClicked:
                    ToTButton.timesOn.append(ToTButton.buttonClock.getTime()) # store time of first click
                    ToTButton.timesOff.append(ToTButton.buttonClock.getTime()) # store time clicked until
                else:
                    ToTButton.timesOff[-1] = ToTButton.buttonClock.getTime() # update time clicked until
                if not ToTButton.wasClicked:
                    continueRoutine = False  # end routine when ToTButton is clicked
                    None
                ToTButton.wasClicked = True  # if ToTButton is still clicked next frame, it is not a new click
            else:
                ToTButton.wasClicked = False  # if ToTButton is clicked next frame, it is a new click
        else:
            ToTButton.wasClicked = False  # if ToTButton is clicked next frame, it is a new click
        
        # *Dontknowbutton* updates
        if Dontknowbutton.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Dontknowbutton.frameNStart = frameN  # exact frame index
            Dontknowbutton.tStart = t  # local t and not account for scr refresh
            Dontknowbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Dontknowbutton, 'tStartRefresh')  # time at next scr refresh
            Dontknowbutton.setAutoDraw(True)
        if Dontknowbutton.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Dontknowbutton.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                Dontknowbutton.tStop = t  # not accounting for scr refresh
                Dontknowbutton.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Dontknowbutton, 'tStopRefresh')  # time at next scr refresh
                Dontknowbutton.setAutoDraw(False)
        if Dontknowbutton.status == STARTED:
            # check whether Dontknowbutton has been pressed
            if Dontknowbutton.isClicked:
                if not Dontknowbutton.wasClicked:
                    Dontknowbutton.timesOn.append(Dontknowbutton.buttonClock.getTime()) # store time of first click
                    Dontknowbutton.timesOff.append(Dontknowbutton.buttonClock.getTime()) # store time clicked until
                else:
                    Dontknowbutton.timesOff[-1] = Dontknowbutton.buttonClock.getTime() # update time clicked until
                if not Dontknowbutton.wasClicked:
                    continueRoutine = False  # end routine when Dontknowbutton is clicked
                    None
                Dontknowbutton.wasClicked = True  # if Dontknowbutton is still clicked next frame, it is not a new click
            else:
                Dontknowbutton.wasClicked = False  # if Dontknowbutton is clicked next frame, it is a new click
        else:
            Dontknowbutton.wasClicked = False  # if Dontknowbutton is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test_RoutineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Test_Routine"-------
    for thisComponent in Test_RoutineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('FC_1.started', FC_1.tStartRefresh)
    trials.addData('FC_1.stopped', FC_1.tStopRefresh)
    trials.addData('Stimulus.started', Stimulus.tStartRefresh)
    trials.addData('Stimulus.stopped', Stimulus.tStopRefresh)
    trials.addData('knowbutton.started', knowbutton.tStartRefresh)
    trials.addData('knowbutton.stopped', knowbutton.tStopRefresh)
    trials.addData('knowbutton.numClicks', knowbutton.numClicks)
    if knowbutton.numClicks:
       trials.addData('knowbutton.timesOn', knowbutton.timesOn)
       trials.addData('knowbutton.timesOff', knowbutton.timesOff)
    else:
       trials.addData('knowbutton.timesOn', "")
       trials.addData('knowbutton.timesOff', "")
    trials.addData('ToTButton.started', ToTButton.tStartRefresh)
    trials.addData('ToTButton.stopped', ToTButton.tStopRefresh)
    trials.addData('ToTButton.numClicks', ToTButton.numClicks)
    if ToTButton.numClicks:
       trials.addData('ToTButton.timesOn', ToTButton.timesOn)
       trials.addData('ToTButton.timesOff', ToTButton.timesOff)
    else:
       trials.addData('ToTButton.timesOn', "")
       trials.addData('ToTButton.timesOff', "")
    trials.addData('Dontknowbutton.started', Dontknowbutton.tStartRefresh)
    trials.addData('Dontknowbutton.stopped', Dontknowbutton.tStopRefresh)
    trials.addData('Dontknowbutton.numClicks', Dontknowbutton.numClicks)
    if Dontknowbutton.numClicks:
       trials.addData('Dontknowbutton.timesOn', Dontknowbutton.timesOn)
       trials.addData('Dontknowbutton.timesOff', Dontknowbutton.timesOff)
    else:
       trials.addData('Dontknowbutton.timesOn', "")
       trials.addData('Dontknowbutton.timesOff', "")
    
    # ------Prepare to start Routine "text_entry"-------
    continueRoutine = True
    # update component parameters for each repeat
    jhonny_davidson.reset()
    jhonny_davidson.setText('   ')
    key_resp_11.keys = []
    key_resp_11.rt = []
    _key_resp_11_allKeys = []
    #jhonny_davidson.refresh()
    # keep track of which components have finished
    text_entryComponents = [jhonny_davidson, key_resp_11, Instruction, text_13]
    for thisComponent in text_entryComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    text_entryClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "text_entry"-------
    while continueRoutine:
        # get current time
        t = text_entryClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=text_entryClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *jhonny_davidson* updates
        if jhonny_davidson.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            jhonny_davidson.frameNStart = frameN  # exact frame index
            jhonny_davidson.tStart = t  # local t and not account for scr refresh
            jhonny_davidson.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(jhonny_davidson, 'tStartRefresh')  # time at next scr refresh
            jhonny_davidson.setAutoDraw(True)
        
        # *key_resp_11* updates
        waitOnFlip = False
        if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.tStart = t  # local t and not account for scr refresh
            key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_11.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_11.getKeys(keyList=['return'], waitRelease=False)
            _key_resp_11_allKeys.extend(theseKeys)
            if len(_key_resp_11_allKeys):
                key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Instruction* updates
        if Instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instruction.frameNStart = frameN  # exact frame index
            Instruction.tStart = t  # local t and not account for scr refresh
            Instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instruction, 'tStartRefresh')  # time at next scr refresh
            Instruction.setAutoDraw(True)
        
        # *text_13* updates
        if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_13.frameNStart = frameN  # exact frame index
            text_13.tStart = t  # local t and not account for scr refresh
            text_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
            text_13.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in text_entryComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "text_entry"-------
    for thisComponent in text_entryComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('jhonny_davidson.text',jhonny_davidson.text)
    trials.addData('jhonny_davidson.started', jhonny_davidson.tStartRefresh)
    trials.addData('jhonny_davidson.stopped', jhonny_davidson.tStopRefresh)
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
        key_resp_11.keys = None
    trials.addData('key_resp_11.keys',key_resp_11.keys)
    if key_resp_11.keys != None:  # we had a response
        trials.addData('key_resp_11.rt', key_resp_11.rt)
    trials.addData('key_resp_11.started', key_resp_11.tStartRefresh)
    trials.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
    trials.addData('Instruction.started', Instruction.tStartRefresh)
    trials.addData('Instruction.stopped', Instruction.tStopRefresh)
    trials.addData('text_13.started', text_13.tStartRefresh)
    trials.addData('text_13.stopped', text_13.tStopRefresh)
    # the Routine "text_entry" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
EndComponents = [text_4, key_resp_5]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
