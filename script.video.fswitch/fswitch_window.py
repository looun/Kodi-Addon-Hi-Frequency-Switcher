import xbmc
import xbmcgui
import xbmcaddon
import os
import fswitch_config as fsconfig
import fswitch_configutil as fsconfigutil
import fswitch_util as fsutil
import fswitch_keylisten as fskeylisten

from pyxbmct.addonwindow import *
from shutil import copyfile

class MapKeysWindow(AddonDialogWindow):

    def __init__(self, title=''):
        # base class constructor
        super(MapKeysWindow, self).__init__(title)

        # set window width + height, and grid rows + columns
        self.setGeometry(750, 650, 12, 13)

        # create, place, then set objects
        self.labelCurrentRes = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelCurrentRes, 1, 1, columnspan=10, pad_y=11)
       
        self.radio60hz = RadioButton('60 hz')
        self.placeControl(self.radio60hz, 2, 1, columnspan=3)
        self.radio60hz.setSelected(fsconfig.radio60hz)
         
        self.radio59hz = RadioButton('59 hz')
        self.placeControl(self.radio59hz, 3, 1, columnspan=3)
        self.radio59hz.setSelected(fsconfig.radio59hz)

        self.radio50hz = RadioButton('50 hz')
        self.placeControl(self.radio50hz, 4, 1, columnspan=3)
        self.radio50hz.setSelected(fsconfig.radio50hz)
 
        self.radio24hz = RadioButton('24 hz')
        self.placeControl(self.radio24hz, 5, 1, columnspan=3)
        self.radio24hz.setSelected(fsconfig.radio24hz)

        self.radio23hz = RadioButton('23 hz')
        self.placeControl(self.radio23hz, 6, 1, columnspan=3)
        self.radio23hz.setSelected(fsconfig.radio23hz)

        self.radioAuto = RadioButton('Automatic')
        self.placeControl(self.radioAuto, 7, 1, columnspan=3)
        self.radioAuto.setSelected(fsconfig.radioAuto)
        
        self.radioInfo = RadioButton('Info')
        self.placeControl(self.radioInfo, 8, 1, columnspan=3)
        self.radioInfo.setSelected(fsconfig.radioInfo)

        self.radioHiPQTools = RadioButton('HiPQTools')
        self.placeControl(self.radioHiPQTools, 9, 1, columnspan=3)
        self.radioHiPQTools.setSelected(fsconfig.radioHiPQTools)

        self.buttonMap60hz = Button('Select Key')
        self.placeControl(self.buttonMap60hz, 2, 7, columnspan=3)
 
        self.buttonMap59hz = Button('Select Key')
        self.placeControl(self.buttonMap59hz, 3, 7, columnspan=3)

        self.buttonMap50hz = Button('Select Key')
        self.placeControl(self.buttonMap50hz, 4, 7, columnspan=3)

        self.buttonMap24hz = Button('Select Key')
        self.placeControl(self.buttonMap24hz, 5, 7, columnspan=3)

        self.buttonMap23hz = Button('Select Key')
        self.placeControl(self.buttonMap23hz, 6, 7, columnspan=3)

        self.buttonMapAuto = Button('Select Key')
        self.placeControl(self.buttonMapAuto, 7, 7, columnspan=3)

        self.buttonMapInfo = Button('Select Key')
        self.placeControl(self.buttonMapInfo, 8, 7, columnspan=3)

        self.buttonMapHiPQTools = Button('Select Key')
        self.placeControl(self.buttonMapHiPQTools, 9, 7, columnspan=3)

        self.labelKey60hz = Label('')
        self.placeControl(self.labelKey60hz, 2, 5, columnspan=2, pad_y=11)
        self.labelKey60hz.setLabel(fsconfig.key60hz)
 
        self.labelKey59hz = Label('')
        self.placeControl(self.labelKey59hz, 3, 5, columnspan=2, pad_y=11)
        self.labelKey59hz.setLabel(fsconfig.key59hz)

        self.labelKey50hz = Label('')
        self.placeControl(self.labelKey50hz, 4, 5, columnspan=2, pad_y=11)
        self.labelKey50hz.setLabel(fsconfig.key50hz)

        self.labelKey24hz = Label('')
        self.placeControl(self.labelKey24hz, 5, 5, columnspan=2, pad_y=11)
        self.labelKey24hz.setLabel(fsconfig.key24hz)

        self.labelKey23hz = Label('')
        self.placeControl(self.labelKey23hz, 6, 5, columnspan=2, pad_y=11)
        self.labelKey23hz.setLabel(fsconfig.key23hz)

        self.labelKeyAuto = Label('')
        self.placeControl(self.labelKeyAuto, 7, 5, columnspan=2, pad_y=11)
        self.labelKeyAuto.setLabel(fsconfig.keyAuto)

        self.labelKeyInfo = Label('')
        self.placeControl(self.labelKeyInfo, 8, 5, columnspan=2, pad_y=11)
        self.labelKeyInfo.setLabel(fsconfig.keyInfo)

        self.labelKeyHiPQTools = Label('')
        self.placeControl(self.labelKeyHiPQTools, 9, 5, columnspan=2, pad_y=11)
        self.labelKeyHiPQTools.setLabel(fsconfig.keyHiPQTools)

        self.buttonMapKeysSave = Button('Activate Keys')
        self.placeControl(self.buttonMapKeysSave, 10, 1, columnspan=4)

        self.buttonMapKeysReset = Button('Deactivate Keys')
        self.placeControl(self.buttonMapKeysReset, 11, 1, columnspan=4)

        self.checkKeyMap()  

        self.labelStatus60hz = Label('')
        self.placeControl(self.labelStatus60hz, 2, 11, columnspan=2, pad_y=11)
        self.labelStatus60hz.setLabel(fsconfig.status60hz)
 
        self.labelStatus59hz = Label('')
        self.placeControl(self.labelStatus59hz, 3, 11, columnspan=2, pad_y=11)
        self.labelStatus59hz.setLabel(fsconfig.status59hz)

        self.labelStatus50hz = Label('')
        self.placeControl(self.labelStatus50hz, 4, 11, columnspan=2, pad_y=11)
        self.labelStatus50hz.setLabel(fsconfig.status50hz)

        self.labelStatus24hz = Label('')
        self.placeControl(self.labelStatus24hz, 5, 11, columnspan=2, pad_y=11)
        self.labelStatus24hz.setLabel(fsconfig.status24hz)

        self.labelStatus23hz = Label('')
        self.placeControl(self.labelStatus23hz, 6, 11, columnspan=2, pad_y=11)
        self.labelStatus23hz.setLabel(fsconfig.status23hz)

        self.labelStatusAuto = Label('')
        self.placeControl(self.labelStatusAuto, 7, 11, columnspan=2, pad_y=11)
        self.labelStatusAuto.setLabel(fsconfig.statusAuto)

        self.labelStatusInfo = Label('')
        self.placeControl(self.labelStatusInfo, 8, 11, columnspan=2, pad_y=11)
        self.labelStatusInfo.setLabel(fsconfig.statusInfo)

        self.labelStatusHiPQTools = Label('')
        self.placeControl(self.labelStatusHiPQTools, 9, 11, columnspan=2, pad_y=11)
        self.labelStatusHiPQTools.setLabel(fsconfig.statusHiPQTools)

        self.labelInfoTitle = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelInfoTitle, 10, 6, columnspan=8, pad_y=11)
        
        self.labelInfoText = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelInfoText, 11, 6, columnspan=8, pad_y=11)

        # connect buttons and actions to functions
        self.connect(self.radio60hz, self.clickRadio60hz)
        self.connect(self.radio59hz, self.clickRadio59hz)
        self.connect(self.radio50hz, self.clickRadio50hz)
        self.connect(self.radio24hz, self.clickRadio24hz)
        self.connect(self.radio23hz, self.clickRadio23hz)
        self.connect(self.radioAuto, self.clickRadioAuto)
        self.connect(self.radioInfo, self.clickRadioInfo)
        self.connect(self.radioHiPQTools, self.clickRadioHiPQTools)
        self.connect(self.buttonMap60hz, self.clickButtonMap60hz)
        self.connect(self.buttonMap59hz, self.clickButtonMap59hz)
        self.connect(self.buttonMap50hz, self.clickButtonMap50hz)
        self.connect(self.buttonMap24hz, self.clickButtonMap24hz)
        self.connect(self.buttonMap23hz, self.clickButtonMap23hz)
        self.connect(self.buttonMapAuto, self.clickButtonMapAuto)
        self.connect(self.buttonMapInfo, self.clickButtonMapInfo)
        self.connect(self.buttonMapHiPQTools, self.clickButtonMapHiPQTools)
        self.connect(self.buttonMapKeysSave, self.clickMapKeysSave)
        self.connect(self.buttonMapKeysReset, self.clickMapKeysReset)       
        self.connect(ACTION_NAV_BACK, self.close)

        # set the enabled state of objects
        self.atSetup = True
        self.clickRadio60hz()
        self.clickRadio59hz()
        self.clickRadio50hz()
        self.clickRadio24hz()
        self.clickRadio23hz()
        self.clickRadioAuto()
        self.clickRadioInfo()
        self.clickRadioHiPQTools()
        self.atSetup = False
        
        # check current display mode setting
        currentOutputMode, currentHiSiliconMode = fsutil.getDisplayMode()
        
        if currentOutputMode == 'unsupported':
            self.labelCurrentRes.setLabel('Unsupported resolution: ' + currentHiSiliconMode)           
            self.disableAll()
        
        elif currentOutputMode == 'invalid':
            self.labelCurrentRes.setLabel('Error: ' + currentHiSiliconMode)       
            self.disableAll()
            
        else:
            # get current resolution
            resSplit = currentOutputMode.find('-')
            self.currentRes = currentOutputMode[0:resSplit]
            self.labelCurrentRes.setLabel('Current resolution: ' + self.currentRes)       

            if self.currentRes == '2160p':
                self.disable59hz()

            if self.currentRes == '720p':
                self.disable24hz()
                
            if self.currentRes == '720p':
                self.disable23hz()

            # check whether res has changed since KeyMap was last saved
            if (self.currentRes != fsconfig.keymapRes) and (fsconfig.keymapRes != ''):
                self.labelCurrentRes.setLabel('Current resolution: ' + self.currentRes + ' (active resolution was ' + fsconfig.keymapRes + ')')       
                self.clickMapKeysReset()

        # define key navigation (up-down)
        self.radio60hz.controlDown(self.radio59hz)
        self.radio59hz.controlUp(self.radio60hz)
        self.radio59hz.controlDown(self.radio50hz)
        self.radio50hz.controlUp(self.radio59hz)
        self.radio50hz.controlDown(self.radio24hz)
        self.radio24hz.controlUp(self.radio50hz)
        self.radio24hz.controlDown(self.radio23hz)
        self.radio23hz.controlUp(self.radio24hz)
        self.radio23hz.controlDown(self.radioAuto)
        self.radioAuto.controlUp(self.radio23hz)
        self.radioAuto.controlDown(self.radioInfo)
        self.radioInfo.controlUp(self.radioAuto)
        self.radioInfo.controlDown(self.radioHiPQTools)
        self.radioHiPQTools.controlUp(self.radioInfo)
        self.radioHiPQTools.controlDown(self.buttonMapKeysSave)      
        self.buttonMapKeysSave.controlUp(self.radioHiPQTools)
        self.buttonMapKeysSave.controlDown(self.buttonMapKeysReset)
        self.buttonMapKeysReset.controlUp(self.buttonMapKeysSave)

        self.buttonMap60hz.controlDown(self.buttonMap59hz)
        self.buttonMap59hz.controlUp(self.buttonMap60hz)
        self.buttonMap59hz.controlDown(self.buttonMap50hz)
        self.buttonMap50hz.controlUp(self.buttonMap59hz)
        self.buttonMap50hz.controlDown(self.buttonMap24hz)
        self.buttonMap24hz.controlUp(self.buttonMap50hz)
        self.buttonMap24hz.controlDown(self.buttonMap23hz)
        self.buttonMap23hz.controlUp(self.buttonMap24hz)
        self.buttonMap23hz.controlDown(self.buttonMapAuto)
        self.buttonMapAuto.controlUp(self.buttonMap23hz)
        self.buttonMapAuto.controlDown(self.buttonMapInfo)
        self.buttonMapInfo.controlUp(self.buttonMapAuto)
        self.buttonMapInfo.controlDown(self.buttonMapHiPQTools)
        self.buttonMapHiPQTools.controlUp(self.buttonMapInfo)
        self.buttonMapHiPQTools.controlDown(self.buttonMapKeysSave)
        
        # define key navigation (left-right)
        self.radio60hz.controlRight(self.buttonMap60hz)
        self.buttonMap60hz.controlLeft(self.radio60hz)
        self.radio59hz.controlRight(self.buttonMap59hz)
        self.buttonMap59hz.controlLeft(self.radio59hz)
        self.radio50hz.controlRight(self.buttonMap50hz)
        self.buttonMap50hz.controlLeft(self.radio50hz)
        self.radio24hz.controlRight(self.buttonMap24hz)
        self.buttonMap24hz.controlLeft(self.radio24hz)
        self.radio23hz.controlRight(self.buttonMap23hz)
        self.buttonMap23hz.controlLeft(self.radio23hz)
        self.radioAuto.controlRight(self.buttonMapAuto)
        self.buttonMapAuto.controlLeft(self.radioAuto)
        self.radioInfo.controlRight(self.buttonMapInfo)
        self.buttonMapInfo.controlLeft(self.radioInfo)
        self.radioHiPQTools.controlRight(self.buttonMapHiPQTools)
        self.buttonMapHiPQTools.controlLeft(self.radioHiPQTools)

        # set initial focus
        self.setFocus(self.radio60hz)

    def disable59hz(self):

        self.radio59hz.setEnabled(False)
        self.buttonMap59hz.setEnabled(False)
        self.labelKey59hz.setEnabled(False)

    def disable24hz(self):

        self.radio24hz.setEnabled(False)
        self.buttonMap24hz.setEnabled(False)
        self.labelKey24hz.setEnabled(False)

    def disable23hz(self):

        self.radio23hz.setEnabled(False)
        self.buttonMap23hz.setEnabled(False)
        self.labelKey23hz.setEnabled(False)

    def disableAll(self):

        self.radio60hz.setEnabled(False)
        self.buttonMap60hz.setEnabled(False)
        self.labelKey60hz.setEnabled(False)

        self.radio59hz.setEnabled(False)
        self.buttonMap59hz.setEnabled(False)
        self.labelKey59hz.setEnabled(False)

        self.radio50hz.setEnabled(False)
        self.buttonMap50hz.setEnabled(False)
        self.labelKey50hz.setEnabled(False)

        self.radio24hz.setEnabled(False)
        self.buttonMap24hz.setEnabled(False)
        self.labelKey24hz.setEnabled(False)

        self.radio23hz.setEnabled(False)
        self.buttonMap23hz.setEnabled(False)
        self.labelKey23hz.setEnabled(False)

        self.radioAuto.setEnabled(False)
        self.buttonMapAuto.setEnabled(False)
        self.labelKeyAuto.setEnabled(False)

        self.radioInfo.setEnabled(False)
        self.buttonMapInfo.setEnabled(False)
        self.labelKeyInfo.setEnabled(False)

        self.radioHiPQTools.setEnabled(False)
        self.buttonMapHiPQTools.setEnabled(False)
        self.labelKeyHiPQTools.setEnabled(False)

        self.buttonMapKeysSave.setEnabled(False)
        self.buttonMapKeysReset.setEnabled(False)

        self.clickMapKeysReset()

    def clickRadio60hz(self):

        if self.radio60hz.isSelected():
            self.buttonMap60hz.setEnabled(True)
            self.labelKey60hz.setEnabled(True)
        else:
            self.buttonMap60hz.setEnabled(False)
            self.labelKey60hz.setEnabled(False)

        if not self.atSetup:
            self.clickMapKeysReset()

    def clickRadio59hz(self):

        if self.radio59hz.isSelected():
            self.buttonMap59hz.setEnabled(True)
            self.labelKey59hz.setEnabled(True)
        else:
            self.buttonMap59hz.setEnabled(False)
            self.labelKey59hz.setEnabled(False)

        if not self.atSetup:
            self.clickMapKeysReset()
                            
    def clickRadio50hz(self):

        if self.radio50hz.isSelected():
            self.buttonMap50hz.setEnabled(True)
            self.labelKey50hz.setEnabled(True)
        else:
            self.buttonMap50hz.setEnabled(False)
            self.labelKey50hz.setEnabled(False)

        if not self.atSetup:
            self.clickMapKeysReset()
                            
    def clickRadio24hz(self):

        if self.radio24hz.isSelected():
            self.buttonMap24hz.setEnabled(True)
            self.labelKey24hz.setEnabled(True)
        else:
            self.buttonMap24hz.setEnabled(False)
            self.labelKey24hz.setEnabled(False)

        if not self.atSetup:
            self.clickMapKeysReset()
                      
    def clickRadio23hz(self):

        if self.radio23hz.isSelected():
            self.buttonMap23hz.setEnabled(True)
            self.labelKey23hz.setEnabled(True)
        else:
            self.buttonMap23hz.setEnabled(False)
            self.labelKey23hz.setEnabled(False)

        if not self.atSetup:
            self.clickMapKeysReset()
                            
    def clickRadioAuto(self):

        if self.radioAuto.isSelected():
            self.buttonMapAuto.setEnabled(True)
            self.labelKeyAuto.setEnabled(True)
        else:
            self.buttonMapAuto.setEnabled(False)
            self.labelKeyAuto.setEnabled(False)

        if not self.atSetup:
            self.clickMapKeysReset()

    def clickRadioInfo(self):

        if self.radioInfo.isSelected():
            self.buttonMapInfo.setEnabled(True)
            self.labelKeyInfo.setEnabled(True)
        else:
            self.buttonMapInfo.setEnabled(False)
            self.labelKeyInfo.setEnabled(False)

        if not self.atSetup:
            self.clickMapKeysReset()

    def clickRadioHiPQTools(self):

        if self.radioHiPQTools.isSelected():
            self.buttonMapHiPQTools.setEnabled(True)
            self.labelKeyHiPQTools.setEnabled(True)
        else:
            self.buttonMapHiPQTools.setEnabled(False)
            self.labelKeyHiPQTools.setEnabled(False)

        if not self.atSetup:
            self.clickMapKeysReset()

    def clickButtonMap60hz(self):
     
        self.clickMapKeysReset()

        keyPressed = fskeylisten.KeyListener.getKeyPressed()
 
        if keyPressed is not None:
            self.labelKey60hz.setLabel(str(keyPressed))
            self.removeDupeKey(keyPressed, '60hz')

    def clickButtonMap59hz(self):
     
        self.clickMapKeysReset()

        keyPressed = fskeylisten.KeyListener.getKeyPressed()
 
        if keyPressed is not None:
            self.labelKey59hz.setLabel(str(keyPressed))
            self.removeDupeKey(keyPressed, '59hz')

    def clickButtonMap50hz(self):
     
        self.clickMapKeysReset()

        keyPressed = fskeylisten.KeyListener.getKeyPressed()
 
        if keyPressed is not None:
            self.labelKey50hz.setLabel(str(keyPressed))
            self.removeDupeKey(keyPressed, '50hz')

    def clickButtonMap24hz(self):
     
        self.clickMapKeysReset()

        keyPressed = fskeylisten.KeyListener.getKeyPressed()
 
        if keyPressed is not None:
            self.labelKey24hz.setLabel(str(keyPressed))
            self.removeDupeKey(keyPressed, '24hz')

    def clickButtonMap23hz(self):
     
        self.clickMapKeysReset()

        keyPressed = fskeylisten.KeyListener.getKeyPressed()
 
        if keyPressed is not None:
            self.labelKey23hz.setLabel(str(keyPressed))
            self.removeDupeKey(keyPressed, '23hz')

    def clickButtonMapAuto(self):
     
        self.clickMapKeysReset()

        keyPressed = fskeylisten.KeyListener.getKeyPressed()
 
        if keyPressed is not None:
            self.labelKeyAuto.setLabel(str(keyPressed))
            self.removeDupeKey(keyPressed, 'Auto')
    
    def clickButtonMapInfo(self):
     
        self.clickMapKeysReset()

        keyPressed = fskeylisten.KeyListener.getKeyPressed()
 
        if keyPressed is not None:
            self.labelKeyInfo.setLabel(str(keyPressed))
            self.removeDupeKey(keyPressed, 'Info')

    def clickButtonMapHiPQTools(self):
     
        self.clickMapKeysReset()

        keyPressed = fskeylisten.KeyListener.getKeyPressed()
 
        if keyPressed is not None:
            self.labelKeyHiPQTools.setLabel(str(keyPressed))
            self.removeDupeKey(keyPressed, 'HiPQTools')

    def removeDupeKey(self, keyPressed, mappedAction):
        
        if (self.labelKey60hz.getLabel() == keyPressed) and (mappedAction != '60hz'):
            self.labelKey60hz.setLabel('')
 
        if (self.labelKey59hz.getLabel() == keyPressed) and (mappedAction != '59hz'):
            self.labelKey59hz.setLabel('')

        if (self.labelKey50hz.getLabel() == keyPressed) and (mappedAction != '50hz'):
            self.labelKey50hz.setLabel('')

        if (self.labelKey24hz.getLabel() == keyPressed) and (mappedAction != '24hz'):
            self.labelKey24hz.setLabel('')

        if (self.labelKey23hz.getLabel() == keyPressed) and (mappedAction != '23hz'):
            self.labelKey23hz.setLabel('')

        if (self.labelKeyAuto.getLabel() == keyPressed) and (mappedAction != 'Auto'):
            self.labelKeyAuto.setLabel('')

        if (self.labelKeyInfo.getLabel() == keyPressed) and (mappedAction != 'Info'):
            self.labelKeyInfo.setLabel('')

        if (self.labelKeyHiPQTools.getLabel() == keyPressed) and (mappedAction != 'HiPQTools'):
            self.labelKeyHiPQTools.setLabel('')

    def clickMapKeysSave(self):
        
        self.labelInfoTitle.setLabel('Keys activating...')
        self.labelInfoText.setLabel('Saving settings...')
        xbmc.sleep(600)
         
        actionRes = self.currentRes

        keyMappings = []

        if self.radio60hz.isSelected():
            if self.labelKey60hz.getLabel() != '':
                keyMappings.insert(0, (self.labelKey60hz.getLabel(), actionRes + '-60hz'))
                self.labelStatus60hz.setLabel('Active')

        if self.radio59hz.isSelected():
            if self.labelKey59hz.getLabel() != '':
                keyMappings.insert(0, (self.labelKey59hz.getLabel(), actionRes + '-59hz'))
                self.labelStatus59hz.setLabel('Active')

        if self.radio50hz.isSelected():
            if self.labelKey50hz.getLabel() != '':
                keyMappings.insert(0, (self.labelKey50hz.getLabel(), actionRes + '-50hz'))
                self.labelStatus50hz.setLabel('Active')

        if self.radio24hz.isSelected() and (actionRes == '1080p'):
            if self.labelKey24hz.getLabel() != '':
                keyMappings.insert(0, (self.labelKey24hz.getLabel(), actionRes + '-24hz'))
                self.labelStatus24hz.setLabel('Active')

        if self.radio23hz.isSelected() and (actionRes == '1080p'):
            if self.labelKey23hz.getLabel() != '':
                keyMappings.insert(0, (self.labelKey23hz.getLabel(), actionRes + '-23hz'))
                self.labelStatus23hz.setLabel('Active')

        if self.radioAuto.isSelected():
            if self.labelKeyAuto.getLabel() != '':
                keyMappings.insert(0, (self.labelKeyAuto.getLabel(), 'auto'))
                self.labelStatusAuto.setLabel('Active')
        
        if self.radioInfo.isSelected():
            if self.labelKeyInfo.getLabel() != '':
                keyMappings.insert(0, (self.labelKeyInfo.getLabel(), 'info'))
                self.labelStatusInfo.setLabel('Active')

        if self.radioHiPQTools.isSelected():
            if self.labelKeyHiPQTools.getLabel() != '':
                keyMappings.insert(0, (self.labelKeyHiPQTools.getLabel(), 'hipqtools'))
                self.labelStatusHiPQTools.setLabel('Active')

        keyScope = 'global'
        
        if not keyMappings:
            mapKeyStatus = "No active keys defined" 
        else:
            mapKeyStatus = fsutil.mapKey(keyScope, keyMappings)
            self.buttonMapKeysReset.setEnabled(True)

        self.labelInfoTitle.setLabel(mapKeyStatus)
        xbmc.sleep(600)

        self.saveAllSettings()

    def clickMapKeysReset(self):
        
        if not fsutil.mapKeyActive():
            self.labelInfoTitle.setLabel('')
            self.labelInfoText.setLabel('')            
        else:
            self.labelInfoTitle.setLabel('Keys deactivating...')
            self.labelInfoText.setLabel('')
            xbmc.sleep(600)
    
            self.labelStatus60hz.setLabel('')
            self.labelStatus59hz.setLabel('')
            self.labelStatus50hz.setLabel('')
            self.labelStatus24hz.setLabel('')
            self.labelStatus23hz.setLabel('')
            self.labelStatusAuto.setLabel('')
            self.labelStatusInfo.setLabel('')
            self.labelStatusHiPQTools.setLabel('')
                        
            mapKeyResetStatus = fsutil.mapKeyReset()
    
            self.labelInfoTitle.setLabel(mapKeyResetStatus)
            xbmc.sleep(600)
    
            self.saveStatusSettings()
    
            self.buttonMapKeysReset.setEnabled(False)

    def checkKeyMap(self):
            
        # check whether keymap has been deleted or renamed by another add-on (e.g Keymap Editor)
        if not fsutil.mapKeyActive():

            # reload key maps
            xbmc.executebuiltin('action(reloadkeymaps)')

            fsconfig.status60hz = ''
            fsconfig.status59hz = ''
            fsconfig.status50hz = ''
            fsconfig.status24hz = ''
            fsconfig.status23hz = ''
            fsconfig.statusAuto = ''
            fsconfig.statusInfo = ''            
            fsconfig.statusHiPQTools = ''
            fsconfig.keymapRes = ''
            
            saveSettingsStatus = fsconfigutil.saveSettings()
 
            self.buttonMapKeysReset.setEnabled(False)
    
    def saveStatusSettings(self):
        
        fsconfig.status60hz = self.labelStatus60hz.getLabel()
        fsconfig.status59hz = self.labelStatus50hz.getLabel()
        fsconfig.status50hz = self.labelStatus50hz.getLabel()
        fsconfig.status24hz = self.labelStatus24hz.getLabel()
        fsconfig.status23hz = self.labelStatus24hz.getLabel()
        fsconfig.statusAuto = self.labelStatusAuto.getLabel()
        fsconfig.statusInfo = self.labelStatusInfo.getLabel()       
        fsconfig.statusHiPQTools = self.labelStatusHiPQTools.getLabel()       
        fsconfig.keymapRes = ''
        
        saveSettingsStatus = fsconfigutil.saveSettings()
        
    def saveAllSettings(self):
        
        fsconfig.radio60hz = self.radio60hz.isSelected()
        fsconfig.radio59hz = self.radio59hz.isSelected()
        fsconfig.radio50hz = self.radio50hz.isSelected()
        fsconfig.radio24hz = self.radio24hz.isSelected()
        fsconfig.radio23hz = self.radio23hz.isSelected()
        fsconfig.radioAuto = self.radioAuto.isSelected()
        fsconfig.radioInfo = self.radioInfo.isSelected() 
        fsconfig.radioHiPQTools = self.radioHiPQTools.isSelected()
        fsconfig.key60hz = self.labelKey60hz.getLabel()
        fsconfig.key59hz = self.labelKey59hz.getLabel()
        fsconfig.key50hz = self.labelKey50hz.getLabel()
        fsconfig.key24hz = self.labelKey24hz.getLabel()
        fsconfig.key23hz = self.labelKey23hz.getLabel()
        fsconfig.keyAuto = self.labelKeyAuto.getLabel()
        fsconfig.keyInfo = self.labelKeyInfo.getLabel()
        fsconfig.keyHiPQTools = self.labelKeyHiPQTools.getLabel()
        fsconfig.status60hz = self.labelStatus60hz.getLabel()
        fsconfig.status59hz = self.labelStatus59hz.getLabel()
        fsconfig.status50hz = self.labelStatus50hz.getLabel()
        fsconfig.status24hz = self.labelStatus24hz.getLabel()
        fsconfig.status23hz = self.labelStatus23hz.getLabel()
        fsconfig.statusAuto = self.labelStatusAuto.getLabel()
        fsconfig.statusInfo = self.labelStatusInfo.getLabel()   
        fsconfig.statusHiPQTools = self.labelStatusHiPQTools.getLabel()
        fsconfig.keymapRes = self.currentRes
        
        saveSettingsStatus = fsconfigutil.saveSettings()

        self.labelInfoText.setLabel(saveSettingsStatus)

