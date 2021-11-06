username = ""  ## Must enter TETR.IO username here and not in capitals. Eg.) username = "booyah"

if username == "":
    username = input(
        "Enter TETR.IO name (change the first line of gui.py if you dont want this message to show) > "
    )

import os
from main import get_stats, compile_stats
import subprocess as sp


current_dir = os.path.dirname(os.path.realpath(__file__))


def csv():
    programName = "notepad.exe"
    fileName = current_dir + r"\data.csv"
    sp.Popen([programName, fileName])


def open_replays():
    sp.Popen(r'explorer /select,"' + current_dir + '"')
    print(r'explorer /select,"' + current_dir + '/replays"')


def usage():
    text = "Type R to run the program \nType C to open CSV file \nType P to open project folder \nType Q to quit"
    print(text)


run = True
usage()
while run:
    action = input("tl-stats>>")
    if action == "R":
        compile_stats(username)
        print("Completed")
    elif action == "C":
        csv()
    elif action == "P":
        open_replays()
    elif action == "Q":
        run = False
    else:
        usage()
