import os
import sys
import platform
import time
import subprocess
import xbmc
import xbmcaddon
import fswitch_config as fsconfig
import fswitch_configutil as fsconfigutil

def getSourceFPS():
# function for getting for source frame rate from the XBMC log file

    # initialize constants
    refVideoOpen = 'NOTICE: DVDPlayer: Opening: '
    refVideoFPSstart = 'NOTICE:  fps: '
    refVideoFPSend = ', pwidth: '
    
    # initialize return values
    videoFileName = None
    videoFPSValue = None
    
    # get location of log file
    if fsconfig.osPlatform == 'HiSTBAndroidV6 Hi3798CV200' or fsconfig.osPlatform == 'HiSTBAndroidV5 Hi3798CV100':
        logFileName = xbmc.translatePath('special://temp') + xbmc.translatePath('special://temp')[xbmc.translatePath('special://temp').find('files')+7:xbmc.translatePath('special://temp').find('temp')].replace('/','') + '.log'

    elif fsconfig.osPlatform == 'Windows 7':
        logFileName = xbmc.translatePath('special://home') + xbmc.translatePath('special://home')[xbmc.translatePath('special://home').find('files')+7:xbmc.translatePath('special://home').find('temp')].replace('/','') + '.log'
    
    else:
        return videoFileName, videoFPSValue
    
    # wait 0.40 second for log file to update (with debug on W7: 0.35 not quite long enough for some files)
    xbmc.sleep(400)
    
    # open log file as read only
    with open(logFileName, 'r') as logFile:
        
        # move pointer to the EOF
        logFile.seek(0, 2)
        
        # get pointer location as the file size
        logFileSize = logFile.tell()
        
        # move pointer to 40k characters before EOF (or to BOF)   
        logFile.seek(max(logFileSize - 40000, 0), 0)
        
        # create list of lines from pointer to EOF
        logFileLines = logFile.readlines()
    
    # slice list to include just the last 1000 lines (with debug on W7: 200=10sec, 600=30sec, 800=45sec, 1000=2min40sec)
    logFileLines = logFileLines[-1000:]
    
    # reverse the list so most recent entry is first
    logFileLines.reverse() 
    
    # parse the list (from most recent backwards)
    for logFileIndex, logFileLine in enumerate(logFileLines):

        # find reference to video opening
        if refVideoOpen in logFileLine:
        
            # find start of video file name  
            linePointer = logFileLine.find(refVideoOpen) + len(refVideoOpen)
            
            # read video file name
            videoFileName = logFileLine[linePointer:].rstrip('\n')

            # Now find the FPS
            
            # slice new list at current index
            logFileLines2 = logFileLines[:logFileIndex]

            # reverse list2 so oldest entry is first
            logFileLines2.reverse() 
            
            # parse list2 (from video opening reference forward)
            for logFileLine2 in logFileLines2:

                # find reference to FPS
                if refVideoFPSstart in logFileLine2:
                
                    # find start and end of FPS value
                    linePointerStart = logFileLine2.find(refVideoFPSstart) + len(refVideoFPSstart)
                    linePointerEnd = logFileLine2.find(refVideoFPSend)

                    # read FPS value
                    videoFPSValue = logFileLine2[linePointerStart:linePointerEnd]

                    # truncate FPS to three decimal places
                    decSplit = videoFPSValue.find('.') + 4
                    videoFPSValue = videoFPSValue[0:decSplit]

                    # only save FPS if not 0.000 (seen on one dvd-iso)
                    if videoFPSValue != '0.000':

                        # save FPS for use in setDisplayModeAuto
                        fsconfig.lastDetectedFps = videoFPSValue
                        fsconfig.lastDetectedFile = videoFileName
                        fsconfigutil.saveLastDetectedFps()

                        # found FPS - stop parsing list2
                        break

                    # FPS is 0.000 - treat as not found
                    else:
                        videoFPSValue = None

            # found video open and FPS (if not 0.000) - stop parsing the list
            break
                             
    return videoFileName, videoFPSValue

def getPlatformType():
# function for getting platform type

    osPlatform = sys.platform
    
    if osPlatform == 'win32':
        osVariant = platform.system() + ' ' + platform.release()

    elif osPlatform == 'linux3' or osPlatform == 'linux4':
        productBrand = subprocess.Popen(['getprop', 'ro.product.brand'], stdout=subprocess.PIPE).communicate()[0].strip()
        productDevice = subprocess.Popen(['getprop', 'ro.product.device'], stdout=subprocess.PIPE).communicate()[0].strip()
        osVariant = productBrand + ' ' + productDevice
        
    else:
        osVariant = 'unsupported'
    
    return osPlatform, osVariant