class ConfigWindow(AddonDialogWindow):
    
    def __init__(self, title=''):
        # base class constructor
        super(ConfigWindow, self).__init__(title)

        # set window width + height, and grid rows + columns
        self.setGeometry(750, 650, 12, 26)

        # create, place, then set objects
        self.radio60hz = RadioButton('60 hz')
        self.placeControl(self.radio60hz, 2, 2, columnspan=6)
        self.radio60hz.setSelected(fsconfig.radioAuto60hz)
         
        self.radio59hz = RadioButton('59 hz')
        self.placeControl(self.radio59hz, 3, 2, columnspan=6)
        self.radio59hz.setSelected(fsconfig.radioAuto59hz)

        self.radio50hz = RadioButton('50 hz')
        self.placeControl(self.radio50hz, 4, 2, columnspan=6)
        self.radio50hz.setSelected(fsconfig.radioAuto50hz)
 
        self.radio24hz = RadioButton('24 hz')
        self.placeControl(self.radio24hz, 5, 2, columnspan=6)
        self.radio24hz.setSelected(fsconfig.radioAuto24hz)

        self.radio23hz = RadioButton('23 hz')
        self.placeControl(self.radio23hz, 6, 2, columnspan=6)
        self.radio23hz.setSelected(fsconfig.radioAuto23hz)

        self.edit60hzFps1 = Edit('')
        self.placeControl(self.edit60hzFps1, 2, 9, columnspan=3, pad_y=11)
        self.edit60hzFps1.setText(fsconfig.edit60hzFps1)

        self.edit60hzFps2 = Edit('')
        self.placeControl(self.edit60hzFps2, 2, 13, columnspan=3, pad_y=11)
        self.edit60hzFps2.setText(fsconfig.edit60hzFps2)
        
        self.edit60hzFps3 = Edit('')
        self.placeControl(self.edit60hzFps3, 2, 17, columnspan=3, pad_y=11)
        self.edit60hzFps3.setText(fsconfig.edit60hzFps3)
        
        self.edit60hzFps4 = Edit('')
        self.placeControl(self.edit60hzFps4, 2, 21, columnspan=3, pad_y=11)
        self.edit60hzFps4.setText(fsconfig.edit60hzFps4)
        
        self.edit59hzFps1 = Edit('')
        self.placeControl(self.edit59hzFps1, 3, 9, columnspan=3, pad_y=11)
        self.edit59hzFps1.setText(fsconfig.edit59hzFps1)

        self.edit59hzFps2 = Edit('')
        self.placeControl(self.edit59hzFps2, 3, 13, columnspan=3, pad_y=11)
        self.edit59hzFps2.setText(fsconfig.edit59hzFps2)
        
        self.edit59hzFps3 = Edit('')
        self.placeControl(self.edit59hzFps3, 3, 17, columnspan=3, pad_y=11)
        self.edit59hzFps3.setText(fsconfig.edit59hzFps3)
        
        self.edit59hzFps4 = Edit('')
        self.placeControl(self.edit59hzFps4, 3, 21, columnspan=3, pad_y=11)
        self.edit59hzFps4.setText(fsconfig.edit59hzFps4)

        self.edit50hzFps1 = Edit('')
        self.placeControl(self.edit50hzFps1, 4, 9, columnspan=3, pad_y=11)
        self.edit50hzFps1.setText(fsconfig.edit50hzFps1)

        self.edit50hzFps2 = Edit('')
        self.placeControl(self.edit50hzFps2, 4, 13, columnspan=3, pad_y=11)
        self.edit50hzFps2.setText(fsconfig.edit50hzFps2)
        
        self.edit50hzFps3 = Edit('')
        self.placeControl(self.edit50hzFps3, 4, 17, columnspan=3, pad_y=11)
        self.edit50hzFps3.setText(fsconfig.edit50hzFps3)
        
        self.edit50hzFps4 = Edit('')
        self.placeControl(self.edit50hzFps4, 4, 21, columnspan=3, pad_y=11)
        self.edit50hzFps4.setText(fsconfig.edit50hzFps4)
                
        self.edit24hzFps1 = Edit('')
        self.placeControl(self.edit24hzFps1, 5, 9, columnspan=3, pad_y=11)
        self.edit24hzFps1.setText(fsconfig.edit24hzFps1)

        self.edit24hzFps2 = Edit('')
        self.placeControl(self.edit24hzFps2, 5, 13, columnspan=3, pad_y=11)
        self.edit24hzFps2.setText(fsconfig.edit24hzFps2)
        
        self.edit24hzFps3 = Edit('')
        self.placeControl(self.edit24hzFps3, 5, 17, columnspan=3, pad_y=11)
        self.edit24hzFps3.setText(fsconfig.edit24hzFps3)
        
        self.edit24hzFps4 = Edit('')
        self.placeControl(self.edit24hzFps4, 5, 21, columnspan=3, pad_y=11)
        self.edit24hzFps4.setText(fsconfig.edit24hzFps4)
        
        self.edit23hzFps1 = Edit('')
        self.placeControl(self.edit23hzFps1, 6, 9, columnspan=3, pad_y=11)
        self.edit23hzFps1.setText(fsconfig.edit23hzFps1)

        self.edit23hzFps2 = Edit('')
        self.placeControl(self.edit23hzFps2, 6, 13, columnspan=3, pad_y=11)
        self.edit23hzFps2.setText(fsconfig.edit23hzFps2)
        
        self.edit23hzFps3 = Edit('')
        self.placeControl(self.edit23hzFps3, 6, 17, columnspan=3, pad_y=11)
        self.edit23hzFps3.setText(fsconfig.edit23hzFps3)
        
        self.edit23hzFps4 = Edit('')
        self.placeControl(self.edit23hzFps4, 6, 21, columnspan=3, pad_y=11)
        self.edit23hzFps4.setText(fsconfig.edit23hzFps4)

        self.buttonConfigSave = Button('Save Configuration')
        self.placeControl(self.buttonConfigSave, 9, 2, columnspan=8)

        self.labelInfoTitle = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelInfoTitle, 9, 12, columnspan=16, pad_y=11)
        
        self.labelInfoText = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelInfoText, 10, 12, columnspan=16, pad_y=11)
        
        # connect buttons and actions to functions
        self.connect(self.radio60hz, self.clickRadio60hz)
        self.connect(self.radio59hz, self.clickRadio59hz)
        self.connect(self.radio50hz, self.clickRadio50hz)
        self.connect(self.radio24hz, self.clickRadio24hz)
        self.connect(self.radio23hz, self.clickRadio23hz)
        self.connect(self.buttonConfigSave, self.clickConfigSave)
        self.connect(ACTION_NAV_BACK, self.close)
        
        # set the enabled state of objects
        self.clickRadio60hz()
        self.clickRadio59hz()
        self.clickRadio50hz()
        self.clickRadio24hz()
        self.clickRadio23hz()

        # define key navigation (up-down)
        self.radio60hz.controlDown(self.radio59hz)
        self.radio59hz.controlDown(self.radio50hz)
        self.radio59hz.controlUp(self.radio60hz)
        self.radio50hz.controlUp(self.radio59hz)
        self.radio50hz.controlDown(self.radio24hz)
        self.radio24hz.controlUp(self.radio50hz)
        self.radio24hz.controlDown(self.radio23hz)
        self.radio23hz.controlUp(self.radio24hz)
        self.radio23hz.controlDown(self.buttonConfigSave)
        self.buttonConfigSave.controlUp(self.radio23hz)
        
        self.edit60hzFps1.controlDown(self.edit59hzFps1)
        self.edit59hzFps1.controlUp(self.edit60hzFps1)
        self.edit59hzFps1.controlDown(self.edit50hzFps1)
        self.edit50hzFps1.controlUp(self.edit59hzFps1)
        self.edit50hzFps1.controlDown(self.edit24hzFps1)
        self.edit24hzFps1.controlUp(self.edit50hzFps1)
        self.edit24hzFps1.controlDown(self.edit23hzFps1)
        self.edit23hzFps1.controlUp(self.edit24hzFps1)
        self.edit23hzFps1.controlDown(self.buttonConfigSave)
        
        self.edit60hzFps2.controlDown(self.edit59hzFps2)
        self.edit59hzFps2.controlUp(self.edit60hzFps2)
        self.edit59hzFps2.controlDown(self.edit50hzFps2)
        self.edit50hzFps2.controlUp(self.edit59hzFps2)
        self.edit50hzFps2.controlDown(self.edit24hzFps2)
        self.edit24hzFps2.controlUp(self.edit50hzFps2)
        self.edit24hzFps2.controlDown(self.edit23hzFps2)
        self.edit23hzFps2.controlUp(self.edit24hzFps2)
        self.edit23hzFps2.controlDown(self.buttonConfigSave)

        self.edit60hzFps3.controlDown(self.edit59hzFps3)
        self.edit59hzFps3.controlUp(self.edit60hzFps3)
        self.edit59hzFps3.controlDown(self.edit50hzFps3)
        self.edit50hzFps3.controlUp(self.edit59hzFps3)
        self.edit50hzFps3.controlDown(self.edit24hzFps3)
        self.edit24hzFps3.controlUp(self.edit50hzFps3)
        self.edit24hzFps3.controlDown(self.edit23hzFps3)
        self.edit23hzFps3.controlUp(self.edit24hzFps3)
        self.edit23hzFps3.controlDown(self.buttonConfigSave)
        
        self.edit60hzFps4.controlDown(self.edit59hzFps4)
        self.edit59hzFps4.controlUp(self.edit60hzFps4)
        self.edit59hzFps4.controlDown(self.edit50hzFps4)
        self.edit50hzFps4.controlUp(self.edit59hzFps4)
        self.edit50hzFps4.controlDown(self.edit24hzFps4)
        self.edit24hzFps4.controlUp(self.edit50hzFps4)
        self.edit24hzFps4.controlDown(self.edit23hzFps4)
        self.edit23hzFps4.controlUp(self.edit24hzFps4)
        self.edit23hzFps4.controlDown(self.buttonConfigSave)

        # define key navigation (left-right)
        self.radio60hz.controlRight(self.edit60hzFps1)
        self.edit60hzFps1.controlLeft(self.radio60hz)
        self.edit60hzFps1.controlRight(self.edit60hzFps2)
        self.edit60hzFps2.controlLeft(self.edit60hzFps1)
        self.edit60hzFps2.controlRight(self.edit60hzFps3)
        self.edit60hzFps3.controlLeft(self.edit60hzFps2)
        self.edit60hzFps3.controlRight(self.edit60hzFps4)
        self.edit60hzFps4.controlLeft(self.edit60hzFps3)
        
        self.radio59hz.controlRight(self.edit59hzFps1)
        self.edit59hzFps1.controlLeft(self.radio59hz)
        self.edit59hzFps1.controlRight(self.edit59hzFps2)
        self.edit59hzFps2.controlLeft(self.edit59hzFps1)
        self.edit59hzFps2.controlRight(self.edit59hzFps3)
        self.edit59hzFps3.controlLeft(self.edit59hzFps2)
        self.edit59hzFps3.controlRight(self.edit59hzFps4)
        self.edit59hzFps4.controlLeft(self.edit59hzFps3)

        self.radio50hz.controlRight(self.edit50hzFps1)
        self.edit50hzFps1.controlLeft(self.radio50hz)
        self.edit50hzFps1.controlRight(self.edit50hzFps2)
        self.edit50hzFps2.controlLeft(self.edit50hzFps1)
        self.edit50hzFps2.controlRight(self.edit50hzFps3)
        self.edit50hzFps3.controlLeft(self.edit50hzFps2)
        self.edit50hzFps3.controlRight(self.edit50hzFps4)
        self.edit50hzFps4.controlLeft(self.edit50hzFps3)

        self.radio24hz.controlRight(self.edit24hzFps1)
        self.edit24hzFps1.controlLeft(self.radio24hz)
        self.edit24hzFps1.controlRight(self.edit24hzFps2)
        self.edit24hzFps2.controlLeft(self.edit24hzFps1)
        self.edit24hzFps2.controlRight(self.edit24hzFps3)
        self.edit24hzFps3.controlLeft(self.edit24hzFps2)
        self.edit24hzFps3.controlRight(self.edit24hzFps4)
        self.edit24hzFps4.controlLeft(self.edit24hzFps3)

        self.radio23hz.controlRight(self.edit23hzFps1)
        self.edit23hzFps1.controlLeft(self.radio23hz)
        self.edit23hzFps1.controlRight(self.edit23hzFps2)
        self.edit23hzFps2.controlLeft(self.edit23hzFps1)
        self.edit23hzFps2.controlRight(self.edit23hzFps3)
        self.edit23hzFps3.controlLeft(self.edit23hzFps2)
        self.edit23hzFps3.controlRight(self.edit23hzFps4)
        self.edit23hzFps4.controlLeft(self.edit23hzFps3)

        # set initial focus
        self.setFocus(self.radio60hz)

    def clickRadio60hz(self):

        if self.radio60hz.isSelected():
            self.edit60hzFps1.setEnabled(True)
            self.edit60hzFps2.setEnabled(True)
            self.edit60hzFps3.setEnabled(True)
            self.edit60hzFps4.setEnabled(True)
        else:
            self.edit60hzFps1.setEnabled(False)
            self.edit60hzFps2.setEnabled(False)
            self.edit60hzFps3.setEnabled(False)
            self.edit60hzFps4.setEnabled(False)

    def clickRadio59hz(self):

        if self.radio59hz.isSelected():
            self.edit59hzFps1.setEnabled(True)
            self.edit59hzFps2.setEnabled(True)
            self.edit59hzFps3.setEnabled(True)
            self.edit59hzFps4.setEnabled(True)
        else:
            self.edit59hzFps1.setEnabled(False)
            self.edit59hzFps2.setEnabled(False)
            self.edit59hzFps3.setEnabled(False)
            self.edit59hzFps4.setEnabled(False)

    def clickRadio50hz(self):

        if self.radio50hz.isSelected():
            self.edit50hzFps1.setEnabled(True)
            self.edit50hzFps2.setEnabled(True)
            self.edit50hzFps3.setEnabled(True)
            self.edit50hzFps4.setEnabled(True)
        else:
            self.edit50hzFps1.setEnabled(False)
            self.edit50hzFps2.setEnabled(False)
            self.edit50hzFps3.setEnabled(False)
            self.edit50hzFps4.setEnabled(False)

    def clickRadio24hz(self):

        if self.radio24hz.isSelected():
            self.edit24hzFps1.setEnabled(True)
            self.edit24hzFps2.setEnabled(True)
            self.edit24hzFps3.setEnabled(True)
            self.edit24hzFps4.setEnabled(True)
        else:
            self.edit24hzFps1.setEnabled(False)
            self.edit24hzFps2.setEnabled(False)
            self.edit24hzFps3.setEnabled(False)
            self.edit24hzFps4.setEnabled(False)
    
    def clickRadio23hz(self):

        if self.radio23hz.isSelected():
            self.edit23hzFps1.setEnabled(True)
            self.edit23hzFps2.setEnabled(True)
            self.edit23hzFps3.setEnabled(True)
            self.edit23hzFps4.setEnabled(True)
        else:
            self.edit23hzFps1.setEnabled(False)
            self.edit23hzFps2.setEnabled(False)
            self.edit23hzFps3.setEnabled(False)
            self.edit23hzFps4.setEnabled(False)

    def clickConfigSave(self):
  
        self.labelInfoTitle.setLabel('Verifying settings...')
        self.labelInfoText.setLabel('')
        xbmc.sleep(600)
        
        fpsEditList = [self.edit60hzFps1,  
                       self.edit60hzFps2, 
                       self.edit60hzFps3, 
                       self.edit60hzFps4, 
                       self.edit59hzFps1, 
                       self.edit59hzFps2, 
                       self.edit59hzFps3, 
                       self.edit59hzFps4,
                       self.edit50hzFps1, 
                       self.edit50hzFps2, 
                       self.edit50hzFps3, 
                       self.edit50hzFps4,
                       self.edit24hzFps1,
                       self.edit24hzFps2, 
                       self.edit24hzFps3, 
                       self.edit24hzFps4,
                       self.edit23hzFps1, 
                       self.edit23hzFps2, 
                       self.edit23hzFps3, 
                       self.edit23hzFps4]

        self.fpsList = []       # FPS list for duplicate checking

        fpsIsValid = True
        for (fpsEditItem) in fpsEditList:
            if fpsIsValid:
                fpsIsValid, fpsMsg = self.verifyFPS(fpsEditItem)
                
        if not fpsIsValid:
            self.labelInfoTitle.setLabel(fpsMsg)
            self.labelInfoText.setLabel('Settings not saved')
        else:     
            self.labelInfoTitle.setLabel('Settings verified')
            self.labelInfoText.setLabel('Saving settings...')
            xbmc.sleep(600)
         
            self.saveFpsSettings()

    def verifyFPS(self, editFps):
    
        currentFps = editFps.getText()

        if currentFps == '':
            fpsIsValid = True
            fpsMsg = ''

        else:              
            # check that edit field contains a number
            try:
                numCurrentFps = float(currentFps)
            # not a valid number - set field text to red
            except ValueError:
                fpsIsValid = False
                fpsMsg = 'Invalid FPS: ' + currentFps
            
            # is a valid number
            else:    
     
                # number is outside reasonable FPS range (1-70)
                if (numCurrentFps < 1) or (numCurrentFps > 70):
                    fpsIsValid = False
                    fpsMsg = 'Invalid FPS: ' + currentFps
     
                # number is within reasonable FPS range (1-70)
                else:
     
                    # truncate FPS to three decimal places
                    decSplit = currentFps.find('.') + 4
                    newFps = currentFps[0:decSplit]
             
                    # check fpsList for duplicates
                    dupeFpsFound = False
                    for (fpsItem) in self.fpsList:
                        if fpsItem == newFps:
                            dupeFpsFound = True
                            break

                    # duplicate FPS detected
                    if dupeFpsFound:
                        fpsIsValid = False
                        fpsMsg = 'Duplicate FPS: ' + currentFps
                    
                    # no duplicate FPS detected
                    else:
                        fpsIsValid = True
                 
                        if currentFps == newFps:
                            fpsMsg = 'OK - FPS verified.'
                        else:
                            editFps.setText(newFps)
                            fpsMsg = 'OK - FPS truncated: ' + currentFps
                    
                        # add FPS to list for dupe checking
                        self.fpsList.insert(0, currentFps)
                
        return fpsIsValid, fpsMsg

    def saveFpsSettings(self):
        
        fsconfig.edit60hzFps1 = self.edit60hzFps1.getText() 
        fsconfig.edit60hzFps2 = self.edit60hzFps2.getText() 
        fsconfig.edit60hzFps3 = self.edit60hzFps3.getText() 
        fsconfig.edit60hzFps4 = self.edit60hzFps4.getText() 
        fsconfig.edit59hzFps1 = self.edit59hzFps1.getText() 
        fsconfig.edit59hzFps2 = self.edit59hzFps2.getText() 
        fsconfig.edit59hzFps3 = self.edit59hzFps3.getText() 
        fsconfig.edit59hzFps4 = self.edit59hzFps4.getText() 
        fsconfig.edit50hzFps1 = self.edit50hzFps1.getText() 
        fsconfig.edit50hzFps2 = self.edit50hzFps2.getText() 
        fsconfig.edit50hzFps3 = self.edit50hzFps3.getText() 
        fsconfig.edit50hzFps4 = self.edit50hzFps4.getText() 
        fsconfig.edit24hzFps1 = self.edit24hzFps1.getText() 
        fsconfig.edit24hzFps2 = self.edit24hzFps2.getText() 
        fsconfig.edit24hzFps3 = self.edit24hzFps3.getText() 
        fsconfig.edit24hzFps4 = self.edit24hzFps4.getText() 
        fsconfig.edit23hzFps1 = self.edit23hzFps1.getText() 
        fsconfig.edit23hzFps2 = self.edit23hzFps2.getText() 
        fsconfig.edit23hzFps3 = self.edit23hzFps3.getText() 
        fsconfig.edit23hzFps4 = self.edit23hzFps4.getText() 

        fsconfig.radioAuto60hz = self.radio60hz.isSelected()
        fsconfig.radioAuto59hz = self.radio59hz.isSelected()
        fsconfig.radioAuto50hz = self.radio50hz.isSelected()
        fsconfig.radioAuto24hz = self.radio24hz.isSelected()
        fsconfig.radioAuto23hz = self.radio23hz.isSelected()
        
        saveSettingsStatus = fsconfigutil.saveSettings()

        self.labelInfoText.setLabel(saveSettingsStatus)

