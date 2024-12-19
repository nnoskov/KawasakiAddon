from vcCommand import * 

app = getApplication()
cmd = getCommand()
  
def showMessage(prop):
    title = app.getLocalizedString("Python","MsgBoxTitle","Text") #1st way
    message = app.getLocalizedString("ComboKey::Python.MsgBoxMessage.Text") #2nd way    
    retval = app.messageBox(message,#message text
                            title, #Title
                            iconValues['Information'], #icon
                            buttonValues['YesNoCancel'], #button
                            0, #default result
                            "yep!", #yesbutton
                            "no...", #nobutton
                            "idk") #cancelbutton
    
    
prop1 = cmd.createProperty(VC_BUTTON,"btnPropName")
prop1.OnChanged = showMessage

prop2 = cmd.createProperty(VC_STRING,"ColorPropName",VC_PROPERTY_STEP)
prop2.StepValues = ["red","green","blue"]
prop2.Value = prop2.StepValues[0]

prop3 = cmd.createProperty(VC_BOOLEAN,"Advanced::togglePropName")
prop3.Value = False

def state():
    executeInActionPanel()
    
cmd.addState(state)

returnValues = {0 : 'None', 
                1 : 'OK',
                2 : 'Cancel', 
                6 : 'Yes', 
                7 : 'No'}

buttonValues = { 'OK' : 0,
                 'OKCancel': 1,
                 'YesNoCancel' : 3,
                 'YesNo' : 4}

iconValues = { 'None' : 0,
               'Error': 16,
               'Question' : 32,
               'Warning' : 48,
               'Information' : 64}

 
