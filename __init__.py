from vcApplication import *

def OnStart():
  cmduri = getApplicationPath() + "ShowContextualRibbonTab.py" 
  cmd = loadCommand("ShowContextualRibbonTab",cmduri)
  print('LoadResult:', cmd)

  cmduri2 = getApplicationPath() + "printHelloLocalized.py" 
  cmd = loadCommand("printHelloLocalized",cmduri2)
  print('LoadResult:', cmd)
  
  cmduri1 = getApplicationPath() + 'PostProcessLauncher.py'
  cmd = loadCommand('PostProcessLauncher', cmduri1)

  iconPath = getCommandPath() + "Hello.svg"
  commands = findCommand("netCommand")
  
  commands.execute("SetLocalizationCommand", "English", "Python", "printHelloLocalized", "Icon", iconPath)
  commands.execute("SetLocalizationCommand", "English", "Python", "PostProcessLauncher", "Icon", "Delfoi/RslToRobot")
  commands.execute("SetLocalizationCommand", "English", "Python", "NewRibbonGroup", "Icon", iconPath)
    
  
  addMenuItem(UxSite = 'pyContextTabGroup',
              UxName = "PythonExtraContextTab", 
              Index = -1, 
              Id = "pyContextTabGroup",
              Parent="gmAction",
              ControlType="ContextualTabGroup",
              BaseBackColor="#ededed")
  
  addMenuItem(UxSite = "pyContextTabGroup/TabHeader",
              UxName="1st Tab", 
              Index = -1, 
              Id = "TabHeader",
              Parent="pyContextTabGroup", 
              ControlType="RibbonTab")
  # now you can add ribbon items in this
  addMenuItem('pyContextTabGroup/TabHeader/NewRibbonGroup', "R Group" , -1, "printHelloLocalized" , "","","","")
  addMenuItem('pyContextTabGroup/TabHeader/NewRibbonGroup', "Run" , -1, "PostProcessLauncher" , "","","","")
  
  