def getDisplayMode():
# function to read the current output mode from display/mode

    modeFile = None
    outputMode = None
    hisiliconMode = None
    
    modeFileAndroid = "/proc/msp/disp1"
    modeFileWindows = "d:\\x8mode.txt"
 
    if fsconfig.osPlatform == 'HiSTBAndroidV6 Hi3798CV200' or fsconfig.osPlatform == 'HiSTBAndroidV5 Hi3798CV100':
        modeFile = modeFileAndroid
    elif fsconfig.osPlatform == 'Windows 7':
        modeFile = modeFileWindows 
    else:
        outputMode = 'Unsupported platform.'
        return outputMode, hisiliconMode
      
    # check file exists
    if os.path.isfile(modeFile):
        # check file is writable
        if os.access(modeFile, os.R_OK):
            with open(modeFile, 'r') as modeFileHandle:      
                # hisiliconMode = modeFileHandle.readline().strip()
                hisiliconMode = modeFileHandle.read().splitlines()
                if fsconfig.osPlatform == 'HiSTBAndroidV5 Hi3798CV100':
                    hisiliconMode = hisiliconMode[2].split(":")[1].split("/")[0].replace("_","P").replace("3840x","").replace("1920x","").replace("1280x","").lower()
                if fsconfig.osPlatform == 'HiSTBAndroidV6 Hi3798CV200':
                    hisiliconMode = hisiliconMode[3].split(":")[1].split("/")[0].replace("_","P").replace("3840x","").replace("1920x","").replace("1280x","").lower()
                print hisiliconMode 
                # convert HISILICON output mode to more descriptive mode
                if hisiliconMode == '2160p60':
                    outputMode = '2160p-60hz'
                elif hisiliconMode == '2160p30':
                    outputMode = '2160p-30hz'
                elif hisiliconMode == '2160p29.97':
                    outputMode = '2160p-29hz'
                elif hisiliconMode == '2160p50':
                    outputMode = '2160p-50hz'
                elif hisiliconMode == '2160p25':
                    outputMode = '2160p-25hz'
                elif hisiliconMode == '2160p24':
                    outputMode = '2160p-24hz'
                elif hisiliconMode == '2160p23.976':
                    outputMode = '2160p-23hz'
                elif hisiliconMode == '1080p60':
                    outputMode = '1080p-60hz'
                elif hisiliconMode == '1080p59.94':
                    outputMode = '1080p-59hz'
                elif hisiliconMode == '1080p50':
                    outputMode = '1080p-50hz'
                elif hisiliconMode == '1080p24':
                    outputMode = '1080p-24hz'
                elif hisiliconMode == '1080p23.976':
                    outputMode = '1080p-23hz'
                elif hisiliconMode == '720p60':
                    outputMode = '720p-60hz'
                elif hisiliconMode == '720p59.94':
                    outputMode = '720p-59hz'
                elif hisiliconMode == '720p50':
                    outputMode = '720p-50hz'
                else:
                    outputMode = "unsupported"
                
            if hisiliconMode == '':
                outputMode = "invalid"
                hisiliconMode = 'Mode file read, but is empty.'
        else:
            outputMode = "invalid"
            hisiliconMode = 'Mode file found, but could not read.'                
    else:
        outputMode = "invalid"
        hisiliconMode = 'Mode file not found.'

    return outputMode, hisiliconMode

def getDisplayModeFileStatus():
# function to check that the display/mode file exists and is writable

    modeFile = None
    fileStatus = None
    
    modeFileAndroid = "/proc/msp/disp1"
    modeFileWindows = "d:\\x8mode.txt"
 
    if fsconfig.osPlatform == 'HiSTBAndroidV6 Hi3798CV200' or fsconfig.osPlatform == 'HiSTBAndroidV5 Hi3798CV100':
        modeFile = modeFileAndroid
    elif fsconfig.osPlatform == 'Windows 7':
        modeFile = modeFileWindows 
    else:
        fileStatus = 'Unsupported platform'
        return modeFile, fileStatus
      
    # check file exists
    if os.path.isfile(modeFile):
        # check file is writable
        # if os.access(modeFile, os.W_OK):
        fileStatus = 'OK: Frequency switching is supported'
        # else:
            # fileStatus = 'HDMI mode file is read only'                
    else:
        fileStatus = 'HDMI mode file not found'

    return modeFile, fileStatus

