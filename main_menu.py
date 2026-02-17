# To use this file in maya run these commands, withou the comment hash
#import main_menu
#main_menu.build_menu()

# If this does not run check the readme for Maya path info.

import maya.cmds as cmds
import step1
import step2
import step3
import step4

def run_step(step):
    if step == 1:
        step1.run()
    elif step == 2:
        step2.run()
    elif step == 3:
        step3.run()
    elif step == 4:
        step4.run()

def build_menu():
    if cmds.window("exampleWin", exists=True):
        cmds.deleteUI("exampleWin")

    win = cmds.window("exampleWin", title="Example Steps")
    cmds.columnLayout(adjustableColumn=True)

    cmds.button(label="Run Step 1", command=lambda *_: run_step(1))
    cmds.button(label="Run Step 2", command=lambda *_: run_step(2))
    cmds.button(label="Run Step 3", command=lambda *_: run_step(3))
    cmds.button(label="Run Step 4", command=lambda *_: run_step(4))

    cmds.showWindow(win)

build_menu()
