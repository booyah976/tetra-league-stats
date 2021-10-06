username = ""  ## Must enter TETR.IO username here and not in capitals. Eg.) username = "booyah"

import os
from main import get_stats, compile_stats
import subprocess as sp
import threading

gui = True
try:
    import PySimpleGUI as sg
except ModuleNotFoundError:
    print("PySimpleGUI not found, resuming without GUI")
    gui = False


font = ("HUN", 36)
current_dir = os.path.dirname(os.path.realpath(__file__))


def csv():
    programName = "notepad.exe"
    fileName = current_dir + r"\data.csv"
    sp.Popen([programName, fileName])


def open_tetrio():
    os.system(r"")


def open_project():
    sp.Popen(r'explorer /select,"' + current_dir + '"')
    print(r'explorer /select,"' + current_dir + '"')


if gui:
    layout = [
        [
            sg.Text("Tetra League Statistics", font=font),
            sg.Text("          "),
            sg.Button("RUN", button_color=(sg.GREENS[0]), size=(12, 2)),
        ],
        [sg.FileBrowse(button_text="Browse")],
        [
            sg.Button("OPEN PROJECT"),
            sg.Button("OPEN CSV"),
            sg.Text("                         "),
            sg.Button("EXIT", button_color=("red"), size=(5, 2)),
        ],
        [sg.Text("PRESS RUN TO RUN THE PROGRAM", text_color="black", key="_TBOX_")],
    ]

    # Create the window
    window = sg.Window("TL Stats", layout, margins=(100, 70), font=("HUN", 16))

    # Create an event loop
    while True:
        event, values = window.read()

        if event == "EXIT" or event == sg.WIN_CLOSED:
            break

        if event == "RUN":
            t1 = threading.Thread(target=compile_stats, args=[username])
            t1.start()
            window.Element("_TBOX_").Update("COMPLETED")

        if event == "OPEN CSV":
            t2 = threading.Thread(target=csv)
            t2.start()
            window.Element("_TBOX_").Update("OPENED CSV!")

        if event == "OPEN TETR.IO":
            t3 = threading.Thread(target=open_tetrio)
            t3.start()
            window.Element("_TBOX_").Update("OPENED TETR.IO")

        if event == "OPEN PROJECT":
            t4 = threading.Thread(target=open_project)
            t4.start()
            window.Element("_TBOX_").Update("OPENED PROJECT FOLDER")

    window.close()
else:
    text = "Type R to run the program \nType C to open CSV file \nType P to open project folder \nType Q to quit"
    print(text)
    run = True
    while run:
        action = input("tl-stats>>")
        if action == "R":
            compile_stats(username)
            print("Completed")
        elif action == "C":
            csv()
        elif action == "P":
            open_project()
        elif action == "Q":
            run = False
        else:
            print(text)
