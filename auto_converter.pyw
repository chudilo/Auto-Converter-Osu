import os #for list of files

import pywinauto #for automatic input

from tkinter import * #for extra window

from pywinauto.application import Application
import inspect

#'To Osu! converter (Made by wanwan159)'
app = Application(backend="uia").start('D:/Osu/converter.exe')
#inspect.getmembers(app, predicate=inspect.ismethod)
#print(pywinauto.findwindows.find_elements())
Wizard = app['To Osu! converter (Made by wanwan159)']
#Wizard.menu_select("File -> Close")
#app.Dialog.print_control_identifiers()
#app.Dialog.Open.click()
app.Dialog.Edit10.set_text("Sasai kudasai")


#dlg_spec.wrapper_object()
#app = Application(backend="uia").start('spyxx_amd64')

'''
    elements = findbestmatch.find_best_control_matches(best_match, wrapped_elems)
  File "D:\Program_Files\Python3\lib\site-packages\pywinauto\findbestmatch.py", line 533, in find_best_control_matches
    raise MatchError(items = name_control_map.keys(), tofind = search_text)
pywinauto.findbestmatch.MatchError: Could not find 'Form1' in 'dict_keys([])'
'''


#working programm
'''
app = Application(backend="uia").start('D:/StepEdit_Lite/stepeditlite.exe')
Wizard = app['StepEdit Lite']
Wizard.menu_select("File -> Exit")
'''