class MapEventsWindow(AddonDialogWindow):

    def __init__(self, title=''):
        # base class constructor
        super(MapEventsWindow, self).__init__(title)

        # set window width + height, and grid rows + columns
        self.setGeometry(750, 650, 12, 26)

        # create, place, then set objects
        self.labelCurrentRes = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelCurrentRes, 1, 2, columnspan=20, pad_y=11)    

        self.labelActiveService = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelActiveService, 2, 2, columnspan=20, pad_y=11)    

        self.radioOnPlayStart = RadioButton('Playback Starts')
        self.placeControl(self.radioOnPlayStart, 3, 2, columnspan=8)
        self.radioOnPlayStart.setSelected(fsconfig.radioOnPlayStart)

        self.labelOnPlayStart = Label('Auto-set HDMI mode on playback start', alignment=ALIGN_LEFT)
        self.placeControl(self.labelOnPlayStart, 3, 11, columnspan=14, pad_y=11)    
         
        self.radioOnPlayStop60 = RadioButton('Default 60 hz')
        self.placeControl(self.radioOnPlayStop60, 4, 2, columnspan=8)
        self.radioOnPlayStop60.setSelected(fsconfig.radioOnPlayStop60)
 
        self.labelOnPlayStop60 = Label('Set mode to 60 hz on playback stop', alignment=ALIGN_LEFT)
        self.placeControl(self.labelOnPlayStop60, 4, 11, columnspan=14, pad_y=11)    

        self.radioOnPlayStop50 = RadioButton('Default 50 hz')
        self.placeControl(self.radioOnPlayStop50, 5, 2, columnspan=8)
        self.radioOnPlayStop50.setSelected(fsconfig.radioOnPlayStop50)
 
        self.labelOnPlayStop50 = Label('Set mode to 50 hz on playback stop', alignment=ALIGN_LEFT)
        self.placeControl(self.labelOnPlayStop50, 5, 11, columnspan=14, pad_y=11)    

        self.radioOnPlayStop24 = RadioButton('Default 24 hz')
        self.placeControl(self.radioOnPlayStop24, 6, 2, columnspan=8)
        self.radioOnPlayStop24.setSelected(fsconfig.radioOnPlayStop24)
 
        self.labelOnPlayStop24 = Label('Set mode to 24 hz on playback stop', alignment=ALIGN_LEFT)
        self.placeControl(self.labelOnPlayStop24, 6, 11, columnspan=14, pad_y=11)    

        self.radioOnPlayStop23 = RadioButton('Default 23.97 hz')
        self.placeControl(self.radioOnPlayStop23, 7, 2, columnspan=8)
        self.radioOnPlayStop23.setSelected(fsconfig.radioOnPlayStop23)
 
        self.labelOnPlayStop23 = Label('Set mode to 23.976 hz on playback stop', alignment=ALIGN_LEFT)
        self.placeControl(self.labelOnPlayStop23, 7, 11, columnspan=14, pad_y=11)    

        self.radioNotifyOn = RadioButton('')
        self.placeControl(self.radioNotifyOn, 8, 2, columnspan=8)
        self.radioNotifyOn.setSelected(fsconfig.radioNotifyOn)

        self.buttonConfigSave = Button('Save Configuration')
        self.placeControl(self.buttonConfigSave, 10, 2, columnspan=8)

        self.labelInfoTitle = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelInfoTitle, 10, 12, columnspan=16, pad_y=11)
        
