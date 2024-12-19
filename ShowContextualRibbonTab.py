from vcCommand import * 

app = getApplication()

def ShowOrHideCustomRibbonTab():
  try:
    if app.CurrentContext.Id == "Teach":
      app.setContextualTabGroup("pyContextTabGroup",True)
    else:
      app.setContextualTabGroup("pyContextTabGroup",False)
  except:
    pass

app.OnContextChanged = ShowOrHideCustomRibbonTab