def setDisplayMode(newOutputMode):
    # function to write the current output mode from display/mode

    # check whether display/mode file it writable 
    modeFile, fileStatus = getDisplayModeFileStatus()
     
    # display/mode file is not writable
    if fileStatus[:2] != 'OK':
        setModeStatus = fileStatus
        statusType = 'warn'
 
    # display/mode file is writable
    else:
        
        # convert output mode to a valid HISILICON mode
        if newOutputMode == '1080p-60hz':
            newHisiliconMode = '1080p60'
            newFMT = '0'
        elif newOutputMode == '1080p-50hz':
            newHisiliconMode = '1080p50'
            newFMT = '1'
        elif newOutputMode == '1080p-24hz':
            newHisiliconMode = '1080p24'
            newFMT = '4'
        elif newOutputMode == '720p-60hz':
            newHisiliconMode = '720p60'
            newFMT = '7'
        elif newOutputMode == '720p-50hz':
            newHisiliconMode = '720p50'
            newFMT = '8'
        elif newOutputMode == '2160p-25hz':
            newHisiliconMode = '2160p25'
            newFMT = '65'
            if fsconfig.osPlatform == 'HiSTBAndroidV5 Hi3798CV100':
                newFMT = '257'
        elif newOutputMode == '2160p-24hz':
            newHisiliconMode = '2160p24'
            newFMT = '64'
            if fsconfig.osPlatform == 'HiSTBAndroidV5 Hi3798CV100':
                newFMT = '256'
        elif newOutputMode == '2160p-50hz':
            newHisiliconMode = '2160p50'
            newFMT = '67'
            if fsconfig.osPlatform == 'HiSTBAndroidV5 Hi3798CV100':
                newFMT = '257'
        elif newOutputMode == '2160p-60hz':
            newHisiliconMode = '2160p60'
            newFMT = '68'
            if fsconfig.osPlatform == 'HiSTBAndroidV5 Hi3798CV100':
                newFMT = '258'
        elif newOutputMode == '2160p-59hz':
            newHisiliconMode = '2160p59.940'
            newFMT = '68'
            if fsconfig.osPlatform == 'HiSTBAndroidV5 Hi3798CV100':
                newFMT = '258'
        elif newOutputMode == '2160p-23hz':
            newHisiliconMode = '2160p23.976'
            newFMT = '74'
            if fsconfig.osPlatform == 'HiSTBAndroidV5 Hi3798CV100':
                newFMT = '260'
        elif newOutputMode == '2160p-29hz':
            newHisiliconMode = '2160p29.970'
            newFMT = '75'  
            if fsconfig.osPlatform == 'HiSTBAndroidV5 Hi3798CV100':
                newFMT = '261'
        elif newOutputMode == '720p-59hz':
            newHisiliconMode = '720p59.94'
            newFMT = '76'
            if fsconfig.osPlatform == 'HiSTBAndroidV5 Hi3798CV100':
                newFMT = '262'
        elif newOutputMode == '1080p-59hz':
            newHisiliconMode = '1080p59.94'
            newFMT = '77'
            if fsconfig.osPlatform == 'HiSTBAndroidV5 Hi3798CV100':
                newFMT = '263'
        elif newOutputMode == '1080p-23hz':
            newHisiliconMode = '1080p23.976'
            newFMT = '79'
            if fsconfig.osPlatform == 'HiSTBAndroidV5 Hi3798CV100':
                newFMT = '265'
        else:
            setModeStatus = 'Unsupported mode requested.'
            statusType = 'warn'
            return setModeStatus, statusType
          
        # check current display mode setting
        currentOutputMode, currentHiSiliconMode = getDisplayMode()
               
        # get current resolution
        resSplit = currentOutputMode.find('-')
        currentRes = currentOutputMode[0:resSplit]

        # get new resolution
        resSplit = newOutputMode.find('-')
        newRes = newOutputMode[0:resSplit]
        
        # get new frequency
        freqSplit = newOutputMode.find('-') + 1
        newFreq = newOutputMode[freqSplit:len(newOutputMode)]
    
        # current output mode is the same as new output mode
        if currentOutputMode == newOutputMode:
            setModeStatus = 'Frequency already set to ' + newFreq 
            statusType = 'warn'
       
        # current output mode is different to new output mode
        else:
            
            # new resolution is different to current resolution
            if newRes != currentRes:
                setModeStatus = 'Resolution changed, please reconfigure'
                statusType = 'warn'
             
            # new resolution is the same as the current resolution
            else: 
             
                fsconfigutil.loadLastFreqChangeSetting()
             
                # check that at least 4 seconds has elapsed since the last frequency change
                secToNextFreqChange = 4 - (int(time.time()) - fsconfig.lastFreqChange)
                if secToNextFreqChange > 1:
                    setModeStatus = 'Stand-down ' + str(secToNextFreqChange) + ' seconds'               
                    statusType = 'warn'
                elif secToNextFreqChange == 1:
                    setModeStatus = 'Stand-down ' + str(secToNextFreqChange) + ' second' 
                    statusType = 'warn'

                # more than 4 seconds has elapsed since the last frequency change 
                else:
                    # set new display mode
                    # with open(modeFile, 'w') as modeFileHandle: 
                       # modeFileHandle.write('fmt ' + newHisiliconMode)
                    os.system('disptest setfmt ' + newFMT)
                    # save time display mode was changed
                    fsconfig.lastFreqChange = int(time.time())
                    fsconfigutil.saveLastFreqChangeSetting()
                    
                    setModeStatus = 'Frequency changed to ' + newFreq
                    statusType = 'info'
     
    return setModeStatus, statusType

