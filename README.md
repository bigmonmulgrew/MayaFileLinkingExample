This repo contains a minimum viable product to show linking up different script files for usage in Maya with python/MEL.

It only outputs messages on sucessfully running each program.
It is a teaching sample only and provides no actual funcationality.

You would usually run from main.py (this is a convention and optional)
main_simple.py - This is one example of how you could link multiple files
main_menu.py - A slightly different example allowing running each step discreetly through a menu


### Warning ####
Maya caches modules and wont update them if you make changes. You can force this without restarting by running this, example for step1.py
import importlib
import step1
importlib.reload(step1)