#         self.labelInfoText = Label('', alignment=ALIGN_LEFT)
#         self.placeControl(self.labelInfoText, 11, 12, columnspan=16, pad_y=11)
        
        # check current display mode setting
        currentOutputMode, currentHiSiliconMode = fsutil.getDisplayMode()
        
        if currentOutputMode == 'unsupported':
            self.labelCurrentRes.setLabel('Unsupported resolution: ' + currentHiSiliconMode)           
            self.disableAll()
        
        elif currentOutputMode == 'invalid':
            self.labelCurrentRes.setLabel('Error: ' + currentHiSiliconMode)       
            self.disableAll()
            
        else:
            # get current resolution
            resSplit = currentOutputMode.find('-')
            self.currentRes = currentOutputMode[0:resSplit]
            self.labelCurrentRes.setLabel('Current resolution: ' + self.currentRes)       

        # connect buttons and actions to functions
        self.connect(self.radioOnPlayStart, self.clickRadioOnPlayStart)
        self.connect(self.radioOnPlayStop60, self.clickRadioOnPlayStop60)
        self.connect(self.radioOnPlayStop50, self.clickRadioOnPlayStop50)
        self.connect(self.radioOnPlayStop24, self.clickRadioOnPlayStop24)
        self.connect(self.radioOnPlayStop23, self.clickRadioOnPlayStop23)
        self.connect(self.radioNotifyOn, self.clickRadioNotifyOn)
        self.connect(self.buttonConfigSave, self.clickConfigSave)
        self.connect(ACTION_NAV_BACK, self.close)
        
        # set the enabled state of objects
        self.checkIfActive()
        self.clickRadioOnPlayStop60()
        self.clickRadioOnPlayStop50()
        self.clickRadioOnPlayStop24()
        self.clickRadioOnPlayStop23()
        self.clickRadioNotifyOn()
        self.clickRadioOnPlayStart()

        # define key navigation (up-down)
        self.radioOnPlayStart.controlDown(self.radioOnPlayStop60)
        self.radioOnPlayStop60.controlUp(self.radioOnPlayStart)

        self.radioOnPlayStop60.controlDown(self.radioOnPlayStop50)
        self.radioOnPlayStop50.controlUp(self.radioOnPlayStop60)
        
        self.radioOnPlayStop50.controlDown(self.radioOnPlayStop24)
        self.radioOnPlayStop24.controlUp(self.radioOnPlayStop50)

        self.radioOnPlayStop24.controlDown(self.radioOnPlayStop23)
        self.radioOnPlayStop23.controlUp(self.radioOnPlayStop24)

        self.radioOnPlayStop23.controlDown(self.radioNotifyOn)
        self.radioNotifyOn.controlUp(self.radioOnPlayStop23)

        self.radioNotifyOn.controlDown(self.buttonConfigSave)
        self.buttonConfigSave.controlUp(self.radioNotifyOn)

        # set initial focus
        self.setFocus(self.radioOnPlayStart)

    def clickRadioOnPlayStart(self):
        if self.radioOnPlayStart.isSelected():
            self.labelOnPlayStart.setEnabled(True)
            self.radioOnPlayStop60.setEnabled(True)
            self.radioOnPlayStop50.setEnabled(True)
            self.radioOnPlayStop24.setEnabled(True)
            self.radioOnPlayStop23.setEnabled(True)
            self.clickRadioOnPlayStop60()
            self.clickRadioOnPlayStop50()
            self.clickRadioOnPlayStop24()
            self.clickRadioOnPlayStop23()
            self.radioNotifyOn.setEnabled(True)
        else:
            self.labelOnPlayStart.setEnabled(False)            
            self.radioOnPlayStop60.setEnabled(False)
            self.radioOnPlayStop50.setEnabled(False)
            self.radioOnPlayStop24.setEnabled(False)
            self.radioOnPlayStop23.setEnabled(False)
            self.labelOnPlayStop60.setEnabled(False)
            self.labelOnPlayStop50.setEnabled(False)
            self.labelOnPlayStop24.setEnabled(False)
            self.labelOnPlayStop23.setEnabled(False)
            self.radioNotifyOn.setEnabled(False)
        
        self.checkIfActive()
            
    def clickRadioOnPlayStop60(self):
        if self.radioOnPlayStop60.isSelected():
            self.labelOnPlayStop60.setEnabled(True)
            self.radioOnPlayStop50.setSelected(False)
            self.radioOnPlayStop24.setSelected(False)
            self.radioOnPlayStop23.setSelected(False)
            self.labelOnPlayStop50.setEnabled(False)
            self.labelOnPlayStop24.setEnabled(False)
            self.labelOnPlayStop23.setEnabled(False)
        else:
            self.labelOnPlayStop60.setEnabled(False)            

        self.checkIfActive()

    def clickRadioOnPlayStop50(self):
        if self.radioOnPlayStop50.isSelected():
            self.labelOnPlayStop50.setEnabled(True)
            self.radioOnPlayStop60.setSelected(False)
            self.radioOnPlayStop24.setSelected(False)
            self.radioOnPlayStop23.setSelected(False)
            self.labelOnPlayStop60.setEnabled(False)
            self.labelOnPlayStop24.setEnabled(False)
            self.labelOnPlayStop23.setEnabled(False)
        else:
            self.labelOnPlayStop50.setEnabled(False)            

        self.checkIfActive()
        
    def clickRadioOnPlayStop24(self):
        if self.radioOnPlayStop24.isSelected():
            self.labelOnPlayStop24.setEnabled(True)
            self.radioOnPlayStop60.setSelected(False)
            self.radioOnPlayStop50.setSelected(False)
            self.radioOnPlayStop23.setSelected(False)
            self.labelOnPlayStop60.setEnabled(False)
            self.labelOnPlayStop50.setEnabled(False)
            self.labelOnPlayStop23.setEnabled(False)
        else:
            self.labelOnPlayStop24.setEnabled(False)            

        self.checkIfActive()

    def clickRadioOnPlayStop23(self):
        if self.radioOnPlayStop23.isSelected():
            self.labelOnPlayStop23.setEnabled(True)
            self.radioOnPlayStop60.setSelected(False)
            self.radioOnPlayStop50.setSelected(False)
            self.radioOnPlayStop24.setSelected(False)
            self.labelOnPlayStop60.setEnabled(False)
            self.labelOnPlayStop50.setEnabled(False)
            self.labelOnPlayStop24.setEnabled(False)
        else:
            self.labelOnPlayStop23.setEnabled(False)            

        self.checkIfActive()

    def checkIfActive(self):
        
        fsconfigutil.loadActiveServiceSetting()
        
        if fsconfig.activeService:
            if fsconfig.radioOnPlayStart:
                self.labelActiveService.setLabel('Service running')
            else:
                self.labelActiveService.setLabel('Service running - restart KODI')
            
        else:
            if fsconfig.radioOnPlayStart:
                self.labelActiveService.setLabel('Service stopped - restart KODI')
            else:
                self.labelActiveService.setLabel('Service stopped')

    def clickRadioNotifyOn(self):
        if self.radioNotifyOn.isSelected():
            self.radioNotifyOn.setLabel('Notifications On') 
        else:
            self.radioNotifyOn.setLabel('Notifications Off') 
    
        self.checkIfActive()
        
    def clickConfigSave(self):
        self.labelInfoTitle.setLabel('Saving settings...')
        xbmc.sleep(600)
                
        fsconfig.radioOnPlayStart = self.radioOnPlayStart.isSelected()
        fsconfig.radioOnPlayStop60 = self.radioOnPlayStop60.isSelected()
        fsconfig.radioOnPlayStop50 = self.radioOnPlayStop50.isSelected()
        fsconfig.radioOnPlayStop24 = self.radioOnPlayStop24.isSelected()
        fsconfig.radioOnPlayStop23 = self.radioOnPlayStop23.isSelected()
        fsconfig.radioNotifyOn = self.radioNotifyOn.isSelected()
        
        saveSettingsStatus = fsconfigutil.saveSettings()

        if not fsconfig.radioOnPlayStart:
            xbmc.sleep(4500)            

        self.labelInfoTitle.setLabel(saveSettingsStatus)

        self.checkIfActive()
        
    def disableAll(self):

        self.labelInfoTitle.setEnabled(False)
        self.labelActiveService.setEnabled(False)

        self.radioOnPlayStart.setEnabled(False)
        self.radioOnPlayStop60.setEnabled(False)
        self.radioOnPlayStop50.setEnabled(False)
        self.radioNotifyOn.setEnabled(False)
        self.buttonConfigSave.setEnabled(False)

        self.disableService()

    def disableService(self):
        
        self.radioOnPlayStart.setSelected(False)
        
        self.clickRadioOnPlayStart()

        self.clickConfigSave()
        