def getCurrentFPS():
    
    # get currently playing video
    videoFileNamePlay = getPlayingVideo()

    # playing video not detected
    if videoFileNamePlay is None:
        setModeStatus = 'No playing video detected.'
        statusType = 'warn'
    
    # playing video detected
    else:

        # check last detected info (before reading the log file)
        fsconfigutil.loadLastDetectedFps()
         
        # last detected file name matches currently playing video, so use last detected FPS
        if fsconfig.lastDetectedFile == videoFileNamePlay:
            videoFileNameLog = fsconfig.lastDetectedFile
            videoFPSValue = fsconfig.lastDetectedFps
        
        # FPS not stored as last detected FPS
        else:
            # read FPS from XBMC log
            videoFileNameLog, videoFPSValue = getSourceFPS()
        
        # FPS not detected
        if videoFPSValue is None:
            setModeStatus = 'Failed to get source framerate.'
            statusType = 'warn'
        
        # FPS detected
        else:
                
            # log file name doesn't match currently playing video
            if videoFileNameLog != videoFileNamePlay:
                setModeStatus = 'Found source framerate for wrong video file.'
                statusType = 'warn'
        
            # log file name matches currently playing video
            else:
                setModeStatus = videoFPSValue
                statusType = 'ok'
    
    return setModeStatus, statusType

