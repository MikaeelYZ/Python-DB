from readmovie import *
from updatemovie import *
from deletemovie import *
from addmovie import *
from filmreport import *

def menuOptions():
    options = 0
    while options not in ["1", "2", "3", "4", "5", "6"]:
        with open("dbmenu.txt", 'r') as menu:
            choices = menu.readlines()
        for line in choices:
            print(line, end = "")
        options = input("Enter a menu option: ")

        if options not in ["1", "2", "3", "4", "5", "6",]:
            print(f"{options} not a valid choice")
    return options

def mainMenu():
    main = True

    while main:
        mainMenu = menuOptions()
        if mainMenu == "1":
            read()
        elif mainMenu == "2":
            insertMovie()
        elif mainMenu == "3":
            update()
        elif mainMenu == "4":
            delete()
        elif mainMenu == "5":
            reportMenu()
        else:
            main = False
    
    input("Press Enter to Exit the Main Menu")
    return main

def reportOptions():
    reportoptions = 0
    while reportoptions not in ["1", "2", "3", "4", "5"]:
        with open("reportmenu.txt", 'r') as report:
            choices = report.readlines()
        for line in choices:
            print(line, end = "")
        reportoptions = input("\nEnter a Report Option: ")

        if reportoptions not in ["1", "2", "3", "4", "5"]:
            print(f"{reportoptions} not a valid choice")
    return reportoptions 

def reportMenu():
    report = True

    while report:
        reportMenu = reportOptions()
        if reportMenu == "1":
            year()
        elif reportMenu == "2":
            rating()
        elif reportMenu == "3":
            duration()
        elif reportMenu == "4":
            genre()
        else:
            report = False
    input("Press Enter to Return to Main Menu")
    return report

if __name__ == "__main__":
    mainMenu()