class MainWindow(AddonDialogWindow):

    def __init__(self, title=''):
        # base class constructor
        super(MainWindow, self).__init__(title)

        # set window width + height, and grid rows + columns
        self.setGeometry(1050, 650, 12, 13)

        self.labelInfoTitle = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelInfoTitle, 1, 1, columnspan=8)
         
        self.labelInfoText = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelInfoText, 2, 1, columnspan=8)
        
        # create and place objects
        self.buttonWindowMapEvents = Button('Service')
        self.placeControl(self.buttonWindowMapEvents, 3, 1, columnspan=5)
        
        self.buttonWindowConfig = Button('Frame Rates')
        self.placeControl(self.buttonWindowConfig, 4, 1, columnspan=5)

        self.buttonWindowMapKeys = Button('Map Keys')
        self.placeControl(self.buttonWindowMapKeys, 5, 1, columnspan=5)

        self.buttonCopyMapKeys = Button('Copy Default Map Keys')
        self.placeControl(self.buttonCopyMapKeys, 6, 1, columnspan=5)

        self.buttonCopyPlayercorefactory = Button('Players')
        self.placeControl(self.buttonCopyPlayercorefactory, 8, 1, columnspan=5)

        self.buttonCleanup = Button('Clean Up')
        self.placeControl(self.buttonCleanup, 10, 1, columnspan=5)

        self.labelInfoStatus1 = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelInfoStatus1, 3, 7, columnspan=8, pad_y=11)

        self.labelInfoStatus2 = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelInfoStatus2, 5, 7, columnspan=8, pad_y=11)

        self.labelDefaultMapKeysStatus = Label('( Suggested buttons map for Addon and Kodi )', alignment=ALIGN_LEFT)
        self.placeControl(self.labelDefaultMapKeysStatus, 6, 7, columnspan=8, pad_y=11)

        self.labelCopyPlayercorefactoryStatus = Label('( Copy playercorefactory.xml with priority players )', alignment=ALIGN_LEFT)
        self.placeControl(self.labelCopyPlayercorefactoryStatus, 8, 7, columnspan=8, pad_y=11)

        self.labelCleanupStatus = Label('', alignment=ALIGN_LEFT)
        self.placeControl(self.labelCleanupStatus, 10, 7, columnspan=8, pad_y=11)
        # check platform type
        self.checkPlatformType()       
        self.checkDisplayModeFileStatus()
        self.checkStatus()
                
        # connect buttons and actions to functions
        self.connect(self.buttonWindowMapEvents, self.windowMapEvents)
        self.connect(self.buttonWindowConfig, self.windowConfig)
        self.connect(self.buttonWindowMapKeys, self.windowMapKeys)
        self.connect(self.buttonCopyMapKeys, self.DefaultMapKeys)
        self.connect(self.buttonCopyPlayercorefactory, self.CopyPlayercorefactory)
        self.connect(self.buttonCleanup, self.cleanup)
        self.connect(ACTION_NAV_BACK, self.close)

        # define key navigation
        self.buttonWindowMapEvents.controlDown(self.buttonWindowConfig)
        self.buttonWindowConfig.controlUp(self.buttonWindowMapEvents)
        
        self.buttonWindowConfig.controlDown(self.buttonWindowMapKeys)
        self.buttonWindowMapKeys.controlUp(self.buttonWindowConfig)

        self.buttonWindowMapKeys.controlDown(self.buttonCopyMapKeys)
        self.buttonCopyMapKeys.controlUp(self.buttonWindowMapKeys)

        self.buttonCopyMapKeys.controlDown(self.buttonCopyPlayercorefactory)
        self.buttonCopyPlayercorefactory.controlUp(self.buttonCopyMapKeys)

        self.buttonCopyPlayercorefactory.controlDown(self.buttonCleanup)
        self.buttonCleanup.controlUp(self.buttonCopyPlayercorefactory)

        # set initial focus
        self.setFocus(self.buttonWindowMapEvents)
                      
    def DefaultMapKeys(self):
        # config key
        #mapKeyResetStatus = fsutil.mapKeyReset()
        fsconfig.keyInfo =  '61489'
        fsconfig.radioInfo = True
        fsconfig.statusInfo = 'Active'
        fsconfig.keyHiPQTools =  '61490'
        fsconfig.radioHiPQTools = True
        fsconfig.statusHiPQTools = 'Active'
        saveSettingsStatus = fsconfigutil.saveSettings()
        # key map file
        _addon = xbmcaddon.Addon()
        addon_path = _addon.getAddonInfo('path').decode('utf-8')
        addon_File = os.path.join(addon_path,'resources/maps/' 'zswitch.xml')
        addon_FileKodi = os.path.join(addon_path,'resources/maps/' 'gen.xml')
        keymapFolder = xbmc.translatePath('special://userdata/keymaps')
        keymapFile = os.path.join(keymapFolder, 'zswitch.xml')
        keymapFileGen = os.path.join(keymapFolder, 'gen.xml')
        try:
            copyfile(addon_File, keymapFile)
            copyfile(addon_FileKodi, keymapFileGen)
            self.labelDefaultMapKeysStatus.setLabel('keys map files copied')
        except Exception:
            self.labelDefaultMapKeysStatus.setLabel('Failed to activate keys')

    def CopyPlayercorefactory(self):
        # playercorefactory file
        _addon = xbmcaddon.Addon()
        addon_path = _addon.getAddonInfo('path').decode('utf-8')
        addon_File = os.path.join(addon_path,'resources/playercorefactory/' 'playercorefactory.xml')
        userFolder = xbmc.translatePath('special://userdata')
        File = os.path.join(userFolder, 'playercorefactory.xml')
        try:
            copyfile(addon_File, File)
            self.labelCopyPlayercorefactoryStatus.setLabel('playercorefactory.xml copied')
        except Exception:
            self.labelCopyPlayercorefactoryStatus.setLabel('Failed to activate playercorefactory.xml')
                      
    def windowConfig(self):
        
        # create and show the Auto Sync configuration window
        fsConfigWindow = ConfigWindow('Refresh rate to frame rate synchronization')
        self.close()
        fsConfigWindow.doModal()
        self.doModal()

    def windowMapEvents(self):
            
        # create and show the Map Events configuration window
        fsMapEventsWindow = MapEventsWindow('Service configuration')
        self.close()
        
        fsMapEventsWindow.doModal()
        
        self.checkStatus()
        self.doModal()
        
    def windowMapKeys(self):
            
        # create and show the Map Keys configuration window
        fsMapKeysWindow = MapKeysWindow('Map keys')
        self.close()

        fsMapKeysWindow.doModal() 

        self.checkStatus()
        self.doModal()
        
    def checkPlatformType(self):

        self.labelInfoTitle.setLabel('Detecting platform...')
        xbmc.sleep(200)
        
        osPlatform, osVariant, ooSDK = fsutil.getPlatformType()

        if osPlatform is None:
            self.labelInfoTitle.setLabel('Failed to detect platform')
            fsconfig.osPlatform = 'unknown'
            self.disableAll()
            
        elif osVariant == 'HiSTBAndroidV6 Hi3798CV200' or osVariant == 'HiSTBAndroidV5 Hi3798CV100':
            self.labelInfoTitle.setLabel(osVariant)
            fsconfig.osPlatform = osVariant

        elif osVariant == 'Windows 7':
            self.labelInfoTitle.setLabel(osVariant + ' (testing only)')
            fsconfig.osPlatform = osVariant

        elif osVariant == 'unsupported':
            self.labelInfoTitle.setLabel('Unsupported platform: ' + osPlatform)
            fsconfig.osPlatform = 'unsupported'
            self.disableAll()

        else:
            self.labelInfoTitle.setLabel('Unsupported OS: ' + osVariant)
            fsconfig.osPlatform = 'unsupported'
            self.disableAll()

        fsconfigutil.saveSettings()
            
    def checkDisplayModeFileStatus(self):

        self.labelInfoText.setLabel('Checking display mode file...')
        xbmc.sleep(200)
        
        modeFile, fileStatus = fsutil.getDisplayModeFileStatus()

        if fileStatus is None:
            self.labelInfoText.setLabel('HDMI mode file check failed.')

        elif fileStatus[:2] == 'OK':
            self.labelInfoText.setLabel(fileStatus[4:])
        
        else:
            self.labelInfoText.setLabel(fileStatus)
            self.disableAll()

    def checkStatus(self):
        
        self.checkIfActive()
        self.checkIfKeysMapped() 

        # check for settings folder
        golbalSettingsFolder = fsconfigutil.settingsFolder()

        if (self.labelInfoStatus1.getLabel() != 'Service stopped') or (self.labelInfoStatus2.getLabel() == 'Keys activated') or (os.path.isdir(golbalSettingsFolder)):
            self.buttonCleanup.setEnabled(True)
        else:
            self.buttonCleanup.setEnabled(False)
            self.labelCleanupStatus.setLabel('Clean up complete')  

    def checkIfActive(self):
        
        fsconfigutil.loadActiveServiceSetting()
        
        if fsconfig.activeService:
            if fsconfig.radioOnPlayStart:
                self.labelInfoStatus1.setLabel('Service running')
            else:
                self.labelInfoStatus1.setLabel('Service running - restart KODI')

        else:
            if fsconfig.radioOnPlayStart:
                self.labelInfoStatus1.setLabel('Service stopped - restart KODI')
            else:
                self.labelInfoStatus1.setLabel('Service stopped')

    def checkIfKeysMapped(self):
        
        if fsutil.mapKeyActive():
            self.labelInfoStatus2.setLabel('Keys activated')

        else:
            self.labelInfoStatus2.setLabel('Keys deactivated')

    def disableAll(self):

        self.buttonWindowConfig.setEnabled(False)
        self.buttonWindowMapEvents.setEnabled(False)
        self.buttonWindowMapKeys.setEnabled(False)

    def cleanup(self):

        self.disableAll()
        
        if (self.labelInfoStatus1.getLabel() != 'Service stopped'):

            self.labelInfoStatus1.setLabel('Service stopping...') 
            
            fsconfig.radioOnPlayStart = False

            saveSettingsStatus = fsconfigutil.saveSettings()
            xbmc.sleep(4500)            

            self.checkIfActive()

        if (self.labelInfoStatus2.getLabel() == 'Keys activated'):

            self.labelInfoStatus2.setLabel('Keys deactivating...')
            xbmc.sleep(600)
            
            mapKeyResetStatus = fsutil.mapKeyReset()
    
            self.labelInfoStatus2.setLabel(mapKeyResetStatus)
            xbmc.sleep(600)
    
            self.checkIfKeysMapped()

        fsconfigutil.deleteAllSettingsFiles()

        self.checkStatus()

        if (self.labelCleanupStatus.getLabel() != 'Clean up complete'):
            self.labelCleanupStatus.setLabel('Clean up incomplete')  

        self.setFocus(self.buttonCleanup)

