import os #for list of files
from tkinter import * #for extra window
from pywinauto.application import Application  #for automatic input

try:
    app = Application(backend="uia").start('converter.exe')
    app = Application(backend="uia").connect(path = 'converter.exe')

    Wizard = app['To Osu! converter (Made by wanwan159)']

    direct = os.getcwd() + '/input/'
    
    allfiles = os.listdir(direct)
    files = list()
    for file in allfiles:
        if ".ojn" in file:
            files.append(file)

    for i in range(len(files)):
        string = direct + files[i]
        app.Dialog.Edit10.set_text(string)
        app.Dialog.Convert.click()

        txt = app.Dialog.Edit8.get_value()
        while("Finished converting!!" not in txt):
            pass

except Exeption:
    pass

else:
    print("Everything is fine")

finally:
    if "converter.exe" in os.listdir(os.getcwd()):
        app.kill()