def setDisplayModeAuto():
    # function to write the current output mode based on FPS to Frequency configuration

    # check current display mode setting
    currentOutputMode, currentHiSiliconMode = getDisplayMode()
    
    if currentOutputMode == 'unsupported':
        setModeStatus = 'Unsupported resolution: ' + currentHiSiliconMode           
        statusType = 'warn'
            
    elif currentOutputMode == 'invalid':
        setModeStatus = 'Error, unexpected mode: ' + currentHiSiliconMode       
        statusType = 'warn'
        
    else:
        # load auto sync settings
        fsconfigutil.loadAutoSyncSettings()
        
        # get current resolution
        resSplit = currentOutputMode.find('-')
        currentRes = currentOutputMode[0:resSplit]
            
        mode60hz = currentRes + '-60hz'
        mode59hz = currentRes + '-59hz'
        mode50hz = currentRes + '-50hz'
        mode24hz = currentRes + '-24hz'
        mode23hz = currentRes + '-23hz'
        
        autoSync = []

        syncConfig = []        
        if fsconfig.radioAuto60hz:
            syncConfig.extend([(fsconfig.edit60hzFps1, mode60hz),
                               (fsconfig.edit60hzFps2, mode60hz), 
                               (fsconfig.edit60hzFps3, mode60hz), 
                               (fsconfig.edit60hzFps4, mode60hz)])

        if fsconfig.radioAuto59hz:
            syncConfig.extend([(fsconfig.edit59hzFps1, mode59hz), 
                               (fsconfig.edit59hzFps2, mode59hz), 
                               (fsconfig.edit59hzFps3, mode59hz), 
                               (fsconfig.edit59hzFps4, mode59hz)])
             
        if fsconfig.radioAuto50hz:
            syncConfig.extend([(fsconfig.edit50hzFps1, mode50hz), 
                               (fsconfig.edit50hzFps2, mode50hz), 
                               (fsconfig.edit50hzFps3, mode50hz), 
                               (fsconfig.edit50hzFps4, mode50hz)])
             
        if fsconfig.radioAuto24hz:
            syncConfig.extend([(fsconfig.edit24hzFps1, mode24hz), 
                               (fsconfig.edit24hzFps2, mode24hz),
                               (fsconfig.edit24hzFps3, mode24hz),
                               (fsconfig.edit24hzFps4, mode24hz)])        

        if fsconfig.radioAuto23hz:
            syncConfig.extend([(fsconfig.edit23hzFps1, mode23hz), 
                               (fsconfig.edit23hzFps2, mode23hz), 
                               (fsconfig.edit23hzFps3, mode23hz), 
                               (fsconfig.edit23hzFps4, mode23hz)])
             
        # build auto sync list
        for (syncFPS, syncMode) in syncConfig:
            if syncFPS != '':
                autoSync.insert(0, (syncFPS, syncMode))

        if not autoSync:
            setModeStatus = 'No FPS to frequency configuration defined'       
            statusType = 'warn'

        else:
    
            # get FPS of currently playing video
            setModeStatus, statusType = getCurrentFPS()
            
            if statusType == 'ok':
                videoFPSValue = setModeStatus
    
                # search auto sync list for FPS
                fpsFoundInSyncList = False
                for (syncFPS, syncFreq) in autoSync:
                    if syncFPS == videoFPSValue:
                        fpsFoundInSyncList = True
                        break
                
                # FPS not found configured in auto sync list
                if not fpsFoundInSyncList:
                    setModeStatus = 'Source framerate not configured: ' + videoFPSValue                        
                    statusType = 'warn'

                # FPS found in auto sync list       
                else:
                    
                    # check for unsupported mode '720p-24hz'
                    if syncFreq == '720p-24hz':
                        setModeStatus = syncFreq + ' is not supported'
                        statusType = 'warn'                      

                    else:
                        # set the output mode
                        setModeStatus, statusType = setDisplayMode(syncFreq)
                            
    return setModeStatus, statusType

def mapKey(keyScope, keyMappings):
# function for saving key mappings - rewrites entire zswitch.xml file

    # build key map
    mapStart = '<keymap><' + keyScope + '><keyboard>'
    keyStart = '<key id="'
    keyMiddle = '">runaddon(script.frequency.switcher,'
    keyEnd = ')</key>'
    mapEnd = '</keyboard></global></keymap>'  
    
    keyMap = mapStart
    for (keyCode, keyFunction) in keyMappings:
        keyMap = keyMap + keyStart + keyCode + keyMiddle + keyFunction + keyEnd
    keyMap = keyMap + mapEnd
       
    # key map file
    keymapFolder = xbmc.translatePath('special://userdata/keymaps')
    keymapFile = os.path.join(keymapFolder, 'zswitch.xml')
 
    # create keymap folder if it doesn't already exist
    if not os.path.exists(keymapFolder):
        os.makedirs(keymapFolder)
         
    # create or overwrite keymap file
    try:
        with open(keymapFile, 'w') as keymapFileHandle: 
            keymapFileHandle.write(keyMap)
        mapKeyStatus = 'Keys activated'
    except Exception:
        mapKeyStatus = 'Failed to activate keys'
          
    # load updated key maps
    xbmc.executebuiltin('action(reloadkeymaps)')

    return mapKeyStatus

def mapKeyReset():
    
    # key map file
    keymapFolder = xbmc.translatePath('special://userdata/keymaps')
    keymapFile = os.path.join(keymapFolder, 'zswitch.xml')

    # check file exists
    if not os.path.isfile(keymapFile):
        mapKeyResetStatus = 'No keys currently active'
        return mapKeyResetStatus
        
    # delete key map file
    try:
        os.remove(keymapFile)
        mapKeyResetStatus = 'Keys deactivated'
    except Exception:
        mapKeyResetStatus = 'Failed to deactivate keys'

    # load updated key maps
    xbmc.executebuiltin('action(reloadkeymaps)')

    return mapKeyResetStatus

def mapKeyActive():
   
    # key map file
    keymapFolder = xbmc.translatePath('special://userdata/keymaps')
    keymapFile = os.path.join(keymapFolder, 'zswitch.xml')

    # check file exists
    return os.path.isfile(keymapFile)

def getPlayingVideo():
# function to get the file name of the currently playing video

    if xbmc.Player().isPlayingVideo():
        videoFileName = xbmc.Player().getPlayingFile() 
    else:
        videoFileName = None
        
    return videoFileName