class InfoPanel():
    
    @staticmethod
    def showInfo():

        # get current window
        windowID = xbmcgui.getCurrentWindowId()
        
        # check for a valid window (10007 = system info, 12005 = full screen video)
#         if (windowID == 12005) or (windowID == 10007):
        if (windowID == 12005):
            currentWindow = xbmcgui.Window(windowID)

            # flag info panel as active
            fsconfig.activeInfo = True
            fsconfigutil.saveActiveInfoSetting()
           
            # create info panel objects

            # same height as codec info
#             panelTop = 19
            # under codec info
            panelTop = 158          
            
            panelBorder = 10
            panelLineTop = panelTop + panelBorder
            panelLineSpacing = 24
            panelLineCount = 32
            
            descHdmiMode = 'Output frequency:'
            descSourceFPS = 'Source framerate:'
            descCurrentFPS = 'Current framerate:'
            descCurrentDISP1 = 'Current DISP1:'
            descCurrentHDMI0 = 'Current HDMI0:'
            
            imageInfoPanel = xbmcgui.ControlImage(-200, panelTop, 1920, (panelBorder * 2) + (panelLineSpacing * panelLineCount), 'DialogBack2.png', colorDiffuse='0xBBBBBBBB')

            # Output Frequency ------------------------------------------------------------------------------------------------------------------------------------------------------------------
            labelHdmiModeTitle = xbmcgui.ControlLabel(50, panelLineTop, 250, 20, descHdmiMode, font='font12')
            labelHdmiMode = xbmcgui.ControlLabel(260, panelLineTop, 100, 30, '', font='font12')
            
            # get current display mode setting
            currentOutputMode, currentHiSiliconMode = fsutil.getDisplayMode()

            # get current frequency
            freqSplit = currentOutputMode.find('-') + 1
            # currentFreq = currentOutputMode[freqSplit:len(currentOutputMode)-2]
            currentFreq = currentHiSiliconMode.replace("_","P").replace("3840x","").replace("1920x","").replace("1280x","").lower().split("p")[1]
            labelHdmiMode.setLabel(currentFreq)
            
            # Source FPS ------------------------------------------------------------------------------------------------------------------------------------------------------------------
            labelSourceFpsTitle = xbmcgui.ControlLabel(50, panelLineTop + (panelLineSpacing * 1), 250, 20, descSourceFPS, font='font12')
            labelSourceFps = xbmcgui.ControlLabel(260, panelLineTop + (panelLineSpacing * 1), 100, 30, '', font='font12')

            # get FPS of currently playing video
            setModeStatus, statusType = fsutil.getCurrentFPS()
            
            if statusType == 'ok':
                labelSourceFps.setLabel(setModeStatus)
            else:
                labelSourceFps.setLabel('')
            
            # Current FPS ------------------------------------------------------------------------------------------------------------------------------------------------------------------
            labelCurrentFpsTitle = xbmcgui.ControlLabel(50, panelLineTop + (panelLineSpacing * 2), 250, 20, descCurrentFPS, font='font12')
            labelCurrentFps = xbmcgui.ControlLabel(260, panelLineTop + (panelLineSpacing * 2), 100, 30, '', font='font12')

            # get current rendered FPS
            currentFPS = xbmc.getInfoLabel('System.FPS')
            
            labelCurrentFps.setLabel(currentFPS)

            # Current HiMedia disp1 --------------------------------------------------------------------------------------------------------------------------------------------------------
            # labelCurrentDisp1Title = xbmcgui.ControlLabel(50, panelLineTop + (panelLineSpacing * 3), 150, 20, descCurrentDISP1, font='font8')
            modeFile = "/proc/msp/disp1"
            labelCurrentDisp1 = xbmcgui.ControlLabel(100, panelLineTop + (panelLineSpacing * 3), 600, 600, '', font='font8')

            with open(modeFile, 'r') as modeFileHandle: 
                currentDisp1 = modeFileHandle.read()
            labelCurrentDisp1.setLabel(currentDisp1)

            # Current HiMedia HDMI0 --------------------------------------------------------------------------------------------------------------------------------------------------------
            # labelCurrentHdmi0Title = xbmcgui.ControlLabel(750, panelLineTop + (panelLineSpacing * 3), 150, 20, descCurrentHDMI0, font='font8')
            modeFile = "/proc/msp/hdmi0"
            labelCurrentHdmi0 = xbmcgui.ControlLabel(700, panelLineTop - (panelLineSpacing * 1), 600, 600, '', font='font8')

            with open(modeFile, 'r') as modeFileHandle: 
                currentDisp1 = modeFileHandle.read()
            labelCurrentHdmi0.setLabel(currentDisp1)

            # ------------------------------------------------------------------------------------------------------------------------------------------------------------------

            # build list of controls
            controlList = [imageInfoPanel, labelHdmiModeTitle, labelHdmiMode, labelSourceFpsTitle, labelSourceFps, labelCurrentFpsTitle, labelCurrentFps, labelCurrentDisp1, labelCurrentHdmi0]

