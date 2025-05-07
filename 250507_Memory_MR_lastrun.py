#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.2),
    on May 07, 2025, at 12:17
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
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
psychopyVersion = '2021.1.2'
expName = '250506_Memory_MR'  # from the Builder filename that created this script
expInfo = {'participant': '001', 'session': '001'}
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
    originPath='E:\\PhD\\REM_TMR_MRI\\Tasks\\250506_Memory_MR_lastrun.py',
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
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "intro"
introClock = core.Clock()
instruction = visual.TextStim(win=win, name='instruction',
    text='In this task, you will be asked to decide which one of the two screenshots displayed on the screen appeared first within a video you saw in the first session.\n\nScreenshots will appear on the screen at the same time and your task is to press with your index finger if the top picture appeared first, or with your middle finger if the bottom picture appeared first. If you are not sure, go with your best guess.\n\nTry to respond as fast as you can.\n\nThe task will start soon. Please stay still.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trigger = keyboard.Keyboard()

# Initialize components for Routine "screenshots"
screenshotsClock = core.Clock()
imCentersMC = [[0, 0.25], [0, (-0.25)]];
#centers for bounding box
#imCentersBB = [[0, 0.5], [0, (-0.5)]];

fixation = visual.TextStim(win=win, name='fixation',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image_before = visual.ImageStim(
    win=win,
    name='image_before', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.8, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_after = visual.ImageStim(
    win=win,
    name='image_after', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.8, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
order_choice = keyboard.Keyboard()
index_finger_text = visual.TextStim(win=win, name='index_finger_text',
    text='index\nfinger',
    font='Open Sans',
    pos=(-0.6, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
middle_finger_text = visual.TextStim(win=win, name='middle_finger_text',
    text='middle\nfinger',
    font='Open Sans',
    pos=(-0.6, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "end_screen"
end_screenClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='Thank you, this task is now finished.\n\nPlease stay still.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_button = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
triggerClock = core.Clock() # to track time since MR input trigger

# ------Prepare to start Routine "intro"-------
continueRoutine = True
# update component parameters for each repeat
trigger.keys = []
trigger.rt = []
_trigger_allKeys = []
# keep track of which components have finished
introComponents = [instruction, trigger]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction* updates
    if instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction.frameNStart = frameN  # exact frame index
        instruction.tStart = t  # local t and not account for scr refresh
        instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction, 'tStartRefresh')  # time at next scr refresh
        instruction.setAutoDraw(True)
    
    # *trigger* updates
    waitOnFlip = False
    if trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger.frameNStart = frameN  # exact frame index
        trigger.tStart = t  # local t and not account for scr refresh
        trigger.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger, 'tStartRefresh')  # time at next scr refresh
        trigger.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(trigger.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(trigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trigger.status == STARTED and not waitOnFlip:
        theseKeys = trigger.getKeys(keyList=['s'], waitRelease=False)
        _trigger_allKeys.extend(theseKeys)
        if len(_trigger_allKeys):
            trigger.keys = _trigger_allKeys[-1].name  # just the last key pressed
            trigger.rt = _trigger_allKeys[-1].rt
            triggerClock.reset()
            trigger_time = triggerClock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruction.started', instruction.tStartRefresh)
thisExp.addData('instruction.stopped', instruction.tStopRefresh)
# check responses
if trigger.keys in ['', [], None]:  # No response was made
    trigger.keys = None
thisExp.addData('trigger.keys',trigger.keys)
if trigger.keys != None:  # we had a response
    thisExp.addData('trigger.rt', trigger.rt)
thisExp.addData('trigger.started', trigger.tStartRefresh)
thisExp.addData('trigger.stopped', trigger.tStopRefresh)
thisExp.addData('trigger_time', trigger_time) # Just to check that it actually reset and the value is close to zero
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('memoryTask_inputs\\\\memory_condition1_2.csv'),
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
    
    # ------Prepare to start Routine "screenshots"-------
    continueRoutine = True
    # update component parameters for each repeat
    # For fixation cross jitter
    import random
    
    jitter = random.uniform(1,2)
    current_jitter = jitter
    thisExp.addData('ITI_jitter', current_jitter)
    #thisExp.addData('ITI_Memory.startTime', globalClock.getTime())
    
    # To shuffle stimulus locations and correct responses
    shuffle(imCentersMC)
    
    MCimg1 = imCentersMC[0]
    MCimg2 = imCentersMC[1]
    
    
    thisExp.addData('xAxes', MCimg1[0]) #position along the x axis correct
    thisExp.addData('yAxes', MCimg1[1]) #position along the y axis correct 
    
    if ((MCimg1[0] == 0) and (MCimg1[1] == (0.25))):
        MCfam_keyboard = 1
    elif((MCimg1[0] == 0) and (MCimg1[1] == (-0.25))):
        MCfam_keyboard = 2
    
    
    thisExp.addData('MCposCorrPic', MCfam_keyboard);
    thisExp.addData('MCRandPositions', imCentersMC);
    fixation.setText('+')
    image_before.setPos([MCimg1])
    image_before.setImage(before)
    image_after.setPos([MCimg2])
    image_after.setImage(after)
    order_choice.keys = []
    order_choice.rt = []
    _order_choice_allKeys = []
    # keep track of which components have finished
    screenshotsComponents = [fixation, image_before, image_after, order_choice, index_finger_text, middle_finger_text]
    for thisComponent in screenshotsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    screenshotsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "screenshots"-------
    while continueRoutine:
        # get current time
        t = screenshotsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=screenshotsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if thisTrial['condition'] == 'NE':
            image_before.setOpacity(0)
            image_after.setOpacity(0)
            index_finger_text.setOpacity(0)
            middle_finger_text.setOpacity(0)
            fixation.draw()  # Draw the fixation cross
        else:
            image_before.setOpacity(1)
            image_after.setOpacity(1)
            index_finger_text.setOpacity(1)
            middle_finger_text.setOpacity(1)
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
            fixation_start = triggerClock.getTime()
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + asarray(current_jitter)-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
                fixation_end = triggerClock.getTime()
        
        # *image_before* updates
        if image_before.status == NOT_STARTED and tThisFlip >= current_jitter + 0.1-frameTolerance:
            # keep track of start time/frame for later
            image_before.frameNStart = frameN  # exact frame index
            image_before.tStart = t  # local t and not account for scr refresh
            image_before.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_before, 'tStartRefresh')  # time at next scr refresh
            image_before.setAutoDraw(True)
            image_before_start = triggerClock.getTime()
        if image_before.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_before.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                image_before.tStop = t  # not accounting for scr refresh
                image_before.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_before, 'tStopRefresh')  # time at next scr refresh
                image_before.setAutoDraw(False)
                image_before_end = triggerClock.getTime()
        
        # *image_after* updates
        if image_after.status == NOT_STARTED and tThisFlip >= current_jitter + 0.1-frameTolerance:
            # keep track of start time/frame for later
            image_after.frameNStart = frameN  # exact frame index
            image_after.tStart = t  # local t and not account for scr refresh
            image_after.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_after, 'tStartRefresh')  # time at next scr refresh
            image_after.setAutoDraw(True)
            image_after_start = triggerClock.getTime()
        if image_after.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_after.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                image_after.tStop = t  # not accounting for scr refresh
                image_after.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_after, 'tStopRefresh')  # time at next scr refresh
                image_after.setAutoDraw(False)
                imgae_after_end = triggerClock.getTime()
        
        # *order_choice* updates
        waitOnFlip = False
        if order_choice.status == NOT_STARTED and tThisFlip >= current_jitter + 0.1-frameTolerance:
            # keep track of start time/frame for later
            order_choice.frameNStart = frameN  # exact frame index
            order_choice.tStart = t  # local t and not account for scr refresh
            order_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(order_choice, 'tStartRefresh')  # time at next scr refresh
            order_choice.status = STARTED
            order_choice_start = triggerClock.getTime()
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(order_choice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(order_choice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if order_choice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > order_choice.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                order_choice.tStop = t  # not accounting for scr refresh
                order_choice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(order_choice, 'tStopRefresh')  # time at next scr refresh
                order_choice_end = triggerClock.getTime()
                order_choice.status = FINISHED
        if order_choice.status == STARTED and not waitOnFlip:
            theseKeys = order_choice.getKeys(keyList=['2', '3'], waitRelease=False)
            _order_choice_allKeys.extend(theseKeys)
            if len(_order_choice_allKeys):
                lastKey = _order_choice_allKeys[-1]
                order_choice.keys = lastKey.name  # just the last key pressed
                order_choice.rt = lastKey.rt
                
                # get press start and end times
                order_choice_press_start = triggerClock.getTime()
                if lastKey.duration is not None:
                    order_choice_press_end = order_choice_press_start + lastKey.duration
                else:
                    order_choice_press_end = None
                    
                # was this correct?
                if (order_choice.keys == str(MCfam_keyboard)) or (order_choice.keys == MCfam_keyboard):
                    order_choice.corr = 1
                else:
                    order_choice.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *index_finger_text* updates
        if index_finger_text.status == NOT_STARTED and tThisFlip >= asarray(current_jitter + 0.1)-frameTolerance:
            # keep track of start time/frame for later
            index_finger_text.frameNStart = frameN  # exact frame index
            index_finger_text.tStart = t  # local t and not account for scr refresh
            index_finger_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(index_finger_text, 'tStartRefresh')  # time at next scr refresh
            index_finger_text.setAutoDraw(True)
        if index_finger_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > index_finger_text.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                index_finger_text.tStop = t  # not accounting for scr refresh
                index_finger_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(index_finger_text, 'tStopRefresh')  # time at next scr refresh
                index_finger_text.setAutoDraw(False)
        
        # *middle_finger_text* updates
        if middle_finger_text.status == NOT_STARTED and tThisFlip >= asarray(current_jitter + 0.1)-frameTolerance:
            # keep track of start time/frame for later
            middle_finger_text.frameNStart = frameN  # exact frame index
            middle_finger_text.tStart = t  # local t and not account for scr refresh
            middle_finger_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(middle_finger_text, 'tStartRefresh')  # time at next scr refresh
            middle_finger_text.setAutoDraw(True)
        if middle_finger_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > middle_finger_text.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                middle_finger_text.tStop = t  # not accounting for scr refresh
                middle_finger_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(middle_finger_text, 'tStopRefresh')  # time at next scr refresh
                middle_finger_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in screenshotsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "screenshots"-------
    for thisComponent in screenshotsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fixation.started', fixation.tStartRefresh)
    trials.addData('fixation.stopped', fixation.tStopRefresh)
    trials.addData('fixation_start', fixation_start)
    trials.addData('fixation_end', fixation_end)
    trials.addData('image_before.started', image_before.tStartRefresh)
    trials.addData('image_before.stopped', image_before.tStopRefresh)
    trials.addData('image_before_start', image_before_start)
    trials.addData('image_before_end', image_before_end)
    trials.addData('image_after.started', image_after.tStartRefresh)
    trials.addData('image_after.stopped', image_after.tStopRefresh)
    trials.addData('image_after_start', image_after_start)
    trials.addData('image_after_end', image_after_end)
    # check responses
    if order_choice.keys in ['', [], None]:  # No response was made
        order_choice.keys = None
        # was no response the correct answer?!
        if str(MCfam_keyboard).lower() == 'none':
           order_choice.corr = 1;  # correct non-response
        else:
           order_choice.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('order_choice.keys',order_choice.keys)
    trials.addData('order_choice.corr', order_choice.corr)
    if order_choice.keys != None:  # we had a response
        trials.addData('order_choice.rt', order_choice.rt)
    trials.addData('order_choice.started', order_choice.tStartRefresh)
    trials.addData('order_choice.stopped', order_choice.tStopRefresh)
    trials.addData('order_choice_press_start', order_choice_press_start)
    trials.addData('order_choice_press_end', order_choice_press_end)
    
    # the Routine "screenshots" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "end_screen"-------
continueRoutine = True
# update component parameters for each repeat
end_button.keys = []
end_button.rt = []
_end_button_allKeys = []
# keep track of which components have finished
end_screenComponents = [end_text, end_button]
for thisComponent in end_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_screen"-------
while continueRoutine:
    # get current time
    t = end_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    
    # *end_button* updates
    waitOnFlip = False
    if end_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_button.frameNStart = frameN  # exact frame index
        end_button.tStart = t  # local t and not account for scr refresh
        end_button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_button, 'tStartRefresh')  # time at next scr refresh
        end_button.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_button.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_button.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_button.status == STARTED and not waitOnFlip:
        theseKeys = end_button.getKeys(keyList=['space', 'esc'], waitRelease=False)
        _end_button_allKeys.extend(theseKeys)
        if len(_end_button_allKeys):
            end_button.keys = _end_button_allKeys[-1].name  # just the last key pressed
            end_button.rt = _end_button_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_screen"-------
for thisComponent in end_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_text.started', end_text.tStartRefresh)
thisExp.addData('end_text.stopped', end_text.tStopRefresh)
# check responses
if end_button.keys in ['', [], None]:  # No response was made
    end_button.keys = None
thisExp.addData('end_button.keys',end_button.keys)
if end_button.keys != None:  # we had a response
    thisExp.addData('end_button.rt', end_button.rt)
thisExp.addData('end_button.started', end_button.tStartRefresh)
thisExp.addData('end_button.stopped', end_button.tStopRefresh)
thisExp.nextEntry()
# the Routine "end_screen" was not non-slip safe, so reset the non-slip timer
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