#             if fsconfig.radioAuto50hz:
#                 syncConfig.extend([(fsconfig.edit50hzFps1, mode50hz), 
#                                    (fsconfig.edit50hzFps2, mode50hz), 
#                                    (fsconfig.edit50hzFps3, mode50hz), 
#                                    (fsconfig.edit50hzFps4, mode50hz)])

#             autoSync.insert(0, (syncFPS, syncMode))
                       
            # add info panel to window
            currentWindow.addControls(controlList) 
            
            refreshCounter = 0
                        
            # check for configuration changes every 0.25 second
            while fsconfig.activeInfo:
                 
                xbmc.sleep(250)

                refreshCounter = refreshCounter + 1
                
                # Every half second (update panel)
                if (refreshCounter == 2) or (refreshCounter == 4):

                    # Update Current FPS ------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    currentFPS = xbmc.getInfoLabel('System.FPS') + ' fps'
                    labelCurrentFps.setLabel(currentFPS)

                # Every second (update panel)
                if refreshCounter == 4:

                    # Update Source FPS ------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    setModeStatus, statusType = fsutil.getCurrentFPS()
                    if statusType == 'ok':
                        labelSourceFps.setLabel(setModeStatus)
                    else:
                        labelSourceFps.setLabel('')
 
                    # Update Output Frequency ------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    currentOutputMode, currentHiSiliconMode = fsutil.getDisplayMode()
                    freqSplit = currentOutputMode.find('-') + 1
                    # currentFreq = currentOutputMode[freqSplit:len(currentOutputMode)-2]
                    currentFreq = currentHiSiliconMode.replace("_","P").replace("3840x","").replace("1920x","").replace("1280x","").lower().split("p")[1]
                    labelHdmiMode.setLabel(currentFreq)

                    # Update HiMedia Disp1 ------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    modeFile = "/proc/msp/disp1"
                    with open(modeFile, 'r') as modeFileHandle: 
                        currentDisp1 = modeFileHandle.read()
                    labelCurrentDisp1.setLabel(currentDisp1)

                    # Update HiMedia HDMI0 ------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    modeFile = "/proc/msp/hdmi0"
                    with open(modeFile, 'r') as modeFileHandle: 
                        currentHdmi0 = modeFileHandle.read()
                    labelCurrentHdmi0.setLabel(currentHdmi0)

                    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        
                # Every quarter second - reload settings, to allow info panel stop
                fsconfigutil.loadActiveInfoSetting()

                 # Every second (check and update panel status)
                if refreshCounter == 4:

                    # check that user has not deactivate in last 0.25 seconds
                    if fsconfig.activeInfo:

                        # check if window is still active
                        windowIDcheck = xbmcgui.getCurrentWindowId()       
    
                        # if window is not activate then disable info panel
                        if windowID != windowIDcheck:
                            fsconfig.activeInfo = False
                        
                        # rewrite flag file (necessary even when active for detection of old flag file should XBMC exit unexpectedly)
                        fsconfigutil.saveActiveInfoSetting()

                    # reset refresh counter
                    refreshCounter = 0
                
                
            # remove info from window
            currentWindow.removeControls(controlList